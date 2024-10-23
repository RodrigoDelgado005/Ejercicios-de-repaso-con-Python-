def leer_archivo():
    try:
        with open("notas.txt", "r") as archivo:
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo 'notas.txt' no existe.")

def agregar_estudiante():
    with open("notas.txt", "a") as archivo:
        nombre = input("Nombre del estudiante: ")
        promedio = input("Promedio: ")
        archivo.write(f"{nombre}: {promedio}\n")

while True:
    opcion = input("\n1. Leer archivo\n2. Agregar estudiante\n3. Salir\nElige una opción: ")

    if opcion == "1":
        leer_archivo()
    elif opcion == "2":
        agregar_estudiante()
    elif opcion == "3":
        break
    else:
        print("Opción no válida.")
