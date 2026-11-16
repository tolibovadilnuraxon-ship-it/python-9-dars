import matplotlib.pyplot as plt

soat = [1, 2, 3, 4, 5, 6, 7]
ball = [40, 48, 55, 65, 72, 85, 90]

plt.scatter(soat, ball, color='green', s=100)
plt.title("O'qish vaqti va test bali")
plt.xlabel("Soat")
plt.ylabel("Ball")
plt.grid(True)
plt.show()
