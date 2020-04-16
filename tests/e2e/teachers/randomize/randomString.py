import string
import random

def randomString():
    return ''.join(random.choice(string.ascii_lowercase) for m in range(20))