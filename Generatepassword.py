import string
import random

def PasswordGen():
    s1 = string.ascii_lowercase
    print('string only:',s1)
    s2 = string.digits
    print('digits:', s2)
    s3 = string.punctuation
    print('punctuation:', s3)
    s4 = s1 +s2 + s3
    print('all in one:', s4)
    length = 10
    s5 = ''.join(random.sample(s4, length))
    print('password:', s5)

PasswordGen()