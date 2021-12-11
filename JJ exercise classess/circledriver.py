from TheCircle import Cylinder
from TheCircle import Circle

def pro() :
    radius1 = eval(input("Enter the radius: "))
    color1 = (input("Enter the color: "))
    height1 = eval(input("Enter the height: "))

    item = Cylinder(radius1,color1,height1)
    print(f"The radius of the cylinder is {item.getRadius()}")
    print(f"The color of the cylinder is {item.getColor()}")
    print(f"The height of the cylinder is {item.getHeight()}")
    print(f"So the volume is {item.getVolume()}")

    

   

pro()


