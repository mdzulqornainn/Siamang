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
    tambah_riwayat (f"Tambah barang {nama}")
    self.refresh

def select_item(self, event):
    selected = self.tree.selection()
    if not selected:
        return
    data = self.tree.item(selected[0]) ["values"]
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
    item_id = self.tree.item(selected[0]) ["values"] [0]
    for item in barang:
        if item["id"] == item_id:
            item["nama"] == nama
            item["stok"] == stok
            item["harga"] == harga
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
    item_id = self.tree.item(selected[0]) ["values"] [0]
    nama_barang = self.tree.item(selected[0]) ["values"] [1]
    konfirmasi = messagebox.askyesno("Konfirmasi", f"Hapus barang'{nama_barang}'?")
    if not konfirmasi:
        return
    for item in barang[:]:
        if item["id"] == item_id:
            barang.remove(item)
            break
        save_json(BARANG_FILE, barang)
        tambah_riwayat(f"Hapus barang: {nama_barang}")
        self.refresh()

def cari_barang(self):
    keyword = self.cari.get().lower()
    self.tree.delete(*self.tree.get_children())
    for item in barang:
        if keyword in item["nama"].lower():
            self.tree.insert("", "end", values=(item["id"], item["nama"], item["stok"], item["harga"]))