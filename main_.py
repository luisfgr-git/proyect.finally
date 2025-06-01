# main.py

#Aca estamos importando las clases "Pelicula" y "CatalogoPëliculas" de donde sacaremos info importante.

from catalogo import Pelicula, CatalogoPeliculas

# Una funcion del menu principal del programa donde el usuario selecciona lo que prefiera.

def mostrar_menu():
    print("\nMenú de opciones:")
    print("1. Agregar Película")
    print("2. Listar Películas")
    print("3. Eliminar catálogo de películas")
    print("4. Salir")

# Okay, algo interesante aca, estamos definiendo una funcion principal, lo primero que observamos es la parte de agregar pelicula.
# Esta parte usara la clase "CatalogoPeliculas" para guardar las propiedades (el nombre)
def main():
    nombre_catalogo = input("Ingrese el nombre del catálogo de películas: ")
    catalogo = CatalogoPeliculas(nombre_catalogo)

# Un While sobre las opciones seleccionadas por el usuario, realmente es necesario que explique cada uno? 
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-4): ")

        if opcion == '1':
            nombre_pelicula = input("Ingrese el nombre de la película: ")
            pelicula = Pelicula(nombre_pelicula)
            if catalogo.agregar(pelicula):
                print(f"Película '{pelicula.nombre}' agregada con éxito.")
            else:
                print("Error al guardar la película.")
        elif opcion == '2':
            peliculas = catalogo.listar()
            if peliculas:
                print("\nPelículas en el catálogo:")
                # Miren un ciclo For en un ciclo While, que curioso
                for p in peliculas:
                    print(f"- {p}")
            else:
                print("El catálogo está vacío o no existe.")
        elif opcion == '3':
            if catalogo.eliminar():
                print("Catálogo eliminado correctamente.")
            else:
                print("No se pudo eliminar el catálogo (no existe).")
        elif opcion == '4':
            print("Programa finalizado. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

# Todo lo anterior es dentro de la funcion, para que inicie hay que llamarla jaja lo cual se hace aca
# Esto de __name__ hace que el archivo "main_.py" sea el archivo principal y se ejecute en formato python segun entendi gracias a mi gran amiga Chatgpt
# Espero no me maltrate cuando domine el mundo

if __name__ == "__main__":
    main()
print(" Se puede salir eligiendo la opción 4.")
print("PELICULAS AGREGADAS")