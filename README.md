# Ejercicios-de-repaso-con-Python-

Ejercicio 1
Crea un programa que muestre un menú de opciones utilizando print() y if, elif, else.
Las opciones del menú serán:
• Mostrar una lista de productos
• Agregar un nuevo producto
• Salir
El programa debe:
• Mostrar la lista de productos al seleccionar la opción 1.
• Permitir agregar un nuevo producto a la lista cuando elijan la opción 2.
• Terminar el programa al elegir la opción 3.

Ejercicio 2
Crea un programa que almacene información de estudiantes en un diccionario
donde las claves sean los nombres de los estudiantes y los valores sean una lista
de cinco notas. El programa debe:
• Pedir al usuario el nombre de un estudiante.
• Permitir ingresar las tres notas.
• Calcular el promedio de las notas e imprimirlo.

Ejercicio 3
1. Crea una base de datos SQLite llamada escuela.db.
2. Crea una tabla llamada estudiantes con las columnas: id (número entero),
nombre (texto) y promedio (real).
3. Crea un programa en Python que:
o Inserte al menos 3 registros en la tabla estudiantes.
o Permita al usuario ingresar el nombre de un estudiante y buscarlo en
la base de datos.
o Si el estudiante existe, muestra su promedio. Si no existe, informa que
no fue encontrado.

Tip: Usa la librería sqlite3 para la manipulación de la base de datos.

Ejercicio 4
Crea un programa que lea y escriba en un archivo de texto. El programa debe:
1. Crear un archivo llamado notas.txt donde se almacenen nombres de
estudiantes y sus promedios (en formato de texto).
2. Leer el archivo y mostrar el contenido en pantalla.
3. Permitir al usuario agregar más estudiantes con sus promedios al archivo,
sin sobrescribir el contenido existente.

Ejercicio 5
Mejora el programa del Ejercicio 3 combinando el uso de archivos y SQLite. El
programa debe:
• Leer los datos de un archivo de texto (por ejemplo, datos_estudiantes.txt)
que contenga una lista de estudiantes y sus promedios.
• Insertar esos datos automáticamente en la base de datos SQLite escuela.db
si no existen.
• Mostrar los registros que se han insertado.