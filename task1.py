# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import os
os.system('cls')
import random

number = int(input('Введите число: '))
sum = 0
list_numbers = []
for i in range(number):
    list_numbers.append(random.randint(0, 10))
print("Сформированный список:", list_numbers)
for i in range(1, number, 2):
    sum += list_numbers[i]
print("Сумма элементов списка с нечетными позициями равна:", sum)