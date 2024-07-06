def saludo():
    print("")

    total_compra = 0

def menu():
    opciones = [
        " Registrar Cliente.",
        " Lista de clientes registrados.",
        " Registrar una nueva compra.",
        " Lista de compras cliente.",
        " Salir.",
    ]
    for i, opcion in enumerate(opciones):
        print(f"{i+1}. {opcion}")

def registrar_cliente(base_datos):
    nombre = input("Ingrese nombre del cliente: ").upper()
    apellido = input("Ingrese apellido del cliente: ").upper()
    correo = input("Ingrese el correo del cliente: ").upper()

    
    id_cliente = len(base_datos) + 1

    base_datos.append(
        {
            "Nombre": nombre,
            "Apellido": apellido,
            "ID": id_cliente,
            "Correo": correo,
        }
    )
print()
print("Se ha registrado correctamente el nuevo socio")
print()

def lista_clientes_registrados(base_datos):
    print()
    print("Los clientes registrados en nuestra plataforma son:")
    print()
    print("Nombre, Apellido, ID, Correo")
    print()
    for cliente in base_datos:
        print(f'{cliente["Nombre"]}\t{cliente["Apellido"]}\t{cliente["ID"]}\t{cliente["Correo"]}')
    print("Su registro se ha generado con éxito.")

def calcular_puntos(monto):
    puntos = monto * 0.01
    puntos_enteros = (puntos) 
    return puntos_enteros

def registrar_nueva_compra(base_datos):
    id_cliente = int(input("Ingrese el ID del cliente que va a realizar la compra: "))

    for cliente in base_datos:
        if cliente["ID"] == id_cliente:
            fecha = input("Ingrese la fecha de la compra (AAAA-MM-DD): ")
            monto = int(input("Ingrese el valor total de la compra: "))
            cliente.setdefault("Compras", []).append({"Fecha": fecha, "Monto": monto})
            puntos_acumulados = calcular_puntos(monto)
            print(f"Compra registrada para el cliente {id_cliente} en la fecha de {fecha}")
            print(f"Monto de la compra: ${monto}")
            print(f"Puntos acumulados: {puntos_acumulados} puntos")
            return

def lista_de_compras_cliente(base_datos):
    id_cliente = int(input("Ingrese el ID del cliente del cual desea listar las compras: "))

    for cliente in base_datos:
        if cliente["ID"] == id_cliente:
            texto = f"ID Cliente: {id_cliente}\n"
            texto += f"Nombre Cliente: {cliente['Nombre']} {cliente['Apellido']}\n"
            texto += "Las compras que ha realizado el cliente son:\n"

            monto = 0

            if "Compras" in cliente:
                for compra in cliente["Compras"]:
                    texto += f'{compra["Fecha"]}\t\t${compra["Monto"]}\n'
                    compra["Monto"]
                print(f"El total de las compras registradas por el cliente son: {monto} Pesos")

            texto += f'El total de las compras registradas por el cliente son: {monto} Pesos\n'
            
            with open(f"COMPRAS_CLIENTE_{id_cliente}.txt", "w", encoding='utf-8') as COMPRAS_CLIENTE:
                COMPRAS_CLIENTE.write(texto)
            
            print(f"Se ha generado el archivo COMPRAS_CLIENTE_{id_cliente}.txt con las compras del cliente.")
            return

    print(f"No se encontró ningún cliente con el ID {id_cliente}.")
                    



       
         
        




