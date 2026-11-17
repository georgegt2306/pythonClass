"""Ejercicio 3.2: Tuplas y cadenas de texto (secuencias inmutables)."""

# 1. Operaciones sobre tupla inmutable
datos = (1, 5, 2, 5, 8, 5, 3)
print("Apariciones del 5:", datos.count(5))
print("Longitud:", len(datos), "| Mín:", min(datos), "| Máx:", max(datos))

# 2. Limpieza, tokenización y slicing de cadenas
texto = " Programar en Python es divertido "
texto_limpio = texto.strip()
texto_lista = texto_limpio.split()
print("Lista de palabras:", texto_lista)
print("Slicing sobre texto:", texto_limpio[13:19], "| Desde lista:", texto_lista[2])
