# Program membuat garis dan objek
print('l033c')
import numpy as np
import matplotlib.pyplot as plt

# Titik koordinat
y1 = 200
x1 = 100
y2 = 1000
x2 = 100

# Vertex diameter
pd = int(6); pr = 255; pg = 255; pb = 0
lw = int(6); lr = 255; lg = 255; lb = 0

col = int(1000)
row = int(2000)
print('col,row=', col, ',', row)

def buatgaris(y1, x1, y2, x2, pd, lw, pr, pg, pb, lr, lg, lb):
    gambar = np.zeros(shape=(row, col, 3), dtype=np.uint8)
    hd = int(pd/2)
    hw = int(lw/2)
    dy = y2 - y1
    dx = x2 - x1

    # Draw first point
    for i in range(x1-hd, x1+hd):
        for j in range(y1-hd, y1+hd):
            if ((i-x1)**2 + (j-y1)**2) < hd**2:
                gambar[j, i, 0] = pr
                gambar[j, i, 1] = pg
                gambar[j, i, 2] = pb

    # Draw second point
    for i in range(x2-hd, x2+hd):
        for j in range(y2-hd, y2+hd):
            if ((i-x2)**2 + (j-y2)**2) < hd**2:
                gambar[j, i, 0] = pr
                gambar[j, i, 1] = pg
                gambar[j, i, 2] = pb

    # Use Bresenham's algorithm to draw the line
    x, y = x1, y1
    dx, dy = abs(x2 - x1), abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    if dy <= dx:
        err = dx / 2.0
        while x != x2:
            for i in range(x-hw, x+hw):
                for j in range(y-hw, y+hw):
                    if (i >= 0 and i < col) and (j >= 0 and j < row):
                        gambar[j, i, 0] = lr
                        gambar[j, i, 1] = lg
                        gambar[j, i, 2] = lb
            err -= dy
            if err < 0:
                y += sy
                err += dx
            x += sx
    else:
        err = dy / 2.0
        while y != y2:
            for i in range(x-hw, x+hw):
                for j in range(y-hw, y+hw):
                    if (i >= 0 and i < col) and (j >= 0 and j < row):
                        gambar[j, i, 0] = lr
                        gambar[j, i, 1] = lg
                        gambar[j, i, 2] = lb
            err -= dx
            if err < 0:
                x += sx
                err += dy
            y += sy

    return gambar

# Main program
hasil = buatgaris(y1, x1, y2, x2, pd, lw, pr, pg, pb, lr, lg, lb)

plt.figure()
plt.imshow(hasil)
plt.show()
