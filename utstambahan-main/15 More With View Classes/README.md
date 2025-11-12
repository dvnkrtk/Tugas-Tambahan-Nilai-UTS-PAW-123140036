# 15: More With View Classes

## Tujuan Percobaan
Percobaan ini bertujuan untuk memahami penggunaan View Classes lebih lanjut di framework Pyramid, khususnya bagaimana cara menangani banyak view dengan logika yang berkaitan dalam satu kelas. Dengan pendekatan ini, kode menjadi lebih terstruktur, mudah dikelola, serta memudahkan proses pengembangan aplikasi berskala besar.

## Analisis
Dalam percobaan ini, konsep utama yang dipelajari adalah bagaimana View Class dapat menampung berbagai handler (fungsi view) untuk beberapa route berbeda namun masih dalam konteks yang sama. Pyramid menyediakan cara mudah untuk mendefinisikan view dengan class menggunakan dekorator `@view_config`.  