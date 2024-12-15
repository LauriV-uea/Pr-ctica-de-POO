

#asignamos una clase
class Animal:
    def __init__(self,name):
        self.name = name

    def comer(self):
        print(f"{self.name}, está comiendo.")

#subclase que hereda de animal
class Dog(Animal):
    def ladrar(self):
        print(f"{self.name}, está ladrando.")

#subclase que hereda de animal
class Cat(Animal):
    def maullar(self):
        print(f"{self.name}, está maullando.")

# instancias de las subclases Dog y Cat
perro = Dog("el chihuagua")
gato = Cat("mimi")

#llamamos a los métodos de los objetos
perro.comer()
perro.ladrar()

gato.comer()
gato.maullar()
