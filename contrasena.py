def comprobar_longitud(contrasena):
    return len(contrasena) >= 8


contrasena = "Hola1234"
print(contrasena)
print("Longitud correcta:", comprobar_longitud(contrasena))

# Pruebas
print("Prueba 'Hola' (4):", comprobar_longitud("Hola"))
print("Prueba 'Hola12345' (9):", comprobar_longitud("Hola12345"))
