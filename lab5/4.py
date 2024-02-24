import re

txt = input()

x= re.search("[A-Z][a-z]",txt)

print(x)