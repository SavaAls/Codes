import random
import string

def RandomPassword(length):
    letters = string.ascii_letters + string.digits
    rand_string = "".join(random.sample(letters, length))
    print("RandomPassword", "is", rand_string)
RandomPassword(16)