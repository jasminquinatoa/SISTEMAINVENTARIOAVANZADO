"""
Archivo: producto.py
Autor: (Jasmin)
Descripción:
Esta clase representa un producto dentro del sistema de inventario.

Aquí aplico Programación Orientada a Objetos utilizando:
- Encapsulamiento (atributos privados)
- Métodos getters y setters
- Método para convertir el objeto a diccionario (para guardarlo en archivo)
"""

class Producto:
    """
    Clase que modela un producto del inventario.
    Cada producto tiene:
    - ID único
    - Nombre
    - Cantidad disponible
    - Precio unitario
    """

    def __init__(self, id_producto, nombre, cantidad, precio):
        # Atributos privados para proteger la información
        self.__id = id_producto
        self.__nombre = nombre
        self.__cantidad = cantidad
        self.__precio = precio

    # ==========================
    # MÉTODOS GETTERS
    # ==========================

    def get_id(self):
        return self.__id

    def get_nombre(self):
        return self.__nombre

    def get_cantidad(self):
        return self.__cantidad

    def get_precio(self):
        return self.__precio

    # ==========================
    # MÉTODOS SETTERS
    # ==========================

    def set_cantidad(self, nueva_cantidad):
        self.__cantidad = nueva_cantidad

    def set_precio(self, nuevo_precio):
        self.__precio = nuevo_precio

    # ==========================
    # CONVERSIÓN A DICCIONARIO
    # ==========================

    def to_dict(self):
        """
        Convierte el objeto en diccionario.
        Esto es necesario para poder guardarlo en formato JSON.
        """
        return {
            "id": self.__id,
            "nombre": self.__nombre,
            "cantidad": self.__cantidad,
            "precio": self.__precio
        }

    def __str__(self):
        """
        Permite mostrar el producto de forma clara cuando se imprime.
        """
        return f"ID: {self.__id} | Nombre: {self.__nombre} | Cantidad: {self.__cantidad} | Precio: ${self.__precio}"