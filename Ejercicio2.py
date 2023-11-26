import math
class Point:
    def __init__(self,x=int,y=int):
        self.__x=x
        self.__y=y 
    
    @property
    def x(self):
        return self.__x
    @property
    def y(self):
        return self.__y

    @x.setter
    def x(self, valor):
        self.__x = valor
    @y.setter
    def y(self, valor):
        self.__y = valor

    def invert_coordinates(self):
        self.__x, self.__y = self.__y, self.__x

    def distance_to(self, another_point):
        return math.sqrt((self.__x - other_point.x) ** 2 + (self.__y - other_point.y) ** 2)

    def __str__(self):
        return f"({self.__x}, {self.__y})"

   


