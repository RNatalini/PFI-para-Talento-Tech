# Pre-entrega del PFI - Natalini Ramiro

# Inicializamos las variables.
lista_productos = []
lista_productos.clear()
contador_productos = None
condicion = True
tituloproducto = "Producto"
titulocantidad = "Cantidad"
tituloprecio = "Precio"

# Bucle while para el menu interactivo

while condicion:
    print(90 * "*")
    print(f"{"":<23}{"Bienvenido al Inventario de Natiri-Rugs."}")
    print()
    print(f"{"":<10} {"1. Alta de producto."}")
    print(f"{"":<10} {"2. Baja de producto."}")
    print(f"{"":<10} {"3. Listado de productos."}")
    print(f"{"":<10} {"4. Salir."}")
    print()

    opcion = input("Ingrese la opcion que desea: ").lower()

    if opcion == "1":
        print("----------Estas en el Menu de alta de productos---------- ")
        while True:
            nombre_producto = (
                input("Ingrese el nombre del producto o escriba 'Salir': ")
                .strip()
                .lower()
            )

            if nombre_producto == "salir":
                break
            elif len(nombre_producto) == 0:
                print("Ingrese un nombre valido.")
            else:
                cantidad_producto = int(input("Cantidad: "))
                precio_lista_producto = float(input("Ingrese el precio: "))
                lista_productos.append(
                    [nombre_producto, cantidad_producto, precio_lista_producto]
                )
            # Agrego los datos del producto como una lista a la lista de productos
            # Falta agregar una verificacion para la existencia de producto y actualizacion de stock.
    elif opcion == "2":
        print("----------Estas en el Menu de baja de productos----------")
        if len(lista_productos) == 0:
            print("No hay productos para eliminar.")
        else:
            for i, producto in enumerate(
                lista_productos
            ):  # Aca hacemos una iteracion de los productos guardados para poder dar de baja alguno
                print(f"Ingrese '{i}' para borrar el producto: {producto[0]}")
            while True:
                eliminar = input(
                    "Indique que producto quiere eliminar o escriba 'salir' "
                ).lower()

                if eliminar == "":  # Verificacion de que no se ingrese un espacio
                    print("Error! Ingrese un valor valido.")
                    eliminar = input(
                        "Indique que producto quiere eliminar o escriba 'salir' "
                    ).lower()
                elif eliminar == "salir":  # Salida de la funcion de eliminar
                    break
                try:
                    eliminar = int(eliminar)
                    if (
                        0 <= eliminar < len(lista_productos)
                    ):  # Verificamos que el numero ingresado este dentro del rango de la lista de productos.
                        del lista_productos[eliminar]
                        print(
                            f"El Producto: '{producto[0]}' fue eliminado correctamente."
                        )
                    else:
                        print("Indice fuera de rango. Intente de nuevo.")
                except ValueError:
                    print("Error! Ingrese un numero valido.")

    elif opcion == "3":
        if len(lista_productos) == 0:
            print("No hay productos registrados.")
        else:
            print("----------LISTADO DE PRODUCTOS----------")
            print("%-15s %-15s %-15s" % (tituloproducto, titulocantidad, tituloprecio))
            indice = 0
            while indice < len(lista_productos):
                elemento = lista_productos[indice]
                print("%-15s %-15s %-15s" % (elemento[0], elemento[1], elemento[2]))
                indice += 1
            print("----------LISTADO DE PRODUCTOS----------")
        print()
        input("Pulse cualquier tecla para continuar. ")
    elif opcion == "4":
        condicion = False
        print("Saliendo del programa de inventario....")
    else:
        print("Opcion no valida, por favor intentelo de nuevo.")
print("Programa Finalizado.")
