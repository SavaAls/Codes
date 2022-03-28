n = int(input("Введите число элементов: "))
m = []
for i in range(n):
    m.append(input("Введите элементы массива: "))
print("Минимальное число: ", min(m))
