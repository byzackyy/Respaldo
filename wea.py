import os

def limpiar():
    if os.name == "nt": # nt literalmente es Windows
        os.system("cls")
    else:
        os.system("clear") # GNU/Linux es literalmente (Linux "no hace falta explicarlo :v)



limpiar()


contador_usuarios = 0
usuarios = {}

menu = True
while menu:
    print("Bienvenido al programa de registros. \n")
    print("Por favor, seleccione una opción del menú: ")
    print("1. Agregar/eliminar registro")
    print("2. Ver los usuarios registrados")
    print("3. Salir del programa")
    opcion = input("Ingrese el número de la opción deseada\n Asegurese de que está ingresando un Número >>")





