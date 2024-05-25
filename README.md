## Bosmudasky Simple GUI

Selamat datang di Bosmudasky Simple GUI! Ini adalah aplikasi Python yang dirancang untuk mempermudah berbagai operasi file dengan antarmuka yang ramah pengguna. Dibangun dengan CustomTkinter, aplikasi ini memungkinkan Anda menambahkan watermark, mengubah tautan, menyalin file dari direktori loader, dan membuat shortcut dengan mudah.

## Fitur

- **Add Watermark**: Tambahkan watermark ke gambar-gambar di folder yang Anda pilih.
- **Rewrite Links**: Ubah tautan di file HTML dalam folder yang Anda pilih.
- **Paste Loader**: Salin file dari folder loader ke folder tujuan yang Anda pilih.
- **Create Shortcut**: Buat shortcut dengan URL dan nama yang Anda pilih di folder tujuan.

## Requirements

Untuk menjalankan aplikasi ini, Anda memerlukan:
- Python 3.6 atau lebih baru
- CustomTkinter
- Pillow
- pywin32

## Instalasi

1. Clone repository ini:
   ```bash
   git clone https://github.com/username-kamu/bosmudasky-simple-gui.git
   cd bosmudasky-simple-gui
   ```

2. Install paket-paket yang dibutuhkan:
   ```bash
   pip install customtkinter pillow pywin32
   ```

## Penggunaan

Jalankan script `GUI.py` untuk memulai aplikasi:
```bash
python GUI.py
```

### Add Watermark

1. Pilih opsi "Add Watermark".
2. Browse ke folder input yang berisi gambar-gambar.
3. Klik "Process Add Watermark" untuk menambahkan watermark ke semua gambar di folder tersebut.

### Rewrite Links

1. Pilih opsi "Rewrite Links / Paste Loader".
2. Browse ke folder input yang berisi file HTML untuk mengubah tautan.
3. Klik "Process Rewrite Links" untuk mengubah tautan di file-file HTML tersebut.

### Paste Loader

1. Pilih opsi "Rewrite Links / Paste Loader".
2. Path default untuk folder loader sudah diset ke `D:/My-Folder/Bosmuda Store/BM Website/Loader`. Anda dapat menggantinya dengan browse ke folder tujuan lain.
3. Klik "Process Paste Loader" untuk menyalin semua file dari folder loader ke folder tujuan yang Anda pilih.

### Create Shortcut

1. Pilih opsi "Create Shortcut".
2. Browse ke folder tujuan di mana Anda ingin membuat shortcut.
3. Masukkan URL untuk shortcut.
4. Masukkan nama untuk shortcut.
5. Klik "Process Create Shortcut" untuk membuat shortcut di folder tujuan yang Anda pilih.

## Struktur Proyek

```
bosmudasky-simple-gui/
├── Data/
│   ├── input_images/        # Folder input default untuk gambar
│   ├── output_jpg/          # Folder output untuk gambar JPG yang sudah di-watermark
│   ├── output_webp/         # Folder output untuk gambar WebP yang sudah di-watermark
│   ├── loader/              # Folder yang berisi file-file untuk dipaste
│   └── write.html           # Contoh file HTML untuk di-rewrite linknya
├── file_operations.py       # Berisi fungsi-fungsi untuk operasi file
├── rewark.py                # Berisi fungsi-fungsi untuk watermark dan rewrite link
└── GUI.py                   # Script utama untuk menjalankan GUI
```

## Lisensi

Proyek ini dilisensikan di bawah MIT License. Lihat file [LICENSE](LICENSE) untuk detail lebih lanjut.

## Kontribusi

Kami selalu terbuka untuk kontribusi. Jangan ragu untuk submit issue atau pull request jika Anda ingin berkontribusi pada proyek ini.

## Penghargaan

- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) untuk framework Tkinter yang modern dan dapat dikustomisasi.
- [Pillow](https://python-pillow.org/) untuk image processing.
- [pywin32](https://github.com/mhammond/pywin32) untuk support Windows COM client.

Terima kasih telah menggunakan Bosmudasky Simple GUI. Kami berharap aplikasi ini dapat membantu memudahkan pekerjaan Anda. Selamat berkarya dan teruslah berinovasi! 🚀
