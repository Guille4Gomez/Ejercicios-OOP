#Para almacenar el valor del  tiempo recibido, se pone el getter de time_receive
    #No se puedde hacer un incremento en el setter de time_made
    #quitaría el setter y getter de total time
    #Total time siempre va a ser la suma de los dos atributos
    #en el metodo call si se produce el incremento 

class Terminal: 
    def __init__(self,number:str):
        self.number = number 
        self.time_received = 'Inicio'
        self.time_made = 'Inicio' 
        self.total_time = 0 

    #Number

    @property
    def number (self):
        return self.__number 

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
        return self.__time_made

    @time_made.setter
    def time_made(self,call_time):
        if call_time == 'Inicio':
            self.__time_made = 0
        else:
            self.__time_made += call_time 
            self.__total_time += call_time
            

    #Time_receive
    @property 
    def time_received(self):
        return self.__time_received
    
    @time_received.setter 
    def time_received(self,call_time):
        if call_time == 'Inicio':
            self.__time_received = 0 
        else:
            self.__time_received += call_time
            self.__total_time += call_time
        



    #Total_time
 
    @property
    def total_time(self):
        return self.__total_time
    
    @total_time.setter
    def total_time(self,call_time):
        self.__total_time = call_time
          
    def call (self,terminal,call_time):
        self.time_made = call_time 
        terminal.time_received =  call_time 

    
    def __str__ (self):
        return (f'{self.number} - Conversation time: {self.total_time}')





    