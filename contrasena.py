from utilidades import comprobar_numero


def comprobar_longitud(contrasena):
    return len(contrasena) >= 10


def comprobar_mayuscula(contrasena):
    for caracter in contrasena:
        if caracter.isupper():
            return True
    return False


contrasena = "Hola1234"
print(contrasena)
print("Longitud correcta:", comprobar_longitud(contrasena))
print("Contiene números:", comprobar_numero(contrasena))
print("Contiene mayúsculas:", comprobar_mayuscula(contrasena))

# Pruebas
print("Prueba 'Hola' (4):", comprobar_longitud("Hola"))
print("Prueba 'Hola12345' (9):", comprobar_longitud("Hola12345"))
print("Prueba números 'abc123':", comprobar_numero("abc123"))
print("Prueba números 'abcdef':", comprobar_numero("abcdef"))
print("Prueba mayúsculas 'Hola1234':", comprobar_mayuscula("Hola1234"))
print("Prueba mayúsculas 'hola1234':", comprobar_mayuscula("hola1234"))
