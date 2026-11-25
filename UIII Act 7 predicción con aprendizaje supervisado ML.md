# 📘 Aprendizaje Supervisado: Dos Ejemplos Prácticos en Python

## 🎯 ¿Qué es el Aprendizaje Supervisado?

El **aprendizaje supervisado** es una técnica de IA donde entrenamos un modelo con datos **etiquetados** (entrada + respuesta correcta) para que aprenda a predecir resultados nuevos. En estos dos ejemplos usaremos **regresión lineal**, que dibuja la "mejor línea recta" que pasa entre los datos.

---

## 🛠️ Configuración del Entorno

### 1. Instala Python y VS Code
- Descarga Python desde [python.org](https://www.python.org)
- Descarga VS Code desde [code.visualstudio.com](https://code.visualstudio.com)
- En VS Code instala la extensión **"Python"** de Microsoft

### 2. Librerías que necesitas instalar

Abre la terminal de VS Code (`Ctrl + ñ` o `Ctrl + `) y ejecuta:

```bash
pip install numpy pandas scikit-learn matplotlib seaborn
```

| Librería | ¿Para qué sirve? |
|----------|------------------|
| `numpy` | Operaciones matemáticas y arreglos |
| `pandas` | Manejo de tablas de datos |
| `scikit-learn` | Algoritmos de Machine Learning |
| `matplotlib` | Crear gráficas |
| `seaborn` | Gráficas más bonitas 🎨 |

---

## 📏 EJEMPLO 1: Predecir el PESO a partir de la ESTATURA

**Idea:** Si conocemos la estatura de varias personas y su peso, el modelo aprenderá la relación para predecir el peso de alguien nuevo.

### 📄 Código completo (`peso_estatura.py`)

```python
# =====================================================
# EJEMPLO 1: Predicción de PESO a partir de ESTATURA
# Aprendizaje Supervisado - Regresión Lineal
# =====================================================

# 1️⃣ IMPORTAR LIBRERÍAS
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# 2️⃣ CREAR LOS DATOS (simulamos 20 personas)
# Estaturas en metros (entre 1.50 y 1.90)
np.random.seed(42)  # Para que los resultados sean siempre iguales
estaturas = np.random.uniform(1.50, 1.90, 20)

# Pesos generados con una fórmula + ruido realista
# Fórmula base: peso ≈ 60 + 40*(estatura - 1.5)
pesos = 60 + 40 * (estaturas - 1.5) + np.random.normal(0, 3, 20)

# Crear tabla (DataFrame)
datos = pd.DataFrame({
    'Estatura_m': estaturas,
    'Peso_kg': pesos
})

print("📊 Primeros 5 datos:")
print(datos.head())

# 3️⃣ SEPARAR EN "ENTRENAMIENTO" Y "PRUEBA"
# X = entrada (estatura), y = salida (peso)
X = datos[['Estatura_m']]   # debe ser matriz (con doble corchete)
y = datos['Peso_kg']        # vector

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
# test_size=0.2 → 80% para entrenar, 20% para probar

# 4️⃣ ENTRENAR EL MODELO
modelo = LinearRegression()
modelo.fit(X_train, y_train)   # ¡Aquí el modelo "aprende"!

# 5️⃣ HACER PREDICCIONES
predicciones = modelo.predict(X_test)

# 6️⃣ EVALUAR EL MODELO
mse = mean_squared_error(y_test, predicciones)
r2 = r2_score(y_test, predicciones)

print(f"\n🎯 Error cuadrático medio (MSE): {mse:.2f}")
print(f"📈 R² (qué tan bien ajusta, 1 es perfecto): {r2:.3f}")
print(f"📐 Fórmula aprendida: Peso = {modelo.intercept_:.2f} + {modelo.coef_[0]:.2f} * Estatura")

# 7️⃣ PREDECIR UN CASO NUEVO
nueva_estatura = np.array([[1.75]])  # persona de 1.75 m
peso_predicho = modelo.predict(nueva_estatura)
print(f"\n👤 Para una persona de 1.75 m, el peso predicho es: {peso_predicho[0]:.2f} kg")

# 8️⃣ VISUALIZAR RESULTADOS
plt.figure(figsize=(10, 6))
sns.set_theme(style="whitegrid")

# Puntos de entrenamiento (azul) y prueba (rojo)
sns.scatterplot(x=X_train['Estatura_m'], y=y_train,
                color='blue', s=80, label='Entrenamiento')
sns.scatterplot(x=X_test['Estatura_m'], y=y_test,
                color='red', s=80, label='Prueba', marker='X')

# Línea de regresión
x_linea = np.linspace(1.5, 1.9, 100).reshape(-1, 1)
y_linea = modelo.predict(x_linea)
plt.plot(x_linea, y_linea, color='green', linewidth=2, label='Línea del modelo')

# Punto de la predicción nueva
plt.scatter(1.75, peso_predicho, color='orange',
            s=150, marker='*', zorder=5, label='Nueva predicción')

plt.title('📏 Predicción de Peso a partir de Estatura', fontsize=14, fontweight='bold')
plt.xlabel('Estatura (m)')
plt.ylabel('Peso (kg)')
plt.legend()
plt.tight_layout()
plt.show()
```

### 🔍 Explicación paso a paso

| Paso | Descripción breve |
|------|-------------------|
| **1. Importar** | Cargamos las herramientas que usaremos |
| **2. Crear datos** | Generamos 20 personas con estatura y peso (con ruido realista) |
| **3. Separar** | Dividimos en datos de entrenamiento (80%) y prueba (20%) |
| **4. Entrenar** | `fit()` hace que el modelo encuentre la mejor línea recta |
| **5. Predecir** | El modelo predice pesos para los datos de prueba |
| **6. Evaluar** | MSE mide el error; R² mide qué tan bien ajusta (1 = perfecto) |
| **7. Caso nuevo** | Probamos con una persona que el modelo nunca vio |
| **8. Visualizar** | Graficamos puntos + línea + predicción nueva |

---

## 🌡️ EJEMPLO 2: Predecir la TEMPERATURA a partir de los DÍAS

**Idea:** Registramos la temperatura durante 30 días consecutivos y predecimos la temperatura de días futuros.

### 📄 Código completo (`temperatura_dias.py`)

```python
# =====================================================
# EJEMPLO 2: Predicción de TEMPERATURA a partir de DÍAS
# Aprendizaje Supervisado - Regresión Lineal
# =====================================================

# 1️⃣ IMPORTAR LIBRERÍAS
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# 2️⃣ CREAR LOS DATOS (30 días de medición)
np.random.seed(7)
dias = np.arange(1, 31).reshape(-1, 1)  # días 1 a 30

# Temperatura base: empieza en 18°C y sube ~0.3°C por día + ruido
temperaturas = 18 + 0.3 * dias.flatten() + np.random.normal(0, 1.2, 30)

datos = pd.DataFrame({
    'Dia': dias.flatten(),
    'Temperatura_C': temperaturas
})

print("📊 Primeros 5 días registrados:")
print(datos.head())

# 3️⃣ SEPARAR ENTRENAMIENTO Y PRUEBA
X = datos[['Dia']]
y = datos['Temperatura_C']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=7
)

# 4️⃣ ENTRENAR EL MODELO
modelo = LinearRegression()
modelo.fit(X_train, y_train)

# 5️⃣ PREDECIR
predicciones = modelo.predict(X_test)

# 6️⃣ EVALUAR
mse = mean_squared_error(y_test, predicciones)
r2 = r2_score(y_test, predicciones)

print(f"\n🎯 MSE: {mse:.2f}")
print(f"📈 R²: {r2:.3f}")
print(f"📐 Fórmula: Temperatura = {modelo.intercept_:.2f} + {modelo.coef_[0]:.3f} * Día")

# 7️⃣ PREDECIR DÍAS FUTUROS (31 al 40)
dias_futuros = np.arange(31, 41).reshape(-1, 1)
temps_futuras = modelo.predict(dias_futuros)

print("\n🔮 Predicción de temperatura para los próximos 10 días:")
for d, t in zip(dias_futuros.flatten(), temps_futuras):
    print(f"   Día {d:2d} → {t:.2f} °C")

# 8️⃣ VISUALIZAR
plt.figure(figsize=(11, 6))
sns.set_theme(style="whitegrid")

# Datos históricos
sns.scatterplot(x=X_train['Dia'], y=y_train,
                color='dodgerblue', s=80, label='Entrenamiento')
sns.scatterplot(x=X_test['Dia'], y=y_test,
                color='crimson', s=100, marker='X', label='Prueba')

# Línea de tendencia histórica
x_linea = np.arange(1, 31).reshape(-1, 1)
y_linea = modelo.predict(x_linea)
plt.plot(x_linea, y_linea, color='green', linewidth=2, label='Modelo (histórico)')

# Predicción futura (zona punteada)
plt.plot(dias_futuros, temps_futuras, color='purple',
         linewidth=2, linestyle='--', marker='o', label='Predicción futura')

plt.title('🌡️ Predicción de Temperatura a partir de los Días', fontsize=14, fontweight='bold')
plt.xlabel('Día')
plt.ylabel('Temperatura (°C)')
plt.legend()
plt.tight_layout()
plt.show()
```

### 🔍 Explicación paso a paso

| Paso | Descripción breve |
|------|-------------------|
| **1. Importar** | Cargamos las librerías necesarias |
| **2. Crear datos** | Simulamos 30 días con temperatura creciente + ruido |
| **3. Separar** | 80% para entrenar, 20% para probar |
| **4. Entrenar** | El modelo aprende la relación día ↔ temperatura |
| **5. Predecir** | Aplica lo aprendido a los datos de prueba |
| **6. Evaluar** | MSE y R² nos dicen qué tan bueno es el modelo |
| **7. Futuro** | ¡Predecimos los días 31 al 40 que nunca vimos! |
| **8. Visualizar** | Gráfica con datos históricos y predicción futura |

---

## 🚀 Cómo ejecutar en VS Code

1. Crea un archivo nuevo: `peso_estatura.py`
2. Copia el primer código y guárdalo
3. Presiona el botón ▶️ de **Run Python File** (arriba a la derecha)
4. Repite con `temperatura_dias.py`

---

## 💡 Conceptos clave que aprendiste

| Concepto | Significado |
|----------|-------------|
| **Variable independiente (X)** | Lo que conocemos (estatura, día) |
| **Variable dependiente (y)** | Lo que queremos predecir (peso, temperatura) |
| **Entrenamiento** | Datos con los que el modelo "estudia" |
| **Prueba** | Datos nuevos para ver si realmente aprendió |
| **MSE** | Error promedio (más bajo = mejor) |
| **R²** | Qué tan bien se ajusta (1 = perfecto, 0 = malo) |
| **`fit()`** | Entrenar el modelo |
| **`predict()`** | Usar el modelo para predecir |

---

## 🎓 Retos para practicar

1. **Modifica los datos:** cambia el número de personas/días (ej. 100 en vez de 20)
2. **Cambia el ruido:** prueba `np.random.normal(0, 5, 20)` y observa cómo empeora el modelo
3. **Predice nuevos casos:** agrega tus propias estaturas o días futuros
4. **Compara modelos:** investiga `PolynomialFeatures` para ajustar curvas en vez de líneas

¡Con estos dos ejemplos ya tienes la base para entrar al mundo de la **Visión Artificial** y la **IA**! 🤖✨
