# 21: Protecting Resources With Authorization

## Tujuan Percobaan
Percobaan ini bertujuan untuk memahami bagaimana melindungi sumber daya (resources) pada aplikasi web Pyramid menggunakan mekanisme otorisasi (authorization). Otorisasi digunakan untuk menentukan hak akses pengguna terhadap halaman atau fitur tertentu sesuai peran (role) mereka.

## Analisis
Berdasarkan hasil percobaan, penggunaan authorization memungkinkan aplikasi membatasi akses ke resource tertentu hanya untuk pengguna yang memiliki hak yang sesuai. Pyramid menyediakan cara untuk mengatur policy otorisasi dan memeriksa hak akses pengguna sebelum mereka dapat mengakses fitur atau data sensitif. Dengan mekanisme ini, aplikasi dapat menjaga keamanan data dan fungsionalitas, mencegah penyalahgunaan, dan memastikan bahwa setiap pengguna hanya dapat mengakses informasi yang diperbolehkan. Secara keseluruhan, modul ini menekankan pentingnya kombinasi autentikasi dan otorisasi untuk membangun aplikasi web yang aman dan terkontrol.