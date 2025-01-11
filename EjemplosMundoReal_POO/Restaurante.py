#sistema de restaurante con pedidos

# clase para representar un palto en el menú
class Plato:
    def __init__(self,nombre,precio):
        self.nombre = nombre           #nombre del plato
        self.precio = precio           #precio del plato

    def __str__(self):
            #representación del plato como cadena

        return f"{self.nombre} - {self.precio:.2f}"

#clase para representar un pedido
class Pedido:
    def __init__(self):
        self.platos =[]     #listas de platos en el pedido

    def agregar_plato(self,plato):
        #agregar un palto al pedido
        self.platos.append(plato)
        print(f"{plato.nombre}  agregado al pedido.")
        #mensaje de confirmación de pedido

    def calcular_total(self):
        #para calcular el total del pedido

      return sum(plato.precio for plato in self.platos)

    #muestra todos los pedidos de platos
    def mostrar_pedido(self):
        if not self.platos:
            return "El pedido se encuentra vacío."
        return "\n".join(str(plato) for plato in self.platos)

    def finalizar_pedido(self):
    #finaliza el pedido y muestra el total

        total = self.calcular_total()
        self.platos =[]
        #vacía el pedido

        return f"*_*....El pedido ha finalizado....Total a pagar es de: ${total:.2f} *_*"


#uso del sistema de restaurante
menu = [
    Plato("Pizza familiar", 11.99),
    Plato("Lasaña",9.99),
    Plato("Hamburguesa",4.50)
    ]

pedido= Pedido()
pedido.agregar_plato(menu[0])
#agregar lasaña al pedido
pedido.agregar_plato(menu[1])
#agregar pizza familiar al pedido

print("\nPedido actual:")
print(pedido.mostrar_pedido())
#mostrar platos del pedido

print(pedido.finalizar_pedido())
#finalizar y pagar el pedido





