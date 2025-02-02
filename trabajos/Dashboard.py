import os
import subprocess
import emoji
from colorama import Fore, Style


#diseño del programa
def mostrar_inicio():
    os.system("cls" if  os.name=="nt" else "clear")  # limpia la pantalla antes de mostrar el diseño
    print("\n" + "="*50)
    print(f"{Fore.CYAN} {emoji.emojize(':rocket:')} Bienvenido al Dashboard {emoji.emojize(':rocket:')}{Style.RESET_ALL}")
    print("="*50)
mostrar_inicio()


#función para mostrar el contenido del script
def mostrar_codigo(ruta_script):

    # se obtiene la  ruta absoluta del archivo
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:    # intentar abrir el archivo en modo lectura
            codigo = archivo.read()   # lee todo el contenido del archivo

            print(f"\n {Fore.CYAN}---Código de {ruta_script}---{Style.RESET_ALL}\n")    #color  Cyan para el encabezado
            print(codigo)   # muestra el código leído
            return codigo    # devuelve el código leído


    except FileNotFoundError:
        print(f"{Fore.RED} El archivo no se encontró. {Style.RESET_ALL}")   # si el archivo no se encuentra, muestra un mensaje en rojo

        return None   # retorna none si ocurre un error
    except Exception as e:
        # en caso de otro error muestra un mensaje mas detallado
        print(f"{Fore.RED} Ocurrió un error al leer el archivo: {e} {Style.RESET_ALL}")
        return None

# función para ejecutar el script
def ejecutar_codigo(ruta_script):
    try:
        if os.name == 'nt':  # Windows

# abre una ventana de cmd para ejecutar el script
            subprocess.Popen(['cmd', '/k', 'python', ruta_script])
        else:  # Unix-based systems
            subprocess.Popen(['xterm', '-hold', '-e', 'python3', ruta_script])
    except Exception as e:

     # si ocurre un error, muestra un mensaje detallado en rojo
        print(f"{Fore.RED} Ocurrió un error al ejecutar el código: {e} {Style.RESET_ALL}")


#función para mostrar el menú principal
def mostrar_menu():
   # obtiene la ruta base del script actual
    ruta_base = os.path.dirname(__file__)

    unidades = {

        '1': '',
        '2': '',
        '3': ''
    }

    while True:
        print(f"\n {Style.BRIGHT}{Fore.GREEN} Menu Principal - Dashboard {Style.RESET_ALL}")
        # Imprime las opciones del menú principal y usa color verde para el título

        for key in unidades:
            print(f"{key} - {unidades[key]}")  #muestra opciones de unidades
        print("0 - Salir")


      # mensaje en rosado para elegir la unidad
        eleccion_unidad = input(f"{Style.BRIGHT}{Fore.WHITE} Elige una unidad o '0' para salir: {Style.RESET_ALL} ")
        if eleccion_unidad == '0':
            # si se elige 0, se muestra un mensaje de salida en color azul
            print(f"{Fore.BLUE} Saliendo del programa...{Style.RESET_ALL}")
            break
        elif eleccion_unidad in unidades:
            ruta_unidad = os.path.join(ruta_base, unidades[eleccion_unidad])# muestra el submenú de la unidad seleccionada
            print(f"Ruta unidad seleccionada: {ruta_unidad}")

            if os.path.exists(ruta_unidad):
                  mostrar_sub_menu(ruta_unidad)

            else:
                print(f"{Fore.RED} La ruta {ruta_unidad} no existe. Verifica la carpeta. {Style.RESET_ALL}")

        else:
            # si la opción es inválida muestra un mensaje en morado
            print(f"{Fore.GREEN} Opción no válida. Por favor, intenta de nuevo. {Style.RESET_ALL}")


#función para mostrar el submenu
def mostrar_sub_menu(ruta_unidad):
    sub_carpetas = [f.name for f in os.scandir(ruta_unidad) if f.is_dir()]  # obtiene las cubcarpetas de la unidad

    while True:
        # Imprime las subcarpetas
        print(f"\n{Style.BRIGHT}{Fore.MAGENTA} Submenú - Selecciona una subcarpeta {Style.RESET_ALL}")  # titulo en magenta

        for i, carpeta in enumerate(sub_carpetas, start=1):
            print(f"{i} - {carpeta}")    #muestra las subcarpetas disponibles
        print("0 - Regresar al menú principio")

        eleccion_carpeta = input(f"{Style.BRIGHT}{Fore.YELLOW} Elige una subcarpeta o '0' para regresar: {Style.RESET_ALL}")  # mensaje en amarillo para elegir subcarpeta
        if eleccion_carpeta == '0':
            break    # regresa al menu principal si se elige o
        else:
            try:
                eleccion_carpeta = int(eleccion_carpeta) - 1    # convierte la elección en un índice
                if 0 <= eleccion_carpeta < len(sub_carpetas):
                    mostrar_scripts(os.path.join(ruta_unidad, sub_carpetas[eleccion_carpeta])) # muestra scripts dentro de la subcarpeta
                else:
                    print(f"{Fore.RED} Opción no válida. Por favor, intenta de nuevo. {Style.RESET_ALL}")
            except ValueError:
                print(f"{Fore.RED} Opción no válida. Por favor, intenta de nuevo. {Style.RESET_ALL}")

#función para mostrar los scripts disponibles en una subcarpeta
def mostrar_scripts(ruta_sub_carpeta):
    scripts = [f.name for f in os.scandir(ruta_sub_carpeta) if f.is_file() and f.name.endswith('.py')]  #filtra solo archivos.py

    while True:
        print(f"\n{Fore.GREEN} Scripts - Selecciona un script para ver y ejecutar {Style.RESET_ALL}")  # titulo en verde
        # Imprime los scripts
        for i, script in enumerate(scripts, start=1):
            print(f"{i} - {script}")
        print("0 - Regresar al submenú anterior")
        print("9 - Regresar al menú principal")

        # muestar en mensaje en rosado para elegir los script
        eleccion_script = input(f"{Fore.RED} Elige un script, '0' para regresar o '9' para ir al menú principal: {Style.RESET_ALL}")
        if eleccion_script == '0':
            break
        elif eleccion_script == '9':
            return  # Regresar al menú principal
        else:
            try:
                eleccion_script = int(eleccion_script) - 1
                if 0 <= eleccion_script < len(scripts):
                    ruta_script = os.path.join(ruta_sub_carpeta, scripts[eleccion_script])   # construye la ruta completa del script
                    codigo = mostrar_codigo(ruta_script)
                    if codigo:
                        ejecutar = input(f"{Fore.BLACK} ¿Desea ejecutar el script? (1: Sí, 0: No): {Style.RESET_ALL}")
                        if ejecutar == '1':
                            ejecutar_codigo(ruta_script)
                        elif ejecutar == '0':
                            print(f"{Fore.GREEN} No se ejecutó el script.  {Style.RESET_ALL}")
                        else:
                            print(f"{Fore.RED} Opción no válida. Regresando al menú de scripts. {Style.RESET_ALL}")
                        input(f"\n{Fore.YELLOW} Presiona Enter para volver al menú de scripts. {Style.RESET_ALL}")   # pausa antes de regresar al menu
                else:
                    print(f"{Fore.RED} Opción no válida. Por favor, intenta de nuevo. {Style.RESET_ALL}")
            except ValueError:
                print(F"{Fore.BLACK} Opción no válida. Por favor, intenta de nuevo. {Style.RESET_ALL}")

# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()   # llama ala función que muestra el menu principal

def mostrar_final():
    print("\n" + "="*50)
    print(emoji.emojize(":star2: Gracias por usar el programa :star2:"))
    print("="*50)
    mostrar_final()