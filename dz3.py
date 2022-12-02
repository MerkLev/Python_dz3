# 3'. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# *Пример:*

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

list = [1.1, 1.2, 3.1, 5, 10.01]
list2 = [] 
for i in list:
    y = str(i)
    list2.append(y)
print(list2)
list3 = []
for i in list2:
    if ("." in i):
        x = i.split(".")
        y = "0."
        y = y+x[1]
        list3.append(float(y))
print(list3)

Max = list3[0]
min = list3[0]

for i in list3:
    if (i > Max):
        Max = i
print(Max)
for i in list3:
    if (i < min):
        min = i
print(min)
print(Max-min)
