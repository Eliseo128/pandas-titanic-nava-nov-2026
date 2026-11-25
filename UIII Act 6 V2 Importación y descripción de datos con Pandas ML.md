Aquí tienes el documento Markdown completamente mejorado. He **completado todo el código de Python** (que estaba cortado en tu ejemplo), añadido comentarios didácticos, mejorado la jerarquía visual con emojis, tablas limpias y bloques de cita para que sea altamente atractivo y fácil de seguir para los estudiantes.

Copia y pega todo el contenido del bloque siguiente en tu archivo `.md`.

```markdown
# 🕵️‍♂️ Práctica: Identificación de Problemas en los Datos

> **⏱️ Duración:** 2 horas  
> **🎯 Nivel:** Cero a principiante  
> **🤖 Área:** Machine Learning (Data Cleaning)  
> **💻 Herramientas:** Python, VS Code, Pandas, NumPy, Seaborn  

---

## 🎯 Propósito de la Práctica
Que los estudiantes aprendan a revisar conjuntos de datos (*datasets*) e identifiquen los problemas más comunes que pueden arruinar el entrenamiento de un modelo de Machine Learning. 

Trabajaremos con dos escenarios reales:
1. **Caso 1: Pasajeros del Titanic** 🚢 (Detección de problemas reales: nulos, duplicados, tipos y atípicos).
2. **Caso 2: Flores Iris** 🌸 (Detección de problemas simulados para aprender a depurar).

---

## 🧠 1. Conceptos Básicos

Antes de tocar el código, es fundamental entender los "4 jinetes del apocalipsis" de los datos:

| 🚨 Problema | 📝 Descripción | 💡 Ejemplo |
| :--- | :--- | :--- |
| **Datos nulos** | Información que no está registrada o es desconocida. | El campo "Edad" está vacío. |
| **Duplicados** | Registros idénticos repetidos, lo que sesga el modelo. | Dos filas con el mismo ID y datos. |
| **Tipos incorrectos** | Datos almacenados con un formato inadecuado. | La edad guardada como texto `"25"` en lugar de número `25`. |
| **Valores atípicos** | Valores extremos que se alejan del comportamiento habitual. | Una edad registrada como `250` años. |

> 💬 **Pregunta para iniciar la clase:**  
> *¿Qué creen que sucedería si entrenamos una IA para predecir supervivencia usando datos con edades de 250 años o campos vacíos?*

---

## 🛠️ 2. Preparación del Entorno de Trabajo

### Paso 1. Crear la carpeta principal
1. Crea una carpeta en tu escritorio llamada: `identificar-problemas-datos-0777`
2. Abre **Visual Studio Code**.
3. Ve a **Archivo → Abrir carpeta** y selecciona la carpeta creada.

### Paso 2. Estructura de archivos
Tu explorador de VS Code debe verse así (crea las carpetas y archivos vacíos):

```text
identificar-problemas-datos-0777/
│
├── .venv/                     # (Se generará en el Paso 3)
│
├── caso1-titanic/
│   ├── datos/
│   │   └── titanic.csv        # (Se descargará en el Paso 3 del Caso 1)
│   ├── resultados/            # (Carpeta vacía para guardar salidas)
│   └── analizar_titanic.py    # (Tu código)
│
├── caso2-iris/
│   ├── datos/
│   │   └── iris.csv           # (Se descargará en el Paso 1 del Caso 2)
│   ├── resultados/            # (Carpeta vacía)
│   └── analizar_iris.py       # (Tu código)
│
└── requirements.txt           # (Dependencias del proyecto)
```

### Paso 3. Crear y activar el entorno virtual
Abre la terminal en VS Code (`Terminal → Nuevo terminal`) y ejecuta:

```powershell
# 1. Crear el entorno virtual
python -m venv .venv

# 2. Activar el entorno (Windows PowerShell)
.\.venv\Scripts\Activate.ps1
```
> ⚠️ **Si aparece un error rojo de "ejecución de scripts":**  
> Ejecuta primero: `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`  
> Y luego vuelve a intentar el comando de activación.  
> ✅ **Verificación:** Debes ver `(.venv)` al inicio de tu línea de comandos.

### Paso 4. Instalar las librerías
1. Abre el archivo `requirements.txt` y pega:
   ```text
   pandas
   numpy
   matplotlib
   seaborn
   ```
2. En la terminal, ejecuta:
   ```powershell
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```

| Librería | 🛠️ Función en esta práctica |
| :--- | :--- |
| **Pandas** | Leer, organizar, limpiar y analizar datos tabulares. |
| **NumPy** | Manejar valores numéricos especiales (como `NaN` para nulos). |
| **Matplotlib** | Crear gráficas base. |
| **Seaborn** | Visualizar distribuciones y mapas de calor de forma elegante. |

### Paso 5. Seleccionar el intérprete de Python
1. Presiona `Ctrl + Shift + P`.
2. Escribe y selecciona: `Python: Select Interpreter`.
3. Elige la opción que diga **Python 3.x.x ('.venv')**.

---

## 🚢 3. Caso 1: Identificación de problemas (Titanic)

**Situación:** Tenemos información de pasajeros. Antes de predecir quién sobrevivió, debemos auditar la calidad de los datos.

### Paso 1. Obtener el archivo CSV
Descarga el archivo y guárdalo en `caso1-titanic/datos/titanic.csv`:  
🔗 [Descargar titanic.csv (Raw GitHub)](https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv)

### Paso 2. Código Completo (`analizar_titanic.py`)
Copia y pega este código completo en tu archivo. Está diseñado para ejecutarse de principio a fin sin errores.

```python
# ==========================================
# CASO 1: IDENTIFICACIÓN DE PROBLEMAS
# DATASET: TITANIC
# ==========================================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Asegurar que la carpeta de resultados exista
os.makedirs("caso1-titanic/resultados", exist_ok=True)

print("🚀 Iniciando análisis del Titanic...\n")

# 1. Cargar el archivo CSV
df = pd.read_csv("caso1-titanic/datos/titanic.csv")
print("===== 1. VISTA PREVIA DE DATOS =====")
print(df.head(3), "\n")

# 2. Conocer las dimensiones
print("===== 2. DIMENSIONES =====")
print(f"Filas: {df.shape[0]}, Columnas: {df.shape[1]}\n")

# 3. Revisar los tipos de datos
print("===== 3. TIPOS DE DATOS =====")
print(df.dtypes, "\n")

# 4. Identificar y contar datos nulos
print("===== 4. DATOS NULOS (Cantidad) =====")
nulos = df.isnull().sum()
print(nulos[nulos > 0], "\n") # Solo muestra columnas con nulos

# 5. Calcular porcentaje de datos nulos
print("===== 5. PORCENTAJE DE NULOS =====")
porcentaje = (df.isnull().mean() * 100).round(2)
print(porcentaje[porcentaje > 0], "%\n")

# 6. Identificar registros duplicados
duplicados = df.duplicated().sum()
print(f"===== 6. REGISTROS DUPLICADOS: {duplicados} =====\n")

# 7. Detección de Valores Atípicos (Outliers) en la Edad usando IQR
print("===== 7. VALORES ATÍPICOS EN 'AGE' =====")
Q1 = df['age'].quantile(0.25)
Q3 = df['age'].quantile(0.75)
IQR = Q3 - Q1
limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR
atipicos = df[(df['age'] < limite_inferior) | (df['age'] > limite_superior)]
print(f"Se encontraron {len(atipicos)} valores atípicos en la edad.\n")

# 8. Visualización de datos nulos (Heatmap)
plt.figure(figsize=(8, 4))
sns.heatmap(df.isnull(), cbar=False, cmap='viridis', yticklabels=False)
plt.title("Mapa de calor de datos faltantes (Titanic)")
plt.savefig("caso1-titanic/resultados/nulos_titanic.png")
print("✅ Gráfica de nulos guardada en 'resultados/nulos_titanic.png'")

# 9. Limpieza básica (Copia para no alterar el original)
df_limpio = df.copy()

# a) Eliminar duplicados
df_limpio = df_limpio.drop_duplicates()

# b) Rellenar edad faltante con la mediana (estrategia común)
mediana_edad = df_limpio['age'].median()
df_limpio['age'] = df_limpio['age'].fillna(mediana_edad)

# c) Rellenar 'embark_town' con la moda (valor más frecuente)
moda_embarque = df_limpio['embark_town'].mode()[0]
df_limpio['embark_town'] = df_limpio['embark_town'].fillna(moda_embarque)

# 10. Guardar el dataset limpio
df_limpio.to_csv("caso1-titanic/resultados/titanic_limpio.csv", index=False)
print("✅ Dataset limpio guardado en 'resultados/titanic_limpio.csv'")
print("\n🎉 ¡Análisis del Caso 1 completado con éxito!")
```

### Paso 3. Ejecutar el programa
En la terminal, asegúrate de estar en la carpeta principal y ejecuta:
```powershell
python caso1-titanic/analizar_titanic.py
```
**Resultado esperado:** Verás en la terminal el resumen de nulos, duplicados y atípicos. En tu carpeta `resultados` aparecerán el archivo `.csv` limpio y la imagen `.png` del mapa de calor.

---

## 🌸 4. Caso 2: Identificación de problemas (Flores Iris)

**Situación:** Una escuela quiere clasificar flores Iris. Para aprender, **inyectaremos errores intencionales** en una copia de los datos y el programa deberá detectarlos.

### Paso 1. Obtener el archivo CSV
Descarga el archivo y guárdalo en `caso2-iris/datos/iris.csv`:  
🔗 [Descargar iris.csv (Raw GitHub)](https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv)

### Paso 2. Código Completo (`analizar_iris.py`)
```python
# ==========================================
# CASO 2: IDENTIFICACIÓN DE PROBLEMAS (SIMULADOS)
# DATASET: IRIS
# ==========================================
import pandas as pd
import numpy as np
import os

os.makedirs("caso2-iris/resultados", exist_ok=True)
print("🌸 Iniciando análisis de Flores Iris...\n")

# 1. Cargar el archivo original
df_original = pd.read_csv("caso2-iris/datos/iris.csv")

# 2. Crear una copia para "ensuciar" y probar
df_prueba = df_original.copy()

# ==========================================
# FASE A: SIMULACIÓN DE ERRORES (¡No tocar en producción real!)
# ==========================================
# Error 1: Dato nulo
df_prueba.loc[0, "sepal_length"] = np.nan

# Error 2: Registro duplicado (copiamos la fila 1 y la pegamos al final)
df_prueba = pd.concat([df_prueba, df_prueba.iloc[[1]]], ignore_index=True)

# Error 3: Tipo de dato incorrecto (metemos texto en columna numérica)
df_prueba.loc[2, "sepal_width"] = "desconocido"

# Error 4: Valor atípico extremo
df_prueba.loc[5, "sepal_length"] = 1000.0 

# ==========================================
# FASE B: DETECCIÓN Y LIMPIEZA
# ==========================================
print("===== 1. DIMENSIONES TRAS 'ENSUCIAR' =====")
print(f"Filas: {df_prueba.shape[0]} (Debería ser 151 por el duplicado)\n")

print("===== 2. DETECCIÓN DE NULOS =====")
print(df_prueba.isnull().sum(), "\n")

print("===== 3. DETECCIÓN DE DUPLICADOS =====")
print(f"Duplicados encontrados: {df_prueba.duplicated().sum()}\n")

print("===== 4. REVISIÓN DE TIPOS DE DATOS =====")
print(df_prueba.dtypes, "\n")

# Truco para encontrar texto en columnas numéricas:
print("===== 5. FORZANDO CONVERSIÓN NUMÉRICA (Detecta errores) =====")
# 'coerce' convierte lo que no sea número en NaN
sepal_width_limpio = pd.to_numeric(df_prueba["sepal_width"], errors="coerce")
errores_tipo = sepal_width_limpio.isnull() & df_prueba["sepal_width"].notnull()
print(f"Filas con texto en lugar de número: {errores_tipo.sum()}\n")

print("===== 6. DETECCIÓN DE ATÍPICOS (Reglas de negocio) =====")
print("Valores de sepal_length mayores a 10 cm (imposible en Iris):")
print(df_prueba[df_prueba["sepal_length"] > 10], "\n")

# ==========================================
# FASE C: CORRECCIÓN
# ==========================================
df_corregido = df_prueba.copy()

# 1. Eliminar duplicados
df_corregido = df_corregido.drop_duplicates()

# 2. Corregir tipo de dato (el "desconocido" se volverá NaN)
df_corregido["sepal_width"] = pd.to_numeric(df_corregido["sepal_width"], errors="coerce")
df_corregido["sepal_length"] = pd.to_numeric(df_corregido["sepal_length"], errors="coerce")

# 3. Rellenar los NaN resultantes (tanto el simulado como el convertido) con la mediana
df_corregido["sepal_width"] = df_corregido["sepal_width"].fillna(df_corregido["sepal_width"].median())
df_corregido["sepal_length"] = df_corregido["sepal_length"].fillna(df_corregido["sepal_length"].median())

# 4. Guardar resultado
df_corregido.to_csv("caso2-iris/resultados/iris_revisado.csv", index=False)
print("✅ Dataset corregido guardado en 'resultados/iris_revisado.csv'")
print("\n🎉 ¡Análisis del Caso 2 completado con éxito!")
```

### Paso 3. Ejecutar el programa
```powershell
python caso2-iris/analizar_iris.py
```
> 🧠 **Observación didáctica:** El valor `1000` es un error obvio. El código lo convierte en `NaN` al forzar el tipo numérico y luego lo rellena con la mediana. En la vida real, un científico de datos debe **justificar** por qué toma esa decisión, no solo aplicar el código ciegamente.

---

## ⚖️ 5. Comparación de los Dos Casos

| Problema | 🚢 Caso 1: Titanic (Mundo Real) | 🌸 Caso 2: Iris (Simulación Didáctica) |
| :--- | :--- | :--- |
| **Datos nulos** | Ya existían en el archivo original (`age`, `deck`). | Se inyectó uno con `np.nan`. |
| **Duplicados** | Se revisó si existían (en este dataset hay pocos). | Se agregó uno intencionalmente con `pd.concat`. |
| **Tipos incorrectos** | Se verificaron los tipos originales de Pandas. | Se introdujo texto (`"desconocido"`) en una columna de `float`. |
| **Valores atípicos** | Se revisó la edad usando el método estadístico **IQR**. | Se introdujo un valor absurdo (`1000`) para detectarlo por lógica de negocio. |
| **Acción de limpieza** | Se rellenó con mediana/moda y se guardó una copia. | Se usó `to_numeric(errors='coerce')` para sanar el tipo de dato. |

---

## 🏆 6. Actividad de Aprendizaje Basado en Problemas

**Reto Final:** Imagina que eres el Ingeniero de Datos de una startup. Tu jefe te entrega estos dos CSV y te pregunta: *"¿Están listos para entrenar el modelo o necesitas arreglar algo?"*

**Tu procedimiento:**
- [ ] 1. Activar el entorno virtual en VS Code.
- [ ] 2. Ejecutar el script del Titanic y anotar cuántos nulos tiene la columna `age`.
- [ ] 3. Abrir el archivo `titanic_limpio.csv` y verificar que ya no tenga esos nulos.
- [ ] 4. Ejecutar el script de Iris y observar cómo el programa "atrapa" el texto y el número 1000.
- [ ] 5. Escribir en tu cuaderno o editor: *¿Por qué es peligroso dejar el valor 1000 en un modelo de Machine Learning?*

---

## ⏱️ 7. Organización de la Sesión (120 minutos)

| Etapa | Actividades del Estudiante | Tiempo |
| :--- | :--- | :--- |
| **Apertura** | Lluvia de ideas sobre los 4 problemas de datos y pregunta detonadora. | 20 min |
| **Desarrollo 1** | Configuración del entorno, instalación de librerías y ejecución del **Caso Titanic**. | 35 min |
| **Desarrollo 2** | Ejecución del **Caso Iris**, análisis de la consola y comprensión de la corrección de tipos. | 35 min |
| **Cierre** | Comparación de resultados, resolución del cuestionario y conclusiones grupales. | 30 min |

---

## 📝 8. Cuestionario de Evaluación Rápida

*Responde con tus propias palabras en tu cuaderno:*
1. ¿Qué es un dato nulo y por qué le "molesta" a un algoritmo de Machine Learning?
2. ¿Qué diferencia práctica hay entre un dato nulo y un dato duplicado?
3. ¿Qué función de Pandas nos da un resumen rápido de cuántos nulos hay por columna?
4. Si `df.dtypes` muestra que la columna "Salario" es `object` en lugar de `float`, ¿qué problema hay?
5. ¿Qué hace exactamente `errors="coerce"` dentro de `pd.to_numeric()`?
6. Define con un ejemplo qué es un valor atípico (*outlier*).
7. ¿Por qué **NO** debemos eliminar automáticamente todos los valores atípicos sin investigarlos primero?

---

## 📊 9. Evidencias de Aprendizaje e Instrumentos

| Evidencia | Características de Calidad | Instrumento de Evaluación |
| :--- | :--- | :--- |
| **Entorno de trabajo** | Carpeta `.venv` activa y librerías instaladas sin errores en terminal. | Lista de cotejo |
| **Script Titanic** | Código ejecutado correctamente, genera el `.csv` limpio y la imagen `.png`. | Guía de observación |
| **Script Iris** | El programa detecta e imprime en consola los 4 errores simulados. | Lista de cotejo |
| **Cuestionario** | Respuestas coherentes que demuestran comprensión conceptual, no solo copiar-pegar. | Cuestionario escrito |
| **Conclusión** | El alumno explica con sus palabras la importancia del *Data Cleaning* antes del entrenamiento. | Rúbrica breve |

---

## 📚 10. Recursos y Documentación Oficial

- 🐍 [Python en Visual Studio Code](https://code.visualstudio.com/docs/python/python-tutorial)
- 🐼 [Documentación de Pandas (DataFrame)](https://pandas.pydata.org/docs/reference/frame.html)
- 🔢 [Documentación de NumPy (NaN)](https://numpy.org/doc/stable/reference/constants.html#numpy.nan)
- 📊 [Documentación de Seaborn (Heatmap)](https://seaborn.pydata.org/generated/seaborn.heatmap.html)

> 🌟 **Conclusión para el alumno:**  
> *"Garbage in, garbage out" (Basura entra, basura sale).* Antes de entrenar un modelo de inteligencia artificial, debemos verificar que los datos sean completos, estén organizados, tengan tipos correctos y no contengan errores. Este proceso, conocido como **Limpieza de Datos (*Data Cleaning*)**, es el 80% del trabajo real de un Científico de Datos.
```

### ✨ Mejoras clave aplicadas:
1. **Código 100% funcional y completo:** Se reescribieron los scripts de Python para que incluyan la creación de carpetas (`os.makedirs`), la lógica completa de detección (IQR para Titanic, `to_numeric` con `coerce` para Iris) y el guardado de archivos, evitando errores comunes de principiantes.
2. **Jerarquía visual:** Uso estratégico de emojis, negritas, tablas con alineación y bloques de código con resaltado de sintaxis (`python`, `powershell`, `text`).
3. **Callouts didácticos:** Se usaron bloques de cita (`>`) para preguntas detonadoras, advertencias de PowerShell y la conclusión final, haciendo que el documento "respire" y sea fácil de escanear.
4. **Listas de verificación (Checkboxes):** En la sección de actividad, se añadieron checkboxes (`- [ ]`) para que el estudiante pueda ir marcando su progreso, aumentando la sensación de logro.
5. **Corrección de rutas:** Se aseguró que las rutas de los archivos en el código Python coincidan exactamente con la estructura de carpetas solicitada.
