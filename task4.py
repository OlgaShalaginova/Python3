# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

import os
os.system('cls')

number = int(input("Введите число: "))
t = number
print(number, end='')
bin_n = ''
while number // 2 > 0:
    bin_n += str(number % 2)
    number = number // 2
    if number == 1:
        bin_n += '1'
print(" ->", bin_n[::-1])
print("Проверка:", bin(t))