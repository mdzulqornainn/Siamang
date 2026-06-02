# 📦 SiAmang (Sistem Aplikasi Manajemen Pesanan dan Gudang)

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/Tkinter-GUI-blueviolet?style=for-the-badge)
![JSON](https://img.shields.io/badge/Database-JSON-lightgrey?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-In%20Progress-orange?style=for-the-badge)

**SiAmang** adalah aplikasi desktop berbasis antarmuka grafis (GUI) yang dirancang untuk mempermudah pencatatan stok gudang dan memproses antrean pesanan secara sistematis. Aplikasi ini dibangun sepenuhnya menggunakan Python dengan pustaka bawaan Tkinter dan struktur penyimpanan data JSON.

## 👥 Anggota Kelompok

- **SALSABILA ISMA NUR ROHMA** — 2517052038
- **RANU SYANDANA SINGGIH** — 2517052045
- **NADINE IVANA T** — 25170520
- **MUHAMMAD DZULQORNAIN** — 2557052047

---

## ✨ Fitur Utama

- 📦 **Manajemen Barang (CRUD)**: Tambah, Perbarui, Hapus, dan Cari data barang (Pencarian Nama & _Binary Search_ ID).
- 📊 **Pengurutan Data (Sorting)**: Urutkan barang berdasarkan Nama, Stok, atau Harga menggunakan algoritma _Bubble Sort_.
- 🛒 **Sistem Antrean Pesanan (Queue)**: Pesanan diproses menggunakan konsep _First-In-First-Out_ (FIFO).
- ↩️ **Batalkan Pesanan (Stack)**: Fitur _Undo_ untuk membatalkan pesanan yang sudah diproses dan mengembalikan stok (LIFO).
- 📑 **Ekspor Laporan**: Simpan data barang saat ini ke dalam format file `.csv`.
- 🕒 **Riwayat Aktivitas**: Perekaman otomatis setiap aksi yang dilakukan oleh pengguna (Login, Tambah Barang, Proses Pesanan, dll).

---

## 🚀 Langkah Instalasi & Persiapan Menjalankan Aplikasi

Aplikasi ini tidak memerlukan konfigurasi _database server_ tambahan (karena menggunakan JSON) dan murni menggunakan _library_ bawaan Python, sehingga sangat mudah untuk dijalankan di komputer mana pun.

### 1. Prasyarat Sistem

Pastikan komputer Anda sudah terinstal:

- **Python** (Versi 3.8 atau lebih baru). Unduh di [python.org](https://www.python.org/downloads/).
- **Git** (Untuk menarik kode dari GitHub).

### 2. Cara Mengunduh (Clone) Kode

Buka aplikasi **Terminal** (Mac/Linux) atau **Command Prompt / PowerShell** (Windows), lalu jalankan perintah berikut:

```bash
git clone https://github.com/mdzulqornainn/Siamang.git
```

### 3. Masuk ke folder proyek

```bash
cd boox-box
```

### 4. Jalankan program

```bash
python main.py
```

---

## 🧩 Konsep yang Digunakan

Program ini memanfaatkan beberapa materi lanjutan seperti:

- GUI Programming menggunakan Tkinter
- Struktur Data: Queue (Antrean) dan Stack (Tumpukan)
- Algoritma: Binary Search dan Bubble Sort
- File Handling (JSON dan CSV)
- Variabel, List, Dictionary, dan Fungsi

---

## 🗂️ Struktur Folder

```
📁 siamang
│── main.py                # Program utama beserta GUI
│── users.json             # Penyimpanan data pengguna (dibuat otomatis)
│── barang.json            # Penyimpanan data stok barang (dibuat otomatis)
│── riwayat.json           # Penyimpanan log aktivitas (dibuat otomatis)
└── README.md              # Dokumentasi project
```
