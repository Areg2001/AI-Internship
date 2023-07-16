class Storage:

    def __init__(self, capacity_GB: int) -> None:
        self._capacity_GB = capacity_GB


class HDD(Storage):

    def __init__(self, size: str, rpm: int, capacity_GB: int) -> None:
        super().__init__(capacity_GB)
        self.__size = size
        self.__rpm = rpm

    @property
    def size(self) -> str:
        return self.__size

    @property
    def rpm(self) -> int:
        return self.__rpm

    @property
    def capacity_GB(self) -> int:
        return self._capacity_GB


class SSD(Storage):

    def __init__(self, interface: str, capacity_GB: int) -> None:
        super().__init__(capacity_GB)
        self.__interface = interface

    @property
    def interface(self) -> str:
        return self.__interface

    @property
    def capacity_GB(self) -> int:
        return self._capacity_GB


class CPU:

    def __init__(self, cores: int) -> None:
        self.__cores = cores

    @property
    def cores(self) -> int:
        return self.__cores
