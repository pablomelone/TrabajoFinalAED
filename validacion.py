def validacion_opcion_busqueda():
    txt =  """
    Ingrese el tipo de busqueda
    1 - Busqueda por ISBN
    2 - Busqueda por Titulo
    3 - Volver al menu
    """
    advertencia = "El tipo de busqueda es invalido. Reintente."
    check = True
    while check:
        tipo = input(txt)
        if str.isnumeric(tipo):
            tipo = int(tipo)
            if  tipo in (1,2,3):
                check = False
            else:
                print(advertencia)
        else:
            print(advertencia)
    return tipo


def validar_isbn(isbn):

    #Validamos el largo del ISBN
    if len(isbn) != 10:
        return False

    #Valido que los primero 9 elementos sean numeros
    for i in isbn[:-1]:
        if not str.isnumeric(i):
            return False

    #Valido que el ultimo elemento sea un numero o x X
    if isbn[-1] not in '0123456789Xx':
        return False

    #Separo el ISBN en digitos y transformo xX en 10
    digitos = []
    for i in isbn:
        if i in 'xX':
            digitos.append(10)
        else:
            digitos.append(int(i))

    #Calculamos la suma de los digitos por los productos
    suma = 0
    polinomio = 10
    for i in digitos:
        suma += i * polinomio
        polinomio -= 1

    #Check modulo de 11
    if suma%11 != 0:
        return False

    return True

def validar_carga_isbn():
    txt =  """
    Ingrese el ISBN a buscar (0- Volver al menu):
    """
    advertencia = "El ISBN ingresado es invalido. Reintente."
    check = True
    while check:
        isbn = input(txt)
        if validar_isbn(isbn):
            check = False
        elif isbn == '0':
            return None
        else:
            print(advertencia)
    return isbn

def validar_carga_titulo():
    txt =  """
    Ingrese el titulo a buscar (0- Volver al menu):
    """
    advertencia = "El titulo ingresado es invalido. Reintente."
    check = True
    while check:
        titulo = input(txt)
        if titulo == '0':
            return None
        elif len(titulo) != 0:
            check = False
        else:
            print(advertencia)
    return titulo
