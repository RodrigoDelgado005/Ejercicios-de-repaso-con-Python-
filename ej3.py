import sqlite3

def crear_tabla():
    conexion = sqlite3.connect('escuela.db')
    cursor = conexion.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS estudiantes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            promedio REAL NOT NULL
        )
    ''')
    
    conexion.commit()
    conexion.close()

def insertar_registros():
    conexion = sqlite3.connect('escuela.db')
    cursor = conexion.cursor()

    estudiantes = [
        ('Lucio', 8.5),
        ('Martín', 7.2),
        ('Barber', 9.0)
    ]
    
    cursor.executemany('''
        INSERT INTO estudiantes (nombre, promedio) VALUES (?, ?)
    ''', estudiantes)
    
    conexion.commit()
    conexion.close()

def buscar_estudiante(nombre):
    conexion = sqlite3.connect('escuela.db')
    cursor = conexion.cursor()
    
    cursor.execute('''
        SELECT promedio FROM estudiantes WHERE nombre = ?
    ''', (nombre,))
    
    resultado = cursor.fetchone()
    
    if resultado:
        print(f"El promedio de {nombre} es: {resultado[0]}")
    else:
        print(f"Estudiante '{nombre}' no encontrado.")
    
    conexion.close()

crear_tabla()          
insertar_registros()   

while True:
    nombre = input("Ingresa el nombre del estudiante para buscar (o 'salir' para terminar): ")
    if nombre.lower() == 'salir':
        break
    buscar_estudiante(nombre)
