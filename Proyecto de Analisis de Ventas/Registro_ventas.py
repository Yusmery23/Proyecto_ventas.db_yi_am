import sqlite3
from datetime import datetime, timedelta
import random
import csv

# Conectar a la base de datos SQLite (o crearla si no existe)
conn = sqlite3.connect('ventas.db')
cursor = conn.cursor()

# Crear la tabla de ventas
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

# Insertar registros de ventas en la base de datos
for _ in range(20):
    producto, categoria = random.choice(productos)
    precio = generar_precio_aleatorio()
    cantidad = generar_cantidad_aleatoria()
    total = round(precio * cantidad, 2)
    fecha = generar_fecha_aleatoria().strftime("%Y-%m-%d")
    
    cursor.execute(''' INSERT INTO ventas (fecha, producto, categoria, precio, cantidad, total)
    VALUES (2023-10-23, "Aire acondicionado", "Electrodomestico", 300000, 2, 600000)''', 
    (fecha, producto, categoria, precio, cantidad, total))

# Guardar los cambios y cerrar la conexión
conn.commit()
conn.close()
