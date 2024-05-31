import os,time

def clean():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")




def tiempo():
    time.sleep(2)
#cine
def menu_general():
    clean()
    print("== Menu ==")
    print("1. Mostrar Sala de cine")
    print("2. Comprar entrada de cine")
    print("3. Eliminar entradas")
    print("4. Mostrar ventas")
    print("5. Salir")

#opciones
def elegir_opcion(max_opciones):
    while True:
        opcion = 0
        try:
            opcion = int(input("Ingrese una de las opciones >> "))
        except:
            pass #pass hace que literalmente no muestre nada, solo continua...
        if opcion < 1 or opcion > max_opciones:
            print("Opción no válida \n")
            tiempo()
            clean()
            menu_general()
        else:
            return opcion #porque rompe el ciclo while? cuando la funcion encuentra "return" mata todo :v literalmente return es un /kill


sala = [
    ['A1','A2','A3','A4','A5'],
    ['B1','B2','B3','B4','B5'],
    ['C1','C2','C3','C4','C5'],
    ['D1','D2','D3','D4','D5'],
    ['E1','E2','E3','E4','E5'],
]
todas_las_entradas = []
entradas_vendidas = []
def imprimir_sala():
    print("\n=== SALA 7 ===\n")
    print(f"Entradas Ocupadas {entradas_vendidas}")
    impreza = ""

    for fila in sala:
        for asiento in fila:
            todas_las_entradas.append(asiento) #esto dejara dentro de la raid "todas_las_entradas" de entradas :v
            impreza += f"| {asiento} "
        impreza += "|\n"    
    print(impreza)

def comprar_entrada():
    entrada = input("Selecciona una entrada >> ")

    if entrada in todas_las_entradas and entrada not in entradas_vendidas:
        print("La entrada esta disponible")
        entradas_vendidas.append(entrada) #con esto se van registrando las entradas vendidas y se almacenan gracias al .append en: entradas_vendidas
    else:
        print("Entrada no existente")



#ejecución de: "def"
salir = False
while not salir: #el poner == False significa que 
    menu_general()
    opcion = elegir_opcion(5)

    if opcion == 1:
        print("== SALA ==")
        imprimir_sala()
        input("ENTER para salir")
    elif opcion == 2:
        imprimir_sala()
        comprar_entrada()

    elif opcion == 3:
        print("== Eliminar entradas ==")
    elif opcion == 4:
        print("== VENTAS ==")
    elif opcion == 5:
        print("== Saliendo ==")
        tiempo()
        salir = True
    else:
        print("Opcion no disponible")
    
    input()