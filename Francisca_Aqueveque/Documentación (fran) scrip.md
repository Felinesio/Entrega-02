### EXPLICACIÓN DEL PROCESO DE SCRIPT


## IMPORTÉ LOS DATOS EN EXCEL PERO DEBÍA TRABAJARLOS EN FORMATO CSV. MODIFIQUÉ LOS ARCHIVOS

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


# Leer datos desde el archivo CSV (PASO 1)
datos = pd.read_csv('/content/drive/MyDrive/Excels Gatos Endemicos/ESPECIES (fran).csv')


# Definir mi filtro según la familia a la que pertenecen los gatos que es la FELIDAE (así se diferencian enseguida de los demás datos) (PASO 2)
felidae = 'FELIDAE'
felidae2 = 'Felidae'
felidae3 = 'felidae'


# Filtrar los datos para las variables de busqueda (PASO 3)
datos_felidae = datos [datos["FAMILIA"].str.contains(felidae) | datos["FAMILIA"].str.contains(felidae2) | datos["FAMILIA"].str.contains(felidae3)]

## LUEGO DE DEFINIR EL FILTRO Y DETERMINAR LAS VARIABLES ME PERCATÉ QUE NECESITABA INFORMACIÓN DE OTRAS VARIABLES. ALGO MUCHO MÁS DETALLADO. AL INTENTAR MODIFICAR EL CÓDIGO DESCRITO EN EL PASO 3 Y AGREGAR OTRAS VARIABLES DABA ERROR. INTENTÉ BUSCAR OTRO CAMINO: ELIMINAR LAS COLUMNAS QUE NO ME SIRVEN

# Eliminar columnas específicas
columnas_a_eliminar = ['SINONIMIA incompleta', 'PHYLLUM /\nDIVISIÓN']
datos_felidae = datos_felidae.drop(columns=columnas_a_eliminar)

print(datos_felidae)


## EN ESTE PUNTO EL CODIGO NO ME PERMITÍA ELIMINAR MÁS DE DOS COLUMNAS. Y DE LAS 43 COLUMNAS SOLO NECESITABA 5 O QUIZÁ 7. VOLVÍ A EMPEZAR OTRA VEZ


#Importar Libreria
import pandas as pd
import numpy as np


#Leer datos desde el archivo CSV
datos = pd.read_csv('/content/drive/MyDrive/Excels Gatos Endemicos/ESPECIES (fran).csv', index_col = 0)

df = pd.DataFrame(datos)
print(df.loc[[11.0, 12.0, 13.0, 14.0, 18.0],['NOMBRE COMÚN', 'NOMBRE CIENTÍFICO', 'REINO', 'CLASE', 'ORDEN', 'FAMILIA', 'DISTRIBUCIÓN REGIONES:\nANT= ANTARTICA\nDV= DESVENTURADAS\nIP= ISLA DE PASCUA\nJF= Arch. JUAN FERNÁNDEZ\nSG= SALAS Y GOMEZ\n? = Sin datos o de presencia dudosa o requiere confirmación']])

## HASTA ESTE PUNTO ESTE CÓDIGO (DF.LOC) PERMITE LOCALIZAR, POR SUEPUESTO, FUNCIONÓ A LA PERFECCIÓN...LUEGO DE DEVANARME LOS CESOS Y ENTENDER QUE PODÍA ORDENAR EL INDICE DESDE LA COLUMNA 0, O SEA, EL ID DE LOS GATUNOS QUE NECESITABA Y EL INDICE DE LAS COLUMNAS QUE QUERÍA SELECCIONAR



## CONTENTA PORQUE EL ANTERIOR FUNCIONÓ INTENTE HACER OTRO FILTRADO DE DATOS...PERO HABÍA COLUMNAS CON DATOS NaN O DATOS INNECESARIOS Y RECURRIRÍA AL MISMO MÉTODO DE "ELIMINAR PARA AVANZAR (CON DROP O DROPNA)" PERO ESTABA DEMÁS. ME QUEDÉ CON EL RESULTADO DEL CÓDIGO ANTERIOR :)


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











