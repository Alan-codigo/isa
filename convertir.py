import pandas as pd
import re

# Ruta del archivo de entrada
archivo_entrada = 'datosin.xlsx'  # Cambia a la ruta de tu archivo
df = pd.read_excel(archivo_entrada)

# Eliminar espacios en blanco en los nombres de columnas y reemplazar NaN
df.columns = df.columns.str.strip()
df.columns = [str(col) if pd.notna(col) else "Unnamed" for col in df.columns]

# Imprimir los nombres de las columnas para verificar
print("Nombres de las columnas:", df.columns)

# Función para convertir binario a decimal, si el valor es un binario válido
def binario_a_decimal(valor_binario):
    valor_binario = str(valor_binario).strip()
    # Validar si el valor es un número binario
    if re.fullmatch(r'[01]+', valor_binario):
        return int(valor_binario, 2)
    else:
        return None  # Si no es binario, retorna None

# Convertir columnas específicas de binario a decimal
for col in ['OP1 (5)', 'OP2 (5)']:
    df[col] = df[col].apply(lambda x: binario_a_decimal(x) if isinstance(x, str) else x)
    print(f"Columna '{col}' después de conversión a decimal:")
    print(df[col])  # Imprimir resultados para cada columna

# Función para convertir decimal a binario, asegurando que tenga un número fijo de bits
def decimal_a_binario(valor_decimal, bits):
    if pd.isna(valor_decimal):
        return None  # Si es NaN, retorna None
    return format(int(valor_decimal), f'0{bits}b')  # Convierte a binario con ceros a la izquierda

# Convertir los valores numéricos a binario para las columnas restantes
def convertir_a_binario(valor_decimal, bits):
    if pd.isna(valor_decimal):
        return None
    try:
        return format(int(valor_decimal), f'0{bits}b')
    except (ValueError, TypeError):
        return None  # Manejar valores que no se pueden convertir

# Aplicar conversión de decimal a binario a las otras columnas
df['We_BR (1)'] = df['We_BR (1)'].apply(lambda x: convertir_a_binario(x, 1))
df['ALUOP (3)'] = df['ALUOP (3)'].apply(lambda x: convertir_a_binario(x, 3))
df['DirRam (5)'] = df['DirRam (5)'].apply(lambda x: convertir_a_binario(x, 5))
df['We_Ram (1)'] = df['We_Ram (1)'].apply(lambda x: convertir_a_binario(x, 1))

# Convertir las columnas de decimal a binario para OP1 y OP2
df['OP1 (5)'] = df['OP1 (5)'].apply(lambda x: decimal_a_binario(x, 5))
df['OP2 (5)'] = df['OP2 (5)'].apply(lambda x: decimal_a_binario(x, 5))

# Imprimir los datos después de la conversión para verificar
print("Datos después de la conversión:")
print(df)

# Filtrar solo filas con datos válidos y convertirlas a string
df_filtrado = df.dropna(subset=['OP1 (5)', 'OP2 (5)', 'We_BR (1)', 'ALUOP (3)', 'DirRam (5)', 'We_Ram (1)'])  # Filtrar solo las filas donde no hay NaN

# Guardar los datos convertidos en un archivo .txt
archivo_salida = 'datos_convertidos.txt'
with open(archivo_salida, 'w') as f:
    for index, row in df_filtrado.iterrows():
        # Escribir los valores en formato binario en el archivo
        f.write(f"{row['OP1 (5)']}{row['OP2 (5)']}{row['We_BR (1)']}{row['ALUOP (3)']}{row['DirRam (5)']}{row['We_Ram (1)']}\n")

print("Los datos se han convertido y guardado en:", archivo_salida)
