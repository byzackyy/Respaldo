import os,time

def animar():
    time.sleep(0.3)
def tiempo_error():
    time.sleep(2)
def limpiar():
    os.system("cls")
def tiempo_leer():
    time.sleep(1.5)

CANTIDAD_TARTA_MANZANA = 0
CANTIDAD_CHEESECAKE_FRAMBUESA = 0
CANTIDAD_PASTEL_CHOCOLATE = 0
CANTIDAD_GALLETA_AVENA = 0
CANTIDAD_MACARONS = 0
DESCUENTO_20K = 10
DESCUENTO = 0
TOTAL_PAGAR = 0
SUBTOTAL = 0
limpiar()
menu_dulces_encantos = True
while menu_dulces_encantos:
    try:
        print("==============[Dulces Encantos]==============")
        animar()
        print("1. Tarta de manzana \t\t 8000$")
        animar()
        print("2. Cheesecake de frambuesa \t 9000$")
        animar()
        print("3. Pastel de chocolate \t\t 7500$")
        animar()
        print("4. Galletas de avena \t\t 5000$")
        animar()
        print("5. Macarons (Docena) \t\t 8000$")
        animar()
        print("6. Anular pedido")
        animar()
        print("7. Pagar el pedido")
        opcion_menu_dulces_encantos = int(input("Seleccione una opción: "))
    except:
        print("La opción debe de ser de carácter numérico")
        tiempo_error()
        limpiar()
    if opcion_menu_dulces_encantos < 1 or opcion_menu_dulces_encantos > 7:
        print("La opción no es válida, intentelo nuevamente.")
        tiempo_error()
        limpiar()
    else:

        if opcion_menu_dulces_encantos == 1:
            CANTIDAD_TARTA_MANZANA = 0
            CANTIDAD_TARTA_MANZANA = int(input("Cuantas unidades desea? "))
            if CANTIDAD_TARTA_MANZANA == 0:
                print("debe de seleccionar almenos 1 unidad")
                tiempo_error()
                limpiar()
            else:
                print(f"Ha agregado al carrito {CANTIDAD_TARTA_MANZANA} Tarta de Manzana")
                tiempo_leer()
        elif opcion_menu_dulces_encantos == 2:
            CANTIDAD_CHEESECAKE_FRAMBUESA = 0
            CANTIDAD_CHEESECAKE_FRAMBUESA == int(input("Cuantas unidades desea? "))
            if CANTIDAD_CHEESECAKE_FRAMBUESA == 0:
                print("debe de seleccionar almenos 1 unidad")
                tiempo_error()
                limpiar()
            else:
                print(f"Ha agregado al carrito {CANTIDAD_CHEESECAKE_FRAMBUESA} Cheesecake de frambuesa")
                tiempo_leer()
                limpiar()
        elif opcion_menu_dulces_encantos == 3:
            CANTIDAD_PASTEL_CHOCOLATE = 0
            CANTIDAD_PASTEL_CHOCOLATE == int(input("Cuantas unidades desea? "))
            if CANTIDAD_PASTEL_CHOCOLATE == 0:
                print("debe de seleccionar almenos 1 unidad")
                tiempo_error()
                limpiar()
            else:
                print(f"Ha agregado al carrito {CANTIDAD_PASTEL_CHOCOLATE} Pastel de chocolate")
                tiempo_leer()
                limpiar()
        elif opcion_menu_dulces_encantos == 4:
            CANTIDAD_GALLETA_AVENA = 0
            CANTIDAD_GALLETA_AVENA == int(input("Cuantas unidades desea? "))
            if CANTIDAD_GALLETA_AVENA == 0:
                print("debe de seleccionar almenos 1 unidad")
                tiempo_error()
                limpiar()
            else:
                print(f"Ha agregado al carrito {CANTIDAD_GALLETA_AVENA} Galleta de avena")
                tiempo_leer()
                limpiar()
        elif opcion_menu_dulces_encantos == 5:
            CANTIDAD_MACARONS = 0
            CANTIDAD_MACARONS == int(input("Cuantas unidades desea? "))
            if CANTIDAD_MACARONS == 0:
                print("debe de seleccionar almenos 1 unidad")
                tiempo_error()
                limpiar()
            else:
                print(f"Ha agregado al carrito {CANTIDAD_MACARONS} Macarons (12 Unidades)")
                tiempo_leer()
                limpiar()
        elif opcion_menu_dulces_encantos == 6:
            try:
                print("Desea anular el pedido?")
                animar()
                print("1. Sí, anular pedido")
                print("2. No, Continuar comprando")
                opcion_anular = int(input("Seleccione una opción: "))
            except:
                print("La opción debe de ser de carácter numérico")
                tiempo_error()
                limpiar()
            if opcion_anular < 1 or opcion_anular > 2:
                print("La opción no es Válida")
                tiempo_error()
                limpiar()
            else:
                if opcion_anular == 1:
                    if CANTIDAD_TARTA_MANZANA == 0 and CANTIDAD_CHEESECAKE_FRAMBUESA == 0 and CANTIDAD_PASTEL_CHOCOLATE == 0 and CANTIDAD_GALLETA_AVENA == 0 and CANTIDAD_MACARONS == 0:
                        print("Debe de tener al menos un producto en su carrito para anular su pedido")
                        tiempo_error()
                        limpiar()
                    else:
                        print("Hasta luego")
                        tiempo_leer()
                        menu_dulces_encantos = False
                elif opcion_anular == 2:
                    print("Volviendo")
                    tiempo_leer()
                    limpiar()
        elif opcion_menu_dulces_encantos == 7:
            if CANTIDAD_TARTA_MANZANA == 0 and CANTIDAD_CHEESECAKE_FRAMBUESA == 0 and CANTIDAD_PASTEL_CHOCOLATE == 0 and CANTIDAD_GALLETA_AVENA == 0 and CANTIDAD_MACARONS == 0:
                print("Debe de tener al menos un producto en su carrito para pagar")
                tiempo_error()
                limpiar()
            else:
                menu_descuento = True
                while menu_descuento:
                        print("====Descuentos====")
                        animar()
                        print("1. Cliente Premium 20%")
                        animar()
                        print("2. Estudiante 15%")
                        animar()
                        print("3. No posee descuento")
                        opcion_menu_descuento = 0
                        try:
                            opcion_menu_descuento = int(input("Seleccione una opcion: "))
                        except:
                            print("La opción debe de ser de carácter numérico")
                            tiempo_error()
                            limpiar()
                        
                        if opcion_menu_descuento < 1 or opcion_menu_descuento > 3:
                            print("La opción no es válida")
                            tiempo_error()
                            limpiar()
                        else:
                            
                            if opcion_menu_descuento == 1:
                                DESCUENTO = 20
                                print("Ha seleccionado Cliente premium")
                            elif opcion_menu_descuento == 2:
                                DESCUENTO = 15
                                print("Ha seleccionado Estudiante")
                            elif opcion_menu_descuento == 3:
                                DESCUENTO = 0
                                print("Usted no posee descuentos")
                            else:
                                print("Opción no válida")
                            
                            menu_descuento = False

                limpiar()
                print("       DULCES ENCANTOS")
                print("_______________________________")
                if CANTIDAD_TARTA_MANZANA > 0:
                    animar()
                    print(f"{CANTIDAD_TARTA_MANZANA} Tarta de Manzana\t {CANTIDAD_TARTA_MANZANA*8000}")
                    
                if CANTIDAD_CHEESECAKE_FRAMBUESA > 0:
                    animar()
                    print(f"{CANTIDAD_CHEESECAKE_FRAMBUESA} Tarta de Manzana\t {CANTIDAD_CHEESECAKE_FRAMBUESA*9000}")               
                    
                if CANTIDAD_PASTEL_CHOCOLATE > 0:
                    animar()
                    print(f"{CANTIDAD_PASTEL_CHOCOLATE} Tarta de Manzana\t {CANTIDAD_PASTEL_CHOCOLATE*7500}")
                    
                if CANTIDAD_GALLETA_AVENA > 0:
                    animar()
                    print(f"{CANTIDAD_GALLETA_AVENA} Tarta de Manzana\t {CANTIDAD_GALLETA_AVENA*5000}")            
                    
                if CANTIDAD_MACARONS > 0:
                    animar()
                    print(f"{CANTIDAD_MACARONS} Tarta de Manzana\t {CANTIDAD_MACARONS*12000}")
                    
                CANTIDAD_PRODUCTOS = CANTIDAD_TARTA_MANZANA + CANTIDAD_CHEESECAKE_FRAMBUESA + CANTIDAD_PASTEL_CHOCOLATE + CANTIDAD_GALLETA_AVENA + CANTIDAD_MACARONS
                SUBTOTAL = CANTIDAD_TARTA_MANZANA*8000 + CANTIDAD_CHEESECAKE_FRAMBUESA*9000 + CANTIDAD_PASTEL_CHOCOLATE*7500 + CANTIDAD_GALLETA_AVENA*5000 + CANTIDAD_MACARONS*12000
                if SUBTOTAL > 20000:
                    print("Se le aplicará un descuento extra del 10%")
                    tiempo_leer()
                    DESCUENTO_2 = DESCUENTO + DESCUENTO_20K
                    TOTAL_PAGAR = SUBTOTAL - SUBTOTAL*DESCUENTO/100
                    print(f"Total a pagar: {TOTAL_PAGAR}")
                    print(f"DESCUENTO {DESCUENTO}")
                    print(f"CANTIDAD DE PRODUCTOS {CANTIDAD_PRODUCTOS}")
                    print("Gracias Por su compra :D")
                    tiempo_leer()

                else:
                    TOTAL_PAGAR = SUBTOTAL - SUBTOTAL*DESCUENTO/100
                    print(f"Total a pagar: {TOTAL_PAGAR}")
                    print(f"DESCUENTO {DESCUENTO}")
                    print(f"CANTIDAD DE PRODUCTOS {CANTIDAD_PRODUCTOS}")
                    print("Gracias Por su compra :D")
                    tiempo_leer()


                


                




                        
                        



#Boleta (cosa que nunca pude terminar en la prueba original Me disculpo por eso)


                        



