# Buat set berisi beberapa buah-buahan
buah = {"apel", "pisang", "jeruk", "anggur"}

# Fungsi untuk mencetak semua buah
def cetak_semua():
    print("Buah-buahan di kantong:", buah)

# Fungsi untuk mencetak jumlah buah-buahan dalam set
def cetak_jumlah():
    print("Jumlah buah yang di kantong:", len(buah))

# Fungsi untuk menambahkan buah baru ke dalam set
def tambah_buah(nama_buah):
    buah.add(nama_buah)
    print(nama_buah, "berhasil diambil.")

# Fungsi untuk mengupdate set dengan buah-buahan baru
def update_buah(buah_baru):
    buah.update(buah_baru)
    print("Kantong kreseknya buah telah diganti.")

# Fungsi untuk menghapus buah dari set
def hapus_buah(nama_buah):
    try:
        buah.remove(nama_buah)
        print(nama_buah, "telah dimakan.")
    except KeyError:
        print(nama_buah, "tidak ada, udah dimakan.")

# Fungsi untuk menghapus buah dari set tanpa menghasilkan KeyError jika tidak ditemukan
def hapus_buah_tanpa_keyerror(nama_buah):
    buah.discard(nama_buah)
    print(nama_buah, "hilang ditelan perut, hehe.")

# Fungsi untuk menghapus dan mengembalikan sebuah item secara acak dari set
def hapus_dan_kembalikan():
    item = buah.pop()
    print("Buah jatuh di jalan:", item)

# Fungsi untuk menghapus semua item dari set
def hapus_semua():
    buah.clear()
    print("Buah membusuk semua.")

# Fungsi untuk menggabungkan dua set buah-buahan
def gabung_set(set_lain):
    gabungan = buah.union(set_lain)
    print("Buah halal lainnya:", gabungan)

# Tambahkan 5 buah-buahan lagi
tambah_buah("nanas")
tambah_buah("mangga")
tambah_buah("durian")
tambah_buah("salak")
tambah_buah("rambutan")

# Demonstrasi penggunaan fungsi-fungsi di atas
cetak_semua()
cetak_jumlah()
update_buah({"nanas", "melon"})
cetak_semua()
hapus_buah("mangga")
hapus_buah_tanpa_keyerror("mangga")
hapus_dan_kembalikan()
cetak_semua()
hapus_semua()
cetak_semua()

# Contoh penggabungan set
set_buah_lain = {"kiwi", "stroberi", "melon", "semangka", "apel"}
gabung_set(set_buah_lain)

cetak_semua(gabung_set)
