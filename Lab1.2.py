n = int(input("Введите число элементов массива: "))
m = []
for i in range(n):
    m.append(input("Введите элемент массива: "))
for i in range(len(m)):
    if i % 2 != 0:
        print(m[i])

