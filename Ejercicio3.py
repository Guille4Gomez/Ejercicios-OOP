
class Rectangle:
    def __init__(self,punto1,punto2):
        self.__punto1= punto1
        self.__punto2= punto2 
    @property
    def area_rectangle(self):
        ancho = self.__punto1.x - self.__punto2.x
        alto = self.__punto1.y -self.__punto2.y
        return ancho * alto
    @property
    def perimetro_rectangle (self):
        ancho= self.__punto1.x - self.__punto2.x
        alto=self.__punto1.y - self.__punto2.y
        return 2*(ancho+alto)
    

    

   
    


