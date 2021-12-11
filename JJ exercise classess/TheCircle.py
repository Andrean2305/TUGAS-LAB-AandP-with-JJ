import math

class Circle(object) :
    def __init__(self, radius = 1.0, color = "red") -> None :
        self.__radius = radius
        self.__color = color

    def getRadius(self) -> float :
        return self.__radius
        
    def setRadius(self,radius: float) -> None :
        self.__radius = radius

    def getColor(self) :
        return self.__color
        
    
    def setColor(self,color: str) -> None :
        self.__color = color

    def toString(self) -> str :
        string = f"The radius of the circle is {self.getRadius()} and the color is {self.getColor()}" 
        return string

    def getArea(self) -> float :
        self.area = math.pi * (self.getRadius())**2  
        return self.area

class Cylinder(Circle):
    def __init__(self,radius,color,height = 1.0) -> None :
        super().__init__(radius,color)
        self.__height = height

    def getHeight(self) -> float :
        return self.__height

    def setHeight(self,height:float) -> None :
        self.__height = height

    def toString(self) -> str :
        string = f"The height is {self.getHeight()}"
        return string

    def getVolume(self) -> float :
        self.volume = self.getArea() * self.__height
        return self.volume