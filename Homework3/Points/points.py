from abc import ABC, abstractmethod
from slottedStruct import SlottedStruct
import math


class Point2D(metaclass=SlottedStruct):

    __slots__ = ('_x', '_y')
    dimension = 2

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def distance(self):
        return math.sqrt(pow(self._x, 2) + pow(self._y, 2))


class Point3D(metaclass=SlottedStruct):
    __slots__ = ('_x', '_y', '_z')
    dimension = 3

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def z(self):
        return self._z

    def distance(self):
        return math.sqrt(pow(self.x, 2) + pow(self.y, 2) + pow(self.z, 2))

    
class Point4D(metaclass=Slot):
​
    __slots__ = ('_x', '_y', '_z', '_k')
    dimension = 4
​
    @property
    def x(self):
        return self._x
​
    @property
    def y(self):
        return self._y
​
    @property
    def z(self):
        return self._z
​
    @property
    def k(self):
        return self._k

    def distance(self):
        return math.sqrt(pow(self.x, 2) + pow(self.y, 2) + pow(self.z, 2) + pow(self.k, 2))
​    

​
class Point5D(metaclass=Slot):
​
    __slots__ = ('_x', '_y', '_z', '_k', '_i')
    dimension = 5
​
    @property
    def x(self):
        return self._x
​
    @property
    def y(self):
        return self._y
​
    @property
    def z(self):
        return self._z
​
    @property
    def k(self):
        return self._k
    
    @property
    def n(self):
        return self._n

    def distance(self):
        return math.sqrt(pow(self.x, 2) + pow(self.y, 2) + pow(self.z, 2) + pow(self.k, 2) + pow(self.n, 2))
