#uso de constructores y destructores en una clase llamada documentación
#clase base Biblioteca
class Biblioteca:
    def __init__(self,nombre):
        #constructor de la clase biblioteca
        self.nombre = nombre
        print(f"se ha creado la biblioteca: {self.nombre}")

#destructor de la clase biblioteca
    def __del__(self):
        print(f"se ha destruido la biblioteca {self.nombre}")


    #subclase libro
class Libro(Biblioteca):
    def __init__(self,nombre_biblioteca,titulo,autor):
    #se llama al constructor de la clase base biblioteca

        super().__init__(nombre_biblioteca)
        #propiedades de la subclase libro

        self.titulo = titulo
        self.autor = autor
        print(f" se ha agregado el libro {self.titulo} a la  biblioteca {self.nombre} .")


#subclase revista
class Revista(Biblioteca):
    def __init__(self,nombre_biblioteca,titulo,numero):
#llamar al constructor de la clase base biblioteca
        super().__init__(nombre_biblioteca)
        #propiedades específicas de la subclase revista

        self.titulo = titulo
        self.numero = numero
        print(f" Se ha agregado a la revista {self.titulo} número {self.numero} a la Biblioteca {self.nombre} .")

#función para agregar un libro
def agregar_libro(nombre_biblioteca):
    titulo = input("Ingrese el título del libro porfavor:")
    autor = input("Ingrese el autor del libro porfavor:")
    libro = Libro(nombre_biblioteca,titulo,autor)
    return libro

#función para agregar una revista
def agregar_revista(nombre_biblioteca):
    titulo = input("Ingrese el titulo de la revista porfavor:")
    numero = input("Ingrese el número de la revista porfavor:")
    revista = Revista(nombre_biblioteca,titulo,numero)
    return revista

# definimos la función principal
def main():
#pedir el nombre de la biblioteca una sola vez
    nombre_biblioteca = input("Ingrese el nombre de la biblioteca:")

#crear una instancia de la bilbioteca
    biblioteca = Biblioteca(nombre_biblioteca)
#solo se llama al constructor sin usar la variable

# creamos un menú interactico
    while True:
        print("\n Bienvenido estas son las opciones del sistema")
        print("1.-Agregar un libro ")
        print("2.-Agregar un revista ")
        print("3.-Salir del sistema")

        opcion = input("Escoja una opción:")
        if opcion == "1":
            agregar_libro(nombre_biblioteca)

        elif opcion == "2":
            agregar_revista(nombre_biblioteca)

        elif opcion == "3":
            print("Saliendo del sistema")
            break

        else:
            print("Esta opción no es válida.Porfavor ingresa una opción diferente gracias *_*")

#usamos main para ejecutar el programa
main()








