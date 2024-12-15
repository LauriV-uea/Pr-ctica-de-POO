## función para ingresare datos diarios de temperaturas
print("*****************************************************************************************")
print("*********************************Bienvenido.*********************************************")
def ingresar_tempertauras():
    dias = ["lunes","Martes", "Miercoles","Jueves","Viernes","Sábado", "Domingo"]
    temperaturas = []
    print("\nIngrese las temperaturas de cada día de la semana")

    for i in range(7):
        temp = float(input(f"{dias[i]}:"))
        temperaturas.append(temp)
    return dias,temperaturas


# función para calcular el valor promedio de las temperaturas

def calcular_promedio(temperaturas):
    return sum(temperaturas)/len(temperaturas)


# función principal para ejecutar el programa

def main():
    dias, temperaturas = ingresar_tempertauras()
    promedio = calcular_promedio(temperaturas)

    print(f"Temperaturas de la semana.")
    for i in range(7):
        print(f"{dias[i]}:{temperaturas[i]}ªC.")

    print(f"\n El promedio semanal de temperaturas es: {promedio:.2f}ºC.")

#ejecutar el programa
if __name__ == "__main__":
    main()

print("Gracias *_*")
print("*****************************************************************************************")