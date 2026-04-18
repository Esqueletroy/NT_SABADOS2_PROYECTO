from modulos.usuarios import registrar_usuario, iniciar_sesion
from modulos.productos import listar_productos
from modulos.carrito import agregar_producto, ver_carrito

def menu():
    while True:
        print("\n=== SISTEMA ===")
        print("1. Registrar")
        print("2. Login")
        print("3. Ver productos")
        print("4. Ver carrito")
        print("0. Salir")

        op = input("Opción: ")

        if op == "1":
            print(registrar_usuario(
                input("Nombre: "),
                input("Correo: "),
                input("Contraseña: ")
            ))

        elif op == "2":
            if iniciar_sesion(input("Correo: "), input("Contraseña: ")):
                print("✅ Login exitoso")
            else:
                print("❌ Error en credenciales")

        elif op == "3":
            productos = listar_productos()
            print(productos)

        elif op == "4":
            print(ver_carrito())

        elif op == "0":
            break

if __name__ == "__main__":
    menu()
