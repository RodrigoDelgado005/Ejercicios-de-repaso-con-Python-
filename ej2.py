estudiantes = {}

while True:
    nombre = input("Ingresa el nombre del estudiante: ")

    notas = []
    for i in range(3):
        nota = float(input(f"Ingresa la nota {i+1}: "))
        notas.append(nota)

    estudiantes[nombre] = notas

    promedio = sum(notas) / 3

    print(f"El promedio de {nombre} es: {promedio:.2f}\n")
    
    continuar = input("¿Queres agregar otro estudiante? (s/n): ").lower()
    if continuar != 's':
        print("Programa finalizado.")
        break
