# catalogo.py

import os

class Pelicula:
    def __init__(self, nombre):
        self.__nombre = nombre  # Atributo privado

    @property
    def nombre(self):
        return self.__nombre

    def __str__(self):
        return self.__nombre


class CatalogoPeliculas:
    def __init__(self, nombre_catalogo):
        self.nombre = nombre_catalogo
        self.ruta_archivo = f"{nombre_catalogo}.txt"

    def agregar(self, pelicula: Pelicula):
        try:
            with open(self.ruta_archivo, 'a', encoding='utf-8') as archivo:
                archivo.write(pelicula.nombre + '\n')
            return True
        except Exception as e:
            print(f"❌ Error al guardar la película: {e}")
            return False

    def listar(self):
        if not os.path.exists(self.ruta_archivo):
            return []

        with open(self.ruta_archivo, 'r', encoding='utf-8') as archivo:
            return [linea.strip() for linea in archivo.readlines()]

    def eliminar(self):
        if os.path.exists(self.ruta_archivo):
            os.remove(self.ruta_archivo)
            return True
        return False
