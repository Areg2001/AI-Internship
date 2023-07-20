from polygon import Polygon
from point import Point2D, Point2DSequence

point1 = Point2D(3, 4)
point2 = Point2D(1, 5)
point3 = Point2D(4, 8)
point4 = Point2D(3, 9)

polygon = Polygon(point1, point2, point3)
polygon.append(point4)

print(polygon)
print(polygon.vertices)
print(point1)


point6 = Point2D(4.5, 7)        #Error becouse x type is float
polygon = Polygon(point1)       #Errpr becouse min_length must be 2