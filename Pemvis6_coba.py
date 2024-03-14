import numpy as np
import matplotlib.pyplot as plt

print("\u033c")

# Inisialisasi ukuran gambar
rowmax = int(1079)
colmax = int(1919)
radius_max = int(1000)

# Pengaturan batas untuk penentuan warna pixel
batas1 = int(0.1 * radius_max)
batas2 = int(0.3 * radius_max)
batas3 = int(0.4 * radius_max)
batas4 = int(0.5 * radius_max)
batas5 = int(0.6 * radius_max)
batas6 = int(0.7 * radius_max)
batas7 = int(0.8 * radius_max)
batas8 = int(0.9 * radius_max)

# Inisialisasi gambar dengan semua nilai piksel set menjadi nol
Gambar = np.zeros(shape=(rowmax + 1, colmax + 1, 3), dtype=np.uint8)

# Iterasi melalui setiap piksel pada gambar
for i in range(0, rowmax + 1):
    for j in range(0, colmax + 1):
        # Memeriksa apakah nilai i^2 + j^2 berada dalam rentang tertentu dan menentukan warna piksel berdasarkan kondisi tersebut
        if (i**2 + j**2) >= 0 and (i**2 + j**2) < batas1**2:
            Gambar[i, j, :] = [255, 128, 0]  # Warna oranye
        elif (i**2 + j**2) >= batas1**2 and (i**2 + j**2) < batas2**2:
            Gambar[i, j, :] = [0, 255, 0]  # Warna hijau
        elif (i**2 + j**2) >= batas2**2 and (i**2 + j**2) < batas3**2:
            Gambar[i, j, :] = [255, 0, 0]  # Warna merah
        elif (i**2 + j**2) >= batas3**2 and (i**2 + j**2) < batas4**2:
            Gambar[i, j, :] = [0, 0, 255]  # Warna biru
        elif (i**2 + j**2) >= batas4**2 and (i**2 + j**2) < batas5**2:
            Gambar[i, j, :] = [255, 255, 0]  # Warna kuning
        elif (i**2 + j**2) >= batas5**2 and (i**2 + j**2) < batas6**2:
            Gambar[i, j, :] = [255, 0, 255]  # Warna ungu
        elif (i**2 + j**2) >= batas6**2 and (i**2 + j**2) < batas7**2:
            Gambar[i, j, :] = [0, 255, 255]  # Warna cyan
        elif (i**2 + j**2) >= batas7**2 and (i**2 + j**2) < batas8**2:
            Gambar[i, j, :] = [128, 128, 128]  # Warna abu-abu
        else:
            Gambar[i, j, :] = [255, 255, 255]  # Warna putih (luar batas)

# Menampilkan gambar
plt.figure(figsize=(10, 10))
plt.imshow(Gambar)
#plt.axis('off')  # Menyembunyikan sumbu
plt.show()
