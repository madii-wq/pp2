def factorial( number ):
    if(number == 0):
        return 1
    return number*factorial(number - 1)
def reverse_string( string):
   return string[:: -1]
def get_max(a, b, c):
    return max(a, b, c)
def is_even(number):
    return True if number%2==0 else False
def filter_prime(list):
    alternative = []
    for i in range(len(list)):
        if(list[i]==2 or list[i]==3):
            alternative.append(list[i])
            continue
        for x in range(2, list[i]):
            if(list[i]%x==0):
                break
        else:
            alternative.append(list[i])
    return alternative
def find_common_elements(list1, list2):
    list3 = []
    for x in list1:
        if x in list2:
            list3.append(x)
    return list3
def word_frequency(strings):
    you = {}
    for x in strings:
        you.__setitem__(x, strings.count(x))
    return you
def fibonacci(n):
    if(n==1):
        return 1
    if(n==2):
        return 1
    return fibonacci(n-1) + fibonacci(n-2)
def calculate_running_average(list):
    sum = 0
    for i in range(1,len(list)+1):
        utn = list[i-1]
        list[i-1]=float(f"{(sum+list[i-1])/i:0.2f}")
        sum += utn
    return list
list = [1,2,3,4,5,6,7,8,9,10]
k = calculate_running_average(list)
print(k)
