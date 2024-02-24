import re

txt = input()
y = re.search("_[a-z]", txt)

if(y==None):
   print(txt)
else:
   x= re.sub("_[a-z]", txt[y.start()+1].upper(), txt, 1)
   print(x)

