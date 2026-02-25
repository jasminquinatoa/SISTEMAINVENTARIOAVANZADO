"""
Archivo: inventario.py
Descripción:
Esta clase se encarga de gestionar todos los productos del inventario.

Aquí utilizo:
- Diccionario como estructura principal (búsqueda rápida por ID)
- Lista para búsquedas por nombre
- JSON para almacenamiento persistente
"""

import json
from modelo.producto import Producto


class Inventario:
    """
    Clase que administra el inventario completo.
    """

    def __init__(self):
        # Diccionario donde:
        # clave = ID del producto
        # valor = objeto Producto
        self.productos = {}

    # ======================================
    # MÉTODOS PRINCIPALES DEL INVENTARIO
    # ======================================

    def agregar_producto(self, producto):
        """
        Agrega un nuevo producto al inventario.
        """
        if producto.get_id() in self.productos:
            print("⚠ Ya existe un producto con ese ID.")
        else:
            self.productos[producto.get_id()] = producto
            print("Producto agregado correctamente.")

    def eliminar_producto(self, id_producto):
        """
        Elimina un producto usando su ID.
        """
        if id_producto in self.productos:
            del self.productos[id_producto]
            print("🗑 Producto eliminado.")
        else:
            print("Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        """
        Permite actualizar la cantidad o el precio de un producto.
        """
        if id_producto in self.productos:

            if cantidad is not None:
                self.productos[id_producto].set_cantidad(cantidad)

            if precio is not None:
                self.productos[id_producto].set_precio(precio)

            print("Producto actualizado correctamente.")
        else:
            print("Producto no encontrado.")

    def buscar_por_nombre(self, nombre):
        """
        Devuelve una lista con los productos que coinciden con el nombre.
        """
        return [
            producto for producto in self.productos.values()
            if producto.get_nombre().lower() == nombre.lower()
        ]

    def mostrar_todos(self):
        """
        Muestra todos los productos registrados.
        """
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for producto in self.productos.values():
                print(producto)

    # ======================================
    # GUARDAR Y CARGAR DESDE ARCHIVO JSON
    # ======================================

    def guardar_en_archivo(self):
        """
        Guarda el inventario en la carpeta data como archivo JSON.
        """
        with open("data/inventario.json", "w") as archivo:
            json.dump(
                {id: prod.to_dict() for id, prod in self.productos.items()},
                archivo,
                indent=4
            )

        print("💾 Inventario guardado correctamente.")

    def cargar_desde_archivo(self):
        """
        Carga los productos desde el archivo JSON si existe.
        """
        try:
            with open("data/inventario.json", "r") as archivo:
                datos = json.load(archivo)

                for id, prod in datos.items():
                    self.productos[id] = Producto(
                        prod["id"],
                        prod["nombre"],
                        prod["cantidad"],
                        prod["precio"]
                    )

            print("Inventario cargado correctamente.")

        except FileNotFoundError:
            print("No existe inventario previo. Se creará uno nuevo.")