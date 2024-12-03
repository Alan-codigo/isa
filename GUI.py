import tkinter as tk
import pandas as pd
import re

# Función para convertir binario a decimal, si el valor es un binario válido
def binario_a_decimal(valor_binario):
    valor_binario = str(valor_binario).strip()
    # Validar si el valor es un número binario
    if re.fullmatch(r'[01]+', valor_binario):
        return int(valor_binario, 2)
    return None  # Si no es binario, retorna None

# Función para convertir decimal a binario, asegurando que tenga un número fijo de bits
def decimal_a_binario(valor_decimal, bits):
    if pd.isna(valor_decimal):
        return None  # Si es NaN, retorna None
    return format(int(valor_decimal), f'0{bits}b')  # Convierte a binario con ceros a la izquierda

# Función para convertir los datos del archivo Excel
def convertir_datos():
    try:
        df = pd.read_excel('datosin.xlsx')  # Cambia la ruta si es necesario
        # Eliminar espacios en blanco en los nombres de columnas y reemplazar NaN
        df.columns = df.columns.str.strip()
        df.columns = [str(col) if pd.notna(col) else "Unnamed" for col in df.columns]

        # Convertir columnas específicas de binario a decimal
        for col in ['OP1 (5)', 'OP2 (5)']:
            df[col] = df[col].apply(lambda x: binario_a_decimal(x) if isinstance(x, str) else x)

        # Convertir las columnas de decimal a binario
        df['We_BR (1)'] = df['We_BR (1)'].apply(lambda x: decimal_a_binario(x, 1))
        df['ALUOP (3)'] = df['ALUOP (3)'].apply(lambda x: decimal_a_binario(x, 3))
        df['DirRam (5)'] = df['DirRam (5)'].apply(lambda x: decimal_a_binario(x, 5))
        df['We_Ram (1)'] = df['We_Ram (1)'].apply(lambda x: decimal_a_binario(x, 1))

        # Convertir las columnas de decimal a binario para OP1 y OP2
        df['OP1 (5)'] = df['OP1 (5)'].apply(lambda x: decimal_a_binario(x, 5))
        df['OP2 (5)'] = df['OP2 (5)'].apply(lambda x: decimal_a_binario(x, 5))

        # Filtrar solo filas con datos válidos
        df_filtrado = df.dropna(subset=['OP1 (5)', 'OP2 (5)', 'We_BR (1)', 'ALUOP (3)', 'DirRam (5)', 'We_Ram (1)'])

        # Guardar los datos convertidos en un archivo .txt
        archivo_salida = 'datos_convertidos.txt'
        with open(archivo_salida, 'w') as f:
            for index, row in df_filtrado.iterrows():
                # Cambiamos el orden y formato según lo solicitado
                f.write(f"{row['OP1 (5)']}{row['OP2 (5)']}{int(row['We_BR (1)'])}{row['ALUOP (3)']}{row['DirRam (5)']}{int(row['We_Ram (1)'])}\n")

        etiqueta.config(text=f"Datos convertidos y guardados en: {archivo_salida}")

    except Exception as e:
        etiqueta.config(text=f"Error: {e}")

# Función para leer y mostrar datos de Excel
def leer_excel():
    try:
        df = pd.read_excel('datosin.xlsx')  # Cambia la ruta si es necesario
        print(df)  # Muestra los datos en la consola
        etiqueta.config(text="Datos leídos correctamente")
    except Exception as e:
        etiqueta.config(text=f"Error: {e}")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Lectura y Conversión de Excel")
ventana.geometry("700x400")

# Crear una etiqueta
etiqueta = tk.Label(ventana, text="Presiona el botón para leer datos")
etiqueta.pack(pady=10)

# Crear un botón para leer Excel
boton_leer = tk.Button(ventana, text="Leer Excel", command=leer_excel)
boton_leer.pack(pady=10)

# Crear un botón para convertir los datos
boton_convertir = tk.Button(ventana, text="Convertir Datos", command=convertir_datos)
boton_convertir.pack(pady=10)

# Ejecutar el bucle principal
ventana.mainloop()
