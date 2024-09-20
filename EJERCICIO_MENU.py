import math

def areacuadrado():
    try:
        a = float(input("Escribe el valor de uno de los lados del cuadrado: "))
        print (f"El área del cuadrado es: {a ** 2}")
    except ValueError:
        print ("Digite una entrada válida...")

def areacirculo():
    try:
        a = float(input("Escribe el valor del radio del círculo: "))
        print (f"El área del circulo es {math.pi * (a ** 2)}")
    except ValueError:
        print ("Digite una entrada válida...")

def arearectangulo():
    try:
        b = float(input("Escribe el valor de la base: "))
        h = float(input("Escribe el valor de la altura: "))
        print (f"El área del rectangulo es {b * h}")
    except ValueError:
        print ("Digite una entrada válida...")

while True:

    menu = input ("""
    CALCULADORA

    ELIGE EL TIPO DE OPERACION QUE DESEAS REALIZAR

    [1] AREA DE UN CUADRADO
    [2] AREA DE UN CIRCULO
    [3] AREA DE UN RECTANGULO
    [4] SALIR
                      
    """)

    print (menu)

    if menu == "1":
        areacuadrado()
    elif menu == "2":
        areacirculo()
    elif menu == "3":
        arearectangulo()
    elif menu == "4":
        print ("Saliendo del programa...")
        break
    else:
        print("Elige una opcion válida...")
