# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)
from random import randint

min1 = int(input("Введите минимум диапазона: "))
max1 = int(input("Введите максимум диапазона: "))
n = int(input("Введите размер массива: "))

list1 = [randint(-10, 11) for _ in range(n)]
print(list1)
list2 = [i for i in range(n) if min1 <= list1[i] <= max1]
print(list2)