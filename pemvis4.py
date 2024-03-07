#Program membuat garis dan objek
print('l033c')
import numpy as np
import matplotlib.pyplot as plt

#Titik koordinat
y1 = 600
x1 = 200
y2 = 200
x2 = 600

#Vertex diameter
pd = int(6); pr = 255; pg = 255; pb =0
lw = int(6); lr= 255; lg = 255; lb = 0

col= int(800)
row = int(800)
print('col,row=', col,',', row)

def buatgaris(y1,x1,y2,x2,pd,lw,pr,pg,pb,lr,lg,lb):
    gambar=np.zeros(shape=(row,col,3), dtype=np.int16)
    hd = int(pd/2)
    hw = int(lw/2)
    dy = y2-y1
    dx = x2-x1

    #draw first point
    for i in range(x1-hd, x1+hd):
        for j in range(y1-hd, y1+hd):
            if((i-x1)**2 + (j-y1)**2)< hd **2:
                gambar[j,i,0]= pr
                gambar[j,i,1]= pg
                gambar[j,i,2]= pb
    #draw second point
    for i in range(x2-hd, x2+hd):
        for j in range(y2-hd, y2+hd):
            if((i-x2)**2 + (j-y2)**2)< hd **2:
                gambar[j,i,0]= pr
                gambar[j,i,1]= pg
                gambar[j,i,2]= pb
    #draw line horizontal
    if dy<=dx:
        my = dy/dx
        for i in range(x1,x2):
            j= int(my*(i-x1) + y1)
            x=i
            y=j
            print('x,y =', x, ',',y)
            for i in range(x-hw,x+hw):
                for j in range(y-hw, y+hw):
                    if((i-x)**2 + (j-y)**2)<hw**2:
                        gambar[j,i,0]=lr
                        gambar[j,i,1]=lg
                        gambar[j,i,0]=lb
    #vertical
    if dy>dx:
        mx = dx/dy
        for j in range(y1,y2):
            i = int(mx * (j-y1) * x1)
            x = i
            y = j
            print('x,y=', x,',',y)
            for i in range(x-hw, x+hw):
                for j in range(y-hw,y+hw):
                    if( (i-x)**2 + (j-y)**2)< hw **2:
                        gambar[j,i,0]=lr
                        gambar[j,i,1]=lg
                        gambar[j,i,0]=lb
    return gambar


    return gambar

#main program
hasil = buatgaris(y1,x1,y2,x2,pd,lw,pr,pg,pb,lr,lg,lb)

plt.figure()
plt.imshow(hasil)
plt.show()
