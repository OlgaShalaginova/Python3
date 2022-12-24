# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#     Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

import os
os.system('cls')

number = int(input("Введите число: "))
fib1 = [0, 1, 1]
for i in range(3, number+1):
    fib1.append(fib1[i-1] + fib1[i-2])
fib2 = [((-1)**(i+2))*fib1[i+1] for i in range(0, len(fib1)-1)]
fib = fib2[::-1] + fib1
print(fib)