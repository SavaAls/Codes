import re

my_string = """ФИО;Возраст;Категория;_Иванов Иван Иванович 23 года Студент 3 курса;_Петров Семен Игоревич;22 года;Студент 2 курса;_Иванов Семен Игоревич;22 года;Студент 2 курса"""

for i, str_ in enumerate(my_string.split('_')):
    if i > 0:
        age = int(re.search('(\d+)', str_).group(0))
        if age >= 0:
            print(str_)