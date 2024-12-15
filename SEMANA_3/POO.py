#definición de la clase clima

print("\nº_º º_ª º_º º_ª º_ª ª_ª º_º º_ª º_º º_ª º_ª ª_ª º_º º_ª º_º º_ª º_ª ª_ª º_º º_ª º_º º_ª º_ª ª_ª")

class Clima:
    def __init__(self):
        self.dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
        self.temperaturas = {} #diccionario para almacenar las temperaturas

    def agregar_temperatura(self, dia, temperatura): #agrega la temperatura de un dia al diccionario
        self.temperaturas[dia] = temperatura

    def calcular_promedio_semanal(self):  # calcula y devuelve el promedio de las temperaturas ingresadas
        if len(self.temperaturas) == 0:
            return 0
        suma = sum(self.temperaturas.values())
        return suma / len(self.temperaturas)

    def mostrar_datos(self):   # muestra las temperaturas ingresadas y el promdeio semanal
        print("\nTEMPERATURAS DE LA SEMANA.")

        for dia in self.dias:
            temp = self.temperaturas.get(dia, "no ingresado")
            print(f"{dia}: {temp}ºC")

        promedio = self.calcular_promedio_semanal()
        print(f"\nPromedio semanal:{promedio:.2f}")

#función principal
def main():
    clima = Clima()
    print("\nIngrese las temperaturas para cada dia de la semana:")
    for dia in clima.dias:
        while True:
            try:
                temp = float(input(f"{dia}: "))
                break           # rompe el bucle si el valor ingresado es correcto
            except ValueError:
                print("debe ingresar un valor númerico")

        clima.agregar_temperatura(dia, temp)
    clima.mostrar_datos()       # muestra los datos despues d eingresar el valor de las temperaturas


#ejecutar el programa
if __name__ == "__main__":
    main()

print("\nº_º º_ª º_º º_ª º_ª ª_ª º_º º_ª º_º º_ª º_ª ª_ª º_º º_ª º_º º_ª º_ª ª_ª º_º º_ª º_º º_ª º_ª ª_ª")






