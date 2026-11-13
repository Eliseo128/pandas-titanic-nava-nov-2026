Un **Random Forest (Bosque Aleatorio)** funciona bajo el principio de "la sabiduría de la multitud": en lugar de depender de un solo Árbol de Decisión que puede cometer errores por mirar solo una parte de los datos, entrena **100 árboles distintos** simultáneamente, cada uno viendo muestras aleatorias de las jugadas, y al final somete a votación si una acción es un tiro o no.

Para realizar esta comparación justa en clase, utilizaremos exactamente el mismo conjunto de entrenamiento (`X_train`, `y_train`) y de prueba (`X_test`, `y_test`) del paso anterior. Crea un archivo nuevo llamado `comparacion_modelos.py` y sigue estos pasos.

---

### 🌲 Paso 1: Cargar Datos y Entrenar Ambos Modelos

Primero prepararemos los datos idénticos al ejercicio anterior y entrenaremos tanto el **Árbol de Decisión** individual como el **Random Forest** para ponerlos a competir en igualdad de condiciones.

```python
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, classification_report

# 1. Cargar y preparar los datos (mismo flujo del paso anterior)
df = pd.read_csv("eventos_partido_local.csv")
df['Duracion'] = df['End Time [s]'] - df['Start Time [s]']

columnas_utiles = ['Type', 'Start X', 'Start Y', 'End X', 'End Y', 'Duracion']
df_ml = df[columnas_utiles].dropna().copy()
df_ml['Es_Tiro'] = (df_ml['Type'] == 'SHOT').astype(int)

X = df_ml[['Start X', 'Start Y', 'End X', 'End Y', 'Duracion']]
y = df_ml['Es_Tiro']

# División 80% entrenamiento / 20% prueba
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y
)

# 2. Modelo A: Árbol de Decisión Individual
modelo_arbol = DecisionTreeClassifier(max_depth=3, class_weight='balanced', random_state=42)
modelo_arbol.fit(X_train, y_train)

# 3. Modelo B: Random Forest (100 árboles votando en conjunto)
modelo_bosque = RandomForestClassifier(
    n_estimators=100,       # Cantidad de árboles en el bosque
    max_depth=5,            # Profundidad máxima de cada árbol
    class_weight='balanced',# Compensa el desbalanceo de pocos tiros
    random_state=42
)
modelo_bosque.fit(X_train, y_train)

print("¡Ambos modelos han sido entrenados con éxito!")

```

---

### 📊 Paso 2: Evaluar y Comparar Métricas en Consola

Ahora evaluaremos ambos modelos sobre el 20% de jugadas desconocidas (`X_test`) para observar cómo cambia el equilibrio entre falsas alarmas y tiros reales detectados.

```python
# Generar predicciones con ambos modelos
pred_arbol = modelo_arbol.predict(X_test)
pred_bosque = modelo_bosque.predict(X_test)

print("\n" + "="*50)
print("REPORTE 1: ÁRBOL DE DECISIÓN INDIVIDUAL")
print("="*50)
print(classification_report(y_test, pred_arbol, target_names=['No Tiro', 'Tiro']))

print("\n" + "="*50)
print("REPORTE 2: RANDOM FOREST (100 ÁRBOLES)")
print("="*50)
print(classification_report(y_test, pred_bosque, target_names=['No Tiro', 'Tiro']))

```

---

### 🖼️ Paso 3: Visualizar las Matrices de Confusión Lado a Lado

En lugar de leer números planos en consola, utilizaremos **Matplotlib** (`plt.subplots`) junto con `ConfusionMatrixDisplay` de Scikit-Learn para generar una comparativa visual directa.

```python
# Calcular las matrices matemáticas
cm_arbol = confusion_matrix(y_test, pred_arbol)
cm_bosque = confusion_matrix(y_test, pred_bosque)

# Crear figura con 2 subgráficas horizontales
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))

# Gráfica 1: Matriz del Árbol de Decisión
disp_arbol = ConfusionMatrixDisplay(confusion_matrix=cm_arbol, display_labels=['No Tiro', 'Tiro'])
disp_arbol.plot(ax=ax1, cmap='Blues', colorbar=False)
ax1.set_title("Árbol de Decisión (1 Árbol)")

# Gráfica 2: Matriz del Random Forest
disp_bosque = ConfusionMatrixDisplay(confusion_matrix=cm_bosque, display_labels=['No Tiro', 'Tiro'])
disp_bosque.plot(ax=ax2, cmap='Greens', colorbar=False)
ax2.set_title("Random Forest (100 Árboles)")

plt.tight_layout()
plt.savefig("5_comparacion_matrices.png", dpi=300)
plt.show()

```

---

### 🔍 Paso 4: ¿Cómo Analizar las Diferencias con tus Alumnos?

Al observar las dos matrices de confusión y los reportes, notarás un comportamiento clásico en Machine Learning llamado **compromiso entre Precisión y Exhaustividad (Precision-Recall Tradeoff)**:

| Aspecto a observar | Árbol de Decisión (`max_depth=3`) | Random Forest (`n_estimators=100`) |
| --- | --- | --- |
| **Falsos Positivos** *(Cuadro superior derecho)* | **Alto.** Al tener pocas reglas simples, clasifica muchos pases largos hacia el área como si fueran tiros. | **Mucho menor.** Como 100 árboles deben ponerse de acuerdo, filtra mejor las falsas alarmas. |
| **Verdaderos Positivos** *(Cuadro inferior derecho)* | Detecta casi todos los tiros reales, pero a costa de equivocarse mucho con los pases. | Mantiene una buena detección de tiros con una **Precisión** y **F1-Score** superiores. |
| **Estabilidad** | Si cambias unos pocos datos, el árbol cambia por completo (alta varianza). | Muy estable y resistente al ruido gracias al promedio de sus 100 árboles. |

---

### 💡 Extra: ¿Qué variable fue más importante para el Bosque?

Una gran ventaja de Random Forest es que nos permite preguntarle qué columna de nuestro dataset tuvo mayor peso para tomar sus decisiones:

```python
importancias = pd.Series(modelo_bosque.feature_importances_, index=X.columns).sort_values(ascending=False)
print("\nImportancia de cada variable según Random Forest:")
print(importancias * 100)

```
