# CASE: MENENTUKAN WARNA PIXEL BERDASARKAN POSISI PIXEL DENGAN KONDISI DAN KOMPARASI

# Masukkan posisi pixel pada layar (nomor baris)
pixel_row = 100
rowmax = int(1079)
batas1 = int(0.5 * rowmax)
print("batas1: ", batas1)
print("Posisi pixel berada pada baris ke-", pixel_row)

if pixel_row < batas1:
    print("Warnai pixel merah.")
elif pixel_row == batas1:
    print("Warnai pixel hitam.")
elif pixel_row > batas1:
    print("Warnai pixel putih.")
elif pixel_row <= batas1:
    print("Warnai pixel kuning.")
elif pixel_row > batas1:
    print("Warnai pixel ungu.")
