import tkinter as tk
import pandas as pd

# Función para leer y mostrar datos de Excel
def leer_excel():
    try:
        df = pd.read_excel('datosin.xlsx', sheet_name='in')
        print(df)  # Muestra los datos en la consola
        etiqueta.config(text="Datos leídos correctamente")
    except Exception as e:
        etiqueta.config(text=f"Error: {e}")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Lectura de Excel")
ventana.geometry("700x400")

# Crear una etiqueta
etiqueta = tk.Label(ventana, text="Presiona el botón para leer datos")
etiqueta.pack(pady=10)

# Crear un botón
boton = tk.Button(ventana, text="Leer Excel", command=leer_excel)
boton.pack(pady=10)

# Ejecutar el bucle principal
ventana.mainloop()
