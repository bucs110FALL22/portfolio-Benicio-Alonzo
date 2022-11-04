import rectangle

class surface:
  def __init__(self,filename,x,y,h,w):
    
    self.image = filename
    self.rect = rectangle.rectangle(x,y,h,w)
    

  def getRect(self):
    shape = self.rect
    return shape