# listas vacías para usuarios y préstamos
usuarios = []  # almacenar información de usuarios
prestamos_bicicletas = []  # almacenar información de préstamos

#registrar un usuario
def registrar_usuario():
    nombre = input("Ingrese el nombre del usuario: ")# ingresar el nombre
    numero_tarjeta = input("Ingrese el número de tarjeta: ")# ingresar el número de tarjeta
    
    usuarios.append([nombre, numero_tarjeta]) # agrega la información a lista de usuarios
    
    print(f"Usuario registrado: {nombre} - Tarjeta: {numero_tarjeta}")# confirmando el registro del usuario

# tomar una bicicleta
def tomar_bicicleta():
    
    numero_tarjeta = input("Ingrese el número de tarjeta del usuario: ")# ingresar el número de tarjeta
    origen = input("Ingrese el origen del préstamo: ")# ingresar el origen del préstamo
    destino = input("Ingrese el destino del préstamo: ")# ingresar el destino del préstamo

    usuario_encontrado = False
    
    for usuario in usuarios: # busca al usuario en la lista de usuarios por su número de tarjeta
        if usuario[1] == numero_tarjeta:
            usuario_encontrado = True
            break

    if usuario_encontrado:
        prestamos_bicicletas.append([numero_tarjeta, origen, destino])# agrega la información del préstamo a la lista de préstamos
        print(f"Usuario con tarjeta {numero_tarjeta} ha tomado una bicicleta en préstamo desde {origen} hasta {destino}")# Iiprime un mensaje confirmando el préstamo de la bicicleta
    else:
        print(f"Usuario con tarjeta {numero_tarjeta} no encontrado")# Imprime un mensaje si el usuario no se encuentra en la lista

# consultar usuarios
def consultar_usuarios():
    print("Listado de Usuarios:")
    for usuario in usuarios:# itera a través de la lista de usuarios e imprime su nombre y número de tarjeta
        print(f"Nombre: {usuario[0]}, Tarjeta: {usuario[1]}")

# consultar el listado de prestamos_bicicletas
def consultar_prestamos():
    print("Listado de Préstamos:")
    for prestamo in prestamos_bicicletas:# Itera a través de la lista de prestamos_bicicletas e imprime la información del prestamos_bicicletas
        print(f"Tarjeta: {prestamo[0]}, Origen: {prestamo[1]}, Destino: {prestamo[2]}")

# Menú principal
while True:
    print("\n**MENU**")
    print("1. Registrar Usuario")
    print("2. Tomar Bicicleta en Préstamo")
    print("3. Consultar Listado de Usuarios")
    print("4. Consultar Listado de Préstamos")
    print("5. Salir")

    opcion = input("Seleccione una opción (1/2/3/4/5): ")

    if opcion == "1":
        registrar_usuario()
    elif opcion == "2":
        tomar_bicicleta()
    elif opcion == "3":
        consultar_usuarios()
    elif opcion == "4":
        consultar_prestamos()
    elif opcion == "5":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida (1/2/3/4/5).")