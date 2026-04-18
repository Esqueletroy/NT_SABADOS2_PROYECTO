usuarios = []

def registrar_usuario(nombre, correo, contraseña):
    for u in usuarios:
        if u["correo"] == correo:
            return "❌ Correo ya registrado"
    usuarios.append({"nombre": nombre, "correo": correo, "contraseña": contraseña})
    return "✅ Registro exitoso"

def iniciar_sesion(correo, contraseña):
    for u in usuarios:
        if u["correo"] == correo and u["contraseña"] == contraseña:
            return True
    return False
