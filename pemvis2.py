print("\033c")
#import libraries
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

#Menentukan titik koordinat
x1= 100; y1= 200
x2= 700; y2=700

#line width and calculate
lw = int(10)
hw = int(lw/2)

#Setting canva size
col = int(800)
row = int(800)
#col = int(5/7*71920)
#row = int(5/7*1000)
print('col, row =', col, ',', row)

#Black Canvas
gambar = np.zeros(shape=(row,col,3), dtype=np.uint8)
gambar [:,:,:] = 255

#gambar titik dengan pixel
gambar[y1,x2,:]=0
gambar[y2,x2,:]=0
gambar[y1,x1,:]=255
gambar[y2,x2,:]-255

#Coloring two points red

for i in range (x1-hw, x1+hw):
    for j in range(y1-hw, y1+hw):
        if ((i-x1)**2 + (j-y1)**2) < hw **2 :
            gambar[j,i,:] = 0
            gambar [j,i,0] = 255
for i in range(x2-hw, x2+hw):
    for j in range(y2-hw, y2+hw):
        if((i-x2)**2 + (j-y2)**2) < hw **2 :
            gambar[j,i,:]=0
            gambar [j,i,0] = 255

plt.figure()
plt.imshow(gambar)
plt.show()
