# 14: AJAX Development With JSON Renderers

## Tujuan Percobaan
Percobaan ini bertujuan untuk memahami bagaimana Pyramid menangani permintaan dan respons berbasis **AJAX (Asynchronous JavaScript and XML)** menggunakan JSON Renderer. Tujuan utamanya adalah agar aplikasi web dapat berkomunikasi secara dinamis antara frontend (JavaScript) dan backend (Python) tanpa perlu melakukan reload seluruh halaman.

## Analisa
Dalam percobaan ini, saya mempelajari bahwa JSON Renderer di Pyramid digunakan untuk secara otomatis mengubah data Python (seperti dictionary atau list) menjadi format JSON. Ketika kita menambahkan `renderer='json'` di dekorator `@view_config`, maka view tersebut akan memberikan response dalam bentuk JSON.
