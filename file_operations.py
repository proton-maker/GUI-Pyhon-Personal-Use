import os
import shutil
import subprocess
import tkinter.messagebox as messagebox
from tkinter import filedialog
from rewark import add_watermark, rewrite_links
import win32com.client

def browse_input_folder(script_dir, entry_widget):
    folder = filedialog.askdirectory(initialdir=os.path.join(script_dir, 'Data', 'input_images'))
    if folder:
        entry_widget.delete(0, "end")
        entry_widget.insert(0, folder)

def browse_folder_with_default(default_path, entry_widget):
    folder = filedialog.askdirectory(initialdir=default_path)
    if folder:
        entry_widget.delete(0, "end")
        entry_widget.insert(0, folder)

def process_action(action, input_folder, script_dir):
    if action == "watermark":
        if not input_folder:
            messagebox.showerror("Error", "Please select an input folder.")
            return
        output_folder_jpg = os.path.join(script_dir, 'Data', 'output_jpg')
        output_folder_webp = os.path.join(script_dir, 'Data', 'output_webp')
        watermark_text = 'Bosmudasky.com'
        font_path = os.path.join(script_dir, 'Data', 'BebasNeue-Regular.ttf')
        success_message = add_watermark(input_folder, output_folder_jpg, output_folder_webp, watermark_text, font_path)
        messagebox.showinfo("Success", success_message)
    elif action == "rewrite":
        data_folder_path = os.path.join(script_dir, 'Data')
        links_rewritten = rewrite_links(poster_url=None, script_dir=data_folder_path)
        if links_rewritten:
            messagebox.showinfo("Success", "Links rewritten successfully.")
        else:
            messagebox.showinfo("Info", "No links found to rewrite.")
    elif action == "paste_loader":
        if not input_folder:
            messagebox.showerror("Error", "Please select a destination folder.")
            return
        loader_folder = os.path.join(script_dir, 'Data', 'loader')
        copy_files(loader_folder, input_folder)
    elif action == "create_shortcut":
        if not input_folder:
            messagebox.showerror("Error", "Please select a destination folder.")
            return
        shortcut_url = input_folder.get('shortcut_url')
        shortcut_name = input_folder.get('shortcut_name')
        create_shortcut(input_folder.get('target_folder'), shortcut_url, shortcut_name)

def open_data_folder(script_dir):
    data_folder_path = os.path.join(script_dir, 'Data')
    if os.path.exists(data_folder_path):
        subprocess.Popen(["explorer", data_folder_path])
    else:
        messagebox.showerror("Error", "The Data folder does not exist.")

def open_html_in_default_editor(script_dir):
    html_file_path = os.path.join(script_dir, 'Data', 'write.html')
    if not os.path.exists(html_file_path):
        messagebox.showerror("Error", "The HTML file does not exist.")
        return
    os.startfile(html_file_path)

def erase_jpg_webp_files(script_dir):
    confirm = messagebox.askyesno("Confirmation", "Are you sure you want to erase JPG and WebP files?")
    if confirm:
        output_folder_jpg = os.path.join(script_dir, 'Data', 'output_jpg')
        output_folder_webp = os.path.join(script_dir, 'Data', 'output_webp')
        delete_files_in_folder(output_folder_jpg)
        delete_files_in_folder(output_folder_webp)
        messagebox.showinfo("Success", "JPG and WebP files deleted successfully.")

def delete_files_in_folder(folder_path):
    try:
        for item in os.listdir(folder_path):
            item_path = os.path.join(folder_path, item)
            if os.path.isfile(item_path):
                os.remove(item_path)
                print(f"Deleted: {item_path}")
        print(f"All files inside {folder_path} deleted successfully.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def copy_files(source_folder, destination_folder):
    try:
        for item in os.listdir(source_folder):
            source_path = os.path.join(source_folder, item)
            destination_path = os.path.join(destination_folder, item)
            if os.path.isfile(source_path):
                shutil.copy2(source_path, destination_path)
                print(f"Copied: {source_path} to {destination_path}")
        messagebox.showinfo("Success", "Files copied successfully.")
    except Exception as e:
        print(f"An error occurred while copying files: {str(e)}")
        messagebox.showerror("Error", f"An error occurred while copying files: {str(e)}")

def create_shortcut(path, target, name):
    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortcut(os.path.join(path, f"{name}.lnk"))
    shortcut.TargetPath = target
    shortcut.Description = name
    shortcut.Save()
