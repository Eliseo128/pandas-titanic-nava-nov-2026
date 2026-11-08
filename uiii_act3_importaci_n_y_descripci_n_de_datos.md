# 📊 Análisis Exploratorio de Datos de Empleados de la Industria con Pandas y Matplotlib

* **Asignatura:** Soluciona problemas de Machine Learning  
* **Nivel:** Tercer semestre de preparatoria  
* **Especialidad:** Inteligencia Artificial  
* **Dificultad:** Cero a principiante  
* **Lenguaje:** Python  
* **Herramientas:** Visual Studio Code, Pandas, Matplotlib y CSV  

---

## 🎯 1. Propósito de la práctica

El estudiante aprenderá a realizar un análisis exploratorio de datos (**EDA**, *Exploratory Data Analysis*) utilizando las bibliotecas **Pandas** y **Matplotlib**.

Se trabajará con información ficticia de seis empleados de una industria, considerando diez características por empleado.

### 📋 Procedimiento de trabajo:
1. Crear un diccionario con diez listas y seis elementos por lista.
2. Convertir el diccionario en un DataFrame.
3. Explorar la estructura de los datos.
4. Guardar la información en un archivo CSV.
5. Leer nuevamente los datos desde el CSV.
6. Identificar tipos de datos, valores faltantes y estadísticas.
7. Ordenar, filtrar y agrupar información.
8. Crear gráficas para interpretar los datos.
9. Obtener conclusiones que puedan utilizarse posteriormente en Machine Learning.

---

## 🛠️ 2. Comandos de Pandas y Matplotlib más utilizados

### A. Comandos para explorar datos con Pandas

| Núm. | Comando | Función |
| :---: | :--- | :--- |
| **1** | `pd.DataFrame()` | Crear un DataFrame. |
| **2** | `pd.read_csv()` | Leer un archivo CSV. |
| **3** | `df.to_csv()` | Guardar un DataFrame en CSV. |
| **4** | `df.head()` | Mostrar los primeros registros. |
| **5** | `df.tail()` | Mostrar los últimos registros. |
| **6** | `df.shape` | Consultar dimensiones (filas y columnas). |
| **7** | `df.columns` | Mostrar nombres de columnas. |
| **8** | `df.index` | Consultar índices. |
| **9** | `df.info()` | Mostrar estructura y tipos de datos. |
| **10** | `df.dtypes` | Consultar tipos de datos. |
| **11** | `df.describe()` | Obtener estadísticas descriptivas numéricas. |
| **12** | `df.describe(include='all')` | Resumir variables numéricas y categóricas. |
| **13** | `df.isnull().sum()` | Contar valores faltantes (nulos). |
| **14** | `df.notnull().sum()` | Contar valores disponibles (no nulos). |
| **15** | `df.nunique()` | Contar valores únicos por columna. |
| **16** | `df['columna'].unique()` | Mostrar los diferentes valores únicos. |
| **17** | `df['columna'].value_counts()` | Contar frecuencias de cada valor. |
| **18** | `df['columna'].mean()` | Calcular el promedio. |
| **19** | `df['columna'].max()` | Obtener el valor máximo. |
| **20** | `df['columna'].min()` | Obtener el valor mínimo. |
| **21** | `df['columna'].sum()` | Calcular la suma total. |
| **22** | `df.sort_values()` | Ordenar registros por columna. |
| **23** | `df.groupby()` | Agrupar registros. |
| **24** | `df.loc[]` | Seleccionar filas y columnas por etiqueta. |
| **25** | `df.iloc[]` | Seleccionar filas y columnas por posición entera. |
| **26** | `df.drop_duplicates()` | Eliminar registros duplicados. |
| **27** | `df.corr(numeric_only=True)` | Calcular correlaciones numéricas. |
| **28** | `df['columna'].value_counts(normalize=True)` | Calcular frecuencias relativas (porcentajes). |

### B. Comandos para visualizar datos con Matplotlib

Primero se importa la biblioteca:
```python
import matplotlib.pyplot as plt
```

| Núm. | Comando | Función |
| :---: | :--- | :--- |
| **1** | `plt.figure()` | Crear una nueva figura/lienzo. |
| **2** | `plt.bar()` | Crear gráfica de barras. |
| **3** | `plt.plot()` | Crear gráfica de líneas. |
| **4** | `plt.scatter()` | Crear gráfica de dispersión. |
| **5** | `plt.hist()` | Crear histograma. |
| **6** | `plt.boxplot()` | Crear diagrama de caja (box plot). |
| **7** | `plt.pie()` | Crear gráfica circular (pastel). |
| **8** | `plt.title()` | Colocar título a la gráfica. |
| **9** | `plt.xlabel()` | Nombrar el eje X. |
| **10** | `plt.ylabel()` | Nombrar el eje Y. |
| **11** | `plt.xticks()` | Modificar marcas/etiquetas del eje X. |
| **12** | `plt.yticks()` | Modificar marcas/etiquetas del eje Y. |
| **13** | `plt.grid()` | Mostrar cuadrícula de fondo. |
| **14** | `plt.legend()` | Mostrar leyenda de elementos. |
| **15** | `plt.tight_layout()` | Ajustar automáticamente los espacios de la figura. |
| **16** | `plt.show()` | Mostrar gráfica en pantalla. |
| **17** | `plt.savefig()` | Guardar la gráfica como archivo de imagen. |
| **18** | `plt.subplots()` | Crear figura y cuadrícula de áreas de gráficas. |

---

## 🏭 3. Situación práctica: información de empleados de una industria

Una empresa industrial necesita analizar las características de sus empleados para conocer sus edades, salarios, antigüedad, departamentos y desempeño laboral.

Se utilizarán **diez variables**:

| Variable | Descripción | Tipo de dato sugerido |
| :--- | :--- | :--- |
| `id_empleado` | Identificador único del trabajador | Numérico (`int64`) |
| `nombre` | Nombre del empleado | Categórico (`object`) |
| `edad` | Edad en años | Numérico (`int64`) |
| `departamento` | Área de trabajo | Categórico (`object`) |
| `puesto` | Cargo o puesto laboral | Categórico (`object`) |
| `salario` | Salario mensual en pesos | Numérico (`int64` / `float64`) |
| `antiguedad` | Años trabajando en la empresa | Numérico (`int64`) |
| `horas_trabajadas` | Horas semanales trabajadas | Numérico (`int64`) |
| `capacitaciones` | Número de capacitaciones realizadas | Numérico (`int64`) |
| `desempeno` | Evaluación de desempeño (1-100) | Numérico (`int64`) |

> ⚠️ **Nota:** Los datos son ficticios y se utilizan exclusivamente con fines educativos.

---

## 💻 4. Preparación del entorno de trabajo en Visual Studio Code

### Paso 1. Crear la carpeta del proyecto
Crear una carpeta con el nombre:
```text
analisis-empleados-industria
```
Abrirla desde **Visual Studio Code**.

### Paso 2. Crear el entorno virtual
Abrir la terminal integrada de VS Code y ejecutar:
```powershell
python -m venv venv
```

### Paso 3. Activar el entorno virtual
En Windows (PowerShell):
```powershell
.\venv\Scripts\Activate.ps1
```
Si utilizas CMD (Símbolo del sistema):
```cmd
.\venv\Scripts\activate.bat
```

### Paso 4. Instalar las bibliotecas necesarias
```powershell
python -m pip install pandas matplotlib
```

### Paso 5. Verificar las instalaciones
```powershell
pip list
```

### Paso 6. Crear los archivos del proyecto
La estructura de archivos de la carpeta debe quedar de la siguiente forma:
```text
analisis-empleados-industria/
├── venv/
├── empleados_industria.csv
├── explorar_datos_empleados.py
└── requirements.txt
```

Crear el archivo `requirements.txt`:
```text
pandas
matplotlib
```

---

## 📦 5. Crear el diccionario con 10 listas y 6 elementos

### Paso 7. Crear los datos de los empleados
En el archivo `explorar_datos_empleados.py`, escribir el siguiente código.

Primero importamos las bibliotecas:
```python
import pandas as pd
import matplotlib.pyplot as plt
```

Después creamos un diccionario llamado `empleados`, que contiene diez listas con seis elementos cada una:

```python
# 1. Crear diccionario de datos de empleados
empleados = {
    "id_empleado": [101, 102, 103, 104, 105, 106],
    "nombre": ["Carlos", "Maria", "Jose", "Ana", "Luis", "Sofia"],
    "edad": [25, 32, 28, 40, 35, 29],
    "departamento": ["Produccion", "Calidad", "Mantenimiento", "Produccion", "Calidad", "Mantenimiento"],
    "puesto": ["Operador", "Inspector", "Tecnico", "Supervisor", "Auditor", "Tecnico"],
    "salario": [12000, 15000, 13500, 22000, 16000, 14500],
    "antiguedad": [2, 6, 4, 12, 8, 3],
    "horas_trabajadas": [40, 42, 45, 48, 40, 44],
    "capacitaciones": [3, 5, 2, 8, 6, 4],
    "desempeno": [85, 90, 78, 95, 88, 82]
}
```

> **💡 Explicación:**
> * `empleados`: es el nombre del diccionario en Python.
> * Las **claves** (ej. `"edad"`, `"salario"`) representan las columnas del conjunto de datos.
> * Los **valores** entre corchetes `[...]` son las listas de datos.
> * Cada lista contiene **seis elementos**, correspondiendo cada índice a un mismo empleado.

---

## 📊 6. Convertir el diccionario en un DataFrame

### Paso 8. Crear la tabla de empleados
Utilizamos `pd.DataFrame()` para convertir el diccionario estructurado en un objeto DataFrame (tabla de Pandas).

```python
# 2. Convertir el diccionario en un DataFrame
df = pd.DataFrame(empleados)

print("--- TABLA ORIGINAL DE EMPLEADOS ---")
print(df)
```

**Resultado esperado (vista parcial):**

| id_empleado | nombre | edad | departamento | salario | antiguedad |
| :---: | :--- | :---: | :--- | :---: | :---: |
| 101 | Carlos | 25 | Produccion | 12,000 | 2 |
| 102 | Maria | 32 | Calidad | 15,000 | 6 |
| 103 | Jose | 28 | Mantenimiento | 13,500 | 4 |
| 104 | Ana | 40 | Produccion | 22,000 | 12 |
| 105 | Luis | 35 | Calidad | 16,000 | 8 |
| 106 | Sofia | 29 | Mantenimiento | 14,500 | 3 |

*(La tabla completa en ejecución muestra las 10 columnas).*

---

## 💾 7. Convertir el DataFrame en archivo CSV

### Paso 9. Guardar los datos
Utilizamos el método `.to_csv()` para exportar nuestro DataFrame a un archivo separado por comas (`.csv`).

```python
# 3. Exportar los datos a CSV
df.to_csv("empleados_industria.csv", index=False, encoding="utf-8-sig")

print("\nArchivo CSV guardado correctamente.")
```

**Explicación de los parámetros:**
| Parámetro | Función |
| :--- | :--- |
| `"empleados_industria.csv"` | Nombre y ruta del archivo a crear. |
| `index=False` | Evita que Pandas guarde el índice numérico como una columna adicional. |
| `encoding="utf-8-sig"` | Asegura la correcta lectura de caracteres especiales (acentos, ñ) en programas como Excel. |

---

## 📂 8. Leer los datos desde el archivo CSV

### Paso 10. Importar nuevamente los datos
En proyectos reales trabajaremos con archivos externos. Leemos el archivo recién creado usando `pd.read_csv()`.

```python
# 4. Importar datos desde el archivo CSV
df = pd.read_csv("empleados_industria.csv")

print("\n--- DATOS LEÍDOS DESDE EL ARCHIVO CSV ---")
print(df)
```

> **❓ ¿Por qué hacemos esto?**  
> Porque en proyectos de Machine Learning es habitual consumir los datos desde archivos CSV, bases de datos o APIS, en lugar de escribirlos manualmente en código.

---

## 🔍 9. Análisis exploratorio de datos (EDA)

A partir de este punto, utilizaremos las funciones principales de Pandas para analizar a fondo nuestro dataset.

### Paso 11. Mostrar los primeros registros
```python
print("\n--- PRIMEROS REGISTROS (head) ---")
print(df.head())
```
*Por defecto `head()` muestra 5 filas. Podemos especificar la cantidad pasando un argumento: `df.head(3)`.*

### Paso 12. Mostrar los últimos registros
```python
print("\n--- ÚLTIMOS REGISTROS (tail) ---")
print(df.tail(3))
```

### Paso 13. Conocer las dimensiones del DataFrame
```python
print("\n--- DIMENSIONES DEL DATAFRAME ---")
print(df.shape)
```
**Resultado:** `(6, 10)` → Significa **6 filas (registros)** y **10 columnas (variables)**.

### Paso 14. Consultar los nombres de las columnas
```python
print("\n--- NOMBRES DE LAS COLUMNAS ---")
print(df.columns)
```

### Paso 15. Identificar los tipos de datos
```python
print("\n--- TIPOS DE DATOS ---")
print(df.dtypes)
```

**Interpretación típica:**
| Variable | Tipo de dato en Pandas |
| :--- | :--- |
| `id_empleado`, `edad`, `salario`, `antiguedad`, `horas_trabajadas`, `capacitaciones`, `desempeno` | `int64` (Números enteros) |
| `nombre`, `departamento`, `puesto` | `object` (Cadenas de texto) |

### Paso 16. Consultar la información general del dataset
```python
print("\n--- INFORMACIÓN GENERAL ---")
df.info()
```
*Permite revisar rápidamente el conteo de no-nulos y uso de memoria.*

### Paso 17. Obtener estadísticas descriptivas
```python
print("\n--- ESTADÍSTICAS DESCRIPTIVAS NUMÉRICAS ---")
print(df.describe())
```
**Métricas generadas automáticamente:**
* `count`: Cantidad de registros no nulos.
* `mean`: Promedio.
* `std`: Desviación estándar.
* `min`: Valor mínimo.
* `25%`, `50%`, `75%`: Cuartiles / Mediana.
* `max`: Valor máximo.

Para incluir también estadísticas de variables categóricas:
```python
print(df.describe(include='all'))
```

### Paso 18. Identificar valores faltantes (nulos)
```python
print("\n--- VALORES FALTANTES POR COLUMNA ---")
print(df.isnull().sum())
```

### Paso 19. Identificar registros duplicados
```python
print("\n--- REGISTROS DUPLICADOS ---")
print(df.duplicated().sum())
```

### Paso 20. Identificar valores únicos
```python
print("\n--- CANTIDAD DE VALORES ÚNICOS PER COLUMNA ---")
print(df.nunique())

print("\nDepartamentos únicos:")
print(df['departamento'].unique())
```
**Resultado esperado:** `['Produccion' 'Calidad' 'Mantenimiento']`

### Paso 21. Contar empleados por departamento
```python
print("\n--- EMPLEADOS POR DEPARTAMENTO ---")
print(df['departamento'].value_counts())
```

### Paso 22. Calcular el promedio del salario
```python
salario_promedio = df['salario'].mean()
print(f"\nSalario promedio: ${salario_promedio:.2f}")
```
*Resultado:* `$15583.33`

### Paso 23. Consultar salario máximo y mínimo
```python
print(f"Salario máximo: ${df['salario'].max()}")
print(f"Salario mínimo: ${df['salario'].min()}")
```

### Paso 24. Ordenar empleados por salario
```python
print("\n--- EMPLEADOS ORDENADOS POR SALARIO (DE MAYOR A MENOR) ---")
print(df.sort_values(by='salario', ascending=False))
```

### Paso 25. Filtrar empleados con salario superior a $15,000
```python
print("\n--- EMPLEADOS CON SALARIO MAYOR A $15,000 ---")
filtro_salario = df[df['salario'] > 15000]
print(filtro_salario)
```

### Paso 26. Agrupar empleados por departamento
```python
print("\n--- ANÁLISIS DE SALARIO POR DEPARTAMENTO ---")
resumen_depto = df.groupby('departamento').agg(
    salario_promedio=('salario', 'mean'),
    total_empleados=('salario', 'count')
)
print(resumen_depto)
```

---

## 📈 10. Visualización de datos con Matplotlib

Representaremos gráficamente los hallazgos para hacer el análisis más comprensible e intuitivo.

### Paso 27. Importar Matplotlib
*(Inscrito previamente al inicio del script)*:
```python
import matplotlib.pyplot as plt
```

### Paso 28. Gráfica de barras: empleados por departamento
```python
conteo_depto = df['departamento'].value_counts()

plt.figure(figsize=(6, 4))
plt.bar(conteo_depto.index, conteo_depto.values, color='skyblue')
plt.title("Empleados por Departamento")
plt.xlabel("Departamento")
plt.ylabel("Cantidad de Empleados")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
```
* **Interpretación:** Permite evaluar visualmente cómo se distribuyen la plantilla y la carga operativa entre las distintas áreas.

### Paso 29. Gráfica de barras: salarios por empleado
```python
plt.figure(figsize=(8, 4))
plt.bar(df['nombre'], df['salario'], color='teal')
plt.title("Salario por Empleado")
plt.xlabel("Empleado")
plt.ylabel("Salario (MXN)")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
```
* **Interpretación:** Facilita la comparación de la estructura salarial individual de cada trabajador.

### Paso 30. Histograma: distribución de edades
```python
plt.figure(figsize=(6, 4))
plt.hist(df['edad'], bins=5, color='orange', edgecolor='black')
plt.title("Distribución de Edades")
plt.xlabel("Edad")
plt.ylabel("Frecuencia")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
```
* **Interpretación:** Muestra el rango y sesgo generacional dentro del grupo evaluado.

### Paso 31. Gráfica de dispersión: edad vs. salario
```python
plt.figure(figsize=(6, 4))
plt.scatter(df['edad'], df['salario'], color='purple', s=100)
plt.title("Relación entre Edad y Salario")
plt.xlabel("Edad (Años)")
plt.ylabel("Salario (MXN)")
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
```
* **Interpretación:** Permite observar patrones visually entre edad y retribución. *(Nota: Correlación visual no implica causalidad).*

### Paso 32. Diagrama de caja: distribución de salarios
```python
plt.figure(figsize=(4, 5))
plt.boxplot(df['salario'])
plt.title("Diagrama de Caja de Salarios")
plt.ylabel("Salario (MXN)")
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
```
* **Interpretación:** Revela la mediana, los cuartiles y la dispersión general, ayudando a identificar valores atípicos (*outliers*).

### Paso 33. Matriz de correlación
```python
# Calcular matriz de correlación en variables numéricas
corr = df.corr(numeric_only=True)

plt.figure(figsize=(7, 5))
plt.imshow(corr, cmap='coolwarm', vmin=-1, vmax=1)
plt.colorbar()
plt.xticks(range(len(corr.columns)), corr.columns, rotation=45, ha='right')
plt.yticks(range(len(corr.columns)), corr.columns)
plt.title("Matriz de Correlación Numérica")
plt.tight_layout()
plt.show()
```

**Interpretación del coeficiente de correlación:**
| Valor de correlación | Interpretación |
| :--- | :--- |
| Cercano a **1** | Asociación lineal positiva fuerte. |
| Cercano a **-1** | Asociación lineal negativa fuerte. |
| Cercano a **0** | Ausencia de asociación lineal. |

> ⚠️ **Importante:** Seis empleados son un tamaño de muestra insuficiente para extraer inferencias estadísticas sólidas o entrenar un modelo definitivo de Machine Learning. El objetivo central de este dataset es puramente didáctico para dominar la sintaxis y el flujo del EDA.

---

## 🐍 11. Código completo del archivo `explorar_datos_empleados.py`

Copia este bloque de código completo en tu archivo `explorar_datos_empleados.py` para ejecutar todo el proceso de forma integrada:

```python
import pandas as pd
import matplotlib.pyplot as plt

# ==========================================
# 1. CREACIÓN DEL DICCIONARIO DE DATOS
# ==========================================
empleados = {
    "id_empleado": [101, 102, 103, 104, 105, 106],
    "nombre": ["Carlos", "Maria", "Jose", "Ana", "Luis", "Sofia"],
    "edad": [25, 32, 28, 40, 35, 29],
    "departamento": ["Produccion", "Calidad", "Mantenimiento", "Produccion", "Calidad", "Mantenimiento"],
    "puesto": ["Operador", "Inspector", "Tecnico", "Supervisor", "Auditor", "Tecnico"],
    "salario": [12000, 15000, 13500, 22000, 16000, 14500],
    "antiguedad": [2, 6, 4, 12, 8, 3],
    "horas_trabajadas": [40, 42, 45, 48, 40, 44],
    "capacitaciones": [3, 5, 2, 8, 6, 4],
    "desempeno": [85, 90, 78, 95, 88, 82]
}

# ==========================================
# 2. CONVERTIR DICCIONARIO A DATAFRAME Y GUARDAR CSV
# ==========================================
df_inicial = pd.DataFrame(empleados)
df_inicial.to_csv("empleados_industria.csv", index=False, encoding="utf-8-sig")
print("✅ Archivo 'empleados_industria.csv' generado con éxito.")

# ==========================================
# 3. LECTURA Y EXPLORACIÓN (EDA)
# ==========================================
df = pd.read_csv("empleados_industria.csv")

print("\n--- VISTA PREVIA (HEAD) ---")
print(df.head())

print("\n--- ESTRUCTURA (SHAPE) ---")
print(f"Filas: {df.shape[0]}, Columnas: {df.shape[1]}")

print("\n--- INFORMACIÓN GENERAL ---")
df.info()

print("\n--- ESTADÍSTICAS DESCRIPTIVAS ---")
print(df.describe())

print("\n--- SALARIO PROMEDIO ---")
print(f"${df['salario'].mean():.2f}")

print("\n--- SALARIOS MAYORES A $15,000 ---")
print(df[df['salario'] > 15000][['nombre', 'departamento', 'salario']])

# ==========================================
# 4. VISUALIZACIÓN DE DATOS CON MATPLOTLIB
# ==========================================
# Gráfica 1: Empleados por departamento
conteo_depto = df['departamento'].value_counts()
plt.figure(figsize=(6, 4))
plt.bar(conteo_depto.index, conteo_depto.values, color='skyblue')
plt.title("Empleados por Departamento")
plt.xlabel("Departamento")
plt.ylabel("Cantidad de Empleados")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# Gráfica 2: Relación Edad vs Salario
plt.figure(figsize=(6, 4))
plt.scatter(df['edad'], df['salario'], color='purple', s=80)
plt.title("Relación Edad vs Salario")
plt.xlabel("Edad")
plt.ylabel("Salario")
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
```

---

## 🖥️ 12. Ejecutar el programa desde la terminal de VS Code

### Paso 34. Verificar la activación del entorno virtual
Comprueba que en tu consola de comandos aparezca el prefijo `(venv)` al inicio de la línea de comandos.

### Paso 35. Ejecutar el script principal
```powershell
python explorar_datos_empleados.py
```

### Paso 36. Verificar los archivos generados
Confirma en el explorador de VS Code que los archivos estén estructurados así:
```text
analisis-empleados-industria/
├── venv/
├── empleados_industria.csv
├── explorar_datos_empleados.py
└── requirements.txt
```
*El programa mostrará las salidas tabulares en la terminal y abrirá secuencialmente las gráficas.*

---

## 🤖 13. Interpretación de resultados para Machine Learning

Una vez completado el EDA, la función del científico/analista de datos es interpretar los resultados antes de construir modelos inteligentes.

### ❓ Matriz de Preguntas de Análisis:

| Pregunta de análisis | Variable utilizada | Comando utilizado |
| :--- | :---: | :---: |
| ¿Cuál es la edad promedio? | `edad` | `df['edad'].mean()` |
| ¿Qué departamento tiene más empleados? | `departamento` | `df['departamento'].value_counts()` |
| ¿Quién tiene el salario más alto? | `salario` | `df['salario'].max()` / `sort_values()` |
| ¿Cuál es la antigüedad promedio? | `antiguedad` | `df['antiguedad'].mean()` |
| ¿Qué empleado tiene mejor desempeño? | `desempeno` | `df['desempeno'].max()` |
| ¿Existe relación entre edad y salario? | `edad`, `salario` | `df[['edad', 'salario']].corr()` |

### 🔄 Conexión con Machine Learning:

Los datos explorados servirán como cimiento para diseñar un modelo de **Aprendizaje Supervisado**.

```text
[ VARIABLES ENTRADA (X) ]                        [ MODELO ML ]                     [ VARIABLE OBJETIVO (Y) ]
  • Edad                                ┌─────────────────────────────┐
  • Salario                             │                             │
  • Antigüedad          ───────────────>│  Algoritmo de Regresión     │───────────────>   Desempeño Laboral
  • Horas trabajadas                    │      o Clasificación        │
  • Capacitaciones                      └─────────────────────────────┘
```

> 🛡️ **Consideración Ética e Importante:** La variable objetivo *(desempeño laboral)* debe evaluarse rigurosamente bajo criterios éticos, objetivos y libres de sesgos o discriminación. Además, recuerda que este conjunto reducido de 6 registros es únicamente pedagógico; para entrenar modelos reales de IA requerirás miles de datos.

---

## 📝 14. Actividad de aprendizaje para los estudiantes

**Instrucciones:** Modifica o extiende el código de `explorar_datos_empleados.py` para resolver de forma independiente las siguientes tareas:

1. ➕ **Agregar 4 empleados nuevos** al diccionario original (manteniendo las 10 variables).
2. 🎂 **Calcular la edad promedio** de todos los empleados.
3. 🏢 **Identificar el departamento** con mayor número de trabajadores.
4. ⏳ **Ordenar la tabla** por `antiguedad` de mayor a menor.
5. 🔍 **Filtrar y mostrar** a los empleados que tengan más de **5 años** trabajando.
6. 💰 **Calcular el salario promedio** agrupado por departamento.
7. 📊 **Generar una gráfica de barras** visualizando los salarios.
8. 📈 **Generar un histograma** con la distribución de las edades.
9. 🔗 **Calcular el coeficiente de correlación** específico entre `antiguedad` y `salario`.
10. ✍️ **Escribir 5 conclusiones** redactadas con tus propias palabras según los resultados obtenidos.

---

## 📑 15. Evidencias de aprendizaje y evaluación

| Evidencia | Características | Instrumento de Evaluación |
| :--- | :--- | :--- |
| **Archivo CSV** | Contiene adecuadamente estructurados los registros de los empleados. | Lista de cotejo |
| **Programa Python** | Utiliza Pandas y Matplotlib para explorar y visualizar información. | Lista de cotejo / Rúbrica |
| **Gráficas** | Presenta 5 visualizaciones bien etiquetadas y formateadas. | Rúbrica |
| **Análisis y Conclusiones** | Interpreta estadísticas y responde a las interrogantes planteadas. | Cuestionario / Rúbrica |

### ⏰ Distribución de tiempo sugerida (Total: 5 Horas):
* **1 hora:** Creación del diccionario de datos y exportación a CSV.
* **2 horas:** Exploración analítica de datos (EDA) con Pandas.
* **1 hora:** Visualización gráfica de patrones mediante Matplotlib.
* **1 hora:** Interpretación final, respuesta a preguntas y conclusiones.

> **👨‍🏫 Recomendación Docente:** Es primordial transmitir que el Análisis Exploratorio de Datos (EDA) constituye la fase previa e indispensable del ciclo de vida del Machine Learning. Conocer qué información poseemos, su grado de calidad y sus anomalías es prerrequisito absoluto antes de compilar cualquier algoritmo.