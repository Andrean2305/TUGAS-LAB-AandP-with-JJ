import math

class Circle():
    def __init__(self, radius = 1.0, color = "red") -> None :
        self.__radius = radius
        self.__color = color

    def getRadius(self) -> float :
        return self.radius

    def setRadius(self,radius: float) -> None :
        self.radius = radius

    def getColor(self) :
        return self.color
    
    def setColor(self,color: str) -> None :
        self.color = color

    def toString() -> str :
        pass

    def getArea() -> float :
        self.area = math.pi * (self.__radius * 1/2)**2  
        return self.area

class Cylinder(Circle):
    def __init__(self,radius,color,height = 1.0) :
        super().__init__(radius,color)
        self.__height = height

    def getHeight(self) -> float :
        return self.height

    def setHeight(self,height:float) -> None :
        self.height = height

    def toString(self) -> str :
        pass

    def getVolume(self) -> float :
        self.volume = self.area * self.height
        return self.volume