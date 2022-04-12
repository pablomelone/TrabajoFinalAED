import os.path
import pickle


class Libros:
    def __init__(self,titulo, revisiones, año, idioma, rating, isbn ):
        self.titulo = titulo
        self.revisiones = revisiones
        self.año = año
        self.idioma = idioma
        self.rating = rating
        self.isbn = isbn

def add_in_order(v, libro):
    n = len(v)
    pos = 0
    izq, der = 0, n-1
    while izq <= der:
        c = (izq + der) // 2
        if v[c].isbn == libro.isbn:
            pos = c
            break
        elif libro.isbn > v[c].isbn:
            izq = c + 1
        else:
            der = c - 1
    if izq > der:
        pos = izq

    v[pos:pos] = [libro]

def cargar_archivo(nombre_archivo='libros.csv'):

    if os.path.exists(nombre_archivo):

        array_guardado = []
        archivo = open(nombre_archivo, mode="rt", encoding="utf-8")
        encabezado = archivo.readline()

        while True:

            # intentar leer una linea...
            line = archivo.readline()
            # si se obtuvo una cadena vacia... cortar el ciclo y terminar...
            if line == '':
                break
            # si lo tenía, eliminar el caracter de salto de línea...
            if line[-1] == '\n':
                line = line[:-1]
            # procesar la cadena resultante...
            line = line.split(',')

            titulo = line[0]
            revisiones = int(line[1])
            año = int(line[2])
            idioma = int(line[3])
            rating = float(line[4])
            isbn = line[5]

            libro = Libros(titulo,revisiones,año,idioma,rating,isbn)
            add_in_order(array_guardado, libro)

        # cerrar antes de irnos...
        archivo.close()


        return array_guardado

    else:
        print("FLAG")
        return None

def busqueda_libro(array_libros, tipo_busqueda,parametro_busqueda):

    if tipo_busqueda == 1:

        n = len(array_libros)

        izq, der = 0, n-1

        while izq <= der:
            c = (izq + der) // 2
            if array_libros[c].isbn == parametro_busqueda:
                return c
            elif parametro_busqueda > array_libros[c].isbn:
                izq = c + 1
            else:
                der = c - 1
        return None

    else:

        for i in range(len(array_libros)):
            if array_libros[i].titulo == parametro_busqueda:
                return i

        return None


def array_filtrado_por_rango(array_libros):
    array_filtrado = []

    for libro in array_libros:
        if libro.año >= 2000 and libro.año <= 2020:
            array_filtrado.append(libro)

    return array_filtrado

def generar_matriz_popular(array_libros):
    matriz = [[0] * (2021-2000) for i in range(27)]

    for libro in array_libros:
        fila = libro.idioma-1
        columna = libro.año-2000
        if matriz[fila][columna] == 0:
            matriz[fila][columna] = libro
        else:
            if libro.rating > matriz[fila][columna].rating:
                matriz[fila][columna] = libro

    return matriz


def contador_decadas(array_libros):
    contador = [0]*10
    mayor = 0

    for i in range(len(array_libros)):
        dec = (array_libros[i].año - 1900)//10
        if dec < 10:
            contador[dec] += 1

    for c in range(len(contador)):
        if contador[c] > mayor:
            mayor = contador[c]

    return contador, mayor


def generar_archivo(matriz, nombre_archivo='populares.dat'):
    archivo = nombre_archivo

    m = open(archivo, 'wb')
    contador_registros = 0

    for f in range(len(matriz)):
        for c in range(len(matriz[0])):
            if matriz[f][c] != 0:
                pickle.dump(matriz[f][c], m)
                contador_registros += 1

    m.close()
    return contador_registros


def cargar_archivo_binario(nombre_archivo='populares.dat'):

    array_guardado = []
    if os.path.exists(nombre_archivo):

        f = open(nombre_archivo, 'rb')
        size = os.path.getsize(nombre_archivo)

        while f.tell() < size:
            libro = pickle.load(f)
            array_guardado.append(libro)
        f.close()

        return array_guardado

    else:
        return None

def mayor_revisiones(array_libros):
    libro_mayor_revision = None
    revisiones = 0

    for libro in array_libros:
        if libro.revisiones > revisiones:
            libro_mayor_revision = libro
            revisiones = libro.revisiones
    
    return libro_mayor_revision


def rating_promedio_idioma(array_libros, libro):
    rating = cantidad = 0
    idioma = libro.idioma

    for libro in array_libros:
        if libro.idioma == idioma:
            rating += libro.rating
            cantidad += 1
    
    #Siempre va a haber 1 de cantidad, ya que minimamente va a estar el libro de mayor revisiones
    promedio = round(rating/cantidad,2)

    return promedio
