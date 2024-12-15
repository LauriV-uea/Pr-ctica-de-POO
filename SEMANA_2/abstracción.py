from abc import ABC, abstractmethod


class Vehiculo(ABC):
    @abstractmethod
    def moverse(self):     # método abstracto que obliga a las subclases a implementarlo
        pass

#subclase que hereda de vehículo
class Bicicleta(Vehiculo):
    def moverse(self):
        #implementación específica para una bicicleta
        return "La bicicleta se mueve pedaleandola"

#subclase que hereda de vehículo
class Motocicleta(Vehiculo):
    def moverse (self):
        #implementación específica para una motocicleta
        return "La motocicleta se mueve con combustible "

#subclase que hereda de vehículo
class Coche(Vehiculo):
    def moverse (self):
        #implementación específica para un coche
        return"El coche se mueve con combustible o electricidad."

#creamos una lista de instancias de los diferentes tipos de vehículos
vehiculos = [Bicicleta(), Motocicleta(), Coche()]

#iteramos por cada vehículo y llamamos al método moverse
for vehiculo in vehiculos:
    print(vehiculo.moverse())

