def binary_search(self):
    try:
        target = int(self.cari.get())
    except:
        messagebox.showerror("Error", "Masukkan Id berupa angka")
        return
    data = sorted(barang, key=lambda x: x["id"])
    kiri = 0
    kanan = len(data) - 1
    while kiri <= kanan:
        tengah = (kiri + kanan) // 2
        if data[tengah]["id"] == target:
            hasil = data[tengah]
            messagebox.showinfo("Barang ditemukan", f"Id: {hasil['id']}\nNama: {hasil['nama']}\nStok:{hasil['stok']}\nHarga: Rp{hasil['harga']:,}")
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
        writer.writerow(["Id", "nama Barang", "Stok", "Harga"])
        for item in barang:
            writer.writerow([item["id"], item["nama"], item["stok"], item["harga"]])
    tambah_riwayat("Ekspor Data CSV")
    messagebox.showinfo("berhasil", "Data berhasil di ekspor")

def logout(self):
    jawab = messagebox.askyesno("Logout", "Yakin ingin keluar?")
    if jawab:
        tambah_riwayat(f"Logout: {self.username}")
        self.root.destroy()
        LoginWindow()