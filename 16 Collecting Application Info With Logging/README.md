# 16: Collecting Application Info With Logging

## Tujuan Percobaan
Percobaan ini bertujuan untuk memahami bagaimana cara menggunakan logging di Pyramid agar pengembang dapat melacak aktivitas aplikasi, mencatat error, serta menganalisis kinerja sistem. Logging sangat penting untuk melakukan debugging, maintenance, dan memonitor perilaku aplikasi saat dijalankan di server produksi.

## Analisis
Dalam framework Pyramid, logging dilakukan dengan memanfaatkan modul standar Python yaitu `logging`. File konfigurasi `.ini` (seperti `development.ini`) dapat digunakan untuk menentukan level logging, format pesan, dan lokasi penyimpanan log.