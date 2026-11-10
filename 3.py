from matplotlib import pyplot

kunlar = [1, 2, 3, 4, 5, 6, 7]
ali = [10, 15, 12, 20, 25, 22, 30]
vali = [8, 12, 18, 16, 22, 27, 28]

pyplot.plot(kunlar, ali, marker="o", linestyle="-.", label="Ali", color="red")
pyplot.plot(kunlar, vali, marker="s", linestyle="--", label="Vali", color="blue")

pyplot.title("O'quvchilarning haftalik o'qish natijalari")
pyplot.xlabel("Kunlar")
pyplot.ylabel("Natijalar")

pyplot.legend()
pyplot.grid(True)
pyplot.show()
