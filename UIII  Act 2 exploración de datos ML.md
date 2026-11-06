¡Hola! Con mucho gusto tomo el rol de docente didáctico de Machine Learning.

En la resolución de problemas de Machine Learning (ML), estructurar conjuntos de datos en **diccionarios de listas** (el formato básico para crear DataFrames con librerías como *Pandas*) es un paso indispensable para representar observaciones y sus características (features).

Aquí tienes **6 ejemplos didácticos**, variados en contexto y tipos de datos (numéricos, categóricos, booleanos), listos para practicar preparación de datos, clasificación, regresión o agrupación.

---

### 1. Diagnóstico de Salud (Modelos de Clasificación Médica)

Este dataset es ideal para entrenar modelos predictivos de riesgo de enfermedades según variables biométricas.

```python
pacientes = {
    "Nombre": ["Ana", "Luis", "Marta", "Roberto", "Carla", "Javier"],
    "Presion_Arterial": [120, 140, 135, 110, 150, 125],
    "Fumador": [False, True, False, False, True, True],
    "Nivel_Riesgo": ["Bajo", "Alto", "Medio", "Bajo", "Alto", "Medio"]
}

```

---

### 2. Predicción de Precios de Inmuebles (Regresión)

Un clásico problema de regresión cuantitativa donde predecimos el valor de una vivienda a partir de sus características físicas.

```python
inmuebles = {
    "Id_Casa": [101, 102, 103, 104, 105, 106],
    "Metros_Cuadrados": [65, 120, 85, 200, 150, 95],
    "Habitaciones": [2, 4, 3, 5, 4, 3],
    "Precio_Miles_USD": [150, 310, 210, 480, 390, 240]
}

```

---

### 3. Fuga de Clientes / Churn (Clasificación Binaria)

Utilizado para detectar qué usuarios están en riesgo de cancelar un servicio de suscripción (banca, telecomunicaciones, etc.).

```python
clientes = {
    "Cliente": ["User1", "User2", "User3", "User4", "User5", "User6"],
    "Antiguedad_Meses": [2, 36, 12, 5, 48, 1],
    "Gasto_Mensual": [29.99, 89.99, 59.99, 19.99, 110.00, 49.99],
    "Cancela_Servicio": [True, False, False, True, False, True]
}

```

---

### 4. Selección y Filtrado de Vehículos (Filtrado / Regresión)

Permite construir algoritmos de recomendación o predecir eficiencia energética basándose en especificaciones técnicas.

```python
vehiculos = {
    "Modelo": ["Sedan X", "SUV Compact", "Hatchback Z", "Pickup Heavy", "Electric Eco", "Coupe Sport"],
    "Tipo_Motor": ["Gasolina", "Hibrido", "Gasolina", "Diesel", "Electrico", "Gasolina"],
    "Autonomia_Km": [600, 800, 550, 700, 450, 500],
    "Precio_USD": [22000, 35000, 18000, 45000, 32000, 41000]
}

```

---

### 5. Detección de Transacciones Fraudulentas (Clasificación para Seguridad)

Ejemplo de datos procesados por redes neuronales o árboles de decisión para detectar fraudes financieros en tiempo real.

```python
transacciones = {
    "Id_Transaccion": ["T001", "T002", "T003", "T004", "T005", "T006"],
    "Monto": [15.50, 2500.00, 45.00, 890.00, 12.00, 3400.00],
    "Ubicacion_Inusual": [False, True, False, True, False, True],
    "Es_Fraude": [False, True, False, False, False, True]
}

```

---

### 6. Desempeño Laboral (Sistemas de Evaluación y Clustering)

Útil para agrupar empleados por rendimiento o predecir el impacto de las horas de capacitación mediante algoritmos de ML.

```python
empleados = {
    "Empleado": ["Elena", "Sergio", "Lucia", "Gonzalo", "Valeria", "Diego"],
    "Departamento": ["Ventas", "IT", "HR", "IT", "Ventas", "Finanzas"],
    "Horas_Capacitacion": [40, 80, 25, 60, 90, 15],
    "Evaluacion_Desempeno": [8.5, 9.2, 7.0, 8.8, 9.6, 6.5]
}

```
