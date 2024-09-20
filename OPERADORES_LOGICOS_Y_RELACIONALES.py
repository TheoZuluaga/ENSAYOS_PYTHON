#OPERADORES LOGICOS Y RELACIONALES

age = int(input("Digite la edad del usuario: "))

if age < 0:
    print("Ingresa una edad valida")
elif age < 16:
    print("Todavia no puede conducir")
elif age < 18:
    print("Puede obtener una licencia para conducir")
elif age < 70:
    print("Puede obtener una licencia estandar")
else:
    print("Necesita una licencia especial para conducir")

#########################################################

a = int(input("¿Cuantos años tiene tu computador? "))

if a < 0:
    print("Ingresa un numero válido")
elif a >= 0 and a <= 2:
    print("Tu computador es nuevo!!!" "\n" 
          "Puedes continuar con tu PC")
else:
    print("Tu computador es viejo" "\n"
          "Considera comprar uno nuevo" "\n")

