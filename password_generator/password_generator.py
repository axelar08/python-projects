#!/usr/bin/env python3
import random
import string

chars = string.ascii_letters + string.digits + string.punctuation
special_characters = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
pass_length = int(input("password length [6-15]\n: "))

def passgen ():
    pwd = ""
    for x in range(pass_length):
        pwd += random.choice(chars)
    print(pwd)

while 1:
    passgen()
    x = str(input(": "))
    if x == "exit":
        break