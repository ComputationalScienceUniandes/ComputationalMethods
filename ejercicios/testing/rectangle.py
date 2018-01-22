
class Rectangle:
    def __init__(self):
        self.x = 10.0
        self.y = 10.0
        self.x0 = 0.0
        self.y0 = 0.0
    def size(self):
        return (self.x, self.y)
    def center(self):
        return (self.x0, self.y0)
    def resize(self,x,y):
        self.x = x
        self.y = y
    def recenter(self,x0,y0):
        self.x0 = x0
        self.y0 = y0

def overlap(A, B):
    over = False    
    if A.x0 < B.x0:
        over = True
    print over, A.x0, B.x0
    return over
