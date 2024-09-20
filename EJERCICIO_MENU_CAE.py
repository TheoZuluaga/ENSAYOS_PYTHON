"""
En este video aprenderemos a crear menus dentro de Python
y adicionalmente continuaremos entrenando los condicionales
viendo algunas características especiales (métodos) de los str
by: Sergio Andres Castaño Giraldo
https:\\controlautomaticoeducacion.com
"""
menu = """
Bienvenidos al registro de usuarios, llene los campos que usted
prefiera a continuaciÃ³n seleccionando un nÃºmero del 1 al 3:
[1] Digitar su Nombre 
[2] Digitar su edad
[3] Digitar su correo electronico  
""" 
print(menu)
opcion = input('Digita una opcion entre 1 y 3: ')
if opcion == '1':
    nombre = input('Digita tu nombre: ')
    if nombre.isalpha():
        print('Tu nombre es {}'.format(nombre))
    else:
        print('Has digitado un nombre no valido...')
elif opcion == '2':
    edad = input('Digita tu edad: ')
    if edad.isnumeric():
        print('Tu edad es {}'.format(edad))
    else:
        print('Has digitado una edad no valida...')
elif opcion == '3':
    email = input('Digita tu email: ')
    if email.find('@')>=0 and email.find('.')>=0:
        print('Tu e-mail es {}'.format(email))
    else:
        print('Has digitado un email no valido...')
else:
    print('Debes digitar un numero entre 1 y 3')
    print('=-='*20)
    