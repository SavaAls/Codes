n = int(input("Введите число элементов массива: "))
m = []
summ = 0
for i in range(n):
    m.append(int(input("Введите элемент массива: ")))
for i in range(len(m)):
    summ +=m[i]
print(summ,"Сумма всех чисел")