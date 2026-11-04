# Práctica demostrativa y guiada: Obtención y exploración de datos con Python

**Duración:** 2 horas  
**Nivel:** Principiante  
**Asignatura:** Soluciona problemas de Machine Learning  
**Semestre:** Tercer semestre de preparatoria  
**Especialidad:** Inteligencia Artificial  
**Herramientas:** Visual Studio Code, Python, Pandas y NumPy.

## 1. Propósito de aprendizaje

Que los estudiantes aprendan a obtener, descargar, cargar y explorar conjuntos de datos públicos en formato CSV, identificando sus filas, columnas, características (*features*) y variable objetivo (*target*), como preparación para desarrollar modelos de Machine Learning.

## 2. Conceptos fundamentales

| Concepto | Explicación |
|---|---|
| Dataset | Conjunto de datos organizados. |
| CSV | Archivo de texto que almacena información separada por comas. |
| Filas | Registros u observaciones del conjunto de datos. |
| Columnas | Campos o variables que describen los registros. |
| Features (X) | Características utilizadas para realizar predicciones. |
| Target (y) | Variable que el modelo intentará predecir. |
| Exploración | Proceso de revisar, conocer y comprender los datos. |

**Ejemplo sencillo:**

Un dataset de estudiantes puede contener las columnas:

| Nombre | Edad | Horas de estudio | Aprobado |
|---|---:|---:|---|
| Ana | 16 | 5 | Sí |
| Luis | 17 | 2 | No |
| María | 16 | 6 | Sí |

- **Filas:** 3 estudiantes.
- **Columnas:** 4 variables.
- **Features:** Edad y horas de estudio.
- **Target:** Aprobado.

---

## 3. Preparación del entorno de trabajo en Visual Studio Code

Los cuatro ejemplos utilizarán Python y Pandas.

### Paso 1. Crear la carpeta del proyecto

Abrir la terminal de Visual Studio Code y ejecutar:

```bash
mkdir practica-obtencion-datos
cd practica-obtencion-datos
```

### Paso 2. Crear el entorno virtual

```bash
python -m venv .venv
```

Activarlo en Windows:

```bash
.venv\Scripts\activate
```

### Paso 3. Instalar las bibliotecas

```bash
python -m pip install pandas numpy
```

### Paso 4. Crear el archivo de dependencias

```bash
pip freeze > requirements.txt
```

### Paso 5. Verificar la instalación

```bash
python -c "import pandas as pd; import numpy as np; print('Pandas:', pd.__version__); print('NumPy:', np.__version__)"
```

### Estructura del proyecto

```text
practica-obtencion-datos/
│
├── .venv/
├── datasets/
│
├── ejemplo1_iris.py
├── ejemplo2_titanic.py
├── ejemplo3_vinos.py
├── ejemplo4_tips.py
│
└── requirements.txt
```

Los archivos CSV se descargarán automáticamente en la carpeta `datasets`.

---

## 4. Ejemplo 1. Dataset Iris: clasificación de flores

**Tipo de práctica:** Demostrativa.

![Comparación de las especies de flores Iris](https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Iris_sanguinea_1.jpg/800px-Iris_sanguinea_1.jpg)

**Problema:** Una inteligencia artificial necesita identificar la especie de una flor utilizando las medidas de sus pétalos y sépalos.

**Dataset:** Iris, conjunto de datos clásico de clasificación con 150 observaciones, cuatro características numéricas y una columna de especie.

**Descargar dataset:** [iris.csv](https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv)

**Archivo:** `ejemplo1_iris.py`

```python
import pandas as pd
import os

# URL del dataset público
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"

# Crear carpeta para guardar los datos
os.makedirs("datasets", exist_ok=True)

# Descargar y cargar el CSV
datos = pd.read_csv(url)

# Guardar una copia local
datos.to_csv("datasets/iris.csv", index=False)

# Explorar los datos
print("PRIMERAS 5 FILAS")
print(datos.head())

print("\\nCANTIDAD DE FILAS Y COLUMNAS")
print(datos.shape)

print("\\nNOMBRES DE LAS COLUMNAS")
print(datos.columns.tolist())

print("\\nINFORMACION DEL DATASET")
print(datos.info())

print("\\nCARACTERISTICAS (X)")
X = datos.drop(columns=["species"])
print(X.head())

print("\\nVARIABLE OBJETIVO (y)")
y = datos["species"]
print(y.head())

print("\\nESPECIES REGISTRADAS")
print(y.unique())
```

### Explicación didáctica

1. `pd.read_csv(url)` obtiene y carga el archivo CSV.
2. `to_csv()` guarda una copia en la computadora.
3. `head()` muestra las primeras cinco filas.
4. `shape` muestra la cantidad de filas y columnas.
5. `columns` obtiene los nombres de las columnas.
6. `info()` muestra los tipos de datos y valores no nulos.
7. `drop()` elimina la variable objetivo para separar las características.
8. `unique()` identifica las especies diferentes.

### Identificación de elementos

| Elemento | Identificación |
|---|---|
| Filas | 150 flores |
| Columnas | 5 |
| Features (X) | sepal_length, sepal_width, petal_length, petal_width |
| Target (y) | species |
| Tipo de problema | Clasificación |

**Pregunta para el estudiante:** ¿Qué medidas de una flor podrían ayudar a identificar su especie?

---

## 5. Ejemplo 2. Dataset Titanic: predicción de supervivencia

**Tipo de práctica:** Guiada.

![Barco Titanic](https://upload.wikimedia.org/wikipedia/commons/thumb/f/fd/RMS_Titanic_3.jpg/800px-RMS_Titanic_3.jpg)

**Problema:** Una inteligencia artificial necesita analizar los datos de los pasajeros del Titanic para identificar qué características están relacionadas con su supervivencia.

**Dataset:** Titanic, conjunto de datos con información de pasajeros, edades, sexo, clase y supervivencia.

**Descargar dataset:** [titanic.csv](https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv)

**Archivo:** `ejemplo2_titanic.py`

```python
import pandas as pd
import os

# URL del conjunto de datos
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv"

# Crear carpeta
os.makedirs("datasets", exist_ok=True)

# Descargar y cargar
datos = pd.read_csv(url)

# Guardar archivo
datos.to_csv("datasets/titanic.csv", index=False)

# Explorar información
print("PRIMEROS 5 PASAJEROS")
print(datos.head())

print("\\nDIMENSIONES")
print(datos.shape)

print("\\nCOLUMNAS")
print(datos.columns.tolist())

print("\\nINFORMACION GENERAL")
print(datos.info())

# Identificar características
columnas = ["pclass", "sex", "age", "fare", "sibsp", "parch"]

X = datos[columnas]

# Identificar variable objetivo
y = datos["survived"]

print("\\nCARACTERISTICAS (X)")
print(X.head())

print("\\nVARIABLE OBJETIVO (y)")
print(y.head())

print("\\nCANTIDAD DE SUPERVIVIENTES")
print(y.value_counts())

print("\\nVALORES FALTANTES")
print(datos.isnull().sum())
```

### Explicación didáctica

- `columns` permite conocer todas las variables disponibles.
- `X` selecciona seis características del pasajero.
- `y` contiene la variable `survived`.
- `value_counts()` cuenta cuántos pasajeros sobrevivieron y cuántos no.
- `isnull().sum()` cuenta los valores faltantes por columna.

### Identificación de elementos

| Elemento | Identificación |
|---|---|
| Filas | 891 pasajeros en esta versión |
| Columnas | 15 |
| Features (X) | Clase, sexo, edad, tarifa y datos familiares |
| Target (y) | survived |
| Tipo de problema | Clasificación binaria |

**Interpretación de la variable objetivo:**

- `0`: No sobrevivió.
- `1`: Sobrevivió.

**Pregunta para el estudiante:** ¿Consideras que la edad, el sexo y la clase del pasajero pueden ayudar a predecir su supervivencia?

---

## 6. Ejemplo 3. Dataset Wine Quality: predicción de calidad del vino

**Tipo de práctica:** Guiada.

![Vino y uvas](https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Red_Wine_Glass.jpg/800px-Red_Wine_Glass.jpg)

**Problema:** Una inteligencia artificial necesita analizar las propiedades químicas de diferentes muestras de vino para estimar su calidad.

**Dataset:** Wine Quality de UCI. Contiene mediciones fisicoquímicas y una calificación de calidad. Se puede utilizar para clasificación o regresión.

**Descargar dataset:** [winequality-red.csv](https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv)

**Archivo:** `ejemplo3_vinos.py`

```python
import pandas as pd
import os

# URL del dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"

# Crear carpeta
os.makedirs("datasets", exist_ok=True)

# Cargar CSV
# sep=";" indica que los valores están separados por punto y coma
datos = pd.read_csv(url, sep=";")

# Guardar archivo
datos.to_csv("datasets/winequality-red.csv", index=False)

# Explorar datos
print("PRIMERAS 5 MUESTRAS")
print(datos.head())

print("\\nDIMENSIONES")
print(datos.shape)

print("\\nCOLUMNAS")
print(datos.columns.tolist())

print("\\nINFORMACION GENERAL")
print(datos.info())

print("\\nESTADISTICAS")
print(datos.describe())

# Separar características
X = datos.drop(columns=["quality"])

# Variable objetivo
y = datos["quality"]

print("\\nCARACTERISTICAS (X)")
print(X.head())

print("\\nVARIABLE OBJETIVO (y)")
print(y.head())

print("\\nCALIFICACIONES REGISTRADAS")
print(y.value_counts().sort_index())
```

### Explicación didáctica

1. `sep=";"` indica que el separador del CSV es punto y coma.
2. `describe()` calcula estadísticas como promedio, mínimo, máximo y desviación estándar.
3. `drop()` separa las características de la variable objetivo.
4. `sort_index()` organiza las calificaciones de menor a mayor.

### Identificación de elementos

| Elemento | Identificación |
|---|---|
| Filas | 1,599 muestras |
| Columnas | 12 |
| Features (X) | 11 propiedades químicas |
| Target (y) | quality |
| Tipo de problema | Regresión o clasificación |

**Pregunta para el estudiante:** ¿Qué propiedades químicas podrían influir en la calidad de una muestra de vino?

---

## 7. Ejemplo 4. Dataset Tips: predicción de propinas en un restaurante

**Tipo de práctica:** Guiada.

![Servicio de restaurante](https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Restaurant_table_setting.jpg/800px-Restaurant_table_setting.jpg)

**Problema:** Un sistema inteligente necesita analizar las cuentas de un restaurante para estimar cuánto dinero podría recibir un mesero como propina.

**Dataset:** Tips, conjunto de datos con información de cuentas, propinas, comensales, días y horarios de servicio.

**Descargar dataset:** [tips.csv](https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv)

**Archivo:** `ejemplo4_tips.py`

```python
import pandas as pd
import os

# URL del dataset
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"

# Crear carpeta
os.makedirs("datasets", exist_ok=True)

# Descargar y cargar CSV
datos = pd.read_csv(url)

# Guardar archivo local
datos.to_csv("datasets/tips.csv", index=False)

# Explorar datos
print("PRIMERAS 5 FILAS")
print(datos.head())

print("\\nDIMENSIONES")
print(datos.shape)

print("\\nNOMBRES DE COLUMNAS")
print(datos.columns.tolist())

print("\\nINFORMACION GENERAL")
print(datos.info())

print("\\nESTADISTICAS")
print(datos.describe())

# Características de entrada
X = datos[["total_bill", "sex", "smoker", "day", "time", "size"]]

# Variable que se desea predecir
y = datos["tip"]

print("\\nCARACTERISTICAS (X)")
print(X.head())

print("\\nVARIABLE OBJETIVO (y)")
print(y.head())

print("\\nPROMEDIO DE PROPINA")
print(y.mean())
```

### Explicación didáctica

- `total_bill`: importe total de la cuenta.
- `sex`: sexo registrado del cliente.
- `smoker`: indica si el cliente es fumador.
- `day`: día de la semana.
- `time`: horario del servicio.
- `size`: número de comensales.
- `tip`: cantidad de dinero correspondiente a la propina.
- `mean()`: calcula el promedio de las propinas.

### Identificación de elementos

| Elemento | Identificación |
|---|---|
| Filas | 244 cuentas |
| Columnas | 7 |
| Features (X) | Cuenta, sexo, fumador, día, horario y comensales |
| Target (y) | tip |
| Tipo de problema | Regresión |

**Pregunta para el estudiante:** ¿Consideras que el importe total de una cuenta puede ayudar a predecir la propina?

---

## 8. Comparación de los cuatro conjuntos de datos

| Dataset | Filas | Columnas | Variable objetivo | Problema |
|---|---:|---:|---|---|
| Iris | 150 | 5 | species | Clasificación |
| Titanic | 891 | 15 | survived | Clasificación |
| Wine Quality | 1,599 | 12 | quality | Regresión / clasificación |
| Tips | 244 | 7 | tip | Regresión |

*Las cantidades corresponden a las versiones utilizadas en estos ejemplos.*

## 9. Organización de la práctica demostrativa y guiada (2 horas)

| Fase | Actividades de enseñanza-aprendizaje | Tiempo |
|---|---|---:|
| Apertura | 1. El docente explica qué es un dataset y para qué se utiliza en Machine Learning. 2. Presenta los conceptos CSV, filas, columnas, features y target. | 20 min |
| Desarrollo | 3. El docente demuestra cómo crear el entorno de Python y descargar un CSV. 4. Explica el ejemplo Iris paso a paso. 5. Los estudiantes ejecutan el ejemplo Titanic con orientación docente. 6. Los estudiantes exploran Wine Quality y Tips, identificando sus características y variables objetivo. | 80 min |
| Cierre | 7. Los estudiantes comparan los cuatro datasets. 8. Explican cuál utilizarían para desarrollar un modelo de clasificación y cuál para regresión. 9. Entregan sus resultados. | 20 min |
| **Total** | | **120 min** |

## 10. Actividad de evaluación para los estudiantes

Después de ejecutar los cuatro ejemplos, completar la siguiente tabla:

| Pregunta | Respuesta del estudiante |
|---|---|
| 1. ¿Qué es un dataset? | |
| 2. ¿Qué representa una fila? | |
| 3. ¿Qué representa una columna? | |
| 4. ¿Qué significa Feature (X)? | |
| 5. ¿Qué significa Target (y)? | |
| 6. ¿Qué función de Pandas permite cargar un CSV? | |
| 7. ¿Qué función permite conocer las dimensiones? | |
| 8. ¿Qué dataset utilizarías para clasificar flores? | |
| 9. ¿Qué dataset utilizarías para predecir propinas? | |
| 10. ¿Cuál es la diferencia entre clasificación y regresión? | |

## 11. Evidencias de aprendizaje e instrumentos de evaluación

| Evidencias | Características | Instrumento |
|---|---|---|
| E1. Entorno de trabajo | Carpeta, entorno virtual y bibliotecas instaladas. | Lista de cotejo |
| E2. Descarga de datasets | Cuatro archivos CSV almacenados correctamente. | Lista de cotejo |
| E3. Exploración de datos | Identifica filas, columnas y dimensiones. | Guía de observación |
| E4. Identificación de variables | Separa correctamente features (X) y target (y). | Ejercicio práctico |
| E5. Cuestionario | Responde las diez preguntas de aprendizaje. | Cuestionario |

## 12. Resultado esperado

Al finalizar las dos horas, el estudiante será capaz de:

1. Descargar conjuntos de datos públicos en formato CSV.
2. Utilizar Pandas para cargar y explorar información.
3. Identificar filas, columnas y tipos de datos.
4. Diferenciar las características de entrada (X) y la variable objetivo (y).
5. Reconocer cuándo un conjunto de datos puede utilizarse para clasificación o regresión.

**Recomendación didáctica:** Comienza con Iris, porque sus cinco columnas son fáciles de comprender. Posteriormente utiliza Titanic, Wine Quality y Tips para que los estudiantes reconozcan diferentes tipos de información y problemas de predicción. Estos ejercicios son de exploración de datos; todavía no entrenan modelos de Machine Learning.

---

## Recursos y enlaces de descarga

- [Dataset Iris (CSV)](https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv)
- [Dataset Titanic (CSV)](https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv)
- [Dataset Wine Quality (CSV)](https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv)
- [Dataset Tips (CSV)](https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv)
