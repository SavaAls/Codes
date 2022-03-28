import numpy as np
n = int(input('количество строк: '))
m = int(input('количество столбцов: '))
arr = np.random.randint(-10,10, (n,m))
print("1-ая матрица")
print(arr)
arr[(arr < 0)] *= 0
print("2-ая матрица после замены отрицательных чисел")
print(arr)