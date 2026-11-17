"""Ejercicio 3.1: Listas (modificación in-place, indexación y slicing)."""

frutas = ["manzana", "banana", "cereza", "dátil"]
print("Tercer elemento:", frutas[2], "| Último:", frutas[-1])

# Modificaciones in-place
frutas.append("mango")
frutas.insert(1, "pera")
eliminado = frutas.pop(2)
print("Lista actualizada:", frutas, "| Extraído:", eliminado)

# Slicing: índice 1 (2º elem.) hasta índice 4 exclusivo (4º elem.)
numeros = [10, 20, 30, 40, 50, 60]
sub_lista_a = numeros[1:4]
print("Sublista:", sub_lista_a)
