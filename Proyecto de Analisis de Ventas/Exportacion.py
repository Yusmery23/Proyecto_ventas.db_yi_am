import csv
from datetime import datetime

Producto_precio = {
    "Aire acondicionado": 250000,
    "Guitarra": 50000,
    "Vestido": 15000,
    "Pantalon": 5000,
    "Cama": 80000,
    "Lavadora": 45000,
    "Refrigerador": 100000,
    "Puerta": 20000,
    "Cuadros": 5000,
    "Juego de comedor": 30000

}

def ingresar_Producto():
    print("Seleccione un Producto:")
    for i, (Producto, precio) in enumerate(Producto_precio.items(), start=1):
        print(f"{i}. {Producto} - {precio}")
    seleccion = int(input("Ingrese el ID correspondiente al Producto: "))
    Producto = list(Producto_precio.keys())
    Categoria = list(Producto_precio.values())
    return Producto[seleccion - 1], precio[seleccion - 1]


def ingresar_datos():
    ID = input("Ingrese el ID: ")
    Fecha = input("Ingrese la Fecha de Venta: ")
    Nombre = input("Ingrese el nombre del producto: ")
    Categoria = input("Ingrese la categoria del producto: ")
    Precio = input("Ingrese el precio")
    Cantidad = float(input("Ingrese la cantidad vendida: "))
   
    return [ID, Fecha, Nombre, Categoria, Cantidad]

def guardar_datos(datos):
    with open('datos.csv', 'a', newline='') as archivo_csv:
        escritor = csv.writer(archivo_csv)
        escritor.writerow(datos)

def main():
    cabecera = ["ID", "Fecha", "Categoria", "Precio", "Cantidad", "Total"]
    # Verificar si el archivo CSV ya existe para no escribir la cabecera nuevamente
    try:
        with open('datos.csv', 'r') as archivo_csv:
            lector = csv.reader(archivo_csv)
            if not any(lector):
                with open('datos.csv', 'a', newline='') as archivo_csv:
                    escritor = csv.writer(archivo_csv)
                    escritor.writerow(cabecera)
    except FileNotFoundError:
        with open('datos.csv', 'a', newline='') as archivo_csv:
            escritor = csv.writer(archivo_csv)
            escritor.writerow(cabecera)

    datos = ingresar_datos()
    guardar_datos(datos)

if __name__ == "__main__":
    main()
