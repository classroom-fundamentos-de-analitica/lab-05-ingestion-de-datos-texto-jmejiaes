import pandas as pd
from pathlib import Path
import os
import zipfile

# Extraer el archivo ZIP
datos = zipfile.ZipFile('data.zip', 'r')
datos.extractall()
datos.close()

def procesar_carpeta(carpeta):
    data = []
    for root, _, files in os.walk(carpeta):
        
        for file in files:
            
            if file.endswith('.txt'):
                file_path = Path(root) / file
                label = Path(root).name 
                
                with file_path.open('r', encoding='utf-8') as f:
                    text = f.read().strip()
                    data.append((text, label)) 
                

    return data

def guardar_csv(datos, nombre_csv):
    df = pd.DataFrame(datos, columns=['phrase', 'sentiment'])
    df.to_csv(nombre_csv, index=False)
    #print(f'Archivo CSV guardado en: {nombre_csv}')



files = ["train_dataset.csv", "test_dataset.csv"]
for file in files:
    guardar_csv(procesar_carpeta(file.split("_")[0]), file)
