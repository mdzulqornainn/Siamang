# 📦 SiAmang (Sistem Aplikasi Manajemen Pesanan dan Gudang)

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/Tkinter-GUI-blueviolet?style=for-the-badge)
![JSON](https://img.shields.io/badge/Database-JSON-lightgrey?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

**SiAmang** adalah aplikasi desktop berbasis antarmuka grafis (GUI) yang dirancang untuk mempermudah pencatatan stok gudang dan memproses antrean pesanan secara sistematis. Aplikasi ini dibangun sepenuhnya menggunakan Python dengan pustaka bawaan Tkinter dan struktur penyimpanan data JSON.

---

## ✨ Fitur Utama

- 📦 **Manajemen Barang (CRUD)**: Tambah, Perbarui, Hapus, dan Cari data barang (Pencarian Nama & *Binary Search* ID).
- 📊 **Pengurutan Data (Sorting)**: Urutkan barang berdasarkan Nama, Stok, atau Harga menggunakan algoritma *Bubble Sort*.
- 🛒 **Sistem Antrean Pesanan (Queue)**: Pesanan diproses menggunakan konsep *First-In-First-Out* (FIFO).
- ↩️ **Batalkan Pesanan (Stack)**: Fitur *Undo* untuk membatalkan pesanan yang sudah diproses dan mengembalikan stok (LIFO).
- 📑 **Ekspor Laporan**: Simpan data barang saat ini ke dalam format file `.csv`.
- 🕒 **Riwayat Aktivitas**: Perekaman otomatis setiap aksi yang dilakukan oleh pengguna (Login, Tambah Barang, Proses Pesanan, dll).

---

## 🚀 Langkah Instalasi & Persiapan Menjalankan Aplikasi

Aplikasi ini tidak memerlukan konfigurasi *database server* tambahan (karena menggunakan JSON) dan murni menggunakan *library* bawaan Python, sehingga sangat mudah untuk dijalankan di komputer mana pun.

### 1. Prasyarat Sistem
Pastikan komputer Anda sudah terinstal:
- **Python** (Versi 3.8 atau lebih baru). Unduh di [python.org](https://www.python.org/downloads/).
- **Git** (Untuk menarik kode dari GitHub).

### 2. Cara Mengunduh (Clone) Kode
Buka aplikasi **Terminal** (Mac/Linux) atau **Command Prompt / PowerShell** (Windows), lalu jalankan perintah berikut:
```bash
git clone [https://github.com/USERNAME_GITHUB/NAMA_REPOSITORY.git](https://github.com/USERNAME_GITHUB/NAMA_REPOSITORY.git)