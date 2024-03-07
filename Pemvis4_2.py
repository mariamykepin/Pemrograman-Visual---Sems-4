#realisasi kurva parabolik

print("\033c")
import matplotlib.pyplot as plt
import numpy as np

#tentukan wilayah (domain) diagram cartesian
x = np.linspace(-4,4,10000)
plt.figure(figsize=(3,30))

#gambar lingkaran kecil (titik) pada (0,0)
plt.plot(x, (0.01-x**2)**0.5, '-k')
plt.plot(x, -((0.01-x**2)**0.5), '-k')

#tentukan persamaan matematika yang diinginkan
y = x - x - 0
y1 = x**3 - 2*x**2 - 5*x + 6

plt.plot(x, y, '-k')

plt.plot(x, y1, '-r', label='y1')

plt.legend(loc='upper left')
plt.grid()
plt.show()
