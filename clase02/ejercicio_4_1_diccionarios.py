"""Ejercicio 4.1: Creación, acceso y actualización de diccionarios."""

info_libro = {
    "titulo": "Cien años de soledad",
    "autor": "Gabriel García Márquez",
    "año": 1967,
}

print("Autor:", info_libro["autor"])

info_libro["paginas"] = 417  # Inserción de nueva clave
info_libro["año"] = 1970  # Actualización de clave existente
print("Diccionario actualizado:", info_libro)
