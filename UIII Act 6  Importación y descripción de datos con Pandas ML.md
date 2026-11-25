# **Práctica: Identificación de problemas en los datos — 2 horas**



Nivel: cero a principiante

Machine Learning

Python + VS Code



**Propósito:** Que los estudiantes aprendan a revisar conjuntos de datos (*datasets*) e identifiquen problemas que pueden afectar el entrenamiento de un modelo de Machine Learning.

Durante la práctica trabajaremos con dos casos diferentes:

1. **Caso 1. Datos de pasajeros del Titanic:** identificación de datos nulos, registros duplicados, tipos de datos y valores atípicos.
2. **Caso 2. Flores Iris:** identificación de problemas en un conjunto de datos al que se incorporarán errores simulados para aprender a detectarlos.

## **1. Conceptos básicos**

Antes de comenzar, el docente explica los cuatro problemas más comunes:

| Problema          | Descripción                                       | Ejemplo                             |
| ----------------- | ------------------------------------------------- | ----------------------------------- |
| Datos nulos       | Información que no está registrada.               | Edad vacía.                         |
| Duplicados        | Registros repetidos.                              | Dos filas con la misma información. |
| Tipos incorrectos | Datos almacenados con un tipo inadecuado.         | Edad guardada como texto.           |
| Valores atípicos  | Valores muy alejados del comportamiento habitual. | Edad de 250 años.                   |

**Pregunta para iniciar:** ¿Qué sucedería si entrenamos un modelo de inteligencia artificial utilizando información incompleta, repetida o incorrecta?

# **2. Preparación del entorno de trabajo**

## **Paso 1. Crear la carpeta principal**

1. Crear una carpeta en el escritorio o unidad de trabajo.
2. Asignarle el nombre `identificar-problemas-datos-0777`.
3. Abrir Visual Studio Code.
4. Seleccionar **Archivo → Abrir carpeta**.
5. Elegir la carpeta creada.

## **Paso 2. Crear la estructura de carpetas y archivos**

La estructura será la siguiente:

**identificar-problemas-datos-0777/**

&#x20;**.venv/**

Entorno virtual

&#x20;**caso1-titanic/**

&#x20;datos

&#x20;titanic.csv

&#x20;resultados

&#x20;analizar_titanic.py

&#x20;**caso2-iris/**

&#x20;datos

&#x20;iris.csv

&#x20;resultados

&#x20;analizar_iris.py

&#x20;requirements.txt

## **Paso 3. Crear y activar el entorno virtual**

En VS Code, abrir la terminal con:

**Terminal → Nuevo terminal**

Ejecutar los siguientes comandos en Windows PowerShell:

**Crear el entorno virtual:**

```
python -m venv .venv
```

**Activar el entorno virtual:**

```
.\.venv\Scripts\Activate.ps1
```

Si aparece un error relacionado con la ejecución de scripts, ejecutar:

```
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Después, activar nuevamente:

```
.\.venv\Scripts\Activate.ps1
```

Verificación

En la terminal debe aparecer `(.venv)` al inicio de la línea de comandos.

## **Paso 4. Instalar las librerías**

Crear el archivo `requirements.txt` y escribir:

```
pandas
numpy
matplotlib
seaborn
```

Instalar las librerías desde la terminal:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

**¿Para qué sirve cada librería?**

| Librería   | Función                               |
| ---------- | ------------------------------------- |
| Pandas     | Leer, organizar y analizar datos CSV. |
| NumPy      | Realizar operaciones numéricas.       |
| Matplotlib | Crear gráficas.                       |
| Seaborn    | Visualizar distribuciones de datos.   |

Verificar que las librerías se instalaron correctamente:

```
pip list
```

## **Paso 5. Seleccionar el intérprete de Python**

1. Presionar `Ctrl + Shift + P`.
2. Escribir `Python: Select Interpreter`.
3. Seleccionar el Python que se encuentra dentro de `.venv`.
4. Abrir la terminal y comprobar que el entorno está activado.

# **3. Caso 1. Identificación de problemas en los datos del Titanic**

[Titanic | National Museum of American History](https://images.openai.com/static-rsc-4/YVbLaEZDdEUfxGv3g_klaapq0MF54uLMDXwOXKZi_3XZkPFc0eKeIFSKuww1xQTSxHKSqiD5PoP0baOD4ObGujmbfrUr5G6i09DcB3-z2TsioQr72DzElS2pYiLCPpTO5klH5Jnx98_j5PFtTDBg2ePPIfhw7G3cMJwu_yjxxe4?purpose=inline)

**Situación problemática**

Tenemos información de pasajeros del Titanic. Antes de entrenar un modelo que prediga si un pasajero sobrevivió, necesitamos comprobar que los datos sean confiables.

## **Paso 1. Obtener el archivo CSV**

Descargar el conjunto de datos desde el siguiente enlace:

\- [Descargar titanic.csv desde GitHub](https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv?utm_source=chatgpt.com)

Guardar el archivo dentro de:

```
caso1-titanic/datos/titanic.csv
```

El dataset contiene información como edad, sexo, clase del pasajero, tarifa y supervivencia. También presenta valores faltantes en algunas columnas.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://github.com\&sz=32)

GitHub+1



## **Paso 2. Crear el archivo Python**

Crear el archivo:

`analizar_titanic.py`

Copiar el siguiente código completo:

```
# 7. Revisar valores estadisticosprint("\n===== ESTADISTICAS =====")print(df.describe())# 8. Identificar valores atipicos con IQRcolumna = "age"Q1 = df[columna].quantile(0.25)Q3 = df[columna].quantile(0.75)IQR = Q3 - Q1limite_inferior = Q1 - 1.5 * IQRlimite_superior = Q3 + 1.5 * IQRatipicos = df[    (df[columna] < limite_inferior) |    (df[columna] > limite_superior)]print("\n===== VALORES ATIPICOS EN EDAD =====")print("Limite inferior:", limite_inferior)print("Limite superior:", limite_superior)print("Cantidad de atipicos:", len(atipicos))# 9. Mostrar grafica de valores nulosplt.figure(figsize=(9, 4))sns.heatmap(df.isnull(), cbar=False, cmap="viridis")plt.title("Datos nulos del Titanic")plt.xlabel("Columnas")plt.ylabel("Registros")plt.tight_layout()os.makedirs("caso1-titanic/resultados", exist_ok=True)plt.savefig("caso1-titanic/resultados/nulos_titanic.png")plt.show()# 10. Crear una copia para limpiar los datosdf_limpio = df.copy()# 11. Eliminar registros completamente duplicadosdf_limpio = df_limpio.drop_duplicates()# 12. Completar edades faltantes con la medianadf_limpio["age"] = df_limpio["age"].fillna(    df_limpio["age"].median())# 13. Completar embarcaciones faltantesdf_limpio["embarked"] = df_limpio["embarked"].fillna(    df_limpio["embarked"].mode()[0])# 14. Convertir tipos de datosdf_limpio["survived"] = df_limpio["survived"].astype(int)# 15. Guardar el dataset limpiodf_limpio.to_csv(    "caso1-titanic/resultados/titanic_limpio.csv",    index=False)print("\n===== RESULTADO FINAL =====")print("Datos originales:", df.shape)print("Datos limpios:", df_limpio.shape)print("Archivo limpio guardado correctamente.")
```

## **Paso 3. Explicación breve del código**

| N.º | Instrucción          | ¿Qué realiza?                             |
| --- | -------------------- | ----------------------------------------- |
| 1   | `pd.read_csv()`      | Carga el archivo CSV.                     |
| 2   | `df.shape`           | Muestra filas y columnas.                 |
| 3   | `df.dtypes`          | Identifica tipos de datos.                |
| 4   | `df.isnull().sum()`  | Cuenta datos nulos.                       |
| 5   | `df.isnull().mean()` | Calcula porcentajes de nulos.             |
| 6   | `df.duplicated()`    | Detecta filas repetidas.                  |
| 7   | `df.describe()`      | Calcula estadísticas.                     |
| 8   | `quantile()`         | Obtiene cuartiles para detectar atípicos. |
| 9   | `sns.heatmap()`      | Representa datos faltantes.               |
| 10  | `df.copy()`          | Crea una copia de los datos.              |
| 11  | `drop_duplicates()`  | Elimina duplicados exactos.               |
| 12  | `fillna()`           | Completa edades faltantes.                |
| 13  | `mode()`             | Obtiene el valor más frecuente.           |
| 14  | `astype()`           | Convierte el tipo de dato.                |
| 15  | `to_csv()`           | Guarda el archivo limpio.                 |

**Importante para el alumno:** La detección de valores atípicos no significa que debamos eliminarlos automáticamente. Primero debemos investigar si representan errores o situaciones reales.

## **Paso 4. Ejecutar el programa**

Desde la terminal, en la carpeta principal:

```
python caso1-titanic/analizar_titanic.py
```

Se generarán los siguientes archivos:

```
caso1-titanic/
├── datos/
│   └── titanic.csv
├── resultados/
│   ├── nulos_titanic.png
│   └── titanic_limpio.csv
└── analizar_titanic.py
```

[Beyond Correlations: Hands-On Guide to Advanced Seaborn Heatmap Techniques | by Artem Grinberg | Medium](https://images.openai.com/static-rsc-4/WJDatcEcYE0FLK_7Mg9Nopp1-Nm35lqEmjKyksIkhSiBmqKVgQJNWi_I2wApMbhPCM6acPrMQdzHvsRapaIlF1oTo-zrIDn168dZtQ_xG5bXmeRunMbrRUc4LYwX7OQuKajxiebBtApikM64LUFAU2JhP-JPMzaiJWMUSIsqYjU?purpose=inline)

[medium.com](https://medium.com/%40grinberg42/beyond-correlations-hands-on-guide-to-advanced-seaborn-heatmap-techniques-0955f84392a4?utm_source=chatgpt.com)

**Resultado esperado:** El estudiante identifica cuántos datos faltan, cuántos duplicados existen, cuáles son los tipos de datos y qué edades se encuentran fuera del rango calculado mediante IQR.

# **4. Caso 2. Identificación de problemas en los datos de flores Iris**

[Michigan Graph Scheme for Stata – Andrew Grogan-Kaylor](https://images.openai.com/static-rsc-4/L--kfjcemshBGGt2K3IyPyL7ZxtB2ySL5t-YvfQo4QyGKI7a2LRjhTn24kFghXuwgbwQqPi_haqIK8YVyRtKHEjA9mBNhle49WuX3mutp2idwwUc3doIptWOjVaPcj-rPz7CsoqoFchqqD2OAefawiu2o16ozh-zJ4treieeT40?purpose=inline)

**Situación problemática**

Una escuela desea entrenar un modelo para clasificar flores Iris según las medidas de sus pétalos y sépalos. Antes de entrenar el modelo, debemos revisar la calidad de sus datos.

## **Paso 1. Obtener el archivo CSV**

Descargar el conjunto de datos:

\- [Descargar iris.csv desde GitHub](https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv?utm_source=chatgpt.com)

Guardar el archivo en:

```
caso2-iris/datos/iris.csv
```

El archivo contiene medidas de flores y una columna llamada `species`, que identifica su especie.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://github.com\&sz=32)

GitHub+1



## **Paso 2. Crear el archivo Python**

Crear:

`analizar_iris.py`

En este caso, para que todos los estudiantes puedan observar los cuatro tipos de problemas, el programa incorporará errores simulados a una copia del dataset. El archivo original permanecerá intacto.

```
# ==========================================# CASO 2: IDENTIFICACION DE PROBLEMAS# DATASET: IRIS# ==========================================import pandas as pdimport numpy as npimport os# 1. Cargar el archivo originaldf = pd.read_csv("caso2-iris/datos/iris.csv")print("\n===== DATOS ORIGINALES =====")print(df.head())# 2. Crear una copia para realizar pruebasdf_prueba = df.copy()# 3. Simular un dato nulodf_prueba.loc[0, "sepal_length"] = np.nan# 4. Simular un registro duplicadodf_prueba = pd.concat(    [df_prueba, df_prueba.iloc[[1]]],    ignore_index=True)# 5. Simular un tipo de dato incorrectodf_prueba["sepal_width"] = df_prueba[    "sepal_width"].astype(object)df_prueba.loc[2, "sepal_width"] = "desconocido"# 6. Simular un valor atipicodf_prueba.loc[3, "petal_length"] = 1000print("\n===== DATASET CON ERRORES SIMULADOS =====")print(df_prueba.head())# 7. Revisar dimensionesprint("\n===== DIMENSIONES =====")print(df_prueba.shape)# 8. Identificar datos nulosprint("\n===== DATOS NULOS =====")print(df_prueba.isnull().sum())# 9. Identificar duplicadosprint("\n===== DUPLICADOS =====")print("Total:", df_prueba.duplicated().sum())# 10. Revisar tipos de datosprint("\n===== TIPOS DE DATOS =====")print(df_prueba.dtypes)# 11. Detectar valores que no pueden convertirse a numeroprint("\n===== VALORES INCORRECTOS =====")
```

## **Paso 3. Explicación breve del código**

| N.º | Instrucción         | ¿Qué realiza?                            |
| --- | ------------------- | ---------------------------------------- |
| 1   | `pd.read_csv()`     | Carga el dataset Iris.                   |
| 2   | `df.copy()`         | Crea una copia de trabajo.               |
| 3   | `np.nan`            | Simula un dato nulo.                     |
| 4   | `pd.concat()`       | Agrega un registro repetido.             |
| 5   | `astype(object)`    | Permite mezclar texto y números.         |
| 6   | `1000`              | Simula un valor atípico.                 |
| 7   | `shape`             | Cuenta filas y columnas.                 |
| 8   | `isnull().sum()`    | Cuenta datos faltantes.                  |
| 9   | `duplicated()`      | Detecta duplicados.                      |
| 10  | `dtypes`            | Revisa los tipos de datos.               |
| 11  | `pd.to_numeric()`   | Detecta texto en columnas numéricas.     |
| 12  | `errors="coerce"`   | Convierte valores no numéricos en nulos. |
| 13  | `drop_duplicates()` | Elimina registros repetidos.             |
| 14  | `fillna()`          | Completa datos numéricos faltantes.      |
| 15  | `quantile()`        | Calcula límites para detectar atípicos.  |
| 16  | `to_csv()`          | Guarda el resultado.                     |

## **Paso 4. Ejecutar el programa**

En la terminal:

```
python caso2-iris/analizar_iris.py
```

Se generará el archivo:

```
caso2-iris/
├── datos/
│   └── iris.csv
├── resultados/
│   └── iris_revisado.csv
└── analizar_iris.py
```

Resultado esperado

El estudiante comprobará que el programa detecta los errores simulados y genera una versión revisada del conjunto de datos.

**Observación didáctica:** El valor `1000` es un error introducido intencionalmente. El programa lo identifica como atípico, pero no lo elimina automáticamente. El estudiante debe justificar si debe corregirse, conservarse o excluirse.

# **5. Comparación de los dos casos**

| Problema          | Caso 1: Titanic                        | Caso 2: Iris                                       |
| ----------------- | -------------------------------------- | -------------------------------------------------- |
| Datos nulos       | Se identifican en el archivo original. | Se simula uno.                                     |
| Duplicados        | Se revisan los existentes.             | Se agrega uno intencionalmente.                    |
| Tipos incorrectos | Se revisan los tipos originales.       | Se introduce texto en una columna numérica.        |
| Valores atípicos  | Se revisa la edad mediante IQR.        | Se introduce el valor 1000.                        |
| Limpieza          | Se completan algunos datos faltantes.  | Se convierten tipos y se corrigen algunos errores. |

# **6. Actividad de aprendizaje basado en problemas**

**Reto:** La escuela recibió dos archivos CSV para desarrollar modelos de Machine Learning. Los estudiantes deben determinar si la información está preparada para entrenar un modelo.

## **Procedimiento de trabajo**

1. Abrir el proyecto en VS Code.
2. Activar el entorno virtual.
3. Ejecutar el programa del Titanic.
4. Identificar los datos nulos y duplicados.
5. Revisar los tipos de datos.
6. Identificar valores atípicos.
7. Ejecutar el programa Iris.
8. Reconocer los cuatro errores simulados.
9. Comparar los resultados de ambos casos.
10. Explicar qué problemas deben corregirse antes de entrenar un modelo.

## **7. Organización de la sesión de 2 horas**

| Etapa      | Actividades                                                           | Tiempo      |
| ---------- | --------------------------------------------------------------------- | ----------- |
| Apertura   | Presentación de los cuatro problemas y preguntas iniciales.           | 20 min      |
| Desarrollo | Crear entorno virtual, instalar librerías y ejecutar el caso Titanic. | 35 min      |
| Desarrollo | Ejecutar el caso Iris, detectar errores y analizar resultados.        | 35 min      |
| Cierre     | Comparar resultados, responder preguntas y presentar conclusiones.    | 30 min      |
| **Total**  |                                                                       | **120 min** |

## **8. Cuestionario de evaluación**

Contesta con tus propias palabras:

1. ¿Qué es un dato nulo?
2. ¿Qué diferencia existe entre un dato nulo y un dato duplicado?
3. ¿Qué función de Pandas permite identificar datos faltantes?
4. ¿Para qué sirve `df.duplicated()`?
5. ¿Qué información proporciona `df.dtypes`?
6. ¿Qué sucede cuando una columna numérica contiene texto?
7. ¿Qué es un valor atípico?
8. ¿Para qué se utiliza el método IQR?
9. ¿Por qué no debemos eliminar automáticamente todos los valores atípicos?
10. ¿Por qué debemos revisar los datos antes de entrenar un modelo de Machine Learning?

## **9. Evidencias de aprendizaje e instrumentos**

| Evidencias       | Características                                    | Instrumento          |
| ---------------- | -------------------------------------------------- | -------------------- |
| Entorno virtual  | Entorno creado y librerías instaladas.             | Lista de cotejo.     |
| Programa Titanic | Código ejecutado y problemas identificados.        | Guía de observación. |
| Programa Iris    | Detección de errores simulados y archivo revisado. | Lista de cotejo.     |
| Cuestionario     | Respuestas correctas y explicadas.                 | Cuestionario.        |
| Conclusión       | Explica por qué es importante limpiar los datos.   | Rúbrica.             |

## **10. Recursos y documentación**

- [Documentación de Python en Visual Studio Code](https://code.visualstudio.com/docs/python/python-tutorial?utm_source=chatgpt.com).
- [Documentación de Pandas](https://pandas.pydata.org/docs/?utm_source=chatgpt.com).
- [Documentación de NumPy](https://numpy.org/doc/?utm_source=chatgpt.com).
- [Documentación de Matplotlib](https://matplotlib.org/stable/users/index.html?utm_source=chatgpt.com).
- [Documentación de Seaborn](https://seaborn.pydata.org/?utm_source=chatgpt.com).

**Conclusión para el alumno:** Antes de entrenar un modelo de inteligencia artificial, debemos verificar que los datos sean completos, estén organizados, tengan tipos correctos y no contengan errores que puedan afectar los resultados. Este proceso se conoce como preparación y limpieza de datos (*Data Cleaning*).
