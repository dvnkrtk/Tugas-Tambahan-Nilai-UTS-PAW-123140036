# 09: Organizing Views With View Classes

## Tujuan Percobaan
Percobaan ini bertujuan untuk memahami bagaimana cara mengorganisir view dalam aplikasi Pyramid menggunakan View Classes, bukan hanya dengan fungsi. Dengan pendekatan berbasis kelas, logika untuk beberapa route yang saling berkaitan dapat dikelompokkan dalam satu kelas, sehingga kode menjadi lebih terstruktur, mudah dibaca, dan mudah dikembangkan.

---

## Analisis
Berdasarkan analisis saya, pada percobaan ini diperkenalkan konsep View Classes, yaitu pendekatan OOP (Object-Oriented Programming) di dalam Pyramid yang memungkinkan beberapa fungsi view dikelompokkan dalam satu kelas. Pyramid juga memungkinkan kita untuk menulis default view configuration di atas kelas (melalui `@view_defaults`), sehingga dapat menghemat baris kode dan mengurangi pengulangan konfigurasi pada setiap metode. Misalnya, jika beberapa fungsi menggunakan template yang sama atau berbagi pengaturan renderer, kita cukup menuliskannya satu kali di bagian atas kelas.
