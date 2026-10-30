import numpy as np
import pandas as pd

titanic = pd.read_csv('titanic.csv',index_col=0)
print(titanic.head())
print()
#2. Mostramos dimensiones
print("------    dimensiones    shape -------")
print("Dimensiones : ",titanic.shape)
print("------    dimensiones    size -------")
print("Numero de datos : ",titanic.size)
print("------    dimensiones    columns -------")
print("Columnas : ",titanic.columns)
print("------    dimensiones    index-------")
print("Filas : ",titanic.index)
print("------    dimensiones    dtypes-------")
print("Tipos de datos : ",titanic.dtypes)
print("------    dimensiones    head() -------")
print("Primeras filas :",titanic.head(2))
print("------    dimensiones    tail(5) los ultimos 5-------")
print("Ultimas filas : ",titanic.tail(5))

print()

#4. Filas impares
# titanic_impares	Nombre de la variable donde se almacenarán los datos seleccionados.
# =	Operador de asignación. Guarda el resultado en la variable.
# titanic	DataFrame original que contiene los datos de los pasajeros del Titanic.
# .iloc[]	Método de Pandas que permite seleccionar filas y columnas mediante posiciones numéricas.
# range()	Función de Python que genera una secuencia de números enteros.
# 0	Posición inicial. Comienza desde la primera fila, cuya posición es 0.
# titanic.shape[0]	Obtiene la cantidad total de filas del DataFrame.
# 2	Paso o incremento. Selecciona una fila cada dos posiciones.
# titanic_impares = titanic.iloc[range(0,titanic.shape[0],2)]
print(" iloc")
# print(range(0,titanic.shape[0]))
# print()
# titanic_impares = titanic.iloc[range(0,10,2)]
titanic_impares = titanic.iloc[range(0,titanic.shape[0],2)]
print(titanic_impares.head(15))
print("porcentaje de sobrevivientes")
#5. Supervivientes
porcentaje_titanic=titanic['Survived'].value_counts()/titanic['Survived'].count()*100
print(porcentaje_titanic)


#6. Segunda clase
print("de segunda clase")
pasajeros_segunda=titanic[titanic['Pclass']==2]['Name'].sort_values()
print(pasajeros_segunda.head(5))

#7. Elimina nulos edad
print("Elimina nulos sin edad NaN")
titanic=titanic.dropna(subset=['Age'])
print(titanic)

#8. Muertos por clase
print("Muertos por clase agrupados por Pclass")
titanic_por_clase=titanic.groupby('Pclass')['Survived'].value_counts(normalize=True)*100
print(titanic_por_clase)

#9. Edad media por clase
print("promedio de edad por clase y sexo" )
print(titanic.groupby(['Pclass','Sex'])['Age'].mean())

#10. Menor de edad
print("pasajeros menores de edad" )
titanic['Menor']=titanic['Age']<18
print(titanic.head(15))