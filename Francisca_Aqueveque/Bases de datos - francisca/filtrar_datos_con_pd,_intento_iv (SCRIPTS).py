# -*- coding: utf-8 -*-
"""Filtrar datos con pd, intento IV.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nEYcIinj_gYoN9CSwcJQmVLh_8uCEWAL
"""

import pandas as pd
datos = pd.read_excel("/content/drive/MyDrive/Excels Gatos Endemicos/ESPECIES.xlsx")
datos

"""MODIFICAR ARCHIVO A CSV

"""

from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
datos = pd.read_csv('/content/drive/MyDrive/Excels Gatos Endemicos/ESPECIES (fran).csv')
datos


#Leer datos desde el archivo CSV
datos = pd.read_csv('/content/drive/MyDrive/Excels Gatos Endemicos/ESPECIES (fran).csv')


# Definir mi filtro según la familia a la que pertenecen los gatos que es la FELIDAE (así se diferencian enseguida de los demás datos)
felidae = 'FELIDAE'
felidae2 = 'Felidae'
felidae3 = 'felidae'


# Filtrar los datos para las variables de busqueda
datos_felidae = datos [datos["FAMILIA"].str.contains(felidae) | datos["FAMILIA"].str.contains(felidae2) | datos["FAMILIA"].str.contains(felidae3)]


# Eliminar columnas específicas
columnas_a_eliminar = ['SINONIMIA incompleta', 'PHYLLUM /\nDIVISIÓN']
datos_felidae = datos_felidae.drop(columns=columnas_a_eliminar)

print(datos_felidae)

#Importar Libreria
import pandas as pd
import numpy as np


#Leer datos desde el archivo CSV
datos = pd.read_csv('/content/drive/MyDrive/Excels Gatos Endemicos/ESPECIES (fran).csv', index_col = 0)

df = pd.DataFrame(datos)
print(df.loc[[11.0, 12.0, 13.0, 14.0, 18.0],['NOMBRE COMÚN', 'NOMBRE CIENTÍFICO', 'REINO', 'CLASE', 'ORDEN', 'FAMILIA', 'DISTRIBUCIÓN REGIONES:\nANT= ANTARTICA\nDV= DESVENTURADAS\nIP= ISLA DE PASCUA\nJF= Arch. JUAN FERNÁNDEZ\nSG= SALAS Y GOMEZ\n? = Sin datos o de presencia dudosa o requiere confirmación']])

#Importar Libreria

import pandas as pd
import numpy as np

# Cargar y leer datos del archivo CSV
df = pd.read_csv('/content/drive/MyDrive/Excels Gatos Endemicos/ESPECIES (fran).csv', index_col = 0)

df.head ()

#Seleccionamos las columnas especificas
df[['NOMBRE COMÚN', 'NOMBRE CIENTÍFICO', 'REINO', 'CLASE', 'ORDEN', 'FAMILIA', 'DISTRIBUCIÓN REGIONES:\nANT= ANTARTICA\nDV= DESVENTURADAS\nIP= ISLA DE PASCUA\nJF= Arch. JUAN FERNÁNDEZ\nSG= SALAS Y GOMEZ\n? = Sin datos o de presencia dudosa o requiere confirmación']]

#Seleccionamos la categoría FELIDAE que es la FAMILIA a la que pertenecen los gatos estudiados

gatos = df[df['FAMILIA'] == 'Felidae']

gatos.head()