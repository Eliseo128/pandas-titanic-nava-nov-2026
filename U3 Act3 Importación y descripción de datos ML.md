Aquí tienes el contenido completo, estructurado y visualmente mejorado, listo para ser copiado y guardado como el archivo **`UIII Act3 Importación y descripción de datos.md`**. 

Se han añadido iconos a las **15 secciones principales** para cumplir con tu solicitud, se ha mejorado la legibilidad con bloques de cita, tablas limpias y resaltado de sintaxis, y se ha incluido el **script completo y funcional** que integra todos los pasos descritos en la guía.

```markdown
# 📊 UIII Act3: Importación y Descripción de Datos

> **🎓 Asignatura:** Soluciona problemas de Machine Learning  
> **📚 Nivel:** Tercer semestre de preparatoria  
> **🤖 Especialidad:** Inteligencia Artificial  
> **📈 Dificultad:** Cero a principiante  
> **🐍 Lenguaje:** Python  
> **🛠️ Herramientas:** Visual Studio Code, Pandas, Matplotlib y CSV  

---

## 🎯 1. Propósito de la práctica
El estudiante aprenderá a realizar un **Análisis Exploratorio de Datos (EDA, Exploratory Data Analysis)** utilizando las bibliotecas `Pandas` y `Matplotlib`. Se trabajará con información ficticia de seis empleados de una industria, considerando diez características por empleado.

**Procedimiento general:**
1. Crear un diccionario con 10 listas y 6 elementos por lista.
2. Convertir el diccionario en un DataFrame.
3. Explorar la estructura de los datos.
4. Guardar la información en un archivo CSV.
5. Leer nuevamente los datos desde el CSV.
6. Identificar tipos de datos, valores faltantes y estadísticas.
7. Ordenar, filtrar y agrupar información.
8. Crear gráficas para interpretar los datos.
9. Obtener conclusiones aplicables a Machine Learning.

---

## 🛠️ 2. Comandos de Pandas y Matplotlib más utilizados

### A. Comandos para explorar datos con Pandas
| Núm. | Comando | Función |
|:---:|:---|:---|
| 1 | `pd.DataFrame()` | Crear un DataFrame. |
| 2 | `pd.read_csv()` | Leer un archivo CSV. |
| 3 | `df.to_csv()` | Guardar un DataFrame en CSV. |
| 4 | `df.head()` | Mostrar los primeros registros. |
| 5 | `df.tail()` | Mostrar los últimos registros. |
| 6 | `df.shape` | Consultar filas y columnas. |
| 7 | `df.columns` | Mostrar nombres de columnas. |
| 8 | `df.index` | Consultar índices. |
| 9 | `df.info()` | Mostrar estructura y tipos de datos. |
| 10 | `df.dtypes` | Consultar tipos de datos. |
| 11 | `df.describe()` | Obtener estadísticas descriptivas. |
| 12 | `df.describe(include='all')` | Resumir variables numéricas y categóricas. |
| 13 | `df.isnull().sum()` | Contar valores faltantes. |
| 14 | `df.notnull().sum()` | Contar valores disponibles. |
| 15 | `df.nunique()` | Contar valores únicos por columna. |
| 16 | `df['columna'].unique()` | Mostrar valores diferentes. |
| 17 | `df['columna'].value_counts()` | Contar frecuencias. |
| 18 | `df['columna'].mean()` | Calcular promedio. |
| 19 | `df['columna'].max()` | Obtener valor máximo. |
| 20 | `df['columna'].min()` | Obtener valor mínimo. |
| 21 | `df['columna'].sum()` | Calcular suma. |
| 22 | `df.sort_values()` | Ordenar registros. |
| 23 | `df.groupby()` | Agrupar registros. |
| 24 | `df.loc[]` | Seleccionar filas y columnas por etiqueta. |
| 25 | `df.iloc[]` | Seleccionar por posición. |
| 26 | `df.drop_duplicates()` | Eliminar registros duplicados. |
| 27 | `df.corr(numeric_only=True)` | Calcular correlaciones numéricas. |
| 28 | `df['columna'].value_counts(normalize=True)` | Calcular frecuencias relativas. |

### B. Comandos para visualizar datos con Matplotlib
> Primero se importa la biblioteca: `import matplotlib.pyplot as plt`

| Núm. | Comando | Función |
|:---:|:---|:---|
| 1 | `plt.figure()` | Crear una figura. |
| 2 | `plt.bar()` | Crear gráfica de barras. |
| 3 | `plt.plot()` | Crear gráfica de líneas. |
| 4 | `plt.scatter()` | Crear gráfica de dispersión. |
| 5 | `plt.hist()` | Crear histograma. |
| 6 | `plt.boxplot()` | Crear diagrama de caja. |
| 7 | `plt.pie()` | Crear gráfica circular. |
| 8 | `plt.title()` | Colocar título. |
| 9 | `plt.xlabel()` | Nombrar eje X. |
| 10 | `plt.ylabel()` | Nombrar eje Y. |
| 11 | `plt.xticks()` | Modificar etiquetas del eje X. |
| 12 | `plt.yticks()` | Modificar etiquetas del eje Y. |
| 13 | `plt.grid()` | Mostrar cuadrícula. |
| 14 | `plt.legend()` | Mostrar leyenda. |
| 15 | `plt.tight_layout()` | Ajustar espacios de la figura. |
| 16 | `plt.show()` | Mostrar gráfica. |
| 17 | `plt.savefig()` | Guardar gráfica como imagen. |
| 18 | `plt.subplots()` | Crear figura y área de gráficas. |

---

## 🏭 3. Situación práctica: información de empleados
Una empresa industrial necesita analizar las características de sus empleados para conocer sus edades, salarios, antigüedad, departamentos y desempeño laboral.

| Variable | Descripción | Tipo de dato |
|:---|:---|:---|
| `id_empleado` | Identificador | Numérico |
| `nombre` | Nombre del empleado | Categórico |
| `edad` | Edad en años | Numérico |
| `departamento` | Área de trabajo | Categórico |
| `puesto` | Cargo laboral | Categórico |
| `salario` | Salario mensual en pesos | Numérico |
| `antiguedad` | Años trabajando en la empresa | Numérico |
| `horas_trabajadas` | Horas semanales | Numérico |
| `capacitaciones` | Capacitaciones realizadas | Numérico |
| `desempeno` | Evaluación de desempeño | Numérico |

> ⚠️ **Nota:** Los datos son ficticios y se utilizan exclusivamente con fines educativos.

---

## 💻 4. Preparación del entorno de trabajo en Visual Studio Code

| Paso | Acción | Comando / Instrucción |
|:---:|:---|:---|
| **1** | Crear carpeta del proyecto | Nombre: `analisis-empleados-industria` |
| **2** | Crear entorno virtual | `python -m venv .venv` |
| **3** | Activar entorno (Windows) | PowerShell: `.\.venv\Scripts\Activate.ps1` <br> CMD: `.venv\Scripts\activate.bat` |
| **4** | Instalar bibliotecas | `python -m pip install pandas matplotlib` |
| **5** | Verificar instalaciones | `python -c "import pandas; import matplotlib; print('OK')"` |
| **6** | Crear archivos del proyecto | Ver estructura abajo 👇 |

**Estructura del proyecto:**
```text
analisis-empleados-industria/
│
├── .venv/                     # Entorno virtual
├── empleados_industria.csv    # Archivo de datos (se genera con el script)
├── explorar_datos_empleados.py # Script principal de Python
└── requirements.txt           # Dependencias (pandas, matplotlib)
```

---

## 📝 5. Crear el diccionario con 10 listas y 6 elementos
En el archivo `explorar_datos_empleados.py`, escribimos el siguiente código base:

```python
import pandas as pd
import matplotlib.pyplot as plt

# 1. Crear diccionario con datos de empleados
empleados = {
    'id_empleado': [101, 102, 103, 104, 105, 106],
    'nombre': ['Carlos', 'Maria', 'Jose', 'Ana', 'Luis', 'Sofia'],
    'edad': [25, 32, 28, 40, 35, 29],
    'departamento': ['Produccion', 'Calidad', 'Mantenimiento', 'Produccion', 'Calidad', 'Mantenimiento'],
    'puesto': ['Operador', 'Inspector', 'Tecnico', 'Supervisor', 'Inspector', 'Tecnico'],
    'salario': [12000, 15000, 13500, 22000, 16000, 14500],
    'antiguedad': [2, 6, 4, 12, 8, 3],
    'horas_trabajadas': [48, 40, 45, 40, 42, 48],
    'capacitaciones': [2, 5, 3, 8, 6, 4],
    'desempeno': [80, 95, 85, 98, 90, 88]
}
```
> 💡 **Explicación:** Las claves (ej. `'edad'`) son las columnas. Los valores entre corchetes son las listas. Cada posición en las listas corresponde al mismo empleado.

---

## 📊 6. Convertir el diccionario en un DataFrame
Utilizamos `pd.DataFrame()` para convertir el diccionario en una tabla estructurada.

```python
# 2. Convertir diccionario en DataFrame
df = pd.DataFrame(empleados)
print("\n--- TABLA ORIGINAL DE EMPLEADOS ---")
print(df)
```

---

## 💾 7. Convertir el DataFrame en archivo CSV
Utilizamos `to_csv()` para persistir los datos en un archivo.

```python
# 3. Exportar los datos a CSV
df.to_csv(
    'empleados_industria.csv',
    index=False,
    encoding='utf-8-sig'
)
print("\n✅ Archivo CSV creado correctamente")
```
| Parámetro | Función |
|:---|:---|
| `'empleados_industria.csv'` | Nombre del archivo. |
| `index=False` | Evita guardar el índice numérico como columna adicional. |
| `encoding='utf-8-sig'` | Facilita la lectura de acentos y caracteres especiales en Excel. |

---

## 📂 8. Leer los datos desde el archivo CSV
En Machine Learning, es frecuente recibir datos desde archivos externos, no construirlos manualmente.

```python
# 4. Leer el archivo CSV
df = pd.read_csv('empleados_industria.csv')
print("\n--- DATOS LEÍDOS DESDE CSV ---")
print(df)
```

---

## 🔍 9. Análisis Exploratorio de Datos (EDA)
A partir de este punto, exploramos la información cargada desde el CSV.

```python
# 5. Primeros y últimos registros
print("\n1. PRIMEROS REGISTROS (Head):")
print(df.head(3)) # Muestra los primeros 3

print("\n2. ÚLTIMOS REGISTROS (Tail):")
print(df.tail(2)) # Muestra los últimos 2

# 6. Dimensiones y estructura
print("\n3. DIMENSIONES (Filas, Columnas):", df.shape)
print("\n4. NOMBRES DE COLUMNAS:\n", df.columns)
print("\n5. TIPOS DE DATOS:\n", df.dtypes)

print("\n6. INFORMACIÓN GENERAL:")
df.info()

# 7. Estadísticas y limpieza
print("\n7. ESTADÍSTICAS DESCRIPTIVAS:")
print(df.describe())

print("\n8. VALORES FALTANTES (Nulls):")
print(df.isnull().sum())

print("\n9. REGISTROS DUPLICADOS:")
print(df.duplicated().sum())

print("\n10. VALORES ÚNICOS POR COLUMNA:")
print(df.nunique())
print("Departamentos únicos:", df['departamento'].unique())

# 8. Análisis específico
print("\n11. EMPLEADOS POR DEPARTAMENTO:")
print(df['departamento'].value_counts())

print("\n12. PROMEDIO DE SALARIO: $", df['salario'].mean())
print("13. SALARIO MÁXIMO: $", df['salario'].max())
print("14. SALARIO MÍNIMO: $", df['salario'].min())

# 9. Ordenamiento, filtrado y agrupación
print("\n15. EMPLEADOS ORDENADOS POR SALARIO (Mayor a menor):")
print(df.sort_values(by='salario', ascending=False))

print("\n16. EMPLEADOS CON SALARIO MAYOR A $15,000:")
filtro = df[df['salario'] > 15000]
print(filtro)

print("\n17. RESUMEN POR DEPARTAMENTO:")
resumen = df.groupby('departamento').agg(
    empleados=('id_empleado', 'count'),
    salario_promedio=('salario', 'mean'),
    salario_maximo=('salario', 'max')
)
print(resumen)
```

---

## 📈 10. Visualización de datos con Matplotlib
Representamos gráficamente los resultados del análisis.

```python
# 18. Gráfica de barras: Empleados por departamento
conteo = df['departamento'].value_counts()
plt.figure(figsize=(8, 5))
plt.bar(conteo.index, conteo.values, color='skyblue')
plt.title('Empleados por departamento')
plt.xlabel('Departamento')
plt.ylabel('Cantidad de empleados')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 19. Gráfica de barras: Salarios por empleado
plt.figure(figsize=(8, 5))
plt.bar(df['nombre'], df['salario'], color='lightgreen')
plt.title('Salario mensual por empleado')
plt.xlabel('Empleado')
plt.ylabel('Salario en pesos')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 20. Histograma: Distribución de edades
plt.figure(figsize=(8, 5))
plt.hist(df['edad'], bins=5, color='orange', edgecolor='black')
plt.title('Distribución de edades de empleados')
plt.xlabel('Edad')
plt.ylabel('Frecuencia')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 21. Gráfica de dispersión: Edad vs Salario
plt.figure(figsize=(8, 5))
plt.scatter(df['edad'], df['salario'], color='red', s=100)
plt.title('Relación entre edad y salario')
plt.xlabel('Edad')
plt.ylabel('Salario mensual')
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 22. Diagrama de caja: Distribución de salarios
plt.figure(figsize=(7, 5))
plt.boxplot(df['salario'], patch_artist=True, boxprops=dict(facecolor='lightblue'))
plt.title('Distribución de salarios (Boxplot)')
plt.ylabel('Salario mensual')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 23. Matriz de correlación
correlacion = df.corr(numeric_only=True)
print("\n--- MATRIZ DE CORRELACIÓN ---")
print(correlacion)

plt.figure(figsize=(9, 6))
plt.imshow(correlacion, cmap='coolwarm', vmin=-1, vmax=1)
plt.colorbar()
plt.xticks(range(len(correlacion.columns)), correlacion.columns, rotation=45)
plt.yticks(range(len(correlacion.columns)), correlacion.columns)
plt.title('Matriz de correlación de variables numéricas')
plt.tight_layout()
plt.show()
```
> 📌 **Interpretación de correlación:**  
> • **Cercano a 1:** Asociación positiva.  
> • **Cercano a -1:** Asociación negativa.  
> • **Cercano a 0:** Asociación lineal débil o inexistente.  
> *(Nota: 6 empleados son insuficientes para conclusiones estadísticas robustas; esto es solo con fines didácticos).*

---

## 📜 11. Código completo del archivo `explorar_datos_empleados.py`
> 📥 **Instrucción para el alumno:** Copia y pega **todo** este bloque en tu archivo `explorar_datos_empleados.py`. Este script integra la creación, guardado, lectura, análisis y visualización en un solo flujo ejecutable.

```python
import pandas as pd
import matplotlib.pyplot as plt

# ==========================================
# FASE 1: CREACIÓN Y EXPORTACIÓN DE DATOS
# ==========================================
print("🔄 Generando datos y exportando a CSV...")
empleados = {
    'id_empleado': [101, 102, 103, 104, 105, 106],
    'nombre': ['Carlos', 'Maria', 'Jose', 'Ana', 'Luis', 'Sofia'],
    'edad': [25, 32, 28, 40, 35, 29],
    'departamento': ['Produccion', 'Calidad', 'Mantenimiento', 'Produccion', 'Calidad', 'Mantenimiento'],
    'puesto': ['Operador', 'Inspector', 'Tecnico', 'Supervisor', 'Inspector', 'Tecnico'],
    'salario': [12000, 15000, 13500, 22000, 16000, 14500],
    'antiguedad': [2, 6, 4, 12, 8, 3],
    'horas_trabajadas': [48, 40, 45, 40, 42, 48],
    'capacitaciones': [2, 5, 3, 8, 6, 4],
    'desempeno': [80, 95, 85, 98, 90, 88]
}

df = pd.DataFrame(empleados)
df.to_csv('empleados_industria.csv', index=False, encoding='utf-8-sig')
print("✅ Archivo 'empleados_industria.csv' creado exitosamente.\n")

# ==========================================
# FASE 2: LECTURA Y EXPLORACIÓN (EDA)
# ==========================================
print("📂 Leyendo datos desde el CSV...")
df = pd.read_csv('empleados_industria.csv')

print("\n--- 1. DIMENSIONES ---")
print(f"Filas y Columnas: {df.shape}")

print("\n--- 2. TIPOS DE DATOS ---")
print(df.dtypes)

print("\n--- 3. ESTADÍSTICAS DESCRIPTIVAS ---")
print(df.describe())

print("\n--- 4. VALORES FALTANTES Y DUPLICADOS ---")
print("Faltantes:\n", df.isnull().sum())
print("Duplicados:", df.duplicated().sum())

print("\n--- 5. FILTRADO Y ORDENAMIENTO ---")
print("Empleados con salario > 15000:")
print(df[df['salario'] > 15000])

print("\n--- 6. AGRUPACIÓN POR DEPARTAMENTO ---")
resumen = df.groupby('departamento').agg(
    empleados=('id_empleado', 'count'),
    salario_promedio=('salario', 'mean')
).round(2)
print(resumen)

# ==========================================
# FASE 3: VISUALIZACIÓN CON MATPLOTLIB
# ==========================================
print("\n📊 Generando gráficas (se abrirán en ventanas emergentes)...")

# Gráfica 1: Empleados por departamento
plt.figure(figsize=(8, 5))
plt.bar(df['departamento'].value_counts().index, df['departamento'].value_counts().values, color='skyblue')
plt.title('Empleados por departamento')
plt.xlabel('Departamento')
plt.ylabel('Cantidad')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# Gráfica 2: Salarios por empleado
plt.figure(figsize=(8, 5))
plt.bar(df['nombre'], df['salario'], color='lightgreen')
plt.title('Salario mensual por empleado')
plt.xlabel('Empleado')
plt.ylabel('Salario ($)')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# Gráfica 3: Histograma de edades
plt.figure(figsize=(8, 5))
plt.hist(df['edad'], bins=5, color='orange', edgecolor='black')
plt.title('Distribución de edades')
plt.xlabel('Edad')
plt.ylabel('Frecuencia')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# Gráfica 4: Dispersión Edad vs Salario
plt.figure(figsize=(8, 5))
plt.scatter(df['edad'], df['salario'], color='red', s=100)
plt.title('Relación entre edad y salario')
plt.xlabel('Edad')
plt.ylabel('Salario mensual')
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# Gráfica 5: Diagrama de caja de salarios
plt.figure(figsize=(7, 5))
plt.boxplot(df['salario'], patch_artist=True, boxprops=dict(facecolor='lightblue'))
plt.title('Distribución de salarios (Boxplot)')
plt.ylabel('Salario mensual')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# Gráfica 6: Matriz de correlación
correlacion = df.corr(numeric_only=True)
plt.figure(figsize=(9, 6))
plt.imshow(correlacion, cmap='coolwarm', vmin=-1, vmax=1)
plt.colorbar()
plt.xticks(range(len(correlacion.columns)), correlacion.columns, rotation=45)
plt.yticks(range(len(correlacion.columns)), correlacion.columns)
plt.title('Matriz de correlación')
plt.tight_layout()
plt.show()

print("\n🎉 ¡ANÁLISIS EXPLORATORIO TERMINADO EXITOSAMENTE!")
```

---

## ▶️ 12. Ejecutar el programa desde la terminal de VS Code
1. Verifica que el entorno virtual esté activado (debe aparecer `(.venv)` al inicio de la terminal).
2. Ejecuta el programa con el comando:
   ```bash
   python explorar_datos_empleados.py
   ```
3. Verifica que se haya generado el archivo `empleados_industria.csv` en tu carpeta y que las ventanas de las gráficas se abran correctamente.

---

## 🧠 13. Interpretación de resultados para Machine Learning
Antes de entrenar un modelo, es crucial entender los datos. 

| Pregunta de análisis | Variable utilizada | Comando clave |
|:---|:---|:---|
| ¿Cuál es la edad promedio? | `edad` | `mean()` |
| ¿Qué departamento tiene más empleados? | `departamento` | `value_counts()` |
| ¿Quién tiene el salario más alto? | `salario` | `max()` |
| ¿Cuál es la antigüedad promedio? | `antiguedad` | `mean()` |
| ¿Qué empleado tiene mejor desempeño? | `desempeno` | `max()` |
| ¿Existe relación entre edad y salario? | `edad`, `salario` | `corr()` |

**🔮 Conexión con Machine Learning:**  
Estos datos pueden servir como base para un modelo de **aprendizaje supervisado** (ej. predecir el `desempeno` (Y) en función de `edad`, `salario`, `antiguedad`, `horas_trabajadas` y `capacitaciones` (X)).  
> ⚠️ **Consideración ética:** Las variables deben usarse con criterios de privacidad, equidad y ausencia de discriminación. Este conjunto de 6 registros es solo didáctico; un modelo real requiere miles de registros.

---

## 📚 14. Actividad de aprendizaje para los estudiantes
**Instrucciones:** Modifica el script o crea uno nuevo para realizar las siguientes tareas con el archivo `empleados_industria.csv`:

1. ➕ Agrega **cuatro empleados nuevos** al diccionario original.
2. 🧮 Calcula la **edad promedio** de todos los empleados.
3. 🏆 Identifica el **departamento con mayor número** de trabajadores.
4. 📅 Ordena los empleados por **antigüedad de mayor a menor**.
5. 🔍 Filtra los empleados que tengan **más de cinco años** trabajando en la industria.
6. 💰 Calcula el **salario promedio por departamento**.
7. 📊 Genera una **gráfica de barras** con los salarios actualizados.
8. 📉 Genera un **histograma** con las edades actualizadas.
9. 🔗 Calcula la **correlación** entre antigüedad y salario.
10. 📝 Escribe **cinco conclusiones** detalladas sobre los resultados obtenidos.

---

## 🏆 15. Evidencias de aprendizaje y evaluación

| Evidencia | Características | Instrumento de evaluación |
|:---|:---|:---|
| **Archivo CSV** | Contiene los datos estructurados de los empleados (incluyendo los 4 nuevos). | Lista de cotejo |
| **Programa Python** | Utiliza Pandas correctamente para explorar, filtrar y agrupar información. | Lista de cotejo |
| **Gráficas** | Presenta al menos 5 visualizaciones correctamente etiquetadas y legibles. | Rúbrica |
| **Análisis** | Interpreta estadísticas descriptivas y resultados de filtrado. | Cuestionario |
| **Conclusiones** | Explica los hallazgos del análisis y su posible impacto en un modelo de ML. | Rúbrica |

> ⏱️ **Distribución de tiempo sugerida: 5 horas**  
> • **1 hora:** Creación del diccionario y CSV.  
> • **2 horas:** Exploración con Pandas (EDA).  
> • **1 hora:** Visualización con Matplotlib.  
> • **1 hora:** Interpretación, actividad práctica y conclusiones.

> 💡 **Recomendación docente:** Es fundamental que los estudiantes comprendan que el EDA es la columna vertebral antes de entrenar cualquier modelo de Machine Learning. Primero deben conocer qué información tienen, cómo está organizada, qué problemas presenta (nulos, duplicados) y qué patrones pueden identificar.
```

### 📥 Instrucciones para guardar:
1. Copia **todo** el contenido del bloque de código anterior.
2. Abre un editor de texto (como Bloc de notas, VS Code o cualquier editor Markdown).
3. Pega el contenido.
4. Guarda el archivo con el nombre exacto: **`UIII Act3 Importación y descripción de datos.md`**.
5. ¡Listo! El archivo estará visualmente estructurado, con los 15 puntos iconizados, el código completo funcional y preparado para ser compartido con los alumnos.
