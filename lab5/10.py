import re

txt = input()

y = re.search("[A-Z]", txt)
if y is None:
    print(txt)
else:
    x = re.sub("[A-Z]", "_" + txt[y.start()].lower(), txt, 1)
    print(x)
