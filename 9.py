import matplotlib.pyplot as plt

kunlar = [1, 2, 3, 4, 5, 6, 7]
qiymat = [10, 20, 15, 30, 25, 40, 35]

plt.plot(kunlar, qiymat, marker='o')
plt.title("Grafik sarlavhasi")
plt.xlabel("Kunlar")
plt.ylabel("Qiymat")
plt.grid(True)
plt.savefig("natija.png")
plt.show()
