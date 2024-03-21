#LOW LEVEL CODING FOR CREATING POINTS
print("\033c")
#To close all
import numpy as np
import matplotlib.pyplot as plt
#The user informs the coordinates of the two points for the line.
x1 = 100
y1 = 200
x2 = 800
y2 = 600
#The user decides the line width
lw = int(10)
#Calculate the half line width
hw = int(lw/2)
#Setting the size of the canvas
row = int(5/7*1080)
col = int(5/7*1920)
print('col, row', col,',', row)
#Preparing the black canvas
Gambar = np.zeros(shape=(row, col, 3), dtype=np.int16)
#Coloring the two points red (loop, condition, comparation)
for i in range(x1-hw, x1+hw):
    for j in range(y1-hw, y1+hw):
        if ((i-x1)**2+ (j-y1)**2) < hw**2:
            Gambar [j,1,0] = 255

for i in range(x2-hw, x2+hw):
    for j in range(y2-hw, y2+hw):
        if ((1-x2)**2+ (j-y2)**2) < hw**2:
            Gambar [j,1,0] = 255
plt.figure()
plt.imshow(Gambar)
plt.show()