import tkinter as tk
from PIL import Image, ImageTk

# Fungsi untuk membuka gambar
def buka_gambar():
  global gambar_asli, lebar_asli, tinggi_asli

  # Membuka file gambar yang dipilih
  filepath = tk.filedialog.askopenfilename(title="Pilih Gambar", filetypes=[("Gambar", "*.jpg *.png *.jpeg")])

  if filepath:
    gambar_asli = Image.open(filepath)
    lebar_asli, tinggi_asli = gambar_asli.size

    # Menampilkan gambar asli di label
    gambar_asli = gambar_asli.resize((300, 300))
    gambar_asli = ImageTk.PhotoImage(gambar_asli)
    label_gambar_asli.configure(image=gambar_asli)
    label_gambar_asli.image = gambar_asli

# Fungsi untuk mengubah ukuran gambar
def ubah_ukuran():
  global gambar_asli, lebar_baru, tinggi_baru

  # Mendapatkan nilai lebar dan tinggi baru dari entry field
  try:
    lebar_baru = int(entry_lebar.get())
    tinggi_baru = int(entry_tinggi.get())
  except ValueError:
    tk.messagebox.showerror("Kesalahan", "Lebar dan tinggi harus berupa angka!")
    return

  # Mengubah ukuran gambar
  if lebar_baru > 0 and tinggi_baru > 0:
    gambar_baru = gambar_asli.resize((lebar_baru, tinggi_baru))
    gambar_baru = ImageTk.PhotoImage(gambar_baru)

    # Menampilkan gambar yang diubah ukurannya di label
    label_gambar_baru.configure(image=gambar_baru)
    label_gambar_baru.image = gambar_baru

# Membangun antarmuka grafis
window = tk.Tk()
window.title("Aplikasi Pengubah Ukuran Gambar")

# Label untuk gambar asli
label_gambar_asli = tk.Label(window)
label_gambar_asli.pack()

# Tombol untuk membuka gambar
tombol_buka = tk.Button(window, text="Buka Gambar", command=buka_gambar)
tombol_buka.pack()

# Entry field untuk lebar dan tinggi baru
label_lebar = tk.Label(window, text="Lebar Baru:")
label_lebar.pack()

entry_lebar = tk.Entry(window)
entry_lebar.pack()

label_tinggi = tk.Label(window, text="Tinggi Baru:")
label_tinggi.pack()

entry_tinggi = tk.Entry(window)
entry_tinggi.pack()

# Tombol untuk mengubah ukuran gambar
tombol_ubah = tk.Button(window, text="Ubah Ukuran", command=ubah_ukuran)
tombol_ubah.pack()

# Label untuk gambar yang diubah ukurannya
label_gambar_baru = tk.Label(window)
label_gambar_baru.pack()

# Menjalankan program
window.mainloop()
