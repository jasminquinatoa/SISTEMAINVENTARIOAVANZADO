"""
Archivo principal del sistema.
Aquí se encuentra el menú interactivo en consola.
"""

from servicios.inventario import Inventario
from modelo.producto import Producto


def menu():
    inventario = Inventario()
    inventario.cargar_desde_archivo()

    while True:
        print("\n========== SISTEMA AVANZADO DE INVENTARIO ==========")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Guardar inventario")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_p = input("ID del producto: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))

            producto = Producto(id_p, nombre, cantidad, precio)
            inventario.agregar_producto(producto)

        elif opcion == "2":
            id_p = input("Ingrese ID a eliminar: ")
            inventario.eliminar_producto(id_p)

        elif opcion == "3":
            id_p = input("ID del producto: ")
            cantidad = int(input("Nueva cantidad: "))
            precio = float(input("Nuevo precio: "))
            inventario.actualizar_producto(id_p, cantidad, precio)

        elif opcion == "4":
            nombre = input("Nombre a buscar: ")
            resultados = inventario.buscar_por_nombre(nombre)

            if resultados:
                for producto in resultados:
                    print(producto)
            else:
                print("No se encontraron productos con ese nombre.")

        elif opcion == "5":
            inventario.mostrar_todos()

        elif opcion == "6":
            inventario.guardar_en_archivo()

        elif opcion == "7":
            inventario.guardar_en_archivo()
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida.")


if __name__ == "__main__":
    menu()