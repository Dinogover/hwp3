# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
from random import uniform
array = [round(uniform(1,10), 2) for _ in range(10)]
maxArray, minArray = round(array[0] % 1, 2) , round(array[1] % 1, 2)
for i in array:
    temp = round(i % 1, 2)
    if maxArray < temp: maxArray = temp
    elif minArray > temp: minArray = temp
print(maxArray - minArray)