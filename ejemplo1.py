import numpy as np
import pandas as pd

datos = {'Mes':['Enero','Febrero','Marzo','Abril'],'Ingresos':[21500,17600,25000,34800],'Gastos':[17000,15400,19200,22500]}
df = pd.DataFrame(datos)
print("---- Datos de la tabla")
print(df)
print()
print("---- Tabla con beneficios ingresos - gastos")
#resta la serie de datos  Ingresos - Gastos
df['Beneficios'] = df['Ingresos'] - df['Gastos']

print(df)