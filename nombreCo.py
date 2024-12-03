import pandas as pd

# Leer el archivo de Excel
archivo_entrada = 'datosin.xlsx'  # Cambia a la ruta de tu archivo
df = pd.read_excel(archivo_entrada)

# Imprimir los nombres de las columnas
print("Nombres de las columnas:", df.columns)
