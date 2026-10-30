import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

meses = ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]

ventas = np.array([120, 135, 150, 160, 175, 190, 210, 205, 220, 240, 260, 300])
gastos = np.array([80, 85, 90, 95, 100, 110, 115, 118, 125, 130, 140, 150])
visitas = np.array([1500, 1700, 1850, 2000, 2300, 2600, 3000, 2950, 3200, 3600, 3900, 4500])
conversion = np.array([2.1, 2.3, 2.5, 2.4, 2.7, 2.9, 3.1, 3.0, 3.2, 3.4, 3.5, 3.8])

beneficio = ventas - gastos


df = pd.DataFrame({
    "mes": meses,
    "ventas": ventas,
    "gastos": gastos,
    "beneficio": beneficio,
    "visitas": visitas,
    "conversion": conversion
})
print ("------ curso pandas, matplotlib ---------------")
print("Nuestro conjunto de datos de ejemplo recoge las ventas" )
print("gastos, beneficio, conversión y visitas de la página web de una cierta empresa:")
print()
print(df)
print()
print("¡Vamos a crear nuestro primer gráfico con matplotlib!")
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio"]
ventas = [120, 150, 170, 160, 210, 240]

plt.plot(meses, ventas)
plt.show()
print()
print("El primer argumento ocupará el eje horizontal y el segundo el eje vertical:")
plt.plot(ventas, meses)
plt.show()
print()
print("DataFrame de Pandas simplemente indicamos en cada argumento")
print("la información relativa a cada una de las series que queremos representar:")

plt.plot(df["mes"], df["ventas"])
plt.show()
print()

print(" se pueden representar varias variables")
print("sobre un mismo eje de manera bastante sencilla e intuitiva")
plt.plot(df["mes"], df["ventas"])
plt.plot(df["mes"], df["gastos"])
plt.plot(df["mes"], df["beneficio"])
plt.show()
print()

