import random
while True:
    chars = list('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM123456789')
    length = int(input("Length password: ")+ "\n")
    random.shuffle(chars)
    password = ''.join(([random.choice(chars) for x in range(length)]))
    print(f'Your password - {password}')