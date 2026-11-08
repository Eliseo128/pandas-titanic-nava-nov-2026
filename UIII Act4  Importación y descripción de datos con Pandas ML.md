¡Hola! Como docente didáctico, me encanta esta iniciativa. Tener una variedad amplia de ejemplos es la mejor manera de que los estudiantes practiquen la creación de DataFrames, el análisis exploratorio (EDA) y la visualización sin aburrirse con el mismo contexto.

A continuación, te presento **60 ejemplos diferentes**, organizados por **10 categorías temáticas** (6 ejemplos por categoría). 

**Regla de oro cumplida en todos:** Cada diccionario tiene exactamente **10 claves (listas)** y cada lista tiene exactamente **6 elementos**.

---

### 🏥 Categoría 1: Salud y Medicina

**1. Pacientes de una clínica**
```python
pacientes_clinica = {
    'id_paciente': [1001, 1002, 1003, 1004, 1005, 1006],
    'nombre': ['Laura', 'Pedro', 'Sofia', 'Miguel', 'Elena', 'Jorge'],
    'edad': [34, 45, 28, 62, 19, 51],
    'tipo_sangre': ['O+', 'A-', 'B+', 'AB+', 'O-', 'A+'],
    'peso_kg': [65.5, 78.2, 58.0, 85.1, 52.3, 74.0],
    'altura_cm': [165, 175, 160, 180, 155, 172],
    'diagnostico': ['Gripe', 'Hipertension', 'Migraña', 'Diabetes', 'Alergia', 'Gastritis'],
    'dias_hospitalizacion': [0, 3, 0, 5, 1, 2],
    'medicamento': ['Paracetamol', 'Enalapril', 'Ibuprofeno', 'Metformina', 'Loratadina', 'Omeprazol'],
    'proximo_control': ['2024-02-01', '2024-01-15', '2024-03-10', '2024-01-20', '2024-04-05', '2024-02-28']
}
```

**2. Inventario de medicamentos**
```python
inventario_medicamentos = {
    'id_medicamento': [501, 502, 503, 504, 505, 506],
    'nombre_comercial': ['Aspirina', 'Amoxicilina', 'Omeprazol', 'Ibuprofeno', 'Loratadina', 'Metformina'],
    'principio_activo': ['Acido acetilsalicilico', 'Amoxicilina', 'Omeprazol', 'Ibuprofeno', 'Loratadina', 'Metformina'],
    'presentacion': ['Tabletas', 'Capsulas', 'Capsulas', 'Tabletas', 'Jarabe', 'Tabletas'],
    'stock_actual': [150, 80, 200, 120, 90, 110],
    'precio_unitario': [45.50, 120.00, 85.00, 65.00, 95.00, 150.00],
    'fecha_caducidad': ['2025-06', '2024-12', '2026-01', '2025-03', '2024-08', '2025-11'],
    'proveedor': ['Farmax', 'SaludTotal', 'MediCorp', 'Farmax', 'BioGen', 'MediCorp'],
    'requiere_receta': [False, True, False, False, False, True],
    'ubicacion_estante': ['A1', 'B3', 'A2', 'C1', 'B2', 'C3']
}
```

**3. Personal médico**
```python
personal_medico = {
    'id_empleado': [201, 202, 203, 204, 205, 206],
    'nombre': ['Dr. Ruiz', 'Dra. Lopez', 'Enf. Garcia', 'Dr. Martinez', 'Enf. Torres', 'Dra. Sanchez'],
    'especialidad': ['Cardiologia', 'Pediatria', 'General', 'Neurologia', 'Urgencias', 'Dermatologia'],
    'tipo_contrato': ['Tiempo completo', 'Tiempo completo', 'Medio tiempo', 'Tiempo completo', 'Turnos', 'Por consulta'],
    'anos_experiencia': [15, 8, 3, 20, 5, 12],
    'consultorio': [101, 102, 105, 103, 100, 104],
    'salario_mensual': [45000, 42000, 18000, 55000, 22000, 38000],
    'pacientes_atendidos_mes': [120, 95, 200, 80, 150, 110],
    'calificacion_pacientes': [4.8, 4.9, 4.5, 4.7, 4.6, 4.9],
    'vacaciones_pendientes': [5, 10, 2, 0, 4, 8]
}
```

**4. Equipos de ultrasonido**
```python
equipos_ultrasonido = {
    'id_equipo': [301, 302, 303, 304, 305, 306],
    'marca': ['GE', 'Philips', 'Siemens', 'GE', 'Canon', 'Philips'],
    'modelo': ['Voluson E8', 'EPIQ 7', 'Acuson S2000', 'Logiq E9', 'Aplio 500', 'Affiniti 70'],
    'ano_fabricacion': [2018, 2020, 2019, 2021, 2017, 2022],
    'ubicacion': ['Ginecologia', 'Cardiologia', 'Radiologia', 'Radiologia', 'Ginecologia', 'Cardiologia'],
    'estado': ['Operativo', 'Operativo', 'Mantenimiento', 'Operativo', 'Operativo', 'Operativo'],
    'horas_uso_total': [4500, 2100, 3800, 1200, 5600, 800],
    'ultimo_mantenimiento': ['2023-10', '2023-11', '2023-12', '2024-01', '2023-09', '2024-01'],
    'costo_adquisicion': [850000, 920000, 780000, 950000, 700000, 880000],
    'tecnico_asignado': ['Juan P.', 'Maria L.', 'Carlos R.', 'Juan P.', 'Ana S.', 'Maria L.']
}
```

**5. Consultas de laboratorio**
```python
consultas_laboratorio = {
    'id_estudio': [401, 402, 403, 404, 405, 406],
    'paciente': ['Laura', 'Pedro', 'Sofia', 'Miguel', 'Elena', 'Jorge'],
    'tipo_estudio': ['Hemograma', 'Glucosa', 'Perfil lipidico', 'Hemoglobina Glicosilada', 'Prueba alergia', 'Coproparasitoscopia'],
    'fecha_toma': ['2024-01-10', '2024-01-10', '2024-01-11', '2024-01-12', '2024-01-12', '2024-01-13'],
    'ayuno_horas': [8, 12, 12, 12, 0, 0],
    'resultado_numerico': [14.2, 105, 180, 6.8, 0, 0],
    'unidad_medida': ['g/dL', 'mg/dL', 'mg/dL', '%', 'N/A', 'N/A'],
    'rango_normal': ['12-16', '70-100', '<200', '<5.7', 'Negativo', 'Negativo'],
    'estatus': ['Normal', 'Alto', 'Alto', 'Alto', 'Negativo', 'Negativo'],
    'tecnico_laboratorio': ['Ana', 'Luis', 'Ana', 'Luis', 'Carmen', 'Carmen']
}
```

**6. Vacunas aplicadas**
```python
registro_vacunas = {
    'id_aplicacion': [601, 602, 603, 604, 605, 606],
    'paciente': ['Sofia', 'Miguel', 'Elena', 'Jorge', 'Laura', 'Pedro'],
    'nombre_vacuna': ['Influenza', 'Neumococo', 'Hepatitis B', 'Tetanos', 'COVID-19 Refuerzo', 'Influenza'],
    'lote': ['L23A', 'L24B', 'L22C', 'L25A', 'L26D', 'L23A'],
    'fecha_aplicacion': ['2023-10-01', '2023-11-15', '2023-08-20', '2023-12-05', '2024-01-10', '2023-10-05'],
    'dosis': [1, 1, 3, 1, 4, 1],
    'via_administracion': ['Intramuscular', 'Intramuscular', 'Intramuscular', 'Intramuscular', 'Intramuscular', 'Intramuscular'],
    'sitio_aplicacion': ['Deltoides', 'Deltoides', 'Deltoides', 'Deltoides', 'Deltoides', 'Deltoides'],
    'reaccion_adversa': [False, False, True, False, False, False],
    'enfermero_aplicador': ['Enf. Garcia', 'Enf. Torres', 'Enf. Garcia', 'Enf. Torres', 'Enf. Garcia', 'Enf. Torres']
}
```

---

### 💻 Categoría 2: Tecnología e Informática

**7. Servidores de la empresa**
```python
servidores_empresa = {
    'id_servidor': ['SRV-01', 'SRV-02', 'SRV-03', 'SRV-04', 'SRV-05', 'SRV-06'],
    'nombre_host': ['web-prod-01', 'db-prod-01', 'app-test-01', 'file-server', 'backup-01', 'mail-server'],
    'sistema_operativo': ['Ubuntu 22.04', 'Windows Server 2022', 'CentOS 8', 'Ubuntu 20.04', 'Debian 11', 'Windows Server 2019'],
    'ram_gb': [32, 128, 16, 64, 32, 32],
    'almacenamiento_tb': [2, 10, 1, 20, 50, 4],
    'ip_address': ['192.168.1.10', '192.168.1.11', '192.168.2.10', '192.168.1.20', '192.168.3.10', '192.168.1.15'],
    'estado': ['Activo', 'Activo', 'Inactivo', 'Activo', 'Activo', 'Activo'],
    'uptime_dias': [120, 365, 0, 200, 400, 150],
    'responsable': ['Carlos', 'Ana', 'Luis', 'Pedro', 'Ana', 'Carlos'],
    'fecha_ultima_parche': ['2024-01-05', '2024-01-05', 'N/A', '2023-12-20', '2024-01-01', '2023-12-15']
}
```

**8. Desarrolladores de software**
```python
desarrolladores_sw = {
    'id_dev': [701, 702, 703, 704, 705, 706],
    'nombre': ['Sofia', 'Javier', 'Valeria', 'Diego', 'Camila', 'Mateo'],
    'rol': ['Frontend', 'Backend', 'DevOps', 'Fullstack', 'Data Scientist', 'QA Tester'],
    'lenguaje_principal': ['JavaScript', 'Python', 'Bash', 'Java', 'Python', 'JavaScript'],
    'anos_experiencia': [3, 5, 7, 4, 2, 3],
    'salario_mensual': [35000, 45000, 55000, 40000, 38000, 28000],
    'proyectos_activos': [2, 3, 5, 2, 1, 4],
    'tickets_resueltos_mes': [45, 60, 80, 50, 30, 75],
    'modalidad': ['Remoto', 'Hibrido', 'Remoto', 'Presencial', 'Remoto', 'Hibrido'],
    'evaluacion_desempeno': [90, 85, 95, 88, 92, 80]
}
```

**9. Tickets de soporte técnico**
```python
tickets_soporte = {
    'id_ticket': [8001, 8002, 8003, 8004, 8005, 8006],
    'solicitante': ['Laura', 'Pedro', 'Sofia', 'Miguel', 'Elena', 'Jorge'],
    'departamento': ['Ventas', 'RH', 'TI', 'Finanzas', 'Ventas', 'Direccion'],
    'categoria': ['Hardware', 'Software', 'Red', 'Software', 'Hardware', 'Accesos'],
    'prioridad': ['Alta', 'Media', 'Critica', 'Baja', 'Media', 'Alta'],
    'estado': ['Resuelto', 'En proceso', 'En proceso', 'Resuelto', 'Pendiente', 'Resuelto'],
    'tiempo_resolucion_horas': [2.5, 4.0, 0.0, 1.0, 0.0, 3.5],
    'tecnico_asignado': ['Diego', 'Valeria', 'Javier', 'Diego', 'Valeria', 'Javier'],
    'fecha_apertura': ['2024-01-10', '2024-01-11', '2024-01-12', '2024-01-12', '2024-01-13', '2024-01-13'],
    'satisfaccion_usuario': [5, 4, 0, 5, 0, 4]
}
```

**10. Dispositivos de red**
```python
dispositivos_red = {
    'id_dispositivo': ['NET-01', 'NET-02', 'NET-03', 'NET-04', 'NET-05', 'NET-06'],
    'tipo': ['Router', 'Switch', 'Switch', 'Firewall', 'Access Point', 'Access Point'],
    'marca': ['Cisco', 'HP', 'Cisco', 'Palo Alto', 'Ubiquiti', 'Ubiquiti'],
    'modelo': ['ISR4321', '2960X', '3850', 'PA-220', 'U6-Pro', 'U6-Lite'],
    'ubicacion_fisica': ['Rack Principal', 'Piso 1', 'Piso 2', 'Rack Principal', 'Sala Juntas', 'Cafeteria'],
    'direccion_mac': ['AA:BB:CC:11', 'AA:BB:CC:22', 'AA:BB:CC:33', 'AA:BB:CC:44', 'AA:BB:CC:55', 'AA:BB:CC:66'],
    'puertos_totales': [4, 48, 48, 8, 0, 0],
    'puertos_usados': [3, 40, 25, 6, 0, 0],
    'firmware_version': ['16.9.4', '15.2.7', '16.6.5', '10.1.3', '6.5.55', '6.5.55'],
    'ultimo_reinicio': ['2023-12-01', '2023-11-15', '2024-01-05', '2023-10-20', '2024-01-10', '2024-01-10']
}
```

**11. Proyectos de desarrollo web**
```python
proyectos_web = {
    'id_proyecto': [901, 902, 903, 904, 905, 906],
    'nombre_proyecto': ['E-commerce', 'Intranet', 'Landing Page', 'App Movil', 'Dashboard BI', 'Blog Corporativo'],
    'cliente': ['Tienda A', 'Empresa B', 'Startup C', 'Empresa B', 'Tienda A', 'Empresa D'],
    'estado': ['En desarrollo', 'Pruebas', 'Finalizado', 'En desarrollo', 'Planificacion', 'Finalizado'],
    'presupuesto': [150000, 80000, 30000, 200000, 120000, 40000],
    'gasto_actual': [90000, 75000, 30000, 50000, 10000, 40000],
    'fecha_inicio': ['2023-10-01', '2023-11-01', '2023-12-01', '2024-01-05', '2024-02-01', '2023-09-01'],
    'fecha_entrega_estimada': ['2024-03-01', '2024-02-15', '2023-12-20', '2024-05-01', '2024-04-01', '2023-11-30'],
    'desarrollador_lider': ['Sofia', 'Javier', 'Diego', 'Valeria', 'Camila', 'Sofia'],
    'porcentaje_avance': [60, 90, 100, 25, 10, 100]
}
```

**12. Licencias de software**
```python
licencias_software = {
    'id_licencia': [101, 102, 103, 104, 105, 106],
    'software': ['Windows 11 Pro', 'Office 365', 'Adobe CC', 'AutoCAD', 'Antivirus Corp', 'Jira'],
    'tipo_licencia': ['Perpetua', 'Suscripcion', 'Suscripcion', 'Perpetua', 'Suscripcion', 'Suscripcion'],
    'cantidad_asientos': [50, 100, 15, 5, 100, 20],
    'costo_unitario_anual': [0, 2500, 12000, 0, 500, 3000],
    'fecha_adquisicion': ['2022-01-01', '2023-01-01', '2023-06-01', '2021-05-01', '2023-01-01', '2023-08-01'],
    'fecha_vencimiento': ['N/A', '2024-01-01', '2024-06-01', 'N/A', '2024-01-01', '2024-08-01'],
    'proveedor': ['Microsoft', 'Microsoft', 'Adobe', 'Autodesk', 'Symantec', 'Atlassian'],
    'departamento_uso': ['General', 'General', 'Diseno', 'Ingenieria', 'General', 'TI'],
    'estado': ['Activa', 'Vencida', 'Activa', 'Activa', 'Vencida', 'Activa']
}
```

---

### 🔧 Categoría 3: Mecánica y Automotriz

**13. Vehículos en taller**
```python
vehiculos_taller = {
    'id_orden': [5001, 5002, 5003, 5004, 5005, 5006],
    'marca': ['Toyota', 'Nissan', 'Ford', 'Chevrolet', 'Honda', 'Volkswagen'],
    'modelo': ['Corolla', 'Sentra', 'Mustang', 'Aveo', 'Civic', 'Jetta'],
    'ano': [2018, 2020, 2015, 2019, 2021, 2017],
    'color': ['Blanco', 'Gris', 'Rojo', 'Negro', 'Azul', 'Plata'],
    'kilometraje': [45000, 30000, 80000, 55000, 20000, 60000],
    'tipo_servicio': ['Mantenimiento', 'Reparacion', 'Reparacion', 'Mantenimiento', 'Mantenimiento', 'Reparacion'],
    'mecanico_asignado': ['Roberto', 'Luis', 'Roberto', 'Carlos', 'Luis', 'Carlos'],
    'costo_estimado': [2500, 8000, 12000, 3000, 2800, 6500],
    'estado_vehiculo': ['En proceso', 'Terminado', 'Espera refaccion', 'En proceso', 'Terminado', 'En proceso']
}
```

**14. Mecánicos del taller**
```python
mecanicos_taller = {
    'id_mecanico': [301, 302, 303, 304, 305, 306],
    'nombre': ['Roberto', 'Luis', 'Carlos', 'Fernando', 'Jorge', 'Miguel'],
    'especialidad': ['Motor', 'Suspension', 'Electrico', 'Frenos', 'Transmision', 'General'],
    'anos_experiencia': [15, 8, 12, 5, 20, 10],
    'salario_base': [18000, 15000, 17000, 14000, 20000, 16000],
    'comision_porcentaje': [10, 10, 10, 10, 10, 10],
    'ordenes_completadas_mes': [25, 30, 20, 15, 35, 28],
    'calificacion_cliente': [4.8, 4.5, 4.9, 4.2, 5.0, 4.6],
    'turno': ['Matutino', 'Vespertino', 'Matutino', 'Vespertino', 'Matutino', 'Vespertino'],
    'certificacion': [True, True, True, False, True, True]
}
```

**15. Refacciones en inventario**
```python
inventario_refacciones = {
    'id_refaccion': [701, 702, 703, 704, 705, 706],
    'nombre': ['Filtro de aceite', 'Bujias (juego)', 'Balatas delanteras', 'Bateria 12V', 'Amortiguador', 'Correa de distribucion'],
    'marca_refaccion': ['Bosch', 'NGK', 'Brembo', 'LTH', 'KYB', 'Gates'],
    'categoria': ['Motor', 'Encendido', 'Frenos', 'Electrico', 'Suspension', 'Motor'],
    'stock': [50, 100, 30, 15, 20, 25],
    'stock_minimo': [20, 40, 15, 10, 10, 10],
    'precio_compra': [80, 250, 400, 1500, 800, 350],
    'precio_venta': [150, 400, 750, 2500, 1500, 600],
    'ubicacion_almacen': ['A-1', 'A-2', 'B-1', 'C-1', 'B-2', 'A-3'],
    'proveedor': ['AutoPartes SA', 'Refacciones MX', 'Frenos Pro', 'Baterias del Norte', 'Suspensiones YA', 'AutoPartes SA']
}
```

**16. Órdenes de servicio**
```python
ordenes_servicio = {
    'id_orden': [6001, 6002, 6003, 6004, 6005, 6006],
    'cliente': ['Juan', 'Maria', 'Pedro', 'Ana', 'Luis', 'Sofia'],
    'telefono': ['551234', '552345', '553456', '554567', '555678', '556789'],
    'vehiculo': ['Toyota Corolla', 'Nissan Sentra', 'Ford Mustang', 'Chevrolet Aveo', 'Honda Civic', 'VW Jetta'],
    'fecha_ingreso': ['2024-01-10', '2024-01-11', '2024-01-11', '2024-01-12', '2024-01-13', '2024-01-13'],
    'fecha_salida_estimada': ['2024-01-12', '2024-01-13', '2024-01-15', '2024-01-13', '2024-01-14', '2024-01-16'],
    'falla_reportada': ['Ruido motor', 'Falla frenos', 'No enciende', 'Cambio aceite', 'Afinacion', 'Fuga liquido'],
    'diagnostico_tecnico': ['Banda floja', 'Balatas gastadas', 'Bateria muerta', 'Mantenimiento normal', 'Mantenimiento normal', 'Manguera rota'],
    'total_facturado': [1200, 2500, 2800, 1500, 1800, 3200],
    'metodo_pago': ['Tarjeta', 'Efectivo', 'Transferencia', 'Efectivo', 'Tarjeta', 'Transferencia']
}
```

**17. Herramientas especializadas**
```python
herramientas_taller = {
    'id_herramienta': [801, 802, 803, 804, 805, 806],
    'nombre': ['Escáner OBD2', 'Torquímetro', 'Gato hidráulico', 'Compresor aire', 'Multimetro digital', 'Juego de dados'],
    'marca': ['Launch', 'Truper', 'Blackhawk', 'Truper', 'Fluke', 'Stanley'],
    'tipo': ['Electronica', 'Manual', 'Hidraulica', 'Neumatica', 'Electronica', 'Manual'],
    'fecha_compra': ['2022-05-01', '2021-03-15', '2020-08-10', '2019-11-20', '2023-01-10', '2021-06-05'],
    'costo': [8000, 1200, 3500, 15000, 2500, 1800],
    'estado': ['Bueno', 'Excelente', 'Regular', 'Bueno', 'Excelente', 'Bueno'],
    'ubicacion': ['Caja herramientas', 'Caja herramientas', 'Foso 1', 'Area compresor', 'Mesa trabajo', 'Caja herramientas'],
    'responsable': ['Roberto', 'Luis', 'Carlos', 'Fernando', 'Jorge', 'Miguel'],
    'requiere_calibracion': [True, True, False, True, True, False]
}
```

**18. Pruebas de emisiones**
```python
pruebas_emisiones = {
    'id_prueba': [901, 902, 903, 904, 905, 906],
    'placa_vehiculo': ['ABC-123', 'DEF-456', 'GHI-789', 'JKL-012', 'MNO-345', 'PQR-678'],
    'modelo_vehiculo': ['2018', '2020', '2015', '2019', '2021', '2017'],
    'tipo_combustible': ['Gasolina', 'Gasolina', 'Gasolina', 'Diesel', 'Gasolina', 'Gasolina'],
    'co_medido': [0.2, 0.1, 0.8, 0.3, 0.1, 0.5],
    'co_limite': [0.5, 0.5, 0.5, 0.5, 0.5, 0.5],
    'hc_medido': [50, 30, 120, 40, 20, 80],
    'hc_limite': [100, 100, 100, 100, 100, 100],
    'resultado': ['Aprobado', 'Aprobado', 'Reprobado', 'Aprobado', 'Aprobado', 'Reprobado'],
    'fecha_prueba': ['2024-01-05', '2024-01-06', '2024-01-07', '2024-01-08', '2024-01-09', '2024-01-10']
}
```

---

### 🎓 Categoría 4: Educación y Escuela

**19. Estudiantes de un grupo**
```python
estudiantes_grupo = {
    'id_estudiante': [1001, 1002, 1003, 1004, 1005, 1006],
    'nombre': ['Ana', 'Luis', 'Sofia', 'Carlos', 'Maria', 'Jorge'],
    'edad': [16, 17, 16, 17, 16, 17],
    'genero': ['F', 'M', 'F', 'M', 'F', 'M'],
    'promedio_general': [9.2, 8.5, 9.8, 7.8, 8.9, 8.1],
    'asistencias': [95, 88, 100, 80, 92, 85],
    'faltas': [5, 12, 0, 20, 8, 15],
    'actividad_extracurricular': ['Debate', 'Futbol', 'Robotica', 'Ninguna', 'Danza', 'Futbol'],
    'beca': [True, False, True, False, True, False],
    'tutor_nombre': ['Sra. Perez', 'Sr. Gomez', 'Sra. Lopez', 'Sr. Ruiz', 'Sra. Diaz', 'Sr. Torres']
}
```

**20. Cursos en línea**
```python
cursos_online = {
    'id_curso': [201, 202, 203, 204, 205, 206],
    'titulo': ['Intro a Python', 'Marketing Digital', 'Diseño UX/UI', 'Finanzas Personales', 'Ingles Intermedio', 'Excel Avanzado'],
    'instructor': ['Carlos', 'Ana', 'Luis', 'Maria', 'Pedro', 'Sofia'],
    'duracion_horas': [40, 30, 50, 20, 60, 35],
    'precio': [1500, 1200, 2000, 800, 2500, 1000],
    'estudiantes_inscritos': [150, 200, 80, 300, 120, 180],
    'calificacion_promedio': [4.8, 4.5, 4.9, 4.2, 4.7, 4.6],
    'nivel': ['Principiante', 'Intermedio', 'Intermedio', 'Principiante', 'Intermedio', 'Avanzado'],
    'fecha_inicio': ['2024-02-01', '2024-02-15', '2024-03-01', '2024-02-05', '2024-03-15', '2024-02-20'],
    'plataforma': ['Udemy', 'Coursera', 'Domestika', 'Udemy', 'Coursera', 'LinkedIn']
}
```

**21. Profesores de la facultad**
```python
profesores_facultad = {
    'id_profesor': [301, 302, 303, 304, 305, 306],
    'nombre': ['Dr. Ramirez', 'Mtra. Sanchez', 'Dr. Flores', 'Mtro. Vargas', 'Dra. Mendoza', 'Mtro. Castro'],
    'departamento': ['Matematicas', 'Humanidades', 'Ciencias', 'Ingenieria', 'Ciencias', 'Humanidades'],
    'grado_academico': ['Doctorado', 'Maestria', 'Doctorado', 'Maestria', 'Doctorado', 'Maestria'],
    'anos_antiguedad': [15, 8, 20, 5, 12, 3],
    'materias_asignadas': [3, 2, 4, 2, 3, 2],
    'alumnos_totales': [120, 80, 150, 60, 110, 70],
    'salario_mensual': [35000, 25000, 40000, 22000, 32000, 20000],
    'publicaciones_ano': [2, 1, 4, 0, 3, 1],
    'tipo_contrato': ['Definitivo', 'Definitivo', 'Definitivo', 'Interino', 'Definitivo', 'Interino']
}
```

**22. Libros de la biblioteca**
```python
libros_biblioteca = {
    'isbn': ['978-1', '978-2', '978-3', '978-4', '978-5', '978-6'],
    'titulo': ['Cien años de soledad', 'El principito', '1984', 'Don Quijote', 'Fahrenheit 451', 'Orgullo y prejuicio'],
    'autor': ['Garcia Marquez', 'Saint-Exupery', 'Orwell', 'Cervantes', 'Bradbury', 'Austen'],
    'ano_publicacion': [1967, 1943, 1949, 1605, 1953, 1813],
    'genero': ['Realismo magico', 'Infantil', 'Distopia', 'Aventuras', 'Ciencia ficcion', 'Romance'],
    'ejemplares_totales': [5, 8, 4, 3, 4, 6],
    'ejemplares_prestados': [2, 5, 1, 0, 2, 3],
    'ubicacion_estante': ['A1', 'B2', 'C1', 'A2', 'C2', 'B3'],
    'estado_conservacion': ['Bueno', 'Regular', 'Excelente', 'Regular', 'Bueno', 'Excelente'],
    'fecha_ultimo_prestamo': ['2024-01-10', '2024-01-12', '2023-12-20', '2023-11-05', '2024-01-08', '2024-01-11']
}
```

**23. Calificaciones por materia**
```python
calificaciones_materia = {
    'id_registro': [401, 402, 403, 404, 405, 406],
    'estudiante': ['Ana', 'Luis', 'Sofia', 'Carlos', 'Maria', 'Jorge'],
    'materia': ['Matematicas', 'Matematicas', 'Matematicas', 'Matematicas', 'Matematicas', 'Matematicas'],
    'parcial_1': [9.0, 8.0, 10.0, 7.0, 9.5, 8.5],
    'parcial_2': [9.5, 8.5, 9.5, 8.0, 8.5, 7.5],
    'parcial_3': [9.0, 9.0, 10.0, 8.5, 8.5, 8.0],
    'tareas_promedio': [9.5, 8.0, 10.0, 7.5, 9.0, 8.0],
    'asistencia_porcentaje': [95, 88, 100, 80, 92, 85],
    'calificacion_final': [9.2, 8.4, 9.9, 7.8, 8.9, 8.0],
    'estado': ['Aprobado', 'Aprobado', 'Aprobado', 'Reprobado', 'Aprobado', 'Aprobado']
}
```

**24. Actividades extracurriculares**
```python
actividades_extracurriculares = {
    'id_actividad': [501, 502, 503, 504, 505, 506],
    'nombre': ['Club de Debate', 'Equipo de Futbol', 'Taller de Robotica', 'Coro Escolar', 'Periodico Mural', 'Ajedrez'],
    'responsable': ['Mtra. Sanchez', 'Prof. Vargas', 'Ing. Flores', 'Mtra. Lopez', 'Prof. Ramirez', 'Prof. Castro'],
    'dia_semana': ['Martes', 'Lunes y Miercoles', 'Jueves', 'Viernes', 'Miercoles', 'Sabado'],
    'horario': ['15:00-17:00', '16:00-18:00', '15:00-18:00', '14:00-16:00', '13:00-14:00', '09:00-12:00'],
    'cupos_totales': [20, 25, 15, 30, 10, 12],
    'inscritos_actuales': [18, 25, 12, 28, 8, 10],
    'costo_mensual': [0, 200, 500, 0, 0, 150],
    'lugar': ['Aula 3', 'Cancha', 'Lab. Computo', 'Auditorio', 'Patio central', 'Sala de juntas'],
    'nivel_competencia': ['Interescolar', 'Estatal', 'Nacional', 'Local', 'Escolar', 'Interescolar']
}
```

---

### 🛒 Categoría 5: Comercio y Productos

**25. Productos de tienda de abarrotes**
```python
productos_abarrotes = {
    'id_producto': [1001, 1002, 1003, 1004, 1005, 1006],
    'nombre': ['Arroz 1kg', 'Frijol 1kg', 'Aceite 1L', 'Leche 1L', 'Pan de caja', 'Huevos 12pz'],
    'categoria': ['Granos', 'Granos', 'Aceites', 'Lacteos', 'Panaderia', 'Refrigerados'],
    'marca': ['Verde Valle', 'La Costena', '1-2-3', 'Lala', 'Bimbo', 'San Juan'],
    'precio_venta': [25.0, 32.0, 45.0, 28.0, 55.0, 48.0],
    'costo_compra': [18.0, 24.0, 35.0, 22.0, 45.0, 40.0],
    'stock_actual': [100, 80, 50, 60, 40, 70],
    'stock_minimo': [20, 20, 15, 20, 10, 15],
    'proveedor': ['Distribuidora Sur', 'Distribuidora Sur', 'Aceites MX', 'Lala Directo', 'Bimbo Directo', 'Granjas Unidas'],
    'fecha_caducidad': ['2025-01', '2025-03', '2024-12', '2024-02', '2024-01-25', '2024-02-10']
}
```

**26. Proveedores de la empresa**
```python
proveedores_empresa = {
    'id_proveedor': [601, 602, 603, 604, 605, 606],
    'nombre_empresa': ['Distribuidora Sur', 'Aceites MX', 'Lala Directo', 'Bimbo Directo', 'Granjas Unidas', 'Papelera Central'],
    'contacto': ['Juan Perez', 'Maria Lopez', 'Carlos Ruiz', 'Ana Garcia', 'Luis Torres', 'Sofia Diaz'],
    'telefono': ['551111', '552222', '553333', '554444', '555555', '556666'],
    'correo': ['juan@dist.com', 'maria@aceites.com', 'carlos@lala.com', 'ana@bimbo.com', 'luis@granjas.com', 'sofia@papel.com'],
    'categoria_suministro': ['Abarrotes', 'Aceites', 'Lacteos', 'Panaderia', 'Refrigerados', 'Papeleria'],
    'dias_credito': [15, 30, 15, 7, 15, 30],
    'calificacion_servicio': [9, 8, 10, 9, 7, 8],
    'compras_ultimo_mes': [15000, 8000, 12000, 20000, 9000, 3000],
    'estado': ['Activo', 'Activo', 'Activo', 'Activo', 'Suspendido', 'Activo'],
    'ciudad': ['CDMX', 'Guadalajara', 'Monterrey', 'CDMX', 'Puebla', 'CDMX']
}
```

**27. Ventas del mes**
```python
ventas_mes = {
    'id_venta': [7001, 7002, 7003, 7004, 7005, 7006],
    'fecha': ['2024-01-05', '2024-01-06', '2024-01-08', '2024-01-10', '2024-01-12', '2024-01-15'],
    'cliente': ['Ana', 'Luis', 'Sofia', 'Carlos', 'Maria', 'Jorge'],
    'producto': ['Leche 1L', 'Pan de caja', 'Aceite 1L', 'Huevos 12pz', 'Arroz 1kg', 'Frijol 1kg'],
    'cantidad': [2, 1, 3, 2, 5, 4],
    'precio_unitario': [28.0, 55.0, 45.0, 48.0, 25.0, 32.0],
    'total_venta': [56.0, 55.0, 135.0, 96.0, 125.0, 128.0],
    'metodo_pago': ['Efectivo', 'Tarjeta', 'Transferencia', 'Efectivo', 'Tarjeta', 'Efectivo'],
    'vendedor': ['Pedro', 'Laura', 'Pedro', 'Laura', 'Miguel', 'Pedro'],
    'sucursal': ['Norte', 'Sur', 'Norte', 'Centro', 'Sur', 'Norte']
}
```

**28. Clientes frecuentes**
```python
clientes_frecuentes = {
    'id_cliente': [801, 802, 803, 804, 805, 806],
    'nombre': ['Ana', 'Luis', 'Sofia', 'Carlos', 'Maria', 'Jorge'],
    'correo': ['ana@mail.com', 'luis@mail.com', 'sofia@mail.com', 'carlos@mail.com', 'maria@mail.com', 'jorge@mail.com'],
    'fecha_registro': ['2022-05-01', '2021-08-15', '2023-01-10', '2022-11-20', '2023-03-05', '2021-12-01'],
    'compras_totales': [45, 60, 30, 25, 50, 40],
    'gasto_total_acumulado': [5500, 8000, 3200, 2800, 6500, 4900],
    'puntos_fidelidad': [550, 800, 320, 280, 650, 490],
    'nivel_membresia': ['Plata', 'Oro', 'Bronce', 'Bronce', 'Plata', 'Plata'],
    'ultima_compra': ['2024-01-12', '2024-01-10', '2024-01-08', '2023-12-20', '2024-01-15', '2024-01-05'],
    'suscripcion_newsletter': [True, True, False, True, True, False]
}
```

**29. Categorías de electrodomésticos**
```python
categorias_electro = {
    'id_categoria': [901, 902, 903, 904, 905, 906],
    'nombre_categoria': ['Refrigeracion', 'Lavado', 'Cocina', 'Climatizacion', 'Entretenimiento', 'Cuidado personal'],
    'descripcion': ['Refrigeradores y congeladores', 'Lavadoras y secadoras', 'Estufas y hornos', 'Aires acondicionados', 'TVs y Audio', 'Secadoras de pelo'],
    'cantidad_productos': [15, 10, 20, 8, 25, 12],
    'margen_ganancia_promedio': [15, 12, 18, 20, 10, 25],
    'producto_mas_vendido': ['Refrigerador 200L', 'Lavadora 15kg', 'Estufa 6Q', 'Minisplit 1T', 'Smart TV 50"', 'Secadora profesional'],
    'proveedor_principal': ['Mabe', 'Whirlpool', 'Iem', 'Carrier', 'Samsung', 'Philips'],
    'garantia_estandar_meses': [12, 12, 12, 12, 12, 6],
    'requiere_instalacion': [True, True, True, True, False, False],
    'estado_categoria': ['Activa', 'Activa', 'Activa', 'Activa', 'Activa', 'Activa']
}
```

**30. Devoluciones de mercancía**
```python
devoluciones_mercancia = {
    'id_devolucion': [1001, 1002, 1003, 1004, 1005, 1006],
    'id_venta_original': [7001, 7003, 7005, 7002, 7006, 7004],
    'cliente': ['Ana', 'Sofia', 'Maria', 'Luis', 'Jorge', 'Carlos'],
    'producto': ['Leche 1L', 'Aceite 1L', 'Arroz 1kg', 'Pan de caja', 'Frijol 1kg', 'Huevos 12pz'],
    'fecha_devolucion': ['2024-01-06', '2024-01-09', '2024-01-13', '2024-01-07', '2024-01-16', '2024-01-11'],
    'motivo': ['Caducado', 'Envase roto', 'Producto equivocado', 'Sabor rancio', 'Cambio de opinion', 'Huevos rotos'],
    'monto_reembolsado': [56.0, 135.0, 125.0, 55.0, 128.0, 96.0],
    'metodo_reembolso': ['Efectivo', 'Transferencia', 'Tarjeta', 'Efectivo', 'Efectivo', 'Transferencia'],
    'estado': ['Completado', 'Completado', 'En proceso', 'Completado', 'Completado', 'En proceso'],
    'empleado_autoriza': ['Laura', 'Pedro', 'Miguel', 'Laura', 'Pedro', 'Miguel']
}
```

---

### 🌾 Categoría 6: Agricultura y Medio Ambiente

**31. Parcelas de cultivo**
```python
parcelas_cultivo = {
    'id_parcela': [101, 102, 103, 104, 105, 106],
    'nombre_parcela': ['El Mirador', 'La Esperanza', 'San Jose', 'El Roble', 'La Pradera', 'Los Pinos'],
    'hectareas': [5.5, 3.2, 8.0, 2.5, 10.0, 4.0],
    'tipo_cultivo': ['Maiz', 'Trigo', 'Maiz', 'Frijol', 'Soya', 'Trigo'],
    'fecha_siembra': ['2023-05-01', '2023-10-15', '2023-05-10', '2023-06-01', '2023-06-15', '2023-10-20'],
    'fecha_cosecha_estimada': ['2023-09-01', '2024-03-15', '2023-09-10', '2023-10-01', '2023-11-15', '2024-03-20'],
    'riego': ['Aspersión', 'Goteo', 'Aspersión', 'Temporal', 'Goteo', 'Goteo'],
    'rendimiento_estimado_ton': [22.0, 12.8, 32.0, 5.0, 30.0, 16.0],
    'trabajador_responsable': ['Juan', 'Pedro', 'Juan', 'Luis', 'Carlos', 'Pedro'],
    'estado': ['Cosechado', 'En crecimiento', 'Cosechado', 'Cosechado', 'Cosechado', 'En crecimiento']
}
```

**32. Tractores de la finca**
```python
tractores_finca = {
    'id_tractor': [201, 202, 203, 204, 205, 206],
    'marca': ['John Deere', 'Massey Ferguson', 'New Holland', 'John Deere', 'Valtra', 'Massey Ferguson'],
    'modelo': ['5075E', '4710', 'T6.145', '6120M', 'A424', '5713'],
    'ano': [2018, 2015, 2020, 2021, 2019, 2017],
    'horas_motor': [3500, 5200, 1800, 1200, 2500, 4000],
    'combustible': ['Diesel', 'Diesel', 'Diesel', 'Diesel', 'Diesel', 'Diesel'],
    'potencia_hp': [75, 100, 145, 120, 100, 110],
    'ultimo_mantenimiento': ['2023-11-01', '2023-10-15', '2023-12-01', '2024-01-05', '2023-11-20', '2023-12-10'],
    'operador_asignado': ['Juan', 'Pedro', 'Luis', 'Carlos', 'Juan', 'Pedro'],
    'estado': ['Operativo', 'En reparacion', 'Operativo', 'Operativo', 'Operativo', 'Operativo']
}
```

**33. Tipos de semillas**
```python
tipos_semillas = {
    'id_semilla': [301, 302, 303, 304, 305, 306],
    'cultivo': ['Maiz', 'Trigo', 'Frijol', 'Soya', 'Sorgo', 'Avena'],
    'variedad': ['Hibrido A', 'Trigo duro', 'Negro Jamapa', 'Transgenica B', 'Sorgo forrajero', 'Avena blanca'],
    'proveedor': ['Semillas MX', 'AgroGlobal', 'Semillas MX', 'BioTech', 'AgroGlobal', 'Semillas MX'],
    'precio_kg': [150, 80, 120, 200, 60, 70],
    'germinacion_porcentaje': [95, 90, 85, 98, 88, 92],
    'ciclo_dias': [120, 150, 90, 110, 100, 130],
    'stock_kg': [500, 300, 200, 150, 400, 250],
    'tratamiento': ['Fungicida', 'Ninguno', 'Insecticida', 'Herbicida', 'Ninguno', 'Fungicida'],
    'lote': ['L23-01', 'L23-02', 'L23-03', 'L23-04', 'L23-05', 'L23-06']
}
```

**34. Registro de plagas**
```python
registro_plagas = {
    'id_registro': [401, 402, 403, 404, 405, 406],
    'parcela': ['El Mirador', 'La Esperanza', 'San Jose', 'El Roble', 'La Pradera', 'Los Pinos'],
    'fecha_deteccion': ['2023-06-15', '2023-11-01', '2023-07-10', '2023-08-05', '2023-09-20', '2023-11-15'],
    'tipo_plaga': ['Gusano cogollero', 'Afid', 'Mosca blanca', 'Chicharrita', 'Pulgón', 'Afid'],
    'nivel_infestacion': ['Alto', 'Medio', 'Bajo', 'Medio', 'Alto', 'Bajo'],
    'area_afectada_porcentaje': [30, 15, 5, 20, 40, 10],
    'accion_tomada': ['Fumigacion', 'Control biologico', 'Monitoreo', 'Fumigacion', 'Fumigacion', 'Control biologico'],
    'producto_aplicado': ['Clorpirifos', 'Jabon potasico', 'Ninguno', 'Imidacloprid', 'Lambda-cialotrina', 'Jabon potasico'],
    'costo_control': [2500, 800, 0, 1500, 3500, 600],
    'resultado': ['Controlado', 'Controlado', 'Controlado', 'En observacion', 'Controlado', 'Controlado']
}
```

**35. Estaciones meteorológicas**
```python
estaciones_meteorologicas = {
    'id_estacion': [501, 502, 503, 504, 505, 506],
    'ubicacion': ['Norte', 'Sur', 'Este', 'Oeste', 'Centro', 'Cima'],
    'latitud': [19.4326, 19.3326, 19.5326, 19.4126, 19.4526, 19.6326],
    'longitud': [-99.1332, -99.2332, -99.0332, -99.1532, -99.1132, -99.3332],
    'temperatura_promedio_c': [22.5, 24.1, 21.8, 23.0, 22.9, 18.5],
    'humedad_promedio_porcentaje': [45, 55, 40, 50, 48, 65],
    'precipitacion_anual_mm': [600, 800, 500, 700, 650, 1200],
    'velocidad_viento_kmh': [15, 12, 18, 14, 13, 25],
    'tipo_sensor': ['Digital', 'Analogico', 'Digital', 'Digital', 'Analogico', 'Digital'],
    'ultimo_calibracion': ['2023-12-01', '2023-11-15', '2024-01-05', '2023-12-20', '2023-10-10', '2024-01-10']
}
```

**36. Trabajadores del campo**
```python
trabajadores_campo = {
    'id_trabajador': [601, 602, 603, 604, 605, 606],
    'nombre': ['Juan', 'Pedro', 'Luis', 'Carlos', 'Miguel', 'Jose'],
    'puesto': ['Capataz', 'Jornalero', 'Operador', 'Jornalero', 'Mecanico', 'Jornalero'],
    'edad': [45, 32, 28, 35, 50, 29],
    'salario_semanal': [3500, 2000, 3000, 2000, 3200, 2000],
    'parcela_asignada': ['El Mirador', 'La Esperanza', 'N/A', 'San Jose', 'N/A', 'El Roble'],
    'dias_trabajados_mes': [26, 24, 26, 22, 26, 25],
    'bono_produccion': [500, 200, 400, 150, 300, 200],
    'equipo_proteccion': [True, True, True, False, True, True],
    'fecha_ingreso': ['2015-03-01', '2020-05-15', '2019-08-10', '2021-02-20', '2010-11-05', '2022-01-10']
}
```

---

### ⚽ Categoría 7: Deportes y Fitness

**37. Jugadores de un equipo de fútbol**
```python
jugadores_futbol = {
    'id_jugador': [10, 7, 9, 1, 4, 11],
    'nombre': ['Lionel', 'Cristiano', 'Kylian', 'Alisson', 'Virgil', 'Neymar'],
    'posicion': ['Delantero', 'Delantero', 'Delantero', 'Portero', 'Defensa', 'Delantero'],
    'edad': [36, 39, 25, 31, 32, 31],
    'nacionalidad': ['Argentina', 'Portugal', 'Francia', 'Brasil', 'Holanda', 'Brasil'],
    'goles_temporada': [25, 30, 28, 0, 3, 15],
    'asistencias_temporada': [15, 8, 10, 0, 2, 12],
    'partidos_jugados': [30, 32, 29, 35, 33, 25],
    'salario_anual_millones': [50, 60, 45, 15, 20, 40],
    'lesion_actual': [False, False, True, False, False, True]
}
```

**38. Clases de un gimnasio**
```python
clases_gimnasio = {
    'id_clase': [101, 102, 103, 104, 105, 106],
    'nombre_clase': ['Spinning', 'Yoga', 'Crossfit', 'Zumba', 'Pilates', 'Boxeo'],
    'instructor': ['Ana', 'Sofia', 'Carlos', 'Laura', 'Maria', 'Pedro'],
    'dia_semana': ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado'],
    'horario': ['07:00', '09:00', '18:00', '19:00', '10:00', '11:00'],
    'duracion_minutos': [45, 60, 60, 50, 50, 60],
    'capacidad_maxima': [20, 15, 12, 25, 15, 10],
    'inscritos_promedio': [18, 12, 12, 20, 10, 8],
    'nivel': ['Intermedio', 'Principiante', 'Avanzado', 'Principiante', 'Intermedio', 'Intermedio'],
    'costo_por_clase': [100, 120, 150, 90, 130, 140]
}
```

**39. Inventario de equipamiento deportivo**
```python
equipamiento_deportivo = {
    'id_equipo': [201, 202, 203, 204, 205, 206],
    'nombre': ['Mancuernas 10kg', 'Colchoneta Yoga', 'Cuerda para saltar', 'Balon Medicinal 5kg', 'Banda elastica', 'Kettlebell 12kg'],
    'categoria': ['Pesas', 'Accesorios', 'Cardio', 'Pesas', 'Accesorios', 'Pesas'],
    'cantidad_total': [40, 30, 50, 20, 40, 25],
    'cantidad_disponible': [35, 28, 45, 18, 38, 22],
    'precio_unitario': [500, 300, 150, 600, 100, 700],
    'fecha_compra': ['2022-01-01', '2023-05-10', '2021-08-15', '2022-11-20', '2023-02-05', '2022-06-30'],
    'estado': ['Bueno', 'Excelente', 'Regular', 'Bueno', 'Excelente', 'Bueno'],
    'ubicacion': ['Sala Pesas', 'Sala Yoga', 'Recepcion', 'Sala Pesas', 'Sala Yoga', 'Sala Pesas'],
    'vida_util_estimada_meses': [60, 24, 12, 36, 18, 48]
}
```

**40. Entrenadores personales**
```python
entrenadores_personales = {
    'id_entrenador': [301, 302, 303, 304, 305, 306],
    'nombre': ['Carlos', 'Ana', 'Luis', 'Maria', 'Pedro', 'Sofia'],
    'especialidad': ['Hipertrofia', 'Perdida de peso', 'Funcional', 'Rehabilitacion', 'Fuerza', 'Yoga'],
    'certificacion': ['ISSA', 'ACE', 'NSCA', 'Fisioterapia', 'CSCS', 'RYT-200'],
    'anos_experiencia': [5, 8, 3, 10, 7, 4],
    'clientes_activos': [15, 20, 10, 8, 12, 18],
    'tarifa_por_hora': [400, 450, 350, 600, 500, 380],
    'calificacion_promedio': [4.8, 4.9, 4.5, 5.0, 4.7, 4.6],
    'horario_disponible': ['Matutino', 'Completo', 'Vespertino', 'Matutino', 'Completo', 'Vespertino'],
    'idiomas': ['Espanol', 'Espanol, Ingles', 'Espanol', 'Espanol', 'Espanol', 'Espanol, Portugues']
}
```

**41. Torneos locales**
```python
torneos_locales = {
    'id_torneo': [401, 402, 403, 404, 405, 406],
    'nombre': ['Copa Primavera', 'Liga de Verano', 'Torneo Relampago', 'Maraton Ciudad', 'Torneo de Tenis', 'Copa Invierno'],
    'deporte': ['Futbol', 'Futbol', 'Futbol', 'Atletismo', 'Tenis', 'Basquetbol'],
    'fecha_inicio': ['2024-03-01', '2024-06-01', '2024-04-15', '2024-09-01', '2024-05-10', '2024-11-01'],
    'fecha_fin': ['2024-05-30', '2024-08-30', '2024-04-16', '2024-09-01', '2024-05-15', '2024-12-30'],
    'equipos_participantes': [16, 20, 8, 500, 32, 12],
    'cuota_inscripcion': [1500, 2000, 800, 300, 500, 1200],
    'premio_primer_lugar': [10000, 15000, 3000, 5000, 4000, 8000],
    'sede': ['Deportivo Norte', 'Deportivo Sur', 'Cancha Municipal', 'Paseo Principal', 'Club Tenis', 'Gimnasio Central'],
    'estado': ['Inscripcion', 'Planificacion', 'Inscripcion', 'Planificacion', 'Inscripcion', 'Planificacion']
}
```

**42. Rutinas de nutrición**
```python
rutinas_nutricion = {
    'id_plan': [501, 502, 503, 504, 505, 506],
    'nombre_plan': ['Definicion', 'Volumen', 'Mantenimiento', 'Vegano', 'Keto', 'Deportista'],
    'calorias_diarias': [1800, 3000, 2200, 2000, 1600, 2800],
    'proteinas_gramos': [150, 200, 120, 80, 120, 180],
    'carbohidratos_gramos': [150, 350, 250, 250, 50, 300],
    'grasas_gramos': [60, 80, 70, 70, 120, 90],
    'comidas_por_dia': [5, 6, 4, 4, 4, 5],
    'costo_semanal_estimado': [800, 1200, 900, 1000, 1100, 1300],
    'dificultad_preparacion': ['Media', 'Alta', 'Baja', 'Media', 'Alta', 'Alta'],
    'aprobado_por_nutriologo': [True, True, True, True, True, True]
}
```

---

### 🏦 Categoría 8: Finanzas y Banca

**43. Cuentas de ahorro**
```python
cuentas_ahorro = {
    'numero_cuenta': [1111, 2222, 3333, 4444, 5555, 6666],
    'titular': ['Ana', 'Luis', 'Sofia', 'Carlos', 'Maria', 'Jorge'],
    'fecha_apertura': ['2020-01-15', '2019-05-20', '2021-08-10', '2022-03-05', '2018-11-30', '2023-02-14'],
    'saldo_actual': [45000, 120000, 15000, 80000, 200000, 5000],
    'tasa_interes_anual': [5.5, 6.0, 5.0, 6.5, 7.0, 4.5],
    'movimientos_mes': [12, 8, 15, 5, 20, 25],
    'tipo_cuenta': ['Digital', 'Tradicional', 'Digital', 'Premium', 'Premium', 'Basica'],
    'estado': ['Activa', 'Activa', 'Activa', 'Activa', 'Activa', 'Bloqueada'],
    'tarjeta_debito': [True, True, True, True, True, False],
    'banco': ['Banamex', 'BBVA', 'Santander', 'Banamex', 'BBVA', 'Santander']
}
```

**44. Asesores financieros**
```python
asesores_financieros = {
    'id_asesor': [701, 702, 703, 704, 705, 706],
    'nombre': ['Roberto', 'Laura', 'Miguel', 'Carmen', 'Diego', 'Valeria'],
    'especialidad': ['Retiro', 'Inversiones', 'Credito', 'Seguros', 'Fiscal', 'Empresarial'],
    'anos_experiencia': [10, 5, 8, 15, 3, 7],
    'clientes_asignados': [50, 30, 45, 60, 20, 35],
    'activo_bajo_gestion_millones': [150, 80, 120, 200, 40, 90],
    'comision_mensual_promedio': [25000, 15000, 20000, 35000, 8000, 18000],
    'certificacion_cnbv': [True, True, True, True, False, True],
    'sucursal': ['Centro', 'Norte', 'Sur', 'Centro', 'Poniente', 'Norte'],
    'evaluacion_desempeno': [95, 88, 90, 98, 82, 89]
}
```

**45. Préstamos aprobados**
```python
prestamos_aprobados = {
    'id_prestamo': [8001, 8002, 8003, 8004, 8005, 8006],
    'cliente': ['Ana', 'Luis', 'Sofia', 'Carlos', 'Maria', 'Jorge'],
    'tipo_prestamo': ['Personal', 'Hipotecario', 'Automotriz', 'Personal', 'Hipotecario', 'Estudiantil'],
    'monto_solicitado': [50000, 1500000, 300000, 30000, 2000000, 100000],
    'monto_aprobado': [50000, 1500000, 280000, 30000, 2000000, 100000],
    'plazo_meses': [24, 240, 60, 12, 300, 48],
    'tasa_interes_mensual': [2.5, 0.8, 1.2, 3.0, 0.8, 1.5],
    'pago_mensual_estimado': [2650, 13500, 6500, 2900, 18000, 2800],
    'fecha_desembolso': ['2024-01-10', '2023-06-15', '2023-11-20', '2024-01-05', '2022-08-01', '2023-09-10'],
    'estatus': ['Al corriente', 'Al corriente', 'Atrasado', 'Al corriente', 'Al corriente', 'Al corriente']
}
```

**46. Tarjetas de crédito**
```python
tarjetas_credito = {
    'id_tarjeta': [901, 902, 903, 904, 905, 906],
    'titular': ['Ana', 'Luis', 'Sofia', 'Carlos', 'Maria', 'Jorge'],
    'tipo_tarjeta': ['Oro', 'Platino', 'Clasica', 'Black', 'Oro', 'Clasica'],
    'limite_credito': [100000, 250000, 50000, 500000, 150000, 40000],
    'saldo_utilizado': [25000, 180000, 10000, 120000, 50000, 35000],
    'disponible': [75000, 70000, 40000, 380000, 100000, 5000],
    'fecha_corte': [5, 12, 20, 8, 15, 25],
    'fecha_pago': [15, 22, 30, 18, 25, 5],
    'puntos_acumulados': [2500, 18000, 1000, 12000, 5000, 3500],
    'estado': ['Activa', 'Activa', 'Activa', 'Activa', 'Activa', 'Bloqueada']
}
```

**47. Inversiones en bolsa**
```python
inversiones_bolsa = {
    'id_inversion': [101, 102, 103, 104, 105, 106],
    'cliente': ['Ana', 'Luis', 'Sofia', 'Carlos', 'Maria', 'Jorge'],
    'ticker': ['AAPL', 'TSLA', 'AMZN', 'MSFT', 'GOOGL', 'META'],
    'nombre_empresa': ['Apple', 'Tesla', 'Amazon', 'Microsoft', 'Google', 'Meta'],
    'cantidad_acciones': [10, 5, 8, 15, 12, 6],
    'precio_compra': [150, 200, 130, 250, 120, 180],
    'precio_actual': [180, 220, 150, 300, 140, 200],
    'inversion_inicial': [1500, 1000, 1040, 3750, 1440, 1080],
    'valor_actual': [1800, 1100, 1200, 4500, 1680, 1200],
    'rendimiento_porcentaje': [20.0, 10.0, 15.3, 20.0, 16.6, 11.1]
}
```

**48. Sucursales bancarias**
```python
sucursales_bancarias = {
    'id_sucursal': [201, 202, 203, 204, 205, 206],
    'nombre_sucursal': ['Centro Historico', 'Polanco', 'Santa Fe', 'Del Valle', 'Coyoacan', 'Reforma'],
    'gerente': ['Sr. Lopez', 'Sra. Diaz', 'Sr. Ramirez', 'Sra. Torres', 'Sr. Gomez', 'Sra. Vargas'],
    'empleados': [25, 35, 40, 20, 18, 30],
    'cajeros_automaticos': [4, 6, 8, 3, 2, 5],
    'clientes_activos': [5000, 12000, 15000, 4000, 3500, 10000],
    'captacion_mensual_millones': [50, 150, 200, 40, 35, 120],
    'ano_apertura': [1995, 2005, 2015, 1980, 1985, 2010],
    'horario_atencion': ['9:00-16:00', '9:00-19:00', '9:00-19:00', '9:00-16:00', '9:00-16:00', '9:00-19:00'],
    'calificacion_servicio': [4.2, 4.5, 4.7, 4.0, 3.9, 4.6]
}
```

---

### 🚚 Categoría 9: Logística y Transporte

**49. Paquetería en tránsito**
```python
paqueteria_transito = {
    'id_guia': [111, 222, 333, 444, 555, 666],
    'remitente': ['Tienda A', 'Empresa B', 'Startup C', 'Tienda A', 'Particular', 'Empresa B'],
    'destinatario': ['Juan', 'Maria', 'Pedro', 'Ana', 'Luis', 'Sofia'],
    'origen': ['CDMX', 'Guadalajara', 'Monterrey', 'CDMX', 'Puebla', 'Guadalajara'],
    'destino': ['Puebla', 'CDMX', 'CDMX', 'Monterrey', 'CDMX', 'Monterrey'],
    'peso_kg': [2.5, 15.0, 1.2, 5.0, 0.5, 10.0],
    'fecha_envio': ['2024-01-10', '2024-01-08', '2024-01-11', '2024-01-09', '2024-01-12', '2024-01-07'],
    'fecha_entrega_estimada': ['2024-01-12', '2024-01-10', '2024-01-13', '2024-01-11', '2024-01-13', '2024-01-09'],
    'costo_envio': [150, 450, 120, 250, 90, 350],
    'estatus': ['En transito', 'Entregado', 'En transito', 'En transito', 'En reparto', 'Entregado']
}
```

**50. Choferes de la flota**
```python
choferes_flota = {
    'id_chofer': [301, 302, 303, 304, 305, 306],
    'nombre': ['Roberto', 'Luis', 'Carlos', 'Fernando', 'Jorge', 'Miguel'],
    'tipo_licencia': ['Tipo C', 'Tipo C', 'Tipo B', 'Tipo C', 'Tipo B', 'Tipo C'],
    'anos_experiencia': [15, 8, 12, 5, 20, 10],
    'salario_base': [18000, 16000, 15000, 14000, 20000, 17000],
    'bono_por_kilometro': [0.5, 0.5, 0.4, 0.4, 0.6, 0.5],
    'kilometros_mes': [4000, 3500, 3000, 2500, 5000, 3800],
    'infracciones_ano': [0, 1, 0, 2, 0, 1],
    'calificacion_cliente': [4.8, 4.5, 4.9, 4.2, 5.0, 4.6],
    'ruta_asignada': ['Norte', 'Sur', 'Este', 'Oeste', 'Foranea', 'Norte']
}
```

**51. Rutas de entrega**
```python
rutas_entrega = {
    'id_ruta': [401, 402, 403, 404, 405, 406],
    'nombre_ruta': ['Ruta Norte A', 'Ruta Sur B', 'Ruta Centro', 'Ruta Foranea 1', 'Ruta Express', 'Ruta Oeste'],
    'distancia_km': [45, 60, 25, 150, 30, 50],
    'tiempo_estimado_horas': [2.5, 3.5, 1.5, 5.0, 1.0, 2.8],
    'paradas_totales': [15, 20, 10, 5, 8, 18],
    'chofer_asignado': ['Roberto', 'Luis', 'Carlos', 'Fernando', 'Jorge', 'Miguel'],
    'vehiculo_asignado': ['V-01', 'V-02', 'V-03', 'V-04', 'V-05', 'V-06'],
    'combustible_estimado_l': [10, 15, 6, 40, 7, 12],
    'peajes': [0, 50, 0, 150, 0, 30],
    'eficiencia_entrega_porcentaje': [95, 88, 100, 80, 98, 90]
}
```

**52. Almacenes de distribución**
```python
almacenes_distribucion = {
    'id_almacen': [501, 502, 503, 504, 505, 506],
    'nombre': ['CEDIS Norte', 'CEDIS Sur', 'Hub Centro', 'Almacen Foraneo', 'Mini Hub Express', 'CEDIS Oeste'],
    'ubicacion': ['Tlalnepantla', 'Tlalpan', 'Doctores', 'Puebla', 'Roma', 'Naucalpan'],
    'area_m2': [5000, 8000, 2000, 10000, 1000, 6000],
    'capacidad_pallets': [2000, 3500, 800, 5000, 400, 2500],
    'ocupacion_actual_porcentaje': [85, 70, 95, 60, 90, 75],
    'empleados': [30, 45, 15, 60, 8, 35],
    'gerente': ['Ana', 'Luis', 'Sofia', 'Carlos', 'Maria', 'Jorge'],
    'sistema_inventario': ['WMS Pro', 'WMS Pro', 'Excel', 'WMS Pro', 'Manual', 'WMS Pro'],
    'ultima_auditoria': ['2023-12-01', '2023-11-15', '2024-01-05', '2023-10-20', '2023-12-10', '2023-11-30']
}
```

**53. Vehículos de carga**
```python
vehiculos_carga = {
    'id_vehiculo': [601, 602, 603, 604, 605, 606],
    'placa': ['ABC-123', 'DEF-456', 'GHI-789', 'JKL-012', 'MNO-345', 'PQR-678'],
    'tipo': ['Torton', 'Tractocamion', 'Van', 'Tractocamion', 'Motocicleta', 'Torton'],
    'marca': ['Freightliner', 'Kenworth', 'Ford', 'Volvo', 'Italika', 'Isuzu'],
    'ano': [2018, 2020, 2021, 2019, 2022, 2017],
    'capacidad_toneladas': [14, 30, 1.5, 30, 0.1, 7],
    'kilometraje_actual': [150000, 200000, 45000, 250000, 10000, 180000],
    'proximo_servicio_km': [155000, 210000, 50000, 260000, 15000, 185000],
    'estado': ['Operativo', 'Operativo', 'Operativo', 'En taller', 'Operativo', 'Operativo'],
    'seguro_vigente': [True, True, True, True, True, False]
}
```

**54. Incidencias en la entrega**
```python
incidencias_entrega = {
    'id_incidencia': [701, 702, 703, 704, 705, 706],
    'id_guia': [111, 333, 555, 222, 666, 444],
    'fecha': ['2024-01-11', '2024-01-12', '2024-01-12', '2024-01-09', '2024-01-08', '2024-01-10'],
    'tipo_incidencia': ['Direccion incorrecta', 'Retraso por clima', 'Cliente ausente', 'Paquete danado', 'Entregado a vecino', 'Retraso trafico'],
    'gravedad': ['Media', 'Alta', 'Baja', 'Alta', 'Baja', 'Media'],
    'responsable': ['Chofer', 'Externo', 'Cliente', 'Almacen', 'Chofer', 'Externo'],
    'accion_correctiva': ['Reprogramar', 'Reprogramar', 'Dejar aviso', 'Reemplazo', 'Validar con cliente', 'Monitoreo'],
    'costo_extra': [0, 0, 0, 500, 0, 0],
    'tiempo_retraso_horas': [24, 48, 24, 0, 0, 4],
    'resuelta': [True, False, True, True, True, True]
}
```

---

### 🎬 Categoría 10: Entretenimiento y Medios

**55. Películas en un catálogo**
```python
peliculas_catalogo = {
    'id_pelicula': [101, 102, 103, 104, 105, 106],
    'titulo': ['Inception', 'The Matrix', 'Interstellar', 'Parasite', 'Avengers', 'Joker'],
    'director': ['C. Nolan', 'L. Wachowski', 'C. Nolan', 'B. Joon-ho', 'J. Whedon', 'T. Phillips'],
    'ano_estreno': [2010, 1999, 2014, 2019, 2012, 2019],
    'genero': ['Ciencia ficcion', 'Ciencia ficcion', 'Ciencia ficcion', 'Drama', 'Accion', 'Drama'],
    'duracion_minutos': [148, 136, 169, 132, 143, 122],
    'calificacion_imdb': [8.8, 8.7, 8.6, 8.5, 8.0, 8.4],
    'recaudacion_millones': [836, 463, 701, 263, 1518, 1074],
    'idioma_original': ['Ingles', 'Ingles', 'Ingles', 'Coreano', 'Ingles', 'Ingles'],
    'disponible_streaming': [True, True, True, True, True, True]
}
```

**56. Suscriptores de streaming**
```python
suscriptores_streaming = {
    'id_usuario': [801, 802, 803, 804, 805, 806],
    'nombre': ['Ana', 'Luis', 'Sofia', 'Carlos', 'Maria', 'Jorge'],
    'plan': ['Basico', 'Estandar', 'Premium', 'Basico', 'Premium', 'Estandar'],
    'fecha_inicio': ['2022-01-01', '2021-05-15', '2023-03-10', '2022-08-20', '2020-11-05', '2023-01-10'],
    'pago_mensual': [139, 199, 299, 139, 299, 199],
    'horas_vistas_mes': [15, 30, 45, 10, 50, 25],
    'dispositivos_registrados': [2, 3, 4, 1, 4, 2],
    'metodo_pago': ['Tarjeta', 'PayPal', 'Tarjeta', 'Transferencia', 'Tarjeta', 'PayPal'],
    'renovacion_automatica': [True, True, True, False, True, True],
    'estado': ['Activo', 'Activo', 'Activo', 'Cancelado', 'Activo', 'Activo']
}
```

**57. Eventos en un teatro**
```python
eventos_teatro = {
    'id_evento': [901, 902, 903, 904, 905, 906],
    'nombre': ['El Fantasma', 'Romeo y Julieta', 'Concierto Sinfonico', 'Stand Up Comedy', 'Ballet Clasico', 'Obra Infantil'],
    'tipo': ['Musical', 'Teatro', 'Musica', 'Comedia', 'Danza', 'Infantil'],
    'fecha': ['2024-02-14', '2024-03-01', '2024-02-20', '2024-02-25', '2024-03-10', '2024-03-15'],
    'hora': ['20:00', '19:00', '20:30', '21:00', '18:00', '12:00'],
    'capacidad_total': [500, 300, 600, 200, 400, 250],
    'boletos_vendidos': [450, 280, 550, 190, 350, 240],
    'precio_boleto': [500, 350, 600, 250, 450, 200],
    'recaudacion_estimada': [225000, 98000, 330000, 47500, 157500, 48000],
    'estado': ['Agotandose', 'Disponible', 'Agotandose', 'Ultimos lugares', 'Disponible', 'Disponible']
}
```

**58. Videojuegos en una tienda**
```python
videojuegos_tienda = {
    'id_juego': [1001, 1002, 1003, 1004, 1005, 1006],
    'titulo': ['Zelda TOTK', 'Mario Wonder', 'Spider-Man 2', 'Hogwarts Legacy', 'FIFA 24', 'Minecraft'],
    'plataforma': ['Switch', 'Switch', 'PS5', 'Multiplataforma', 'Multiplataforma', 'Multiplataforma'],
    'genero': ['Aventuras', 'Plataformas', 'Accion', 'RPG', 'Deportes', 'Sandbox'],
    'precio': [1200, 1100, 1400, 1300, 1500, 700],
    'stock': [20, 15, 10, 25, 30, 50],
    'ventas_mes': [40, 35, 50, 30, 60, 80],
    'calificacion_metacritic': [96, 90, 91, 84, 78, 93],
    'clasificacion_edad': ['E10+', 'E', 'T', 'T', 'E', 'E10+'],
    'desarrollador': ['Nintendo', 'Nintendo', 'Insomniac', 'Avalanche', 'EA Sports', 'Mojang']
}
```

**59. Artistas de una discográfica**
```python
artistas_discografica = {
    'id_artista': [201, 202, 203, 204, 205, 206],
    'nombre': ['Shakira', 'Bad Bunny', 'Taylor Swift', 'The Weeknd', 'Rosalía', 'Peso Pluma'],
    'genero': ['Pop Latino', 'Reggaeton', 'Pop', 'R&B', 'Flamenco Pop', 'Regional Mexicano'],
    'ano_debut': [1995, 2016, 2006, 2011, 2013, 2020],
    'albumes_publicados': [11, 5, 10, 5, 3, 2],
    'seguidores_millones': [80, 65, 90, 50, 30, 25],
    'regalias_anuales_millones': [15, 20, 30, 18, 8, 12],
    'contrato_vigente': [True, True, True, True, True, True],
    'proximo_tour': ['2024-05', '2024-03', '2024-06', '2024-04', '2024-07', '2024-02'],
    'manager': ['Juan M.', 'Noah A.', 'Tree P.', 'Wassim S.', 'Carlos G.', 'George P.']
}
```

**60. Episodios de una serie**
```python
episodios_serie = {
    'id_episodio': [1, 2, 3, 4, 5, 6],
    'titulo': ['El Comienzo', 'La Revelacion', 'El Conflicto', 'La Traicion', 'El Sacrificio', 'El Final'],
    'temporada': [1, 1, 1, 1, 1, 1],
    'numero_episodio': [1, 2, 3, 4, 5, 6],
    'duracion_minutos': [45, 42, 48, 50, 55, 65],
    'director': ['Ana G.', 'Luis R.', 'Ana G.', 'Carlos M.', 'Sofia L.', 'Ana G.'],
    'fecha_estreno': ['2023-01-01', '2023-01-08', '2023-01-15', '2023-01-22', '2023-01-29', '2023-02-05'],
    'audiencia_millones': [5.0, 4.8, 5.2, 6.0, 7.5, 10.0],
    'calificacion_imdb': [8.5, 8.3, 8.6, 8.8, 9.2, 9.5],
    'presupuesto_miles': [2000, 2000, 2200, 2500, 3000, 4000]
}
```

---

### 💡 Consejo Didáctico para el Docente:
Puedes pedir a tus alumnos que **elijan aleatoriamente 3 números del 1 al 60** y que, sin ver el código, intenten deducir qué tipo de análisis (Pandas) o gráfica (Matplotlib) sería más útil para ese conjunto de datos específico. Por ejemplo:
- Para el **#47 (Inversiones)**: Un diagrama de dispersión (`scatter`) entre `precio_compra` y `precio_actual`.
- Para el **#51 (Rutas)**: Un `boxplot` de los `tiempo_estimado_horas` por `chofer_asignado`.
- Para el **#1 (Pacientes)**: Un histograma de la `edad` o un conteo de `tipo_sangre`.

¡Espero que este banco de 60 ejemplos sea de gran utilidad para tus clases! Si necesitas que alguno se expanda o modifique, solo dímelo.
