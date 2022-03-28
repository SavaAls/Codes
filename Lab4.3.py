my_len = [["БО-331101",["Акулова Алена Викторовна","Бабушкина Ксения Сергеевна","Ширяев Остин Ярославович"]],["БОВ-421102",["Кобзар Изольда Юхимовна","Худобяк Любовь Викторовна","Устинова София Алексеевна"]],["БО-331103",["Петренко София Сергеевна","Гурьева Оксана Анатолиевна","Ермакова Алина Платоновна"]]]
number,number_1,number_2= [],[],[],[]
number += my_len[0]
number_1 += my_len[1]
number_2 += my_len[2]
number_2 += my_len[3]
print("<{}>".format(number[0]),end = ":")
for i in  number[1]:
    print("<{}>".format(i),end = ",")
print("\n<{}>".format(number_1[0]),end = ":")
for i in  number_1[1]:
    print("<{}>".format(i),end = ",")
print("\n<{}>".format(number_2[0]),end = ":")
for i in  number_1[1]:
    print("<{}>".format(i),end = ",")
input("\nНажмите ENTER для завершения программы :")