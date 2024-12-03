import pandas as pd

# Cargar todas las hojas y mostrar sus nombres
archivo = 'datosin.xlsx'
hojas = pd.ExcelFile(archivo).sheet_names
print("Hojas disponibles en el archivo:", hojas)
