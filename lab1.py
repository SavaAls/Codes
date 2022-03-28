a = int(input('Введите число a: '))
b = int(input('Введите число b: '))
c = int(input('Введите число c: '))
d = int(input('Введите чилсо d: '))
k = int(input('введите число k: '))
Example = ((a**2-b**3-c**3-a**2)*(b-c+c*(k-d/b**3))-(k/b-k/a)*c)**2-20000
try:
     b = 0
     a = 0
except ZeroDivisionError:
    print('На ноль делить нельзя')
if Example < 0:
    print(Example*(-1))
if Example >= 0:
    print(Example)