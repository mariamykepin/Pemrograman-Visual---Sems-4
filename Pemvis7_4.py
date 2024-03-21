print('l033c')
import matplotlib.pyplot as plt
import numpy as np

def rumus_persamaan_garis(x1, y1, x2, y2):
    def persamaan(x):
        m = (y2 - y1) / (x2 - x1)
        y = m * (x - x1) + y1
        return y
    return persamaan

def membuat_lingkaran(x, y, radius, warna, gambar, row, col):
    for j in range(max(int(y - radius), 0), min(int(y + radius), row)):
        for i in range(max(int(x-radius), 0), min(int(x+radius), col)):
            if (i - x)**2 + (j - y):
                gambar[j,i] = warna
    return gambar
def garis_vertikal(x1, y1, x2, y2):
    def persamaan(y):
        m = (x2 - x1) / (y2 - y1)
        x = m * (y - y1) + x1
        return x
    return persamaan
# Menyatukan semua garis
# Lingkaran
# x^2 + y^2 = r^2
# y = sqrt(r^2 - x^2)

# set  col row baru
col = 1920
row = 1200
radius = 10
# reset canvas
bcg_canvas = np.zeros((row, col, 3), dtype=np.uint8)
bcg_canvas[:,:,:] = 0

# garis 1
titik_a = (100, 200)
titik_b = (1800, 1000)
# garis 2
titik_c = (100, 1000)
titik_d = (1800, 1000)
# garis 3
titik_e = (100, 200)
titik_f = (100, 1000)
# garis 4
titik_g = (200, 800)
titik_h = (700, 500)



# Gambar dua titik tujuan
membuat_lingkaran(titik_a[0], titik_a[1], 20, [213,85,239], bcg_canvas, row, col)
membuat_lingkaran(titik_b[0], titik_b[1], 20, [155,0,186], bcg_canvas, row, col)
membuat_lingkaran(titik_c[0], titik_c[1], 20, [213,85,239], bcg_canvas, row, col)
membuat_lingkaran(titik_d[0], titik_d[1], 20, [155,0,186], bcg_canvas, row, col)
membuat_lingkaran(titik_e[0], titik_e[1], 20, [213,85,239], bcg_canvas, row, col)
membuat_lingkaran(titik_f[0], titik_f[1], 20, [155,0,186], bcg_canvas, row, col)
membuat_lingkaran(titik_g[0], titik_g[1], 20, [213,85,239], bcg_canvas, row, col)
membuat_lingkaran(titik_h[0], titik_h[1], 20, [155,0,186], bcg_canvas, row, col)


# garis 1
for x in range(max(titik_a[0] - 50, 0), min(titik_b[0] + 50, col)):
    y = rumus_persamaan_garis(titik_a[0],titik_a[1],titik_b[0],titik_b[1])
    warna = [255, 0, 255]  # RGB color
    membuat_lingkaran(x, int(y(x)), radius, warna, bcg_canvas, row, col)

# garis 2
for x in range(max(titik_c[0] - 50, 0), min(titik_d[0] + 50, col)):
    y = rumus_persamaan_garis(titik_c[0],titik_c[1],titik_d[0],titik_d[1])
    warna = [0, 255, 255]  # RGB color
    membuat_lingkaran(x, int(y(x)), radius, warna, bcg_canvas, row, col)

# garis 3
for y in range(max(titik_e[1] - 50, 0), min(titik_f[1] + 50, row)):
    x = garis_vertikal(titik_e[0], titik_e[1], titik_f[0], titik_f[1])
    warna = [255, 255, 0]  # RGB color
    membuat_lingkaran(int(x(y)), y, radius, warna, bcg_canvas, row, col)

# garis 4
for x in range(max(titik_g[0], 0), min(titik_h[0], col)):
    y = rumus_persamaan_garis(titik_g[0],titik_g[1],titik_h[0],titik_h[1])
    warna = [0, 255, 255]  # RGB color
    membuat_lingkaran(x, int(y(x)), radius, warna, bcg_canvas, row, col)


#Set lebar canvas sesuai dengan resolusi
plt.figure(figsize=(20,20))
plt.imshow(bcg_canvas)
plt.show()