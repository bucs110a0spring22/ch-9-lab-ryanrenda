
class Rectangle:
  def __init__(self, x, y, h, w):
    self.x = max(x, 0)
    self.y = max(y, 0)
    self.height = max(h, 0)
    self.width = max(w, 0)
    
  def __str__(self):
    return "x: " + str(self.x) + " y: " + str(self.y) + " width: " + str(self.width) + " height: " + str(self.height)