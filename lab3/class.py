class My_shape :
    def __init__(self, color,is_filled) :
        self.color = color
        self.is_filled = is_filled
    def __str__(self):
     
        return(f"the color is : {self.color} and it is {self.is_filled} shape")
    def getArea(its):
        return 0
    
class Rectangle(My_shape):
  def __init__(self,a, b, l, w):
     self.x_top_left = a
     self.y_top_left = b
     self.width = w
     self.length = l
  def getArea(measure):
     return measure.width*measure.length
  def __str__(self):
        return f"x_top_left is at {self.x_top_left} and y_top_left is at {self.y_top_left}."
class Circle(My_shape):
    def __init__(self,x, y, r):
     self.x_center = x
     self.y_center = y
     self.radius = r
    def getArea(measure):
     return f"{measure.radius*measure.radius*3.1415 :0.2f}"
    def __str__(self):
        return f"x_center is {self.x_center}cm and y_center is {self.y_center}cm." 
initial = My_shape("Green", True)   
pp2 = Rectangle(12, 3, 5, 4)
print(pp2.getArea(), pp2)
pp2 = Circle(2,5,5)
print(pp2.getArea(), pp2)
  

