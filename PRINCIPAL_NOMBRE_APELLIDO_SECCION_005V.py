from FUNCIONES_NOMBRE_APELLIDO_SECCION_005V import *

base_datos = [
    {
        "Nombre": "Jairo",
        "Apellido": "Cortés",
        "ID": 1,
        "Correo": "jai.cortesf@duocuc.cl",
        "Compras": [{"Fecha": "2024-09-03", "Monto": 48.356, "Puntos Acumulados": 534}, {"Fecha": "2024-08-04", "Monto": 1.000, "Puntos Acumulados": 357}]
    }
]

print("¡Bienvenido a nuestra plataforma de gestión de puntos en TODOAHORRO.")

while True:


    menu()    
    opcion = input("Ingrese la opción a ejecutar: ")

    if opcion == "1":
        registrar_cliente(base_datos)

    elif opcion == "2":
        lista_clientes_registrados(base_datos)

    elif opcion == "3":
        registrar_nueva_compra(base_datos)

    elif opcion == "4":
        lista_de_compras_cliente(base_datos)

    elif opcion == "5":
        print("¡GRACIAS POR PREFERIRNOS, HASTA LA PRÓXIMA!")
        break 

    else:
        print("Estimado cliente, la opción a ejecutar no es válida, por favor, inténtelo nuevamente.")