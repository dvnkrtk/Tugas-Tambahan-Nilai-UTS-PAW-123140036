# 03: Application Configuration with .ini Files

## Tujuan Percobaan
Percobaan ini bertujuan untuk memahami cara mengatur konfigurasi aplikasi Pyramid menggunakan file `.ini`. File `.ini` merupakan bagian penting dalam arsitektur Pyramid karena memungkinkan pengaturan aplikasi dilakukan tanpa perlu mengubah kode program secara langsung.

## Analisa
Dalam framework Pyramid, konfigurasi aplikasi, seperti alamat server, logging, pengaturan database, hingga environment dapat didefinisikan di file `.ini`.  
Biasanya ada dua jenis konfigurasi utama:
- `development.ini` → digunakan untuk tahap pengembangan (debug aktif, reload otomatis)
- `production.ini` → digunakan saat aplikasi dipublikasikan (optimasi performa, debug nonaktif).

Inti dari guide ini menurut saya untuk kita mengetahui kalau kita bisa melakukan konfigurasi menggunakan file .ini

File `.ini` dibaca oleh perintah:
```bash
pserve development.ini --reload
