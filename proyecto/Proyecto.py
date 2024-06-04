import sqlite3
import random
import csv
from datetime import datetime, timedelta

# Conectar a la base de datos SQLite (o crearla si no existe)
conn = sqlite3.connect('Registro_ventas.db')
cursor = conn.cursor()

# Crear la tabla de ventas si no existe
cursor.execute('''
CREATE TABLE IF NOT EXISTS ventas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fecha TEXT,
    producto TEXT,
    categoria TEXT,
    precio REAL,
    cantidad INTEGER,
    total REAL
)
''')

# Lista de productos y categorías para generar datos 
productos = [
    ("Aire acondicionado", "Electrodomestico"),
    ("Guitarra", "Electrónica"),
    ("Vestido", "Ropa"),
    ("Pantalon", "Ropa"),
    ("Cama", "Muebles"),
    ("Lavadora", "Electrodomestico"),
    ("Refrigerador", "Electrodomésticos"),
    ("Puerta", "Hogar"),
    ("Cuadros", "Hogar"),
    ("Juego de comedor", "Hogar")
]

# Función para generar una fecha aleatoria en el último año
def generar_fecha_aleatoria():
    inicio = datetime.now() - timedelta(days=365)
    fin = datetime.now()
    return inicio + (fin - inicio) * random.random()

# Función para generar un precio aleatorio
def generar_precio_aleatorio():
    return round(random.uniform(10.0, 1000.0), 2)

# Función para generar una cantidad vendida aleatoria
def generar_cantidad_aleatoria():
    return random.randint(1, 20)

def ingresar_datos(fecha, producto, categoria, precio, cantidad, total):
    cursor.execute(''' 
    INSERT INTO ventas (fecha, producto, categoria, precio, cantidad, total)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', (fecha, producto, categoria, precio, cantidad, total))
    conn.commit()

    # Insertar registros de ventas aleatorias en la base de datos


def ingresar_datos():
    fecha = datetime.now().strftime("%Y-%m-%d")
    producto = input("Ingrese el nombre del producto: ")
    categoria = input("Ingrese la categoría del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad vendida: "))
    total = precio * cantidad

    cursor.execute(''' 
    INSERT INTO ventas (fecha, producto, categoria, precio, cantidad, total)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', (fecha, producto, categoria, precio, cantidad, total))
    conn.commit()

def generar_datos_aleatorios():
    for _ in range(20):
        producto, categoria = random.choice(productos)
        precio = generar_precio_aleatorio()
        cantidad = generar_cantidad_aleatoria()
        total = round(precio * cantidad, 2)
        fecha = generar_fecha_aleatoria().strftime("%Y-%m-%d")
        
        cursor.execute(''' 
        INSERT INTO ventas (fecha, producto, categoria, precio, cantidad, total)
        VALUES (?, ?, ?, ?, ?, ?)
        ''', (fecha, producto, categoria, precio, cantidad, total))
    conn.commit()


while True:
    print("1. Ingresar datos manualmente")
    print("2. Generar datos aleatorios")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        ingresar_datos()
    elif opcion == '2':
        generar_datos_aleatorios()
    elif opcion == '3':
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")


# Obtener datos de la tabla ventas
cursor.execute("SELECT * FROM ventas")
ventas = cursor.fetchall()

# Escribir los datos en un archivo CSV
with open('ventas.csv', 'w', newline='') as archivo_csv:
    # Crear un escritor CSV
    escritor_csv = csv.writer(archivo_csv)
    
    # Escribir el encabezado
    escritor_csv.writerow(['ID', 'Fecha', 'Producto', 'Categoría', 'Precio', 'Cantidad', 'Total'])
    
    # Escribir los datos de ventas
    for venta in ventas:
        escritor_csv.writerow(venta)

# Guardar los cambios y cerrar la conexión
conn.commit()
conn.close()
