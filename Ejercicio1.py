import random
class Dice:
    def __init__(self,sides=int):
        self.__sides = 6
    
    def roll(self):
        return random.randint(1,self.__sides)
    
    

def prueba():
    dice1 = Dice()
    dice2= Dice()
    
    for i in range (5):
    
        resultado1= dice1.roll()
        resultado2= dice2.roll()
        print(f'En el lanzamiento número {i+1}, el resultado del primer dado es de {resultado1} y el del segundo dado es de {resultado2}.')
prueba()

    