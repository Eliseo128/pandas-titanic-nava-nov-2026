¡Excelente pregunta, futuros ingenieros! 👨‍💻 En la clase anterior descargamos los datos "al vuelo" directamente desde la URL, pero en un proyecto real de Machine Learning, **siempre debemos tener una copia local de nuestros datos**. ¿Por qué?

1. **Velocidad:** Leer del disco duro es 100x más rápido que de internet.
2. **Reproducibilidad:** Si la URL cambia o se cae, tu código deja de funcionar.
3. **Versionado:** Puedes anotar qué versión del dataset usaste.
4. **Privacidad:** En empresas, los datos sensibles NUNCA se leen directo de internet.

Hoy les mostraré **3 métodos** para hacer esto, del más sencillo al más profesional.

---

### 📂 Estructura de Carpetas Recomendada

Antes de empezar, organicémonos como verdaderos Data Scientists:

```text
MachineLearning_Prepa/
│
├── data/                    # 📁 Aquí van TODOS los CSVs
│   ├── raw/                 # 📁 Datos originales sin modificar
│   │   ├── penguins.csv
│   │   ├── heart.csv
│   │   ├── housing.csv
│   │   └── titanic.csv
│   └── processed/           # 📁 Datos ya limpios (lo veremos en futuras clases)
│
├── notebooks/               # 📁 Sus notebooks de Jupyter/Colab
└── scripts/                 # 📁 Scripts de Python (.py)
```

---

### 🥇 Método 1: Pandas Puro (El más usado en ML)

Este es el método **estándar de la industria**. Simple, rápido y con una sola línea.

```python
import pandas as pd
import os

# --- PASO 1: Crear la carpeta si no existe ---
os.makedirs("data/raw", exist_ok=True)

# --- PASO 2: URL del dataset ---
url = "https://raw.githubusercontent.com/allisonhorst/palmerpenguins/master/inst/extdata/penguins.csv"

# --- PASO 3: Leer directamente desde la URL ---
print("📥 Descargando dataset de pingüinos...")
df = pd.read_csv(url)
print(f"✅ Dataset cargado: {df.shape[0]} filas, {df.shape[1]} columnas")

# --- PASO 4: Guardarlo localmente como CSV ---
ruta_local = "data/raw/penguins.csv"
df.to_csv(ruta_local, index=False)  # index=False evita guardar los índices de fila
print(f"💾 Guardado exitosamente en: {ruta_local}")

# --- PASO 5: Verificar que podemos leerlo desde el disco ---
df_local = pd.read_csv(ruta_local)
print(f"🔍 Verificación: {df_local.shape[0]} filas leídas desde el disco local")
```

**💡 Tip didáctico:** `index=False` es CRÍTICO. Si no lo pones, Pandas guardará una columna extra con los números de fila, y al volver a leerlo tendrás una columna fantasma.

---

### 🥈 Método 2: `requests` + Pandas (El más robusto)

Este método es **profesional** porque maneja errores de conexión, tiempos de espera y códigos HTTP.

```python
import pandas as pd
import requests
import os

os.makedirs("data/raw", exist_ok=True)

url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/heart.csv"
ruta_local = "data/raw/heart.csv"

print("📥 Descargando dataset cardíaco con manejo de errores...")

try:
    # Hacer la petición HTTP con timeout de 10 segundos
    respuesta = requests.get(url, timeout=10)
    
    # Verificar que la petición fue exitosa (código 200)
    respuesta.raise_for_status()
    
    # Guardar el contenido en un archivo local
    with open(ruta_local, 'wb') as archivo:
        archivo.write(respuesta.content)
    
    print(f"✅ Descarga completada. Tamaño: {len(respuesta.content)} bytes")
    
    # Ahora lo leemos con Pandas normalmente
    df = pd.read_csv(ruta_local)
    print(f"📊 Dataset listo: {df.shape}")
    
except requests.exceptions.HTTPError as e:
    print(f"❌ Error HTTP: {e}")
except requests.exceptions.ConnectionError:
    print("❌ Error: No hay conexión a internet")
except requests.exceptions.Timeout:
    print("❌ Error: La descarga tardó demasiado")
except Exception as e:
    print(f"❌ Error inesperado: {e}")
```

**💡 Tip didáctico:** `raise_for_status()` lanza una excepción si la URL devuelve un error 404 (no encontrado) o 500 (servidor caído). ¡Siempre úsenlo!

---

### 🥉 Método 3: `urllib` (Nativo de Python, sin instalaciones)

Si están en una computadora donde **no pueden instalar librerías** (`requests` no viene por defecto), usen `urllib` que ya viene incluido en Python.

```python
import pandas as pd
import urllib.request
import os

os.makedirs("data/raw", exist_ok=True)

url = "https://raw.githubusercontent.com/ageron/handson-ml/master/datasets/housing/housing.csv"
ruta_local = "data/raw/housing.csv"

print("📥 Descargando dataset de viviendas con urllib...")

try:
    # Descargar y guardar directamente
    urllib.request.urlretrieve(url, ruta_local)
    print(f"✅ Archivo guardado en: {ruta_local}")
    
    # Leer con Pandas
    df = pd.read_csv(ruta_local)
    print(f"📊 Dataset listo: {df.shape}")
    
except urllib.error.URLError as e:
    print(f"❌ Error de URL: {e}")
except Exception as e:
    print(f"❌ Error: {e}")
```

---

### 🎯 Ejemplo Integrador: Descargar los 4 Datasets de la Clase Anterior

Aquí les dejo un **script completo** que descarga los 4 datasets que usamos en la clase anterior y los organiza en su carpeta local. ¡Perfecto para copiar y pegar!

```python
import pandas as pd
import os

# --- CONFIGURACIÓN ---
os.makedirs("data/raw", exist_ok=True)

# Diccionario con todas las URLs y nombres de archivo
datasets = {
    "penguins": "https://raw.githubusercontent.com/allisonhorst/palmerpenguins/master/inst/extdata/penguins.csv",
    "heart": "https://raw.githubusercontent.com/jbrownlee/Datasets/master/heart.csv",
    "housing": "https://raw.githubusercontent.com/ageron/handson-ml/master/datasets/housing/housing.csv",
    "titanic": "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
}

# --- DESCARGA MASIVA ---
print("=" * 50)
print("🚀 INICIANDO DESCARGA DE DATASETS")
print("=" * 50)

for nombre, url in datasets.items():
    ruta_local = f"data/raw/{nombre}.csv"
    
    # Si ya existe, no lo descargamos de nuevo (¡ahorra tiempo!)
    if os.path.exists(ruta_local):
        print(f"⏭️  {nombre}.csv ya existe. Saltando descarga.")
        continue
    
    try:
        print(f"\n📥 Descargando {nombre}...")
        df = pd.read_csv(url)
        df.to_csv(ruta_local, index=False)
        print(f"   ✅ {nombre}: {df.shape[0]} filas, {df.shape[1]} columnas")
    except Exception as e:
        print(f"   ❌ Error con {nombre}: {e}")

print("\n" + "=" * 50)
print("🎉 ¡DESCARGA COMPLETADA!")
print("=" * 50)

# --- VERIFICACIÓN FINAL ---
print("\n📂 Archivos en data/raw/:")
for archivo in os.listdir("data/raw"):
    tamaño_kb = os.path.getsize(f"data/raw/{archivo}") / 1024
    print(f"   • {archivo} ({tamaño_kb:.2f} KB)")
```

---

### 🔄 ¿Cómo leer el CSV local en las prácticas siguientes?

Una vez guardados, en las próximas clases **ya no usarán URLs**, sino rutas locales. Así se verá su código:

```python
# ❌ ANTES (clase anterior - lento y frágil)
url = "https://raw.githubusercontent.com/..."
df = pd.read_csv(url)

# ✅ AHORA (profesional - rápido y confiable)
df = pd.read_csv("data/raw/titanic.csv")

# O usando rutas relativas más robustas:
import pathlib
ruta = pathlib.Path("data/raw/titanic.csv")
df = pd.read_csv(ruta)
```

---

### 📝 Tabla Comparativa de Métodos (para su cuaderno)

| Método | ¿Requiere instalación? | Manejo de errores | Velocidad | Recomendado para... |
|--------|------------------------|-------------------|-----------|---------------------|
| **`pd.read_csv(url)`** | No (solo Pandas) | Básico | ⭐⭐⭐ | Prototipos rápidos |
| **`requests` + Pandas** | Sí (`pip install requests`) | Excelente | ⭐⭐⭐ | Proyectos profesionales |
| **`urllib`** | No (viene en Python) | Medio | ⭐⭐⭐ | Entornos restringidos |

---

### 🧩 Reto para la Casa

"Jóvenes, su misión es:
1. Crear la estructura de carpetas `data/raw/` y `data/processed/`.
2. Descargar los 4 datasets usando el **Método 1** (Pandas puro).
3. Verificar que cada archivo tenga el tamaño correcto comparando `df.shape` antes y después de guardar.
4. **Bonus:** Investiguen qué pasa si leen un CSV con `encoding='latin1'` en lugar del default `utf-8`. ¿Cuándo sería necesario? (Pista: datos con acentos en español o caracteres especiales).

¡Nos vemos la próxima clase donde aprenderemos a **limpiar** estos datos! 🧹📊"
