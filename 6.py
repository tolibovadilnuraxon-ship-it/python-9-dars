import matplotlib.pyplot as plt

mahsulotlar = ["Non", "Sut", "Tuxum", "Yog", "Shakar"]
sotuv = [45, 30, 60, 20, 25]

plt.bar(mahsulotlar, sotuv, color='skyblue')
plt.title("Bir haftada sotilgan mahsulotlar")
plt.show()

max_sotuv = max(sotuv)
min_sotuv = min(sotuv)
print("Eng ko'p:", mahsulotlar[sotuv.index(max_sotuv)])
print("Eng kam:", mahsulotlar[sotuv.index(min_sotuv)])
