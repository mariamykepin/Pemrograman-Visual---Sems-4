#LOW LEVEL CODING FOR CREATING POINTS
print("\033c")
#To close all
import numpy as np
import matplotlib.pyplot as plt
#The user informs the coordinates of the two points for the line.
ya = 200; xa = 100
yb = 200; xb = 1800

pd = int(20); pr = 255; pg = 0; pb = 255
lw = int(20); lr = 255; lg = 0; lb = 255

#The user decides the line width
lw = int(10)
#Calculate the half line width
hw = int(lw/2)
#Setting the size of the canvas
row = int(5/7*5000)
col = int(5/7*5000)
print('col, row', col,',', row)
#Preparing the black canvas


def buat_garis(y1, x1, y2, x2, pd, lw, pr, pg, pb, lr, lg, lb):
    Gambar = np.zeros(shape=(row, col, 3), dtype=np.uint8)
    hd = int(pd / 2)
    hw = int(lw / 2)
    dy = y2 - y1
    dx = x2 - x1

    # First point
    for i in range(x1 - hd, x1 + hd):
        for j in range(y1 - hd, y1 + hd):
            if ((i - x1) ** 2 + (j - y1) ** 2) < hd ** 2:
                Gambar[j, i, 0] = pr
                Gambar[j, i, 1] = pg
                Gambar[j, i, 2] = pb

    # Second point
    for i in range(x2 - hd, x2 + hd):
        for j in range(y2 - hd, y2 + hd):
            if ((i - x2) ** 2 + (j - y2) ** 2) < hd ** 2:
                Gambar[j, i, 0] = pr
                Gambar[j, i, 1] = pg
                Gambar[j, i, 2] = pb

    # Draw the line
    if dy == 0:  # Horizontal line
        for i in range(min(x1, x2), max(x1, x2)):
            for j in range(y1 - hw, y1 + hw):
                for k in range(j - hw, j + hw):
                    Gambar[k, i, 0] = lr
                    Gambar[k, i, 1] = lg
                    Gambar[k, i, 2] = lb
    elif dx == 0:  # Vertical line
        for j in range(min(y1, y2), max(y1, y2)):
            for i in range(x1 - hw, x1 + hw):
                for k in range(i - hw, i + hw):
                    Gambar[j, k, 0] = lr
                    Gambar[j, k, 1] = lg
                    Gambar[j, k, 2] = lb
    else:  # Diagonal line
        if abs(dy) <= abs(dx):
            my = dy / dx
            for i in range(x1, x2):
                j = int(my * (i - x1) + y1)
                for k in range(j - hw, j + hw):
                    for l in range(i - hw, i + hw):
                        Gambar[k, l, 0] = lr
                        Gambar[k, l, 1] = lg
                        Gambar[k, l, 2] = lb
        else:
            mx = dx / dy
            for j in range(y1, y2):
                i = int(mx * (j - y1) + x1)
                for k in range(j - hw, j + hw):
                    for l in range(i - hw, i + hw):
                        Gambar[k, l, 0] = lr
                        Gambar[k, l, 1] = lg
                        Gambar[k, l, 2] = lb
    return Gambar


hasil = buat_garis(ya, xa, yb, xb, pd, lw, pr, pg, pb, lr, lg, lb)
plt.figure()
plt.imshow(hasil)
plt.show()