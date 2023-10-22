# ===========================================================
# Ejercicio
# En casos reales y prácticos tenemos lo siguiente:

#       * Listas de Listas (Listas 2D)
#       * Listas de Tuplas
#       * Listas de Diccionarios

# PERO:
# - Básicamente, lo que aprendimos en la lección anterior
# - sobre la clasificación de diccionarios
# - utilizando key y la función lambda
# - se aplica en estos casos para permitirnos el orden
# - en el caso de diccionarios, es un poco especial
# - porque no podemos acceder con indexing normal
# - por lo cual como ya aprendimos podemos trasnformar
# - a lista de tuplas y luego a diccionario con dict()
# ===========================================================


#? EJERCICIO - Lista de Diccionarios
print('\nEJERCICIO - Lista de Diccionarios\n')

jugadores = [
    {
        'caracter' : 'mago',
        'ataque'   :  150,
        'defensa'  :  80
    },
    {
        'caracter' : 'elfo',
        'ataque'   :  120,
        'defensa'  :  100
    },
    {
        'caracter' : 'gladiador',
        'ataque'   :  220,
        'defensa'  :  90
    },
    {
        'caracter' : 'hechicera',
        'ataque'   :  170,
        'defensa'  :  110
    },
    {
        'caracter' : 'caballero',
        'ataque'   :  120,
        'defensa'  :  75
    },
]

# -----------------------------------------------------------------------------
# INDICACIONES
# 1) Crear 2 tipos de funciones:
#       A. una función para pasar de lista de diccionarios a lista de listas
#       B. otra función para pasar de lista de listas al diccionario original

# La lista de listas tiene que lucir de la siguiente manera:

"""
lista_de_listas = [
    ['caracter', 'ataque', 'defensa'],
    ['mago', 150, 180],
    ['elfo', 120, 100],
    ['gladiador', 220, 90],
    ['hechicera', 170, 110],
    ['caballero', 120, 75]
]
"""

# 2) En la lista de listas:
#       A. Ordenamiento alfabético (A-Z) por caracter
#       B. Ordenamiento por ataque de mayor a menor
#       C. Ordenamiento por defensa de menor a mayor

# 3) En la lista de diccionarios:
#       A. Ordenamiento alfabético (Z-A) por caracter
#       B. Ordenamiento por ataque de menor a mayor
#       C. Ordenamiento por defensa de mayor a menor
# -----------------------------------------------------------------------------

#? 1) Función EXTRA: Presentar Datos - Lista de Listas
print('\n1) Función EXTRA: Presentar Datos - Lista de Listas')

def print_datos(lista_listas):
    for lista in lista_listas:
        print(lista)
    # end for
# end def



#? 2) Función para pasar de lista de diccionarios a lista de listas
print('\n2) Función para pasar de lista de diccionarios a lista de listas')

def crear_lista_listas(lista_diccionarios):
    lista_resultado = []
    
    # => 1era fila títulos
    fila_temp = list( lista_diccionarios[0].keys() )
    lista_resultado.append(fila_temp)
    
    for diccionario in lista_diccionarios:
        fila_temp = []
        for valor in diccionario.values():
            fila_temp.append(valor)
        # end for
        lista_resultado.append(fila_temp)
    # end for
    
    return lista_resultado
# end def
    
# => TEST
lista_de_listas = crear_lista_listas(jugadores)
print_datos(lista_de_listas)



#? 3) Función para pasar de lista de listas a lista de diccionarios
print('\n3) Función para pasar de lista de listas a lista de diccionarios')
# - RECORDAR: para pasar a un diccionario
# - debemos tener una lista de tuplas
# - EJ:

"""
lista_tuplas_ex = [
    ('key_1' , 100),
    ('key_2' , 200),
    ('key_3' , 300)
]

print(lista_tuplas_ex)
lista_diccionarios_ex = dict(lista_tuplas_ex)
print(lista_diccionarios_ex)

"""

# => definición de la función:

def crear_lista_diccionarios(lista_listas):
    lista_resultado = []
    
    # => extraemos las claves / 1era fila
    keys = lista_de_listas[0]
    
    for index, lista in enumerate(lista_listas):
        fila_temp = []
        
        if index == 0:
            continue
        else:
            for index, valor in enumerate(lista):
                tupla_temp = tuple( (keys[index], valor) )
                fila_temp.append(tupla_temp)
            # end for
            
            # => transformar a diccionario
            fila_temp = dict(fila_temp)
            
            # => anexar diccionario a la lista resultado
            lista_resultado.append(fila_temp)
        # end if
    # end for
    
    return lista_resultado
# end def


# => TEST
lista_de_diccionarios = crear_lista_diccionarios(lista_de_listas)
print_datos(lista_de_diccionarios)



#? 4) Ordenamiento en Lista de Listas
print('\n4) Ordenamiento en Lista de Listas')
# - en todos estos ordenamientos, debemos excluir la primera fila
# - que vendrían a ser como los títulos del resto de datos

"""
lista_de_listas = [
    ['caracter', 'ataque', 'defensa'],
    ['mago', 150, 180],
    ['elfo', 120, 100],
    ['gladiador', 220, 90],
    ['hechicera', 170, 110],
    ['caballero', 120, 75]
]
"""

# ----------------------------------------------------------
# A. Ordenamiento alfabético (A-Z) por caracter
print('\nA. Ordenamiento alfabético (A-Z) por caracter\n')
# ----------------------------------------------------------

por_caracter = lambda x : x[0]

lista_listas_ordenada = sorted(
    lista_de_listas[1:], # hacemos con la sublista de listas, evitando los títulos
    key = por_caracter,
    #reverse=False
)

# => insertando títulos al inicio
lista_listas_ordenada.insert(0, lista_de_listas[0])

print_datos(lista_listas_ordenada)

    

# ----------------------------------------------------------
# B. Ordenamiento por ataque de mayor a menor
print('\nB. Ordenamiento por ataque de mayor a menor\n')
# ----------------------------------------------------------

por_ataque = lambda x : x[1]

lista_listas_ordenada = sorted(
    lista_de_listas[1:], # hacemos con la sublista de listas, evitando los títulos
    key = por_ataque,
    reverse=True
)

# => insertando títulos al inicio
lista_listas_ordenada.insert(0, lista_de_listas[0])

print_datos(lista_listas_ordenada)



# ----------------------------------------------------------
# C. Ordenamiento por defensa de menor a mayor
print('\nC. Ordenamiento por defensa de menor a mayor\n')
# ----------------------------------------------------------

por_defensa = lambda x : x[2]

lista_listas_ordenada = sorted(
    lista_de_listas[1:], # hacemos con la sublista de listas, evitando los títulos
    key = por_defensa,
    #reverse=False
)

# => insertando títulos al inicio
lista_listas_ordenada.insert(0, lista_de_listas[0])

print_datos(lista_listas_ordenada)



#? 5) Ordenamiento en Lista de Diccionarios
print('\n5) Ordenamiento en Lista de Diccionarios')

# ----------------------------------------------------------
# A. Ordenamiento alfabético (Z-A) por caracter
print('\nA. Ordenamiento alfabético (Z-A) por caracter\n')
# ----------------------------------------------------------

por_caracter = lambda x : x['caracter']

lista_dict_ordenada = sorted(
    lista_de_diccionarios,
    key = por_caracter,
    reverse=True
)

print_datos(lista_dict_ordenada)



# ----------------------------------------------------------
# B. Ordenamiento por ataque de menor a mayor
print('\nB. Ordenamiento por ataque de menor a mayor\n')
# ----------------------------------------------------------

por_ataque = lambda x : x['ataque']

lista_dict_ordenada = sorted(
    lista_de_diccionarios,
    key = por_ataque,
    #reverse=False
)

print_datos(lista_dict_ordenada)



# ----------------------------------------------------------
# C. Ordenamiento por defensa de mayor a menor
print('\nC. Ordenamiento por defensa de mayor a menor\n')
# ----------------------------------------------------------

por_defensa = lambda x : x['defensa']

lista_dict_ordenada = sorted(
    lista_de_diccionarios,
    key = por_defensa,
    reverse=True
)

print_datos(lista_dict_ordenada)