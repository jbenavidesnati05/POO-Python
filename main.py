class Coche():
    # constructor
    def __init__(self):
        # __ es para encapsular la propiedad
        self.largoChasis = 250
        self.__anchoChasis = 120
        self.__ruedas = 4
        self.enMarcha = True

    def arrancar(self):
        self.enMarcha = True

        if (self.enMarcha):
            chequeo = self.chequeoInterno()

        if (self.enMarcha and chequeo):
            print("el coche esta en marcha") 
        elif(self.enMarcha and chequeo==False):
            print("algo salio mal") 


    def chequeoInterno(self):
        print("realizando chequeo interno")
        self.gasolina = "ok"
        self.aceite = "mal"
        self.puertas = "cerradas"

        if (self.gasolina == "ok" and self.aceite == "ok" and self.puertas == "cerradas"):
            return True
        else:
            return False



print("-------------------PARA MI COCHE---------------------")
miCoche = Coche()
# print(f"El largo del coche es : {miCoche.largoChasis}")
miCoche.arrancar()

print("------------------PARA TU COCHE-----------------------")
tuCoche = Coche()
# print(f"El largo del coche es : {miCoche.largoChasis}")
miCoche.arrancar()
