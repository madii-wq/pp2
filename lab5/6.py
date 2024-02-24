import re

txt = input()

x = re.sub("[\s\.\,]",":", txt)

print(x)