import re

txt = str(input())

x = re.search("a0|ab+", txt)

print(x)