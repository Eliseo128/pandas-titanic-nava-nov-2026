Construir un modelo predictivo en Machine Learning es como enseñarle a una computadora a reconocer patrones en la cancha sin programarle reglas manuales. Usando el archivo local `eventos_partido_local.csv` que guardamos en el paso anterior, entrenaremos un **Árbol de Decisión** con **Scikit-Learn** para predecir si una acción en el campo terminará siendo un **Tiro a portería (`SHOT`)** o no, basándonos en la ubicación y duración de la jugada.

---

### 🛠️ Paso 1: Instalar Scikit-Learn en tu entorno

Abre la terminal integrada de VS Code (asegúrate de que esté activo tu entorno `(.venv)`) e instala la librería estándar de Machine Learning en Python:

```bash
pip install scikit-learn

```

Crea un archivo nuevo en tu carpeta del proyecto llamado `modelo_tiros.py`.

---

### 🧹 Paso 2: Preparación y Selección de Datos (Preprocesamiento)

Los algoritmos matemáticos no entienden palabras como `"SHOT"` o `"PASS"`, ni pueden operar si existen celdas vacías (`NaN`). En este paso seleccionaremos las variables útiles (*Features*) y crearemos nuestra variable objetivo (*Target*).

Copia este bloque inicial en `modelo_tiros.py`:

```python
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# 1. Cargar el archivo local que guardamos en el EDA
df = pd.read_csv("eventos_partido_local.csv")

# 2. Crear nuestra variable calculada de duración
df['Duracion'] = df['End Time [s]'] - df['Start Time [s]']

# 3. Seleccionar solo las columnas numéricas relevantes para predecir
columnas_utiles = ['Type', 'Start X', 'Start Y', 'End X', 'End Y', 'Duracion']
df_ml = df[columnas_utiles].copy()

# 4. Eliminar filas con valores nulos (NaN) en las coordenadas o duración
df_ml = df_ml.dropna()

# 5. Crear la variable objetivo (Target): 1 si es 'SHOT', 0 si es cualquier otro evento
df_ml['Es_Tiro'] = (df_ml['Type'] == 'SHOT').astype(int)

print("Distribución de clases (0 = No Tiro, 1 = Tiro):")
print(df_ml['Es_Tiro'].value_counts())

```

> **Concepto clave para alumnos:** Aquí aplicamos lo descubierto en el EDA: notarás que hay muy pocos `1` (tiros) comparados con `0` (pases, recuperaciones, etc.). A esto se le llama **desbalanceo de clases**.

---

### ✂️ Paso 3: Dividir los Datos (Entrenamiento vs. Prueba)

Si evalúas a un alumno con exactamente las mismas preguntas que memorizó en clase, no sabrás si realmente aprendió. En Machine Learning dividimos los datos: **80% para entrenar** al modelo y **20% ocultos para evaluarlo**.

Agrega este código a tu script:

```python
# Definir X (características de entrada) e y (lo que queremos predecir)
X = df_ml[['Start X', 'Start Y', 'End X', 'End Y', 'Duracion']]
y = df_ml['Es_Tiro']

# Dividir en 80% entrenamiento y 20% prueba
# stratify=y asegura que ambos grupos mantengan la misma proporción de tiros
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y
)

print(f"\nDatos para entrenar: {len(X_train)} jugadas")
print(f"Datos para examinar al modelo: {len(X_test)} jugadas")

```

---

### 🧠 Paso 4: Entrenar el Modelo (Árbol de Decisión)

Usaremos un `DecisionTreeClassifier` porque es visual, intuitivo y permite ver exactamente qué reglas matemáticas aprendió la IA (por ejemplo: *"Si Start X es mayor a 0.85, entonces es probable que sea tiro"*).

Además, usaremos el parámetro `class_weight='balanced'` para corregir el desbalanceo de clases que detectamos en el EDA, obligando al algoritmo a prestar especial atención a los pocos tiros que existen.

```python
# 1. Instanciar el modelo con profundidad máxima de 3 niveles para evitar memorización (overfitting)
modelo = DecisionTreeClassifier(max_depth=3, class_weight='balanced', random_state=42)

# 2. Entrenar el modelo (aquí ocurre el aprendizaje matemático)
modelo.fit(X_train, y_train)

print("\n¡Modelo entrenado con éxito!")

```

---

### 📊 Paso 5: Evaluar el Rendimiento del Modelo

Ahora pondremos a prueba el modelo con el 20% de jugadas que nunca ha visto (`X_test`) y compararemos sus predicciones contra la realidad (`y_test`).

```python
# Realizar predicciones sobre los datos de prueba
predicciones = modelo.predict(X_test)

# 1. Exactitud general (Accuracy)
exactitud = accuracy_score(y_test, predicciones)
print(f"\nExactitud general (Accuracy): {exactitud * 100:.2f}%")

# 2. Matriz de Confusión (Aciertos y errores detallados)
print("\nMatriz de Confusión:")
print(confusion_matrix(y_test, predicciones))

# 3. Reporte completo (Precisión, Recall y F1-Score)
print("\nReporte de Clasificación:")
print(classification_report(y_test, predicciones, target_names=['No Tiro', 'Tiro']))

```

#### ¿Cómo interpretar estos resultados en clase?

* **Matriz de Confusión:** Muestra 4 números en un cuadro de $2 \times 2$. La diagonal principal (arriba-izquierda y abajo-derecha) son los **aciertos**. Los otros dos son falsas alarmas o tiros que el modelo no detectó.
* **Recall (Sensibilidad) en la fila "Tiro":** Indica qué porcentaje de los tiros reales del partido logró detectar nuestro modelo. En problemas desbalanceados, el *Recall* y el *F1-Score* son mucho más importantes que el *Accuracy*.

---

### 🌳 Paso 6: Visualizar lo que Aprendió la Inteligencia Artificial

Para conectar este ejercicio con **Matplotlib**, dibujaremos el árbol de reglas que construyó Scikit-Learn y lo guardaremos como imagen.

```python
plt.figure(figsize=(16, 8))
plot_tree(
    modelo,
    feature_names=['Start X', 'Start Y', 'End X', 'End Y', 'Duracion'],
    class_names=['No Tiro', 'Tiro'],
    filled=True,
    rounded=True,
    fontsize=10
)
plt.title("Reglas de Decisión Aprendidas por el Modelo para Predecir Tiros")
plt.tight_layout()
plt.savefig("4_arbol_decision_tiros.png", dpi=300)
plt.show()

```

### 🎮 Prueba Interactiva: Simular una jugada nueva

Al final de tu script, puedes probar tu modelo inventando una jugada con coordenadas específicas para ver qué predice:

```python
# Jugada inventada: empieza cerca del área rival (X=0.90, Y=0.50) y termina en la portería (X=1.0, Y=0.52)
jugada_nueva = pd.DataFrame({
    'Start X': [0.90],
    'Start Y': [0.50],
    'End X': [1.00],
    'End Y': [0.52],
    'Duracion': [1.2]
})

resultado = modelo.predict(jugada_nueva)
print("\nPredicción para la jugada cerca del área:", "ES UN TIRO ⚽" if resultado[0] == 1 else "NO ES TIRO")

```
