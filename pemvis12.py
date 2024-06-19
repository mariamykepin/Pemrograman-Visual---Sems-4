from tkinter import *

print('====================Exercise#1=====================')
print('===Mencetak data dari Entry Widget dengan Button===')
print('=============')

root = Tk()
root.geometry('400x200')

def CetakData():
    teks = entry1.get()
    print(teks)
    return None

entry1 Entry(root, width = 20); entry1.pack()
Button (root, text="Cetak Data", command=CetakData).pack()

root.mainloop()