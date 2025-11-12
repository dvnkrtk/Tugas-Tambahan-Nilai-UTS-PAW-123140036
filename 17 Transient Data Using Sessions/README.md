# 17: Transient Data Using Sessions

## Tujuan Percobaan
Percobaan ini bertujuan untuk memahami bagaimana cara menyimpan data sementara (transient data) di sisi server menggunakan session dalam framework Pyramid. Session digunakan untuk menyimpan informasi pengguna yang bersifat sementara antar permintaan (request), seperti data login, preferensi pengguna, atau keranjang belanja.

## Analisis
Berdasarkan hasil percobaan, penggunaan session memungkinkan data tetap tersimpan selama pengguna masih berada dalam sesi yang sama, tanpa harus menyimpannya ke database.  