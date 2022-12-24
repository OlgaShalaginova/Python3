# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import os
os.system('cls')
import random

number = int(input("Введите число: "))
list_numbers = []
for i in range(number):
    list_numbers.append(round(random.randint(0, 1000) / 100, 2))
print("Сформированный список:",list_numbers)
list_drobi = [i % 1 for i in list_numbers]
print("Разница между максимальным и минимальным значением дробной части элементов равна:", round(max(list_drobi) - min(list_drobi), 2))