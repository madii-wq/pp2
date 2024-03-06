import os

list = []
number = int(input())

for i in range(number):
    element = input()
    list.append(element)
list1 = str(list)
with open("row.txt", 'w') as f:
    f.write(list1)
with open('row.txt', encoding='utf-8') as f: 
     print(f.read())
       
         