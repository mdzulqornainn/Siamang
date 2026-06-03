import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from collections import deque
import json
import csv
import os
from datetime import datetime

USER_FILE = "users.json"
BARANG_FILE = "barang.json"
RIWAYAT_FILE = "riwayat.json"

def load_json(path, default):
    if os.path.exists(path):
        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            return default
    return default

def save_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

users = load_json(USER_FILE, [
    {
        "email": "admin@gmail.com",
        "username": "admin",
        "password": "admin123"
    }
])

barang = load_json(BARANG_FILE, [])
riwayat = load_json(RIWAYAT_FILE, [])

queue_pesanan = deque()
undo_stack = []

def generate_id_barang():
    if len(barang) == 0:
        return 1
    return max(item["id"] for item in barang) + 1

def tambah_riwayat(aktivitas):
    riwayat.append({
        "waktu": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
        "aktivitas": aktivitas
    })
    save_json(RIWAYAT_FILE, riwayat)

def bubble_sort(data, key):
    n = len(data)
    for i in range(n):
        for j in range(0, n - i - 1):
            if data[j][key] > data[j + 1][key]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data

class LoginWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Sistem Manajemen Gudang & Pesanan")
        self.root.geometry("500x500")
        self.root.configure(bg="#f4f6f9")
        self.ui_header()
        self.ui_login()
        self.root.mainloop()

    def ui_header(self):
        frame = tk.Frame(self.root, bg="#1f4e79", height=90)
        frame.pack(fill="x")
        tk.Label(frame, text="SISTEM MANAJEMEN GUDANG & PESANAN", bg="#1f4e79", fg="white", font=("Segoe UI", 14, "bold")).pack(pady=30)

    def ui_login(self):
        container = tk.Frame(self.root, bg="#f4f6f9")
        container.pack(pady=40)
        tk.Label(container, text="Email", bg="#f4f6f9").pack(anchor="w")
        self.email = ttk.Entry(container, width=35)
        self.email.pack(pady=5)
        tk.Label(container, text="Password", bg="#f4f6f9").pack(anchor="w")
        self.password = ttk.Entry(container, show="*", width=35)
        self.password.pack(pady=5)
        ttk.Button(container, text="Login", command=self.login).pack(fill="x", pady=10)
        ttk.Button(container, text="Register", command=self.register).pack(fill="x")

    def login(self):
        email = self.email.get()
        pw = self.password.get()
        for u in users:
            if u["email"] == email and u["password"] == pw:
                tambah_riwayat(f"Login: {u['username']}")
                self.root.destroy()
                Dashboard(u["username"])
                return
        messagebox.showerror("Gagal", "Email atau password salah")

    def register(self):
        win = tk.Toplevel(self.root)
        win.title("Register")
        win.geometry("350x300")
        tk.Label(win, text="Email").pack()
        email = ttk.Entry(win)
        email.pack()
        tk.Label(win, text="Username").pack()
        username = ttk.Entry(win)
        username.pack()
        tk.Label(win, text="Password").pack()
        password = ttk.Entry(win, show="*")
        password.pack()

        def simpan():
            e = email.get()
            u = username.get()
            p = password.get()
            if not e or not u or not p:
                messagebox.showerror("Error", "Semua field wajib diisi")
                return
            if "@" not in e:
                messagebox.showerror("Error", "Email tidak valid")
                return
            for user in users:
                if user["email"] == e:
                    messagebox.showerror("Error", "Email sudah terdaftar")
                    return
            users.append({"email": e, "username": u, "password": p})
            save_json(USER_FILE, users)
            tambah_riwayat(f"Register: {u}")
            messagebox.showinfo("Sukses", "Akun berhasil dibuat")
            win.destroy()

        ttk.Button(win, text="Simpan", command=simpan).pack(pady=10)

class Dashboard:
    def __init__(self, username):
        self.username = username
        self.root = tk.Tk()
        self.root.title("Sistem Manajemen Gudang & Pesanan")
        self.root.geometry("1300x750")
        self.root.configure(bg="#f4f6f9")
        self.style = ttk.Style()
        self.style.theme_use("clam")

        self.build_header()
        self.build_statistik()
        self.build_form_barang()
        self.build_table()
        self.build_pesanan()
        self.build_riwayat()
        self.refresh()
        self.root.mainloop()

    def build_header(self):
        frame = tk.Frame(self.root, bg="#1f4e79", height=80)
        frame.pack(fill="x")
        tk.Label(frame, text="SISTEM MANAJEMEN GUDANG & PESANAN", bg="#1f4e79", fg="white", font=("Segoe UI", 16, "bold")).pack(side="left", padx=20)
        tk.Label(frame, text=f"User: {self.username}", bg="#1f4e79", fg="white").pack(side="right", padx=20)

    def build_statistik(self):
        frame = tk.Frame(self.root, bg="#f4f6f9")
        frame.pack(fill="x", padx=10, pady=10)
        self.card_barang = tk.Label(frame, text="Barang: 0", bg="#ffffff", width=20)
        self.card_barang.pack(side="left", padx=10)
        self.card_stok = tk.Label(frame, text="Stok: 0", bg="#ffffff", width=20)
        self.card_stok.pack(side="left", padx=10)
        self.card_nilai = tk.Label(frame, text="Nilai: 0", bg="#ffffff", width=20)
        self.card_nilai.pack(side="left", padx=10)
        ttk.Button(frame, text="Logout", command=self.logout).pack(side="right")

    def build_form_barang(self):
        frame = tk.LabelFrame(self.root, text="Manajemen Barang")
        frame.pack(fill="x", padx=10, pady=5)
        tk.Label(frame, text="Nama Barang").grid(row=0, column=0)
        self.nama = ttk.Entry(frame, width=25)
        self.nama.grid(row=0, column=1, padx=5)
        tk.Label(frame, text="Stok").grid(row=0, column=2)
        self.stok = ttk.Entry(frame, width=25)
        self.stok.grid(row=0, column=3, padx=5)
        tk.Label(frame, text="Harga").grid(row=1, column=2)
        self.harga = ttk.Entry(frame, width=25)
        self.harga.grid(row=1, column=3, padx=5)
        ttk.Button(frame, text="Tambah", command=self.tambah_barang).grid(row=0, column=6, padx=5, pady=5)
        ttk.Button(frame, text="Update", command=self.update_barang).grid(row=0, column=7, padx=5, pady=5)
        ttk.Button(frame, text="Hapus", command=self.hapus_barang).grid(row=0, column=8, padx=5, pady=5)
        tk.Label(frame, text="Cari").grid(row=1, column=0)
        self.cari = ttk.Entry(frame, width=25)
        self.cari.grid(row=1, column=1)
        ttk.Button(frame, text="Cari Nama", command=self.cari_barang).grid(row=1, column=6, padx=5, pady=5)
        ttk.Button(frame, text="Cari ID", command=self.binary_search).grid(row=1, column=7, padx=5, pady=5)
        ttk.Button(frame, text="Urut Nama", command=self.sort_nama).grid(row=1, column=8, padx=5, pady=5)
        ttk.Button(frame, text="Urut Stok", command=self.sort_stok).grid(row=1, column=9, padx=5, pady=5)
        ttk.Button(frame, text="Urut Harga", command=self.sort_harga).grid(row=1, column=10, padx=5, pady=5)
        ttk.Button(frame, text="Export CSV", command=self.export_csv).grid(row=1, column=11, padx=5, pady=5)

    def build_table(self):
        frame = tk.Frame(self.root)
        frame.pack(fill="both", expand=True, padx=10, pady=10)
        columns = ("ID", "Nama", "Stok", "Harga")
        self.tree = ttk.Treeview(frame, columns=columns, show="headings")
        for c in columns:
            self.tree.heading(c, text=c)
            self.tree.column(c, width=150)
        self.tree.pack(fill="both", expand=True)
        self.tree.bind("<<TreeviewSelect>>", self.select_item)

    def refresh(self):
        self.tree.delete(*self.tree.get_children())
        total_stok = 0
        total_nilai = 0
        for b in barang:
            self.tree.insert("", "end", values=(b["id"], b["nama"], b["stok"], b["harga"]))
            total_stok += b["stok"]
            total_nilai += b["stok"] * b["harga"]
        self.card_barang.config(text=f"Barang: {len(barang)}")
        self.card_stok.config(text=f"Stok: {total_stok}")
        self.card_nilai.config(text=f"Nilai: Rp {total_nilai}")
        
        if hasattr(self, "tree_pesanan"):
            self.tree_pesanan.delete(*self.tree_pesanan.get_children())
            nomor = 1
            for pesanan in queue_pesanan:
                self.tree_pesanan.insert("", "end", values=(nomor, pesanan["barang"], pesanan["jumlah"]))
                nomor += 1
                
        if hasattr(self, "list_riwayat"):
            self.list_riwayat.delete(0, tk.END)
            for item in reversed(riwayat):
                self.list_riwayat.insert(tk.END, f"[{item['waktu']}] {item['aktivitas']}")

    def tambah_barang(self):
        try:
            nama = self.nama.get()
            stok = int(self.stok.get())
            harga = int(self.harga.get())
        except:
            messagebox.showerror("Error", "Stok & Harga harus angka")
            return
        if not nama:
            messagebox.showerror("Error", "Nama tidak boleh kosong")
            return
        data = {"id": generate_id_barang(), "nama": nama, "stok": stok, "harga": harga}
        barang.append(data)
        save_json(BARANG_FILE, barang)
        tambah_riwayat(f"Tambah barang {nama}")
        self.refresh()

    def select_item(self, event):
        selected = self.tree.selection()
        if not selected:
            return
        data = self.tree.item(selected[0])["values"]
        self.nama.delete(0, "end")
        self.stok.delete(0, "end")
        self.harga.delete(0, "end")
        self.nama.insert(0, data[1])
        self.stok.insert(0, data[2])
        self.harga.insert(0, data[3])

    def update_barang(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Peringatan", "Pilih data yang ingin diperbarui")
            return
        try:
            nama = self.nama.get().strip()
            stok = int(self.stok.get())
            harga = int(self.harga.get())
        except:
            messagebox.showerror("Error", "Stok dan Harga harus berupa angka")
            return
        item_id = self.tree.item(selected[0])["values"][0]
        for item in barang["id"] == item_id:
            item["nama"] = nama
            item["stok"] = stok
            item["harga"] = harga
            break
        save_json(BARANG_FILE, barang)
        tambah_riwayat(f"Perbarui Barang: {nama}")
        self.refresh()
        messagebox.showinfo("Berhasil", "Data berhasil diperbarui")

    def hapus_barang(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Peringatan", "Pilih data yang ingin dihapus")
            return
        item_id = self.tree.item(selected[0])["values"][0]
        nama_barang = self.tree.item(selected[0])["values"][1]
        konfirmasi = messagebox.askyesno("Konfirmasi", f"Hapus nama barang '{nama_barang}'?")
        if not konfirmasi:
            return
        for item in barang[:]:
            if item["id"] == item_id:
                barang.remove(item)
                break
        save_json(BARANG_FILE, barang)
        tambah_riwayat(f"Hapus Barang: {nama_barang}")
        self.refresh()

    def cari_barang(self):
        keyword = self.cari.get().lower()
        self.tree.delete(*self.tree.get_children())
        for item in barang:
            if keyword in item["nama"].lower():
                self.tree.insert("", "end", values=(item["id"], item["nama"], item["stok"], item["harga"]))

    def binary_search(self):
        try:
            target = int(self.cari.get())
        except:
            messagebox.showerror("Error", "Masukkan Id berupan angka")
            return
        data = sorted(barang, key=lambda x: x["id"])
        kiri = 0
        kanan = len(data) - 1
        while kiri <= kanan:
            tengah = (kiri + kanan) // 2
            if data[tengah]["id"] == target:
                hasil = data[tengah]
                messagebox.showinfo("Barang ditemukan", f"Id:{hasil['id']}\nNama: {hasil['nama']}\nStok: {hasil['stok']}\nHarga: {hasil['harga']:,}")
                return
            elif data[tengah]["id"] < target:
                kiri = tengah + 1
            else:
                kanan = tengah - 1
        messagebox.showwarning("Tidak ditemukan", "Id barang tidak ditemukan")
    
    def sort_nama(self):
        bubble_sort(barang, "nama")
        tambah_riwayat("Urutkan Data Berdasarkan Nama")
        self.refresh()
    
    def sort_stok(self):
        bubble_sort(barang, "stok")
        tambah_riwayat("Urutkan Data Berdasarkan Stok")
        self.refresh()

    def sort_harga(self):
        bubble_sort(barang, "harga")
        tambah_riwayat("Urutkan Data Berdasarkan Harga")
        self.refresh()
    
    def export_csv(self):
        lokasi = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV File", "*.csv")])
        if not lokasi:
            return
        with open(lokasi, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Id", "Nama Barang", "Stok", "Harga"])
            for item in barang:
                writer.writerow([item["id"], item["nama"], item["stok"], item["harga"]])
            tambah_riwayat("Ekspor Data CSV")
            messagebox.showinfo("Berhasil", "Data berhasil di ekspor")
    
    def logout(self):
        jawab = messagebox.askyesno("Logout", "Yakin ingin keluar?")
        if jawab: 
            tambah_riwayat(f"Logout: {self.username}")
            self.root.destroy()
            LoginWindow()

    def build_pesanan(self):
        frame = tk.LabelFrame(self.root, text="Manajemen Pesanan")
        frame.pack(fill="x", padx=10, pady=5)
        tk.LabelFrame(frame, text="Nama Barang").grid(row=0,column=0,padx=5,pady=5)
        self.pesanan_barang = ttk.Entry(frame, width=25)
        self.pesanan_barang.grid(row=0, column=1)
        tk.Label(frame, text="Jumlah").grid(row=0, coulmn=2)
        self.pesanan_jumlah = ttk.Entry(frame, width=10)
        self.pesanan_jumlah.grid(row=0, column=3)

        ttk.Button(frame, text="Tambah Pesanan", command=self.tambah_pesanan).grid(row=0, column=4, padx=5)
        ttk.Button(frame, text="Proses Pesanan", command=self.proses_pesanan).grid(row=0, column=5, padx=5)
        ttk.Button(frame, text="Batalkan Proses", command=self.undo_pesanan).grid(row=0, column=6, padx=5)
        ttk.Button(frame, text="Hapus Antrean", command=self.hapus_antrean_pesanan).grid(row=0, column=7, padx=5)

        columns = ("No", "Barang", "Jumlah")
        self.tree_pesanan = ttk.Treeview(frame, columns=columns, show="headings", height=5)
        for col in columns:
            self.tree_pesanan.heading(col, text=col)
            self.tree_pesanan.column(col, width=150)
        self.tree_pesanan.grid(row=1, column=0, columnspan=8, sticky="nsew", padx=5, pady=10)

    def hapus_antrean_pesanan(self):
        if not queue_pesanan:
            messagebox.showwarning("Kosong", "Tidak ada pesanan di antrean")
            return
        pesanan_batal = queue_pesanan.pop()
        tambah_riwayat(f"Hapus antrean : {pesanan_batal['barang']}")
        self.refresh()

    def tambah_pesanan(self):
        nama = self.pesanan_barang.get().strip()
        if not nama:
            messagebox.showerror("Error", "Nama barang wajib diisi")
            return
        try:
            jumlah = int(self.pesanan_jumlah.get())
        except:
            messagebox.showerror("Error", "Jumlah harus angka")
            return
        if jumlah <= 0:
            messagebox.showerror("Error", "Jumlah minimal 1")
            return
        queue_pesanan.append({"barang": nama, "jumlah": jumlah})
        tambah_riwayat(f"Tambah Pesanan : {nama} ({jumlah})")
        self.pesanan_barang.delete(0, tk.END)
        self.pesanan_jumlah.delete(0, tk.END)
        self.refresh()

    def proses_pesanan(self):
        if not queue_pesanan:
            messagebox.showwarning("Kosong", "Tidak ada pesanan")
            return
        pesanan = queue_pesanan.popleft()
        nama = pesanan["barang"]
        jumlah = pesanan["jumlah"]
        ditemukan = False
        for item in barang:
            if item["nama"].lower() == nama.lower():
                ditemukan = True
                if item["stok"] >= jumlah:
                    item["stok"] -= jumlah
                    undo_stack.append({"barang": nama, "jumlah": jumlah})
                    save_json(BARANG_FILE, barang)
                    tambah_riwayat(f"Proses FIFO : {nama}")
                    messagebox.showinfo("Berhasil", f"Pesanan {nama} diproses")
                else:
                    messagebox.showwarning("Stok Kurang", f"Stok tersedia {item['stok']}")
                    queue_pesanan.appendleft(pesanan)
                break
        if not ditemukan:
            messagebox.showwarning("Tidak Ditemukan", "Barang tidak ditemukan")
            queue_pesanan.appendleft(pesanan)
        self.refresh()

    def undo_pesanan(self):
        if not undo_stack:
            messagebox.showwarning("Kosong", "Tidak ada data undo")
            return
        data = undo_stack.pop()
        for item in barang:
            if item in barang:
                if item["nama"].lower() == data["barang"].lower():
                    item["stok"] += data["jumlah"]
                    save_json(BARANG_FILE, barang)
                    tambah_riwayat(f"Undo Pesanan : {data['barang']}")
                    break
            queue_pesanan.appendleft(data)
            self.refresh()

    def build_riwayat(self):
        frame = tk.LabelFrame(self.root, text="Riwayat Aktivitas")
        frame.pack(fill="both", expand=True, padx=10, pady=5)
        self.list_riwayat = tk.Listbox(frame, height=8)
        self.list_riwayat.pack(fill="both", expand=True, padx=5, pady=5)