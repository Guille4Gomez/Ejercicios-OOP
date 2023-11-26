import random 

class Dice:
    def __init__(self,number=0,faces=6):
        self.__faces=faces

        if number==0:
            self.__number = random.randint(0,faces)
        else:
            self.__number = number

    @property 
    def number(self):
        return self.__number
    @number.setter 
    def number (self,value):
        self.__number = value
    @property
    def faces (self):
        return self.__faces
    @faces.setter
    def faces (self,value):
        self.__faces=value


    def __repr__ (self):
        return (f'El numero es: {self.__number} y el número de caras de el dado es: {self.__faces}')
    def roll (self):
        self.__number = random.randint(1,self.__faces)
    

