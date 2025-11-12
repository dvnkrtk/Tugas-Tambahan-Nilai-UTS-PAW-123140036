# 11: Dispatching URLs To Views With Routing

## Tujuan Percobaan
Percobaan ini bertujuan untuk memahami bagaimana framework Pyramid melakukan dispatching URL ke fungsi view menggunakan sistem routing. Routing merupakan mekanisme yang menentukan fungsi atau kelas mana yang akan dipanggil berdasarkan URL yang diakses oleh pengguna. Dengan routing, aplikasi dapat merespons berbagai endpoint dengan cara yang terstruktur dan mudah dikelola.

## Analisis
Berdasarkan hasil percobaan, dapat dipahami bahwa routing di Pyramid berfungsi sebagai penghubung antara URL dan view function. Setiap kali pengguna mengakses URL tertentu, Pyramid akan mencari route yang cocok, lalu mengeksekusi view yang terdaftar dengan route tersebut.