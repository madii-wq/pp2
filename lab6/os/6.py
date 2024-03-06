
import os

dir_list = os.listdir()
print("List of directories and files before creation:")
print(dir_list)
print()
listchar = 'abcdefghijklmnopqrstwxyz'


for i in listchar:
 with open(i.upper() + '.txt', 'w') as f:
    pass

dir_list = os.listdir()
print("List of directories and files after creation:")
print(dir_list)