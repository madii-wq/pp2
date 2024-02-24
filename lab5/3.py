import re

txt = input()

x = re.search("[a-z]_[a-z]", txt)

print(x)