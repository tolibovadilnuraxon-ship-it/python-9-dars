import matplotlib.pyplot as plt

fanlar = ["Matematika", "Python", "Ingliz tili", "Fizika", "Tarix"]
ballar = [85, 95, 72, 80, 88]

a = plt.bar(fanlar, ballar, align="center", width=0.3, label="Fanlar", color="red")

plt.bar_label(a)

plt.legend()
plt.title("Fanlardan olingan ballar")

plt.show()
