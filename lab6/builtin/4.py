import time
import math

def square_root_after_milliseconds(number, milliseconds):
    time.sleep(milliseconds / 1000)
    square_root = math.sqrt(number)
    return square_root

number = input()
milliseconds = input()

result = square_root_after_milliseconds(number, milliseconds)

print(result)
