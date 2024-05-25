import os
import customtkinter as ctk
from file_operations import browse_input_folder, browse_folder_with_default, process_action, open_data_folder, open_html_in_default_editor, erase_jpg_webp_files

ctk.set_appearance_mode("Dark")  # Default to Dark Mode
ctk.set_default_color_theme("blue")  # Themes: "blue", "green", "dark-blue"

class RewarkGUI(ctk.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Bosmudasky Simple GUI")
        self.geometry("1300x700")
        self.script_dir = os.path.dirname(os.path.abspath(__file__))

        # configure grid layout (2x2)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = ctk.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=2, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)

        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="Bosmudasky GUI", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.radio_var = ctk.StringVar(value="watermark")

        self.radio_watermark = ctk.CTkRadioButton(self.sidebar_frame, text="Add Watermark", variable=self.radio_var, value="watermark", command=self.update_content)
        self.radio_watermark.grid(row=1, column=0, padx=20, pady=10)

        self.radio_rewrite = ctk.CTkRadioButton(self.sidebar_frame, text="Rewrite Links / Paste Loader", variable=self.radio_var, value="rewrite", command=self.update_content)
        self.radio_rewrite.grid(row=2, column=0, padx=20, pady=10)

        self.radio_loader = ctk.CTkRadioButton(self.sidebar_frame, text="Create Shortcut", variable=self.radio_var, value="loader", command=self.update_content)
        self.radio_loader.grid(row=3, column=0, padx=20, pady=10)

        # create main content frame
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.grid(row=0, column=1, rowspan=2, sticky="nsew")
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)

        # create container frame to center content
        self.container_frame = ctk.CTkFrame(self.main_frame)
        self.container_frame.grid(row=1, column=0, padx=20, pady=20)
        self.container_frame.grid_columnconfigure(0, weight=1)
        self.container_frame.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight=1)

        # create widgets for watermark and rewrite actions
        self.label_input_watermark = ctk.CTkLabel(self.container_frame, text="Input Folder:")
        self.input_folder_watermark = ctk.CTkEntry(self.container_frame, width=350)
        self.button_input_watermark = ctk.CTkButton(self.container_frame, text="Browse", command=lambda: browse_input_folder(self.script_dir, self.input_folder_watermark))

        self.label_input_rewrite = ctk.CTkLabel(self.container_frame, text="Rewrite Links Input Folder:")
        self.input_folder_rewrite = ctk.CTkEntry(self.container_frame, width=350)
        self.button_input_rewrite = ctk.CTkButton(self.container_frame, text="Browse", command=lambda: browse_input_folder(self.script_dir, self.input_folder_rewrite))

        self.label_input_paste = ctk.CTkLabel(self.container_frame, text="Paste Loader Destination Folder:")
        self.input_folder_paste = ctk.CTkEntry(self.container_frame, width=350)
        self.button_input_paste = ctk.CTkButton(self.container_frame, text="Browse", command=lambda: browse_folder_with_default("D:/My-Folder/Bosmuda Store/BM Website/Loader", self.input_folder_paste))

        self.button_process_watermark = ctk.CTkButton(self.container_frame, text="Process Add Watermark", command=self.process_watermark)
        self.button_process_rewrite = ctk.CTkButton(self.container_frame, text="Process Rewrite Links", command=self.process_rewrite_links)
        self.button_process_paste = ctk.CTkButton(self.container_frame, text="Process Paste Loader", command=self.process_paste_loader)

        # create widgets for loader action
        self.label_loader_target = ctk.CTkLabel(self.container_frame, text="Target Folder:")
        self.input_loader_target = ctk.CTkEntry(self.container_frame, width=350, placeholder_text="Target folder for shortcut")
        self.button_loader_target = ctk.CTkButton(self.container_frame, text="Browse", command=lambda: browse_input_folder(self.script_dir, self.input_loader_target))

        self.label_loader_url = ctk.CTkLabel(self.container_frame, text="Shortcut URL:")
        self.input_loader_url = ctk.CTkEntry(self.container_frame, width=350, placeholder_text="URL for the shortcut")

        self.label_loader_name = ctk.CTkLabel(self.container_frame, text="Shortcut Name:")
        self.input_loader_name = ctk.CTkEntry(self.container_frame, width=350, placeholder_text="Name of the shortcut")

        self.button_process_loader = ctk.CTkButton(self.container_frame, text="Process Create Shortcut", command=self.process_create_shortcut)

        self.button_open_html = ctk.CTkButton(self.container_frame, text="Open The HTML", command=lambda: open_html_in_default_editor(self.script_dir))
        self.button_open_data_folder = ctk.CTkButton(self.container_frame, text="Open Data Folder", command=lambda: open_data_folder(self.script_dir))
        self.button_erase_jpg_webp = ctk.CTkButton(self.container_frame, text="Erase JPG and WebP", command=lambda: erase_jpg_webp_files(self.script_dir))

        # default to watermark layout
        self.show_watermark_fields()

    def show_watermark_fields(self):
        self.clear_container_frame()
        default_input_folder = os.path.join(self.script_dir, 'Data', 'input_images')
        self.input_folder_watermark.delete(0, ctk.END)
        self.input_folder_watermark.insert(0, default_input_folder)
        self.label_input_watermark.grid(row=0, column=0, padx=20, pady=10, sticky="e")
        self.input_folder_watermark.grid(row=0, column=1, padx=20, pady=10, columnspan=2, sticky="ew")
        self.button_input_watermark.grid(row=0, column=3, padx=20, pady=10)
        self.button_process_watermark.grid(row=1, column=0, columnspan=4, pady=20, sticky="ew")
        self.button_erase_jpg_webp.grid(row=2, column=0, columnspan=4, pady=10, sticky="ew")
        self.button_open_data_folder.grid(row=3, column=0, columnspan=4, pady=10, sticky="ew")

    def show_rewrite_fields(self):
        self.clear_container_frame()
        self.label_input_rewrite.grid(row=0, column=0, padx=20, pady=10, sticky="e")
        self.input_folder_rewrite.grid(row=0, column=1, padx=20, pady=10, columnspan=2, sticky="ew")
        self.button_input_rewrite.grid(row=0, column=3, padx=20, pady=10)
        self.button_process_rewrite.grid(row=1, column=0, columnspan=4, pady=20, sticky="ew")
        
        self.label_input_paste.grid(row=2, column=0, padx=20, pady=10, sticky="e")
        self.input_folder_paste.delete(0, ctk.END)
        self.input_folder_paste.insert(0, "D:/My-Folder/Bosmuda Store/BM Website/Loader")
        self.input_folder_paste.grid(row=2, column=1, padx=20, pady=10, columnspan=2, sticky="ew")
        self.button_input_paste.grid(row=2, column=3, padx=20, pady=10)
        self.button_process_paste.grid(row=3, column=0, columnspan=4, pady=20, sticky="ew")
        
        self.button_open_html.grid(row=4, column=0, columnspan=4, pady=10, sticky="ew")

    def show_loader_fields(self):
        self.clear_container_frame()
        self.label_loader_target.grid(row=0, column=0, padx=20, pady=10, sticky="e")
        self.input_loader_target.grid(row=0, column=1, padx=20, pady=10, columnspan=2, sticky="ew")
        self.button_loader_target.grid(row=0, column=3, padx=20, pady=10)
        
        self.label_loader_url.grid(row=1, column=0, padx=20, pady=10, sticky="e")
        self.input_loader_url.grid(row=1, column=1, padx=20, pady=10, columnspan=2, sticky="ew")
        
        self.label_loader_name.grid(row=2, column=0, padx=20, pady=10, sticky="e")
        self.input_loader_name.grid(row=2, column=1, padx=20, pady=10, columnspan=2, sticky="ew")
        
        self.button_process_loader.grid(row=3, column=0, columnspan=4, pady=20, sticky="ew")

    def update_content(self):
        if self.radio_var.get() == "watermark":
            self.show_watermark_fields()
        elif self.radio_var.get() == "rewrite":
            self.show_rewrite_fields()
        elif self.radio_var.get() == "loader":
            self.show_loader_fields()

    def clear_container_frame(self):
        for widget in self.container_frame.winfo_children():
            widget.grid_forget()

    def process_watermark(self):
        process_action("watermark", self.input_folder_watermark.get(), self.script_dir)

    def process_rewrite_links(self):
        process_action("rewrite", self.input_folder_rewrite.get(), self.script_dir)

    def process_paste_loader(self):
        process_action("paste_loader", self.input_folder_paste.get(), self.script_dir)

    def process_create_shortcut(self):
        shortcut_info = {
            'target_folder': self.input_loader_target.get(),
            'shortcut_url': self.input_loader_url.get(),
            'shortcut_name': self.input_loader_name.get()
        }
        process_action("create_shortcut", shortcut_info, self.script_dir)

if __name__ == "__main__":
    app = RewarkGUI()
    app.mainloop()
