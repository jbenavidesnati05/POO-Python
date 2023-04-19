class Coche():
    # constructor 
    def __init__(self):
        # __ es para encapsular la propiedad         
        self.__largoChasis = 250 
        self.__anchoChasis = 120
        self.__ruedas = 4
        self.enMarcha = False
        
    def arrancar(self):
     self.enMarcha = True
     
    def estado(self):
        if (self.enMarcha):
            return "el coche esta en marcha"
        else:
            return "el coche esta detenido"
              
miCoche = Coche()

print(f"El largo del coche es : {miCoche.largoChasis}")
miCoche.arrancar()
print(miCoche.estado())

tuCoche = Coche()
print(f"El largo del coche es : {miCoche.largoChasis}")
miCoche.arrancar()