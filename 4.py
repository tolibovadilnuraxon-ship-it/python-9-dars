import matplotlib.pyplot as plt

tillar = ["Python", "C", "JavaScript", "Java"]
oquvchilar = [15, 8, 12, 5]

plt.figure(figsize=(8, 6))
plt.pie(
    oquvchilar, 
    labels=tillar, 
    autopct='%1.1f%%', 
    startangle=140
)
plt.axis('equal')
plt.title("Sinf o'quvchilarining sevimli dasturlash tillari")
plt.show()
