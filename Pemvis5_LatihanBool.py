print("Case 1")
#Data bertipe Boolean yang Kita Deklarasikan (Cara Standar)
f = bool (True)
g = bool (False)
print(f)
print(g)
print("=================================")
#Case 2
print("Case 2")
#Data Bertipe Boolean Dalam Berbagai Konteks
#Tercatat Dengan Sendirinya oleh Komputer tanpa Deklarasi.
print(6 > 2)
print(6 + 2 == 10)  # Mengganti 5 dengan 10
print(6 < 2)
print("========================================")

print("Case 3")
#Data Bertipe Boolean Dalam Berbagai Konteks
#Tercatat Dengan Sendirinya oleh Komputer tanpa Deklarasi.
Penghasilan = 252525525252525
PenghasilanTanpaPajak = 45454545455454545
if Penghasilan <= PenghasilanTanpaPajak:
    PajakYangHarusDibayar = 93847
if Penghasilan > PenghasilanTanpaPajak:
    PajakYangHarusDibayar = 0.1 * Penghasilan
print("Pajak yang harus Anda bayar: Rp", PajakYangHarusDibayar)

#PART 2
#Case 4
print("=============================================")
print("Case 4")
#Semua data yang tidak nol (kosong) memiliki nilai Boolean True
#1
a = 5
b = "Ini data string."
c = ("sedih", "senang", "marah")
d = ["sedih", "senang", "marah"]
e = {"sedih": "senang", "marah":"air_mata", "bibir": "lidah"}
f = (1, 2, 3, 4, 5)
print(bool(a))
print(bool(b))
print(bool(c))
print(bool(d))
print(bool(e))
print(bool(f))
print("======================================")

#Case 5
print("Case 5")
#Variabel yang kosong memiliki nilai Boolean False
a = 0
b = ""
c = ()
d = []
e = {}
print(bool(a))
print(bool(b))
print(bool(c))
print(bool(d))
print(bool(e))
print("===================================================")


#Case 6
print("Case 6")
#Variabel yang panjangnya not memiliki nilai Boolean False

class myclass():
    def __len__(self):
        return 0
print(bool(myclass()))
print("==========================================")

