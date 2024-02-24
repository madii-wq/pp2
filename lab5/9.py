import re

txt = input()

x=re.findall("[A-Z]", txt)
y = set(x)
for i in y:
    txt = re.sub(i, " " + i, txt);
print(txt.strip())