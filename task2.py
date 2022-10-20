# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
array = [1,2,3,5,6]
multArray = []
count = 1
for i in range(len(array)):
    if i <= len(array) // 2 - 1:
        count = array[i] * array[i-1]
        multArray.append(count)
print(array)
print(multArray)