""" Polygon Module"""

from point import Point2DSequence, Point2D


class Polygon:

    """
        Take one argument:list.
        Has append method to add points in list. Polygon is collection of points in 2D area.
    """

    vertices = Point2DSequence(2, 7)

    def __init__(self, *vertices: list) -> None:
        self.vertices: Point2D = list(vertices)

    def append(self, point: Point2D) -> None:
        if isinstance(point, Point2D):
            self.vertices.append(point)
        else:
            raise Exception(f"Argument must type Point2D and max length must be {self.vertices.max_length}")

    def __repr__(self):
        return f"{self.__class__.__name__}"





