"""Ejercicio 4.2: Creación de DataFrame, selección (.iloc) y filtrado (.isin)."""

import pandas as pd

datos_empleados = {
    "ID": [101, 102, 103, 104],
    "Nombre": ["Ana", "Luis", "Marta", "Carlos"],
    "Departamento": ["Ventas", "IT", "Ventas", "Marketing"],
    "Ciudad": ["Madrid", "Valencia", "Madrid", "Sevilla"],
    "Salario": [50000, 65000, 52000, 48000],
}
df_empleados = pd.DataFrame(datos_empleados)

# 2. Columnas y acceso por corchetes
print("Columnas:", df_empleados.columns)
print(df_empleados["Salario"])

# 3. Indexación posicional (2 primeras filas x 3 primeras columnas)
print(df_empleados.iloc[0:2, 0:3])

# 4. Filtrado condicional y pertenencia (.isin)
df_ventas = df_empleados[df_empleados["Departamento"] == "Ventas"]
df_ciudades = df_empleados[df_empleados["Ciudad"].isin(["Madrid", "Sevilla"])]
print("\nEmpleados de Ventas:")
print(df_ventas)
print("\nEmpleados en Madrid o Sevilla:")
print(df_ciudades)
