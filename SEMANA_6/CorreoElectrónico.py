# clase base correo electrónico
print("................................................................................................................................................................................................................")
class CorreoElectronico:
    def __init__(self, remitente, destinatario, asunto, cuerpo) :
        self.remitente = remitente      # atributo privado
        self.destinatario = destinatario
        self.asunto = asunto
        self.cuerpo = cuerpo

#definimos una función para salida de correo
    def enviar(self):
        return f"Enviando el correo desde {self.remitente} a {self.destinatario} con asunto ´{self.asunto}´ y cuerpo ´{self.cuerpo}´"


# métodos getter y setter para el atributo privado __remitente
    def get__remitente(self):
        return self.remitente
    def set__remitente(self, nuevo_remitente, ):
        self.remitente = nuevo_remitente


  #subclase-correoConArrchivo     herencia
class CorreoConArchivo (CorreoElectronico):
    def __init__(self, remitente, destinatario, asunto, cuerpo, archivo_adjunto) :
        super().__init__(remitente, destinatario, asunto, cuerpo)
        self.archivo_adjunto = archivo_adjunto

 #polimorfismo- sobrecarga del metodo enviar
    def enviar(self):
        base_mensaje =  super().enviar()
        return f"{base_mensaje} y el archivo adjunto {self.archivo_adjunto}"

#uso del programa
#creación de un objeto de la clase correoElectronico
correo1 = CorreoElectronico( "estrella@gmail.com","Nelson23@gmail.com","reunión 8AM","Buenos días Nelson, espero te encuentres muy bien.")
print(correo1.enviar())


#creación de un objeto de la subclase CorreoConArchivo
correo2 = CorreoConArchivo( "estrella@gmail.com","Nelson23@gmail.com","documentos","Aquí están los documnetos que me pediste","documento.pdf")
print(correo2.enviar())

#cambio del remitente utilizando  setter
correo1.set__remitente("Esteban15@gmail.com")

print(correo1.enviar())




