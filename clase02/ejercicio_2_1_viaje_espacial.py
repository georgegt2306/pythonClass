"""Ejercicio 2.1: Simulación de viaje espacial (operadores y funciones matemáticas)."""

import math

# Fase 1: Definición de parámetros
distancia = 384400  # int (km)
velocidad = 28000.5  # float (km/h)
dias_mision = 7  # int

# Fase 2: División, redondeo y raíz cuadrada
tiempo_viaje = distancia / velocidad
print("Tiempo estimado (h):", round(tiempo_viaje, 1))
print("Raíz cuadrada de la distancia:", round(math.sqrt(distancia), 2))
