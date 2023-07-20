"""Type module"""


class Int:

    """
        Takes two arguments:int.
        This Descriptor checks that taken argument be int type.
    """

    def __init__(self, min_value: int = None, max_value: int = None) -> None:
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self, owner: object, name) -> None:
        self.name = name

    def __get__(self, instance: object, owner: object) -> int:
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance: object, value: int) -> None:

        if self.min_value is not None and value < self.min_value:
            raise ValueError(f"Value must be greater or equal {self.min_value}...")

        if self.max_value is not None and value > self.max_value:
            raise ValueError(f"Value must be less or equal {self.max_value}...")

        if not isinstance(value, int):
            raise ValueError(f"Value must be int type...")

        instance.__dict__[self.name] = value
