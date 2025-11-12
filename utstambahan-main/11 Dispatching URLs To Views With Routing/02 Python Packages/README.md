# 02: Python Packages for Pyramid Applications

## Tujuan Percobaan
Percobaan ini bertujuan untuk mempelajari bagaimana membangun aplikasi Pyramid dalam bentuk **Python package**. Berbeda dengan aplikasi satu file, pendekatan ini memberikan struktur proyek yang lebih profesional, modular, dan mudah dikembangkan.

## Analisa
- Dengan menggunakan Python package, setiap bagian aplikasi (views, templates, models, routes) dapat ditempatkan dalam file atau folder terpisah.
- File development.ini menjadi pusat konfigurasi server, log, dan environment.
- setup.py memungkinkan aplikasi dikenali oleh Pyramid dan digunakan bersama alat seperti pserve, pytest, dan WebTest.
- __init__.py menangani konfigurasi umum. Dan untuk views.py berfokus pada logika presentasi (request–response).
