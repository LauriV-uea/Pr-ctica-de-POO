

#definición de la clase de usuario
class Usuario:
    def __init__(self, nombre,contrasena):
        self.nombre = nombre
        # atributo público para el nombre usuario
        self.__contrasena = contrasena
        #atributo privado para almacenar la contraseña

    def cambiar_contrasena(self, nueva_contra):
    # cambiar la contraseña si se cumple la longitud miníma

         if len(nueva_contra) >= 8:
             self.__contrasena = nueva_contra
            #actualizar el artibuto privado

             print("contraseña actualizada")
         else:
             print("la nueva contraseña que ingresó debe tener al menos 8 caracteres")

    def verificar_usuario(self,nombre,contrasena):
#se verifica si el nombre y contraseña son correctos
        return self.nombre == nombre and self.__contrasena == contrasena

# se crea la instancia de usuario
usuario1 = Usuario("Juan","soyjuan1")

# solicitar al usuario los datos de acceso
nombre_ingresado = input("Ingresa el nombre de su usuario: ")
contrasena_ingresada = input("ingresa la contraseña:")

# verificar si el usuario y la clave son correctas
if usuario1.verificar_usuario(nombre_ingresado, contrasena_ingresada):
    print("Bienvenido!!, Juan, puedes cambiar tu contraseña.")

#pedir al usuario que ingrese la nueva contraseña
    nueva_contrasena = input("ingresa tu nueva contraseña, por favor:")

#cambiar la contraseña usando la instancia  usuario1
    usuario1.cambiar_contrasena(nueva_contrasena)
    print("Proceso finalizado.Vuelve a iniciar sesión para verificar.")

else:
    print("Usuario o contraseña incorrectos.")