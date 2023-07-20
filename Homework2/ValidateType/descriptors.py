"""Descriptors module"""


class ValidType:
    """Base Descriptor"""

    def __init__(self, property_type: int|float|list) -> None:
        self.property_type = property_type

    def __set_name__(self, owner, property) -> None:
        self.property = property

    def __set__(self, instance: object, value: int | float | list) -> None:
        if not isinstance(value, self.property_type):
            raise ValueError(f"Type Error: value must be {self.property_type.__name__}.")

        instance.__dict__[self.property] = value

    def __get__(self, instance: object, owner: object) -> object|int|list|float:
        if instance is None:
            return self
        return instance.__dict__.get(self.property, None)


class Int(ValidType):
    """Descriptor that checks whether property type is integer or not."""

    def __init__(self) -> None:
        super().__init__(int)


class Float(ValidType):
    """Descriptor that checks whether property type is float or not."""

    def __init__(self) -> None:
        super().__init__(float)


class List(ValidType):
    """Descriptor that checks whether property type is list or not."""

    def __init__(self) -> None:
        super().__init__(list)
