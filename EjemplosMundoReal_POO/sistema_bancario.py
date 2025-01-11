#clase para representar una cuenta bancaria
class CuentaBancaria:
    def __init__(self,titular,numero,saldo=0.0):
        self.titular = titular      #titular de la cuenta
        self.numero = numero      #numero de la cuenta
        self.saldo = saldo         #saldo inicial

    def depositar(self,valor):
# se incrementa el saldo con el valor depositado
       if valor > 0:
           self.saldo += valor
           return f"Depósito exitoso.Su nuevo saldo es: {self.saldo}"
       else:
            return "el valor a depositar debe ser mayor que 0."

    def retirar(self,valor):
#disminuye el saldo si hay suficiente dinero en la cuenta
       if valor <= self.saldo:
          self.saldo-=valor
          return f"El  retiro fue exitoso.Nuevo saldo es:${self.saldo}"
       else:
            return f"saldo insuficiente para realizar el retiro."


    def consultar_saldo(self):
#retorna el saldo actual de la cuenta
        return f"{self.titular},el saldo actual en la cuenta {self.numero} es :${self.saldo}:"


#uso del sistema bancario
cuenta1 = CuentaBancaria("Miguel Fernandez", 234543, 700.0)
#crear una cuenta

print(cuenta1.consultar_saldo())
#muestra la información de la cuenta

print(cuenta1.depositar(700.0))
# se realiza un deposito

print(cuenta1.retirar(100.0))
#se realiza un retiro

print(cuenta1.consultar_saldo())
# consultar el saldo final de la cuenta
