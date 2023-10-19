# ===================================================================
# Función Interna sorted() => para Tuplas y Diccionarios

# - como se dijo anteriormente
# - para SETS no tiene sentido => elementos DESORDENADOS por defecto
# - DICCIONARIOS => a partir de Python 3.7 + => ORDENADOS
# - Tuplas y Diccionarios tienen sentido ordenar
# - .sort() => método exclusivo de las LISTAS
# ===================================================================


#? 1) sorted() + Tuplas
print('\n1) sorted() + Tuplas')

tupla_1 = (10, 50, 5, 20.5, 8.9)
tupla_2 = ('python', 'hola', 'abecedario')

# => valores numéricos: Menor a Mayor
tupla_1_sorted = sorted(tupla_1)
print(tupla_1_sorted)

# => valores numéricos: Mayor a Menor
tupla_1_sorted = sorted(tupla_1, reverse=True)
print(tupla_1_sorted)

# => texto: (A-Z)
tupla_2_sorted = sorted(tupla_2)
print(tupla_2_sorted)

# => texto: (Z-A)
tupla_2_sorted = sorted(tupla_2, reverse=True)
print(tupla_2_sorted)

# => especial: texto Pequeño a Grande
tupla_2_sorted = sorted(tupla_2, key=len)
print(tupla_2_sorted)

# => especial: texto Grande a Pequeño
tupla_2_sorted = sorted(tupla_2, key=len, reverse=True)
print(tupla_2_sorted)



#? 2) sorted() + Diccionarios => Versión Incorrecta
print('\n2) sorted() + Diccionarios => Versión Incorrecta')

notas = {
    'Literatura' : 15,
    'Matemáticas' : 20,
    'Inglés' : 13,
    'Geometría' : 18,
    'Biología' : 14 
}

notas_sorted = sorted(notas)
print(notas_sorted)
# ['Biología', 'Geometría', 'Inglés', 'Literatura', 'Matemáticas']

# ----------------------------------------------------------
# - lo que me ordena son las claves del diccionario
# - en orden alfabético
# - nosotros deseamos ordenar el diccionario
# - no que nos devuelva una lista con las claves ordenadas
# ! Este no es el comportamiento que deseamos
# ----------------------------------------------------------



#? 3) sorted() + Diccionarios => VERSIÓN CORRECTA
print('\n3) sorted() + Diccionarios => VERSIÓN CORRECTA')

notas = {
    'Literatura' : 15,
    'Matemáticas' : 20,
    'Inglés' : 13,
    'Geometría' : 18,
    'Biología' : 14 
}

# RECORDAR el .items() de diccionarios
# - nos devuelve un objeto de tipo 'dict_items'
# - que no es más que una lista de tuplas
# - cada tupla contiene la clave y el valor
# - en el orden como fue construido el diccionario

print( notas.items() , type(notas.items()) )


# => aplicando sorted() de manera correcta

# --------------------------------------------
# Diccionario con claves de (A-Z)
print('\nDiccionario con claves de (A-Z)\n')
# --------------------------------------------
# - para esto utilizamos el parámetro especial key
# - con una función lambda que haga referencia
# - a la columna donde deseamos aplicar el ordenamiento
# - tenemos 2 opciones:
#       * [0] => para las claves
#       * [2] => para los valores de las claves

notas_sorted = sorted(
    notas.items(),
    key = lambda x : x[0] # haciendo referencia a la columna 1 => de las claves
)

print(notas_sorted, type(notas_sorted)) # lista de tuplas con clave (A-Z)

# - este formato de lista de tuplas
# - y las tuplas de 2 valores
# - puede ser llevado a un diccionario
# - utilizando el casting con la función "dict()"

notas = dict(notas_sorted)

print(notas) # aquí ya tenemos el diccionario ordenado

# - en las siguientes líneas de código
# - vamos a ejemplificar el resto de opciones de clasificación
# - que pod'riamos aplicar al diccionario


# --------------------------------------------
# Diccionario con claves de (A-Z)
print('\nDiccionario con claves de (A-Z)\n')
# --------------------------------------------

notas = {
    'Literatura' : 15,
    'Matemáticas' : 20,
    'Inglés' : 13,
    'Geometría' : 18,
    'Biología' : 14 
}

notas_sorted = sorted(
    notas.items(),
    key = lambda x : x[0],
    reverse=True
)

notas = dict(notas_sorted)

print(notas)


# --------------------------------------------------------------
# Diccionario con valores de claves de Menor a Mayor
print('\nDiccionario con valores de claves de Menor a Mayor\n')
# --------------------------------------------------------------

notas = {
    'Literatura' : 15,
    'Matemáticas' : 20,
    'Inglés' : 13,
    'Geometría' : 18,
    'Biología' : 14 
}

notas_sorted = sorted(
    notas.items(),
    key = lambda x : x[1]
)

notas = dict(notas_sorted)

print(notas)


# --------------------------------------------------------------
# Diccionario con valores de claves de Mayor a Menor
print('\nDiccionario con valores de claves de Mayor a Menor\n')
# --------------------------------------------------------------

notas = {
    'Literatura' : 15,
    'Matemáticas' : 20,
    'Inglés' : 13,
    'Geometría' : 18,
    'Biología' : 14 
}

notas_sorted = sorted(
    notas.items(),
    key = lambda x : x[1],
    reverse=True
)

notas = dict(notas_sorted)

print(notas)