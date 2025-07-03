import pandas as pd
import math
import os

# Configuración
archivo_original = r"C:\Users\57318\02-07-2025.csv"
output_folder = r"C:\Users\57318\Cargues"
tamaño_cargue = 1900

# Leer archivo original
df = pd.read_csv(archivo_original, sep=";", dtype={'PAGARE': str}, encoding='latin1')

# Formatear columna FECHA correctamente (aceptando fechas sin ceros iniciales, ejemplo: 6/16/2025)
# df['FECHA'] = pd.to_datetime(df['FECHA'], dayfirst=False, errors='coerce')
# df['FECHA'] = df['FECHA'].dt.strftime('%d/%m/%Y')

# Número de archivos
num_cargues = math.ceil(len(df) / tamaño_cargue)

for i in range(num_cargues):
    inicio = i * tamaño_cargue
    fin = inicio + tamaño_cargue
    df_cargue = df.iloc[inicio:fin]
    nombre_archivo = os.path.join(output_folder, f'cargue_{i+1}.csv')
    df_cargue.to_csv(nombre_archivo, index=False, encoding='latin1', sep=';')
    print(f"Archivo generado: {nombre_archivo}")

print("Proceso de división completado.")
