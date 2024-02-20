import datetime
#EX1
x = datetime.datetime.now()
print(x)
#EX2
x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))
#EX3
x = datetime.datetime(2020, 5, 17)

print(x)
#EX4
x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))