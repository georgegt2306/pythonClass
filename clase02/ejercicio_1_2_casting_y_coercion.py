"""Ejercicio 1.2: Conversión de tipos (casting explícito y coerción implícita)."""

# 1. Casting explícito de str a int
codigo_str = "105"
codigo_int = int(codigo_str) + 5
print("Código numérico:", codigo_int, type(codigo_int))

# 2. Coerción implícita (int + float -> float)
entero = 10
resultado = entero + 2.5
print("Resultado:", resultado, type(resultado))
