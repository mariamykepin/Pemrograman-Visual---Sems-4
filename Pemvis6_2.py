def hitung_ppn(nilai):
    if nilai > 10000:
        return nilai * 0.12
    else:
        return 0

try:
    # Input nilai a dan b
    a = float(input("Masukkan nilai a: "))
    b = float(input("Masukkan nilai b: "))

    # Cek boolean a lebih besar dari b
    print("a lebih besar dari b:", a > b)

    # Cek boolean b lebih besar dari a
    print("b lebih besar dari a:", b > a)

    # Cek boolean a sama dengan b
    print("a sama dengan b:", a == b)

    # Hitung PPN a dan b
    ppn_a = hitung_ppn(a)
    ppn_b = hitung_ppn(b)

    # Tambahkan kedua PPN
    total_ppn = ppn_a + ppn_b

    # Cek boolean dari total PPN agar hasilnya True
    print("Total PPN lebih besar dari 0:", total_ppn > 0)

except ValueError:
    print("Masukan harus berupa angka.")
except NameError:
    print("Nilai a atau b tidak ditemukan karena terjadi kesalahan saat penginputan.")

# Hapus nilai a dan b
del a
del b

# Cek boolean apakah nilai a masih ada setelah dihapus, atur agar hasilnya False
try:
    print("Nilai a masih ada setelah dihapus:", bool(a) == True)
except NameError:
    print("Nilai a masih ada? : False")

# Cek boolean apakah nilai b masih ada setelah dihapus, atur agar hasilnya False
try:
    print("Nilai b masih ada setelah dihapus:", bool(b) == True)
except NameError:
    print("Nilai b masih ada? : False")
