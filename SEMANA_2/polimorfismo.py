#clase base
class Figura:
    def perimetro(self):  # metodo generico que será suscrito por las subclases
        pass

    def nombre(self):
        return self.__class__.__name__

#subclase que implementa cuadrado
class Cuadrado(Figura):
    def __init__(self,lado):
        self.lado = lado

#calcula el operimetro de cuadrado
    def perimetro(self):
        return 4*self.lado


# subclase que implementa triangulo
class Triangulo(Figura):
    def __init__(self,lado1,lado2,lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

# calcula el perimetro de triangulo
    def perimetro(self):
        return self.lado1 + self.lado2 + self.lado3

# subclase que implementa rombo
class Rombo(Figura):
    def __init__(self,lado):
        self.lado = lado

    # calcula el perimetro de rombo
    def perimetro(self):
        return 4*self.lado

# listas de figuras y uso
figuras = [Cuadrado(7),Triangulo(9,5,7),Rombo(5)]


# iteramos  y calculams el perimetro sobre cada figura
for figura in figuras:
     print(f"El Perimetro del {figura.nombre()} es: {figura.perimetro()}")
