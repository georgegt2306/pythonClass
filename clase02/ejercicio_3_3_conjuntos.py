"""Ejercicio 3.3: Conjuntos (set) y eliminación de duplicados."""

numeros_duplicados = [1, 2, 2, 3, 4, 4, 4]
numeros_set = set(numeros_duplicados)  # Elimina duplicados automáticamente
numeros_set.add(5)
numeros_set.remove(2)
print("Conjunto resultante:", numeros_set)
