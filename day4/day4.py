import random

names_string = input("insira o nome das pessoas que consumiram, separados por ', ': ")
names_array = names_string.split(', ')
quem_pagara = names_array[random.randint(0,names_array.__len__() - 1)]

print(f"{quem_pagara} pagará a conta hoje")