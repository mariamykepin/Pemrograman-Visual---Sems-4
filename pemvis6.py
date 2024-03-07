import numpy as np
import matplotlib.pyplot as plt

# Titik koordinat
x1, y1 = 100, 100
x2, y2 = 300, 400
x3, y3 = 500, 100

# Ukuran gambar
row, col = 600, 600

# Warna garis
lr, lg, lb = 255, 0, 0  # Merah

# Membuat array kosong untuk gambar
gambar = np.zeros(shape=(row, col, 3), dtype=np.uint8)

def buat_garis(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    err = dx - dy

    while x1 != x2 or y1 != y2:
        gambar[y1, x1] = [lr, lg, lb]
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x1 += sx
        if e2 < dx:
            err += dx
            y1 += sy

# Menggambar segitiga dengan tiga garis
buat_garis(x1, y1, x2, y2)
buat_garis(x2, y2, x3, y3)
buat_garis(x3, y3, x1, y1)

# Menampilkan gambar
plt.imshow(gambar)
plt.show()
