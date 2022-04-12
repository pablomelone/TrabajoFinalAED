import textwrap
from prettytable import PrettyTable

def menu():

    print("")
    print("Menu de opciones")
    print("1 - Cargar archivo.")
    print("2 - Sumar Revision.")
    print("3 - Mayores Revisiones.")
    print("4 - Popularidad 2000.")
    print("5 - Publicaciones por decada.")
    print("6 - Guardar populares.")
    print("7 - Mostrar archivo")
    print("8 - Salir")

    op = input("Ingrese opción: ")

    return op

def print_libro(libro):


    rating = f"{round(libro.rating, 2)}"
    titulo = textwrap.shorten(libro.titulo, width=50, placeholder="...")

    print_libro = PrettyTable()
    print_libro.field_names = ["ISBN", "Titulo", "Revisiones", "Año", "Codigo Idioma", "Rating"]
    print_libro.add_row([libro.isbn, titulo, libro.revisiones, libro.año,libro.idioma, rating])

    print(print_libro)


def mostrar_libros(array_libros):
    print(" ")
    print("="*120)
    print(" "*50+"Libros populares del 2000")
    print("="*120)

    listado = PrettyTable()
    listado.field_names = ["ISBN", "Titulo", "Revisiones", "Año", "Codigo Idioma", "Rating"]

    for libro in array_libros:

        rating = f"{round(libro.rating, 2)}"
        titulo = textwrap.shorten(libro.titulo, width=50, placeholder="...")
        listado.add_row([libro.isbn, titulo, libro.revisiones, libro.año,libro.idioma, rating])

    print(listado)


def mostrar_libros_por_decada(contador):
    print(" ")
    print("="*120)
    print(" "*50+"Publicaciones por decada")
    print("="*120)

    listado = PrettyTable()
    listado.field_names = ["Decada", "Cant. de Libros"]

    for c in range(len(contador)):
        dec = 1900 + (c*10)
        listado.add_row([dec, contador[c]])

    print(listado)


def mayor_por_decada(contador, mayor):
    print(" ")
    print("="*120)
    print(" "*50+"Decadas con mas publicaciones")
    print("="*120)

    for h in range(len(contador)):
        if contador[h] == mayor:
            dec = 1900 + (h*10)
            print(f"Decada {dec} con {contador[h]} publicaciones.")
