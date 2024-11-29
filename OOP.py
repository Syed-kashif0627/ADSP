from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self,len,wid):
        self.length=len
        self.width=wid

    def area(self):
        return self.length*self.width
    
    def perimeter(self):
        return 2*(self.length+self.width)
    
class Square(Shape):
    def __init__(self,side):
        self.side=side

    def area(self):
        return self.side**2
    
    def perimeter(self):
        return self.side*4
    

rect = Rectangle(3, 4) 
print(f"Rectangle area: {rect.area()}") 
print(f"Rectangle perimeter: {rect.perimeter()}") 

sq = Square(5) 
print(f"Square area: {sq.area()}")
print(f"Square perimeter: {sq.perimeter()}")