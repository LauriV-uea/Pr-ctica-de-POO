#programa para calcular las ventas de una semana en una empresa de cosméticos


#definición de función para calcular el promedio de ventas a partir de una lista de ventas
#y retorna el promedio de las ventas
print("***************************************************************************************************")
def calcular_promedio_ventas(ventas):

    total_ventas =sum(ventas)
    promedio = total_ventas/len(ventas)
    return promedio


#programa principal
if __name__ == '__main__':
    print("cálculo del promedio de ventas semanales.")

#listas de los dias de la semana
    dias_semana = ["Lunes","Martes","Miércoles","Jueves","Viernes","Sábado","Domingo"]


#listas para almacenar las ventas diarias
    Ventas =[]

  # para solicitar ventas diarias
    for dia in dias_semana:
        while True:
            try:
                venta = float(input(f"Ingrese las ventas del día {dia} (en doláres):"))
                if venta < 0:
                    print("Las  ventas no pueden ser un número negativo, intente de nuevo.")
                else:
                    Ventas.append(venta)
                    break
            except ValueError:
                print("Error. Ingrese un número válido")


#calcular el promedio de ventas
    promedio_ventas = calcular_promedio_ventas(Ventas)

#verificar si las ventas superaron los $400
    ventas_exitosas = promedio_ventas > 400   # booleans


   #mostrar resultados
    print("....Resultados de las ventas ....")

    print(f"Promedio semanal de ventas: $ {promedio_ventas: }")

    if ventas_exitosas:

        print("¡Las ventas fueron exitosas esta semana!")

    else:
        print("Las ventas no alcanzaron el objetivo.")
        print("Suerte para la próxima semana.º_º")




