word = "word" # 2 Проверь себя =, олностью сделанная
vowels = 0
consonants = 0
for i in word:
    letter = i.lower()
    if letter == "a" or letter == "e" or\
       letter == "i" or letter == "o" or\
       letter == "u" or letter == "y":
        vowels += 1
    else:
        consonants += 1
letters = ("Vowels %i\nConsonants %i" % (vowels, consonants))
print(letters, "1-Гласные", "2-Согласные", sep='\n')
