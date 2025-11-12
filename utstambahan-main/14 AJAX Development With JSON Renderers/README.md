# 14: AJAX Development With JSON Renderers

## 🎯 Tujuan Percobaan
Percobaan ini bertujuan untuk memahami bagaimana Pyramid menangani permintaan dan respons berbasis AJAX (Asynchronous JavaScript and XML) menggunakan JSON Renderer. Tujuan utamanya adalah agar aplikasi web dapat berkomunikasi secara dinamis antara **frontend (JavaScript) dan backend (Python) tanpa perlu melakukan reload seluruh halaman.

## Analisis
Dari hasil percobaan, saya mempelajari bahwa Pyramid mendukung pengiriman dan penerimaan data **JSON** melalui konfigurasi `renderer='json'` pada view. Ketika sebuah fungsi view menggunakan renderer JSON, maka nilai yang dikembalikan (return) secara otomatis akan dikonversi menjadi JSON response oleh Pyramid.