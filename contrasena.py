def comprobar_longitud(contrasena):
    return len(contrasena) >= 8


def comprobar_mayuscula(contrasena):
    for caracter in contrasena:
        if caracter.isupper():
            return True
    return False


contrasena = "Hola1234"
print(contrasena)
print("Contiene mayúsculas:", comprobar_mayuscula(contrasena))
print("Longitud correcta:", comprobar_longitud(contrasena))

# Pruebas
print("Prueba 'Hola' (4):", comprobar_longitud("Hola"))
print("Prueba mayúsculas 'Hola1234':", comprobar_mayuscula("Hola1234"))
print("Prueba mayúsculas 'hola1234':", comprobar_mayuscula("hola1234"))
print("Prueba 'Hola12345' (9):", comprobar_longitud("Hola12345"))
