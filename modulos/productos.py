import pandas as pd

productos = [
    {"nombre": "Laptop", "precio": 2500000},
    {"nombre": "Mouse", "precio": 50000},
    {"nombre": "Teclado", "precio": 120000}
]

def listar_productos():
    return pd.DataFrame(productos)
