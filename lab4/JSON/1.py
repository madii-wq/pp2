import json
str ="""Interface Status​

================================================================================​

DN                                                 Description           Speed    MTU  ​

-------------------------------------------------- --------------------  ------  ------"""
f = open('sample-data.json')
datalist = json.load(f)
print(str)
for i in datalist['imdata']:
       print(i['l1PhysIf']['attributes']['dn'],'\t\t\t\t', i['l1PhysIf']['attributes']['speed'], i['l1PhysIf']['attributes']['mtu']) 

f.close()
