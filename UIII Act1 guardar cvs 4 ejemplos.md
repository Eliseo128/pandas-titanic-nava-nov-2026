¡Perfecto! Vamos a modificar el código para que, en lugar de leer los datos directamente desde internet cada vez, el script revise si el archivo ya existe en la carpeta `datos/` 📁. Si no existe, lo descarga desde la URL y lo guarda localmente usando **Pandas** 🐍.

Para guardar un DataFrame como un archivo CSV en local, utilizamos el método **`df.to_csv()`**.

---

### 💻 Código en Python para Descarga y Guardado Local

Aquí tienes el código listo para tu archivo `exploracion_datos.py`:

```python
import os
import pandas as pd

# 1. Creamos la carpeta 'datos' si aún no existe en el proyecto
os.makedirs("datos", exist_ok=True)

# ---------------------------------------------------------
# EJEMPLO 1: California Housing
# ---------------------------------------------------------
ruta_housing = "datos/california_housing.csv"
url_housing = "https://raw.githubusercontent.com/datasets/california-housing/main/data/california-housing.csv"

# Verificamos si ya está guardado localmente
if not os.path.exists(ruta_housing):
    print("⬇️ Descargando California Housing...")
    df_housing = pd.read_csv(url_housing)
    # Guardamos en la carpeta local (index=False evita guardar el número de fila)
    df_housing.to_csv(ruta_housing, index=False)
    print("✅ Guardado en:", ruta_housing)
else:
    print("📁 Cargando California Housing desde almacenamiento local...")
    df_housing = pd.read_csv(ruta_housing)

# ---------------------------------------------------------
# EJEMPLO 2: Iris Dataset
# ---------------------------------------------------------
ruta_iris = "datos/iris.csv"
url_iris = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"

if not os.path.exists(ruta_iris):
    print("⬇️ Descargando Iris Dataset...")
    df_iris = pd.read_csv(url_iris)
    df_iris.to_csv(ruta_iris, index=False)
    print("✅ Guardado en:", ruta_iris)
else:
    print("📁 Cargando Iris Dataset desde almacenamiento local...")
    df_iris = pd.read_csv(ruta_iris)

print("\n📊 Muestra del dataset Iris cargado:")
print(df_iris.head(2))

```

---

### 🔑 Concepto Clave

En la línea `df.to_csv(ruta, index=False)` incluimos el parámetro **`index=False`**.

**¿Por qué crees que es importante agregar `index=False` al momento de guardar un archivo CSV con Pandas?** *(Pista: piensa en qué pasa con los números de las filas `0, 1, 2...` cuando se genera el archivo).*
