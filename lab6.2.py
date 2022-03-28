import  re
x = input("Введите строчку: ")
z = input("Введите строчку: ")
c = re.sub('\D','',x)
v = re.sub('\D','',z)
q = int(c)
w = int(v)
print(q+w,"--> Сумма чисел из строчек x и z")