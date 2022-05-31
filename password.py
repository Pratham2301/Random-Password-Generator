import random

collection='ABCDEFGHIJKLMNOPQRSTUVWXYZ@#!$%&?abcdefghijklmnopqrstuvwxyz0123456789'

str=""

for i in range(0,8):
    x=random.choice(collection)
    str+=x

print(str)
