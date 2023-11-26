#Para almacenar el valor del  tiempo recibido, se pone el getter de time_receive
    #No se puedde hacer un incremento en el setter de time_made
    #quitaría el setter y getter de total time
    #Total time siempre va a ser la suma de los dos atributos
    #en el metodo call si se produce el incremento 

class Terminal: 
    def __init__(self,number:str):
        self.number = number 
        self.time_receive = 0 
        self.time_made = 0 
        self.total_time = 0 

    #Number

    @property
    def number (self):
        return self.number 

    @number.setter
    def number(self,value):
        if isinstance(value,str):
            if value.isdigit() and value.startswith (('6','7','9')) and len(value) == 9:
                self.__number = value
            else:
                raise TypeError(f'{value} no es un número de teléfono válido.')      #Raise: es una excepción del código
        else: 
            raise TypeError(f'{value} no es un número de teléfono válido.')


        
    
    #Time_made
    @property
    def time_made(self):
        return self.time_made

    @time_made.setter
    def time_made(self,call_time):
        self.__time_made = call_time 

    #Time_receive
    @property 
    def time_receive(self):
        return self.time_receive
    
    @time_receive.setter 
    def time_receive(self,call_time):
        self.__time_receive= call_time



    #Total_time
    @property

    def total_time(self):
        return self.time_made + self.time_receive
    
        

    def call (self,terminal,call_time):
        self.time_made= self.time_made + call_time 
        terminal.time_receive = terminal.time_receive + call_time 

    
    def __str__ (self):
        return (f'{self.number} - Conversation time: {}')




#TEST

t1 = Terminal("666112233")
t2 = Terminal("666744459")
t3 = Terminal("632128919")
t4 = Terminal("664135818")
print(t1)
print(t2)
t1.call(t2, 420)
t1.call(t3, 210)
print(t1)
print(t2)
print(t3)
print(t4)
    