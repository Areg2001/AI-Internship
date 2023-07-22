from points import Point2D, Point3D

point1 = Point2D(3, 4)
point2 = Point2D(3, 4)
print(point1 == point2)
print(hash(point1))
print(point1)


point3 = Point3D(4, 5, 6)
point4 = Point3D(3, 6, 9)
print(point3 == point4)
print(hash(point2))
print(point3)

point6 = Point3D(2, 3)          #Error: Must be 3 arguments
po7 = Point2D(3, 4, 5)          #Error: Must be 2 arguments