"""Main module"""

from type import Int


class Point2D:

    """
        This class has two attributes x coordinate and y coordinate. Instances are points in 2D area.
    """

    x: int = Int(min_value=0)
    y: int = Int(min_value=0)

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __str__(self):
        return "Point in 2D area..."

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


class Point2DSequence:
      """
          This class has two attributes min length:int and max_length:int.
          This Descriptor Validates that each item be Point2D type, validate max and min length of sequence.
      """

    def __init__(self, min_length: int = None, max_length: int = None) -> None:
        self.min_length = min_length
        self.max_length = max_length

    def __set_name__(self, owner: object, name: object) -> None:
        self.name = name

    def __get__(self, instance: object, owner: object) -> Point2D:
        if instance is None:
            return self

        return instance.__dict__.get(self.name, None)

    def __set__(self, instance: object, value: Point2D) -> None:
        print("Length:",len(value))
        if self.min_length is not None and self.min_length > len(value):
            raise ValueError(f"Length must be greater or equal {self.min_length}...")

        if self.max_length is not None and self.max_length < len(value):
            raise ValueError(f"Length must be less or equal {self.max_length}...")

        if isinstance(value, (list, tuple)):
            for item in value:
                if not isinstance(item, Point2D):
                    raise ValueError("Each element must be Point2D type...")
        else:
            raise ValueError(f"Value must be type list or tuple...")

        instance.__dict__[self.name] = value
