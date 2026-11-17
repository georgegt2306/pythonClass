"""Ejercicio 4.3: Combinación de DataFrames (pd.concat y pd.merge)."""

import pandas as pd

# DataFrame base (el mismo del ejercicio 4.2)
datos_empleados = {
    "ID": [101, 102, 103, 104],
    "Nombre": ["Ana", "Luis", "Marta", "Carlos"],
    "Departamento": ["Ventas", "IT", "Ventas", "Marketing"],
    "Ciudad": ["Madrid", "Valencia", "Madrid", "Sevilla"],
    "Salario": [50000, 65000, 52000, 48000],
}
df_empleados = pd.DataFrame(datos_empleados)

# 1. Concatenación vertical de filas (ignore_index=True regenera el índice)
df_nuevo = pd.DataFrame(
    {
        "ID": [105],
        "Nombre": ["Elena"],
        "Departamento": ["BI"],
        "Ciudad": ["Bilbao"],
        "Salario": [58000],
    }
)
df_total = pd.concat([df_empleados, df_nuevo], ignore_index=True)
print("Concatenación (con Elena):")
print(df_total)

# 2. Unión relacional (JOIN) por clave común 'ID'
df_proyectos = pd.DataFrame(
    {
        "ID": [101, 103, 106],
        "Proyecto": ["IA Generativa", "ETL Cloud", "Data Lake"],
    }
)
df_inner = pd.merge(df_empleados, df_proyectos, on="ID", how="inner")
df_left = pd.merge(df_empleados, df_proyectos, on="ID", how="left")

print("\nMerge how='inner' (solo IDs en ambas tablas: 101 y 103):")
print(df_inner)
print("\nMerge how='left' (todos los empleados, NaN sin proyecto: 102 y 104):")
print(df_left)
