import matplotlib.pyplot as plt

# Inisialisasi data
x = range(-10, 11)
y1 = [2*i for i in x]  # Garis lurus y = 2x
y2 = [i**2 for i in x]  # Parabola y = x^2

# Plot data
for i in range(len(x)):
    if x[i] < 0 and y1[i] < 0:
        plt.scatter(x[i], y1[i], color='red', label='y = 2x' if i == 0 else "")
    elif x[i] >= 0 or y1[i] >= 0:
        plt.scatter(x[i], y1[i], color='blue', label='y = 2x' if i == 0 else "")
    if y2[i] < 0 and x[i] < 0:
        plt.scatter(x[i], y2[i], color='green', label='y = x^2' if i == 0 else "")
    elif y2[i] >= 0 or x[i] >= 0:
        plt.scatter(x[i], y2[i], color='orange', label='y = x^2' if i == 0 else "")

# Tambahkan garis horizontal pada y = 0
plt.axhline(0, color='black', linestyle='--', linewidth=0.5)

# Tambahkan garis vertikal pada x = 0
plt.axvline(0, color='black', linestyle='--', linewidth=0.5)

# Tambahkan label pada sumbu x dan y
plt.xlabel('x')
plt.ylabel('y')

# Tampilkan legenda
plt.legend()

# Tampilkan grid
plt.grid(True)

# Tampilkan plot
plt.title('Plot Garis Lurus dan Parabola')
plt.show()
