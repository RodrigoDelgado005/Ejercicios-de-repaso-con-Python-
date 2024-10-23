productos = ["Lucio", "Martin", "Barber"]

def mostrar_menu():
    print("\nMenú de opciones:")
    print("1. Mostrar lista de productos")
    print("2. Agregar un nuevo producto")
    print("3. Salir")

while True:
    mostrar_menu()
    opcion = input("Elige una opción (1-3): ")

    if opcion == "1":
        if productos:
            print("\nLista de productos:")
            for producto in productos:
                print(f"{producto}")
        else:
            print("\nNo hay productos en la lista.")
    elif opcion == "2":
        nuevo_producto = input("Ingresa el nombre del nuevo producto: ")
        productos.append(nuevo_producto)
        print(f"\nProducto '{nuevo_producto}' agregado a la lista.")
    elif opcion == "3":
        print("finalizando programa")
        break
    else:
        print("\nEsta opcion no existe. Intenta nuevamente.")
