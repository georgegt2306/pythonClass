"""Ejercicio 1.1: Creación, reglas de nombrado e inspección de variables."""

# 1. Definición de variables básicas (snake_case)
nombre = "Laura"
edad = 28
altura = 1.68
es_estudiante = True

# 2. Inspección de valor y tipo de objeto
print(nombre, "->", type(nombre))
print(edad, "->", type(edad))
print(altura, "->", type(altura))
print(es_estudiante, "->", type(es_estudiante))

# 3. Comprobación en el espacio de nombres activo
print(dir())
