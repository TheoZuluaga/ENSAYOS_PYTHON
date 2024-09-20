def convertirCelsius (temp, unidad):
    
    try:
        temp = float(temp)
    except ValueError:
        print ("¡¡¡ERROR!!! La temperatura debe ser un número")
        return
    
    if not unidad.isalpha():
        print ("¡¡¡ERROR!!! La unidad debe ser una letra (F/K)")
        return
    
    unidad = unidad.upper()

    if unidad not in ["F" , "K"]:
        print (f"Ingresa una unidad válida (F/K)")
    elif float(temp) and unidad == "K":
        print (f"{temp} celsius equivalen a {temp + 273.15} {unidad}")
    elif float(temp) and unidad == "F":
        print (f"{temp} celsius equivalen a {(temp * 1.8) + 32} {unidad}")


temp = input("Ingresa el valor de temperatura que quieres convertir: ")
unidad = input ("Ingresa la unidad que quieres saber (F/K): ")

convertirCelsius(temp, unidad)
