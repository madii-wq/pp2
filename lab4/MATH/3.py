import math

num_side = int(input())

len_side = int(input())

apothem = len_side/(2*math.tan(math.pi/num_side))
area = (num_side*len_side*apothem)/2
print(int(area))