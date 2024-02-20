import mymodule
#EX1
mymodule.greeting("Jonathan")
#EX2
a = mymodule.person1["age"]
print(a)
#EX3
import mymodule as mx

a = mx.person1["age"]
print(a)
#EX4
import platform

x = dir(platform)
print(x)
#EX5
from mymodule import person1

print (person1["age"])