import os
import re
from urllib.parse import urlparse
from PIL import Image, ImageDraw, ImageFont
from tkinter import messagebox

# ANSI color codes for colorful output
COLOR_GREEN = '\033[92m'
COLOR_YELLOW = '\033[93m'
COLOR_RESET = '\033[0m'

# Regular expressions for matching img and video tags in HTML
img_pattern = r'<img\s+src="([^"]+)"\s+loading="lazy"\s+style="([^"]+)">'
video_pattern = r'<video\s+controls="?"\s+src="([^"]+)"\s+width="([^"]+)"\s+height="([^"]+)"\s+class="note-video-clip"></video>'

def rewrite_links(poster_url=None, script_dir="."):
    """
    Rewrites image and video links in HTML files to include additional attributes.
    Args:
    - poster_url: The URL to use for the video poster attribute.
    - script_dir: The directory containing the HTML files.
    """
    html_found = False
    video_rewritten = False
    img_rewritten = False
    processed_info = ""
    processed_urls = []

    # Traverse through all files in the directory
    for file in os.listdir(script_dir):
        if file.endswith('.html'):
            html_found = True
            file_path = os.path.join(script_dir, file)
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Rewrite video links
            rewritten_content, count = re.subn(
                video_pattern, 
                r'<video controls="" preload="none" src="\1" poster="{}" width="\2" height="\3" class="note-video-clip"></video>'.format(poster_url), 
                content
            )
            if count > 0:
                video_rewritten = True

            # Rewrite image links
            img_matches = re.finditer(img_pattern, content)
            for match in img_matches:
                img_url = match.group(1)
                alt_text = get_alt_text(img_url)
                rewritten_content = rewritten_content.replace(
                    match.group(0), 
                    f'<a href="{img_url}" target="_blank" rel="noopener noreferrer">'
                    f'<img loading="lazy" src="{img_url}"  style="{match.group(2)}" alt="{alt_text}"></a>'
                )
                processed_urls.append((img_url, alt_text))
                img_rewritten = True

            # Write the updated content back to the file
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(rewritten_content)

    if not html_found:
        messagebox.showwarning("No HTML files found", "No HTML files found in the specified directory.")
    else:
        if video_rewritten:
            print(COLOR_GREEN + "Video links have been rewritten successfully." + COLOR_RESET)
        else:
            print(COLOR_YELLOW + "No video links found in the HTML files." + COLOR_RESET)

        if img_rewritten:
            processed_info += "Processed URLs with alt names:\n\n"
            for url, alt in processed_urls:
                processed_info += f"Alt Name: {alt}\n\n"
        if processed_info:
            messagebox.showinfo("Success", processed_info)
        else:
            messagebox.showinfo("Failed", "No image links found in the HTML files.")

def get_alt_text(url):
    """
    Extracts a descriptive alt text from a given URL.
    Args:
    - url: The URL to extract the alt text from.
    """
    parsed_url = urlparse(url)
    filename = os.path.basename(parsed_url.path)
    filename_without_extension = os.path.splitext(filename)[0]
    alt_text = filename_without_extension.replace('-', ' ')
    return alt_text

def add_watermark(input_dir, output_dir_jpg, output_dir_webp, watermark_text, font_path):
    """
    Adds a watermark to all images in the input directory and saves them in both JPEG and WebP formats.
    Args:
    - input_dir: The directory containing input images.
    - output_dir_jpg: The directory to save watermarked JPEG images.
    - output_dir_webp: The directory to save watermarked WebP images.
    - watermark_text: The text to use as the watermark.
    - font_path: The path to the font file to use for the watermark.
    """
    default_font_size = 100
    font = ImageFont.truetype(font_path, default_font_size)
    num_output_files = len(os.listdir(output_dir_jpg))
    num_inputdir = len(os.listdir(input_dir))

    text_color = (255, 255, 255, 30)
    max_file_size = 1024 * 1024
    total_processed_images = 0

    for filename in os.listdir(input_dir):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
            input_image_path = os.path.join(input_dir, filename)
            output_image_path_jpg = os.path.join(output_dir_jpg, f"{filename.split('.')[0]}.jpg")
            output_image_path_webp = os.path.join(output_dir_webp, f"{filename.split('.')[0]}.webp")

            if filename.lower().endswith(('.png', '.webp')):
                input_image = Image.open(input_image_path).convert("RGB")
            else:
                input_image = Image.open(input_image_path)

            if input_image.width < 700 or input_image.height < 700:
                font_size = 50
            else:
                font_size = default_font_size

            font = ImageFont.truetype(font_path, font_size)
            text_image = Image.new('RGBA', input_image.size, (255, 255, 255, 0))
            draw = ImageDraw.Draw(text_image)

            text_width = draw.textlength(watermark_text, font=font)
            text_height = font_size
            position = ((input_image.width - text_width) // 2, (input_image.height - text_height) // 2)

            draw.text(position, watermark_text, font=font, fill=text_color)
            input_image.paste(text_image, (0, 0), text_image)

            if os.path.getsize(input_image_path) > max_file_size:
                output_quality = 95
                while True:
                    output_image = Image.new("RGB", input_image.size)
                    output_image.paste(input_image)
                    output_image.save(output_image_path_jpg, "JPEG", quality=output_quality)
                    if os.path.getsize(output_image_path_jpg) <= max_file_size:
                        break
                    else:
                        output_quality -= 5
            else:
                input_image.save(output_image_path_jpg, "JPEG")
            
            total_processed_images += 1
            input_image.save(output_image_path_webp, "WEBP", quality=90)

    success_message = (
        f"Text watermark added to all images and converted to JPEG and WebP successfully!\n\n"
        f"Total input images: {num_inputdir}\n\n"
        f"Total processed images: {total_processed_images}\n\n"
        f"Number of files in output_jpg folder: {num_output_files}"
    )
    return success_message
