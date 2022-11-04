class rectangle:
   def __init__(self,x,y,h,w):
     if x <0:
      x=0
     if y <0:
      y=0
     if h <0:
      h=0
     if w <0:
      w=0
     
     self.x = x
     self.y = y
     self.height = h
     self.width = w
   def __str__(self):
      
     result_str = f"(x: {self.x}, y: {self.y}) width: {self.width}, height: {self.height}, where the integers are the values of the instance variables"
     return result_str



