# 08: HTML Generation With Templating

## Tujuan Percobaan
Percobaan ini bertujuan untuk memahami cara menghasilkan halaman HTML dinamis dengan menggunakan templating system pada framework Pyramid. Templating memungkinkan pemisahan antara logika aplikasi (Python) dan tampilan (HTML), sehingga struktur kode menjadi lebih rapi dan mudah dikelola.

## Analisis
- Template berfungsi untuk memisahkan logika aplikasi dan tampilan, sehingga mudah diubah tanpa mengubah kode Python.
- Parameter renderer pada @view_config menentukan file template yang digunakan.
- View tidak mengembalikan Response, tetapi dictionary agar Pyramid otomatis me-render template.
- Opsi --reload memudahkan debugging karena aplikasi akan memuat ulang setiap kali file berubah.
