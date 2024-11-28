# precios.py
PRECIO_BASE = 10.0

def calcular_precio(precio_base, dia, edad):
    precio = precio_base
    if dia.lower() == "miércoles":
        precio *= 0.8
    if edad >= 65:
        precio *= 0.7
    return precio
