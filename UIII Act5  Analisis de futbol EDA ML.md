Esta guía práctica está diseñada paso a paso para alumnos de tercer semestre de Inteligencia Artificial (nivel cero a principiante). Aprenderás a preparar tu entorno en Visual Studio Code y realizar un **Análisis Exploratorio de Datos (EDA)** sobre eventos reales de un partido de fútbol de **Metrica Sports**, aplicando los comandos exactos de tu tabla de **Pandas** y **Matplotlib** para dejar los datos listos para futuros modelos de Machine Learning.

---

## 🛠️ Fase 1: Preparación del Entorno de Trabajo en VS Code

Antes de escribir código, necesitamos configurar un espacio aislado y ordenado para evitar conflictos entre librerías.

1. **Crear la carpeta del proyecto:**
Abre tu terminal (o el símbolo del sistema) y ejecuta:
```bash
mkdir eda_futbol_ia
cd eda_futbol_ia
code .

```


*(El comando `code .` abrirá directamente esa carpeta en Visual Studio Code).*
2. **Instalar extensiones en VS Code:**
Ve al icono de extensiones (`Ctrl + Shift + X`) e instala:
* **Python** (de Microsoft).
* **Jupyter** (de Microsoft, útil si deseas ejecutar el código por bloques en archivos `.ipynb`).


3. **Crear y activar un entorno virtual (`.venv`):**
Abre la terminal integrada en VS Code (`Ctrl + ñ` o menú *Terminal - Nuevo terminal*) y escribe:
```bash
# Crear entorno virtual
python -m venv .venv

# Activar en Windows:
.venv\Scripts\activate

# Activar en Mac/Linux:
source .venv/bin/activate

```


4. **Instalar las librerías necesarias:**
Con el entorno activado (verás `(.venv)` al inicio de la línea), instala Pandas y Matplotlib:
```bash
pip install pandas matplotlib

```


5. **Crear el archivo de trabajo:**
Crea un archivo nuevo en VS Code llamado `analisis_futbol.py`.

---

## 📥 Fase 2: Carga y Respaldo de los Datos (Comandos 1 al 3)

Un error muy común al usar enlaces de GitHub es copiar la URL de la página web (`[github.com/.../blob/](https://github.com/.../blob/)...`), la cual descarga código HTML en lugar de los datos. Para leerlo con Pandas, debemos usar la ruta **Raw** (`raw.githubusercontent.com`).

Copia y pega este bloque inicial en `analisis_futbol.py`:

```python
import pandas as pd
import matplotlib.pyplot as plt

# URL corregida en formato RAW para lectura directa
url = "https://raw.githubusercontent.com/metrica-sports/sample-data/e706dd506b360d69d9d123d5b8026e7294b13996/data/Sample_Game_2/Sample_Game_2_RawEventsData.csv"

# 1. Leer el archivo CSV desde la web (Comando A.2)
df = pd.read_csv(url)

# 2. Guardar una copia local para trabajar sin internet (Comando A.3)
df.to_csv("eventos_partido_local.csv", index=False)

# Ejemplo extra: Cómo crear un DataFrame manual desde cero (Comando A.1)
resumen_manual = pd.DataFrame({'Equipo': ['Home', 'Away'], 'Estado': ['Local', 'Visitante']})
print("DataFrame de prueba creado:\n", resumen_manual, "\n")

```

---

## 🔍 Fase 3: Inspección Inicial de la Estructura (Comandos 4 al 12)

En Machine Learning, antes de entrenar un modelo, debemos conocer la "anatomía" de nuestro dataset: cuántas filas tenemos, cómo se llaman las columnas y qué tipo de dato contiene cada una.

Agrega este código a tu script:

```python
print("--- 1. PRIMEROS Y ÚLTIMOS REGISTROS ---")
print(df.head(5))      # Mostrar los primeros 5 registros (Comando A.4)
print(df.tail(5))      # Mostrar los últimos 5 registros (Comando A.5)

print("\n--- 2. DIMENSIONES Y ETIQUETAS ---")
print("Filas y columnas:", df.shape)      # Consultar filas y columnas (Comando A.6)
print("Nombres de columnas:", df.columns) # Mostrar nombres de columnas (Comando A.7)
print("Rango de índices:", df.index)      # Consultar índices (Comando A.8)

print("\n--- 3. TIPOS DE DATOS Y ESTRUCTURA ---")
print(df.dtypes)       # Consultar tipos de datos por columna (Comando A.10)
df.info()              # Mostrar estructura general y memoria (Comando A.9)

print("\n--- 4. ESTADÍSTICAS DESCRIPTIVAS ---")
print(df.describe())                # Estadísticas de variables numéricas (Comando A.11)
print(df.describe(include='all'))   # Resumen de numéricas y categóricas (Comando A.12)

```

> **Nota técnica sobre este dataset:** Verás columnas como `Team` (Equipo), `Type` (Tipo de evento: pase, tiro, pérdida), `Subtype` (Subtipo), `Period` (Tiempo 1 o 2), `Start Time [s]`, `End Time [s]`, y las coordenadas espaciales normalizadas (`Start X`, `Start Y`, `End X`, `End Y`) que van de `0` a `1` en el campo de juego.

---

## 🧹 Fase 4: Calidad de Datos y Limpieza Básica (Comandos 13 al 16 y 26)

Los algoritmos de Machine Learning fallan si reciben valores nulos (`NaN`) o registros duplicados que sesgan el aprendizaje. Aquí diagnosticamos la calidad del dataset.

```python
print("\n--- DIAGNÓSTICO DE CALIDAD DE DATOS ---")
# Contar valores faltantes por columna (Comando A.13)
print("Valores nulos por columna:\n", df.isnull().sum())

# Contar valores disponibles/no nulos (Comando A.14)
print("\nValores disponibles por columna:\n", df.notnull().sum())

# Contar cuántos valores únicos existen por columna (Comando A.15)
print("\nCantidad de valores únicos:\n", df.nunique())

# Ver los valores exactos y diferentes de la columna 'Type' (Comando A.16)
print("\nTipos de eventos en el partido:", df['Type'].unique())

# Eliminar registros exactamente duplicados (Comando A.26)
df_limpio = df.drop_duplicates()
print(f"\nRegistros antes: {len(df)} | Registros sin duplicados: {len(df_limpio)}")

```

---

## 📊 Fase 5: Análisis Estadístico, Filtrado y Agrupación (Comandos 17 al 25, 27 y 28)

Aquí respondemos preguntas futbolísticas clave y extraemos características (*Feature Engineering* básico) para entender el comportamiento del juego.

```python
print("\n--- ANÁLISIS DE FRECUENCIAS Y MÉTRICAS ---")
# Contar frecuencias absolutas de cada tipo de evento (Comando A.17)
print("Frecuencia de eventos:\n", df['Type'].value_counts())

# Calcular frecuencias relativas / porcentajes (Comando A.28)
print("\nPorcentaje de eventos:\n", df['Type'].value_counts(normalize=True) * 100)

# Crear una columna calculada: Duración de cada evento en segundos
df['Duracion'] = df['End Time [s]'] - df['Start Time [s]']

# Métricas estadísticas sobre la duración (Comandos A.18, A.19, A.20, A.21)
print("\nDuración promedio (s):", df['Duracion'].mean())
print("Duración máxima (s):", df['Duracion'].max())
print("Duración mínima (s):", df['Duracion'].min())
print("Suma total de tiempo activo (s):", df['Duracion'].sum())

# Ordenar registros por duración de mayor a menor (Comando A.22)
eventos_largos = df.sort_values(by='Duracion', ascending=False)
print("\nTop 3 eventos más largos:\n", eventos_largos[['Team', 'Type', 'Duracion']].head(3))

# Agrupar registros por Equipo y Tipo de evento (Comando A.23)
resumen_equipos = df.groupby(['Team', 'Type']).size()
print("\nEventos agrupados por equipo:\n", resumen_equipos)

# Selección por etiqueta: Filtrar solo los tiros ('SHOT') usando .loc[] (Comando A.24)
tiros = df.loc[df['Type'] == 'SHOT', ['Team', 'Subtype', 'Start X', 'Start Y']]
print("\nTiros registrados en el partido:\n", tiros.head())

# Selección por posición: Obtener las primeras 3 filas y primeras 4 columnas con .iloc[] (Comando A.25)
print("\nSelección por posición (iloc):\n", df.iloc[0:3, 0:4])

# Calcular matriz de correlaciones numéricas (Comando A.27)
print("\nCorrelación entre variables numéricas:\n", df.corr(numeric_only=True))

```

---

## 📈 Fase 6: Visualización de Datos con Matplotlib (Comandos B.1 al B.18)

Un buen científico de datos comunica sus hallazgos visualmente. A continuación, crearemos 4 gráficas distintas integrando todos los comandos de tu tabla de Matplotlib.

### Gráfica 1: Frecuencia de Eventos (Gráfica de Barras y Circular)

```python
conteo_eventos = df['Type'].value_counts()

# Crear figura con 2 subgráficas lado a lado (Comandos B.1 y B.18)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# Subgráfica 1: Gráfica de barras (Comando B.2)
ax1.bar(conteo_eventos.index, conteo_eventos.values, color='steelblue')
ax1.set_title("Cantidad de Eventos por Tipo")     # (Comando B.8)
ax1.set_xlabel("Tipo de Evento")                  # (Comando B.9)
ax1.set_ylabel("Frecuencia")                      # (Comando B.10)
ax1.tick_params(axis='x', rotation=45)            # Equivalente a plt.xticks (Comando B.11)
ax1.grid(axis='y', linestyle='--', alpha=0.7)     # (Comando B.13)

# Subgráfica 2: Gráfica circular (Comando B.7)
top_5 = conteo_eventos.head(5)
ax2.pie(top_5.values, labels=top_5.index, autopct='%1.1f%%', startangle=90)
ax2.set_title("Proporción del Top 5 Eventos")

plt.tight_layout()                                # Ajustar espacios (Comando B.15)
plt.savefig("1_frecuencia_eventos.png", dpi=300)  # Guardar imagen (Comando B.17)
plt.show()                                        # Mostrar gráfica (Comando B.16)

```

### Gráfica 2: Mapa de Calor / Posición de Tiros en la Cancha (Gráfica de Dispersión)

```python
plt.figure(figsize=(10, 6)) # Crear figura independiente (Comando B.1)

# Filtrar tiros por equipo
tiros_home = df[(df['Type'] == 'SHOT') & (df['Team'] == 'Home')]
tiros_away = df[(df['Type'] == 'SHOT') & (df['Team'] == 'Away')]

# Crear gráfica de dispersión (Comando B.4)
plt.scatter(tiros_home['Start X'], tiros_home['Start Y'], color='blue', label='Local (Home)', s=80, alpha=0.8)
plt.scatter(tiros_away['Start X'], tiros_away['Start Y'], color='red', label='Visitante (Away)', s=80, alpha=0.8)

plt.title("Ubicación de los Tiros en el Campo (Coordenadas Normalizadas)") # (B.8)
plt.xlabel("Largo del Campo (Start X: 0 a 1)")                              # (B.9)
plt.ylabel("Ancho del Campo (Start Y: 0 a 1)")                              # (B.10)
plt.xticks([0, 0.25, 0.5, 0.75, 1.0])                                      # (B.11)
plt.yticks([0, 0.25, 0.5, 0.75, 1.0])                                      # (B.12)
plt.grid(True, linestyle=':', alpha=0.6)                                    # (B.13)
plt.legend(loc="upper right")                                               # (B.14)
plt.tight_layout()                                                          # (B.15)
plt.savefig("2_mapa_tiros.png", dpi=300)                                    # (B.17)
plt.show()                                                                  # (B.16)

```

### Gráfica 3: Distribución de Duración de Posesiones y Evolución Temporal (Histograma, Caja y Líneas)

```python
# Filtrar pases válidos con duración menor a 15 segundos para evitar valores extremos
pases = df[(df['Type'] == 'PASS') & (df['Duracion'] > 0) & (df['Duracion'] < 15)]

plt.figure(figsize=(12, 4))

# Histograma de duración de pases (Comando B.5)
plt.subplot(1, 3, 1)
plt.hist(pases['Duracion'], bins=20, color='mediumseagreen', edgecolor='black')
plt.title("Histograma: Duración de Pases")
plt.xlabel("Segundos")
plt.ylabel("Cantidad de Pases")
plt.grid(True, alpha=0.3)

# Diagrama de caja para detectar valores atípicos / outliers (Comando B.6)
plt.subplot(1, 3, 2)
plt.boxplot(pases['Duracion'], vert=True)
plt.title("Boxplot: Detección de Outliers")
plt.ylabel("Segundos")
plt.grid(True, alpha=0.3)

# Gráfica de líneas: Eventos acumulados en los primeros 50 registros (Comando B.3)
plt.subplot(1, 3, 3)
primeros_50 = df.head(50)
plt.plot(primeros_50.index, primeros_50['Start Time [s]'], color='purple', marker='o', markersize=3)
plt.title("Línea de Tiempo (Primeros 50 Eventos)")
plt.xlabel("Índice del Evento")
plt.ylabel("Tiempo de Partido (s)")
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig("3_distribucion_y_tiempo.png", dpi=300)
plt.show()

```

---

## 🧠 Conexión con Machine Learning: ¿Para qué sirve todo esto?

Como estudiantes de Inteligencia Artificial, este Análisis Exploratorio resuelve los problemas previos al entrenamiento de algoritmos:

* **Detección de desbalanceo de clases (`value_counts`):** Si quisieras entrenar un modelo de clasificación para predecir si una jugada termina en gol (`GOAL`) o tiro (`SHOT`), notarás que el 95% de los datos son pases (`PASS`). Sin este análisis, tu modelo aprendería a predecir siempre "pase" y fallaría en detectar goles.
* **Limpieza de valores nulos (`isnull`):** Columnas como `Subtype` o `To` (jugador que recibe el balón) tienen valores vacíos cuando el balón sale del campo. En ML debes imputar esos datos o eliminarlos antes de entrenar.
* **Detección de valores atípicos (`boxplot` y `describe`):** Identificar jugadas con tiempos anómalos evita que algoritmos sensibles a la escala (como Regresión Logística o Redes Neuronales) distorsionen sus pesos.
