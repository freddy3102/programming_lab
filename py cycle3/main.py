from mypackage import circle
from mypackage import rectangle
from mypackage.threeDgraphics import *

("\n---mypackage---\n")

r=int(input("Enter the radius of circle:" ))
l=int(input("Enter the length of rectangle:" ))
b=int(input("Enter the breadth of rectangle:" ))

ca=circle.circarea(r)
cp=circle.circperi(r)
ra=rectangle.rectarea(l,b)
rp=rectangle.rectperi(l,b)

print("Area of circle is",ca)
print("perimeter of circle is",cp)
print("Area of rectangle is",ra)
print("perimeter of rectangle is",rp)

("\n---3dgraphics---\n")

sr=int(input("Enter the radius of sphere:"))
cl=int(input("Enter the length of cuboid:"))
cb=int(input("Enter the breadth of cuboid:"))
ch=int(input("Enter the height of cuboid:"))

p=cuboid.cuboidarea(cl,cb,ch)
q=cuboid.cuboidperi(cl,cb,ch)
s=sphere.spherearea(sr)
t=sphere.sphereperi(sr)

print("Area of cuboid is",p)
print("perimeter of cuboid is",q)
print("Area of sphere is",s)
print("perimeter of cuboid is",t)

