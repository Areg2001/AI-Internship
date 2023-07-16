class Resource:

    def __init__(self, name: str, manufacturer: str, total: int, allocated: int) -> None:
        self.__name = name
        self.__manufacturer = manufacturer
        self.__total = total
        self.__allocated = allocated
        self.__validator()

    def __validator(self):
        if not isinstance(self.__total, int):
            raise TypeError("Total must be type int...")

        if not isinstance(self.__allocated, int):
            raise TypeError("Allocated must be type int...")

    @property
    def name(self) -> str:
        return self.__name

    @property
    def manufacturer(self) -> str:
        return self.__manufacturer

    @property
    def total(self) -> int:
        return self.__total

    @property
    def allocated(self) -> int:
        return self.__allocated

    def claim(self, n: int, resource) -> None:
        if n <= self.__total:
            print(f"Claimed {n} {resource.__class__.__name__}...")
            self.__allocated += n
        else:
            print(f"Inventory does not have {n} resources...")

    def freeup(self, n: int, resource) -> None:
        if n <= self.__allocated:
            self.__allocated -= n
            print(f"Returned {n} {resource.__class__.__name__}...")
        else:
            print("It is so much...")

    def died(self, n: int, resource) -> None:
        self.__total -= n
        print(f"Remove {n} {resource.__class__.__name__} from the pool...")

    def purchased(self, n: int, resource) -> None:
        self.__total += n
        print(f"Purchased {n} {resource.__class__.__name__}...")

    def __str__(self):
        return f"Resource name is {self.__name}..."

    def __repr__(self):
        return f"name-{self.__name}, manufacturer-{self.__manufacturer}, total-{self.__total}, " \
               f"allocated-{self.__allocated}"

    def category(self):
        return self.__class__.__name__.lower()