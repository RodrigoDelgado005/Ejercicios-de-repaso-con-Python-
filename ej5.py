import sqlite3
import os

def crear_base_de_datos():
    conexion = sqlite3.connect('escuela.db')
    cursor = conexion.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS estudiantes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT UNIQUE,
            promedio REAL
        )
    ''')
    conexion.commit()
    conexion.close()

def insertar_estudiantes():
    if not os.path.exists('notas.txt'):
        print("El archivo 'notas.txt' no existe.")
        return
    
    conexion = sqlite3.connect('escuela.db')
    cursor = conexion.cursor()

    with open('notas.txt', 'r') as archivo:
        for linea in archivo:
            nombre, promedio = linea.strip().split(':')
            nombre = nombre.strip()
            promedio = float(promedio.strip())
            
            try:
                cursor.execute('INSERT INTO estudiantes (nombre, promedio) VALUES (?, ?)', (nombre, promedio))
                print(f"Estudiante '{nombre}' agregado.")
            except sqlite3.IntegrityError:
                print(f"Estudiante '{nombre}' ya existe.")

    conexion.commit()
    conexion.close()

def mostrar_estudiantes():
    conexion = sqlite3.connect('escuela.db')
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM estudiantes")
    registros = cursor.fetchall()
    conexion.close()

    if registros:
        print("\nRegistros de estudiantes:")
        for id, nombre, promedio in registros:
            print(f"ID: {id}, Nombre: {nombre}, Promedio: {promedio}")
    else:
        print("No hay registros de estudiantes.")

def main():
    crear_base_de_datos()
    
    while True:
        opcion = input("\n1. Insertar estudiantes desde archivo\n2. Mostrar estudiantes\n3. Salir\nElige una opción: ")

        if opcion == "1":
            insertar_estudiantes()
        elif opcion == "2":
            mostrar_estudiantes()
        elif opcion == "3":
            print("Finalizando programa.")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
