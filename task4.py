# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

import os
os.system('cls')

number = int(input("Введите число: "))
print(number, end='')
bin = ''
while number // 2 > 0:
    bin += str(number % 2)
    number = number // 2
    if number == 1:
        bin += '1'
print(" ->", bin)