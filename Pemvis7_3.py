import numpy as np
import matplotlib.pyplot as plt

def buat_garis(y1, x1, y2, x2, pd, lw, pr, pg, pb, lr, lg, lb):
    Gambar = np.zeros(shape=(row, col, 3), dtype=np.uint8)
    hd = int(pd / 2)
    hw = int(lw / 2)

    # Draw the first point
    for i in range(x1 - hd, x1 + hd):
        for j in range(y1 - hd, y1 + hd):
            if ((i - x1) * 2 + (j - y1) * 2) < hd ** 2:
                if 0 <= i < col and 0 <= j < row:
                    Gambar[j, i, 0] = pr
                    Gambar[j, i, 1] = pg
                    Gambar[j, i, 2] = pb

    # Draw the second point
    for i in range(x2 - hd, x2 + hd):
        for j in range(y2 - hd, y2 + hd):
            if ((i - x2) * 2 + (j - y2) * 2) < hd ** 2:
                if 0 <= i < col and 0 <= j < row:
                    Gambar[j, i, 0] = pr
                    Gambar[j, i, 1] = pg
                    Gambar[j, i, 2] = pb

    # Draw the line (vertical)
    if x1 == x2:
        for j in range(min(y1, y2), max(y1, y2)):
            for i in range(x1 - hw, x1 + hw):
                if 0 <= i < col and 0 <= j < row:
                    Gambar[j, i, 0] = lr
                    Gambar[j, i, 1] = lg
                    Gambar[j, i, 2] = lb

    # Draw the line (diagonal)
    elif abs(y2 - y1) <= abs(x2 - x1):
        my = (y2 - y1) / (x2 - x1)
        for i in range(x1, x2):
            j = int(my * (i - x1) + y1)
            for k in range(j - hw, j + hw):
                for l in range(i - hw, i + hw):
                    if 0 <= l < col and 0 <= k < row:
                        Gambar[k, l, 0] = lr
                        Gambar[k, l, 1] = lg
                        Gambar[k, l, 2] = lb

    # Draw the line (diagonal)
    else:
        mx = (x2 - x1) / (y2 - y1)
        for j in range(y1, y2):
            i = int(mx * (j - y1) + x1)
            for k in range(j - hw, j + hw):
                for l in range(i - hw, i + hw):
                    if 0 <= l < col and 0 <= k < row:
                        Gambar[k, l, 0] = lr
                        Gambar[k, l, 1] = lg
                        Gambar[k, l, 2] = lb

    return Gambar

# Parameters
ya = 400; xa = 1800
yb = 200; xb = 1800
pd = 20; pr = 255; pg = 0; pb = 255
lw = 10; lr = 255; lg = 0; lb = 255

# Calculate the half line width
hw = int(lw/2)
# Setting the size of the canvas
row = int(5/7*5000)
col = int(5/7*5000)
print('col, row', col,',', row)

hasil = buat_garis(ya, xa, yb, xb, pd, lw, pr, pg, pb, lr, lg, lb)
plt.figure()
plt.imshow(hasil)
plt.show()