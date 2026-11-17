from utilidades import comprobar_numero


def comprobar_longitud(contrasena):
    return len(contrasena) >= 8


contrasena = "Hola1234"
print(contrasena)
print("Longitud correcta:", comprobar_longitud(contrasena))
print("Contiene números:", comprobar_numero(contrasena))

# Pruebas
print("Prueba 'Hola' (4):", comprobar_longitud("Hola"))
print("Prueba 'Hola12345' (9):", comprobar_longitud("Hola12345"))
print("Prueba números 'abc123':", comprobar_numero("abc123"))
print("Prueba números 'abcdef':", comprobar_numero("abcdef"))
