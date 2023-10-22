# ==============================================================
# sort / map / filter / reduce
# => filter en Python

# https://www.w3schools.com/python/ref_func_filter.asp

# ? RECORDAR: las colecciones avanzadas de casos reales:

#       * Listas de Listas (Listas 2D)
#       * Listas de Tuplas
#       * Listas de Diccionarios

# ? TIP: la función la podemos definir con lambda
# - recordar que lambda se define en una sola línea
# - si la expresión es muy complicada podemos siempre optar
# - por nuestras funciones normales

# ? RECORDAR !!!
# - la función filter nos debe retornar un patrón de filtrado
# - en True o False
# - o con lambda se define la expresión que me devuelve True

# ! PARTE 1
# => aplicando filter a una lista de TUPLAS
# ==============================================================


#? Filter + Lista de TUPLAS
print('\nFilter + Lista de TUPLAS')

estudiantes = [
    ('Leonardo', [18, 15, 16], 'becado'),
    ('María', [15, 14, 17], 'no-becado'),
    ('Juan', [20, 19, 17], 'no-becado'),
    ('Carlos', [12, 15, 20], 'becado'),
    ('Fernando', [20, 19, 18], 'becado'),
    ('Lucía', [20, 20, 19], 'no-becado'),
]


# ----------------------------------------------------------------------------------------------------
# EJERCICIO
# - se tiene una lista de estudiantes
# - la información de cada estudiante se pone en una tupla
# - se tiene básicamente el nombre, las notas en una lista, y la situación actual (becado / no-becado)
# - se pide:

## A) Aplicar map y crear una nueva lista => estudiantes_mod
#    - donde tendremos una nueva 3 columna que nos diga el promedio de las notas
#    - la situación actual (becado / no-becado) será ahora la columna 4
#    - como quinta columna una nueva información:
#*        => si la nota promedio es >= 18 y el estudiante es becado: 'mantiene beca'
#*        => si la nota promedio es >= 18 y el estudiante es no-becado: 'accede a beca'
#*        => si la nota promedio es < 18 y el estudiante es becado: 'pierde beca'
#*        => si la nota promedio es < 18 y el estudiante es no-becado: 'no accede a beca'

# ==> con la nueva lista: estudiantes_mod

## B) Aplicar filter y devolver la lista: promedio_mayor_16
#    - devolvemos los estudiantes cuyo promedio sea mayor o igual a 16

## C) Aplicar filter y devolver la lista: beca_disponible
#    - aquí tendremos los estudiantes que pueden acceder a la beca
#    - o que mantienen la beca
#    - básicamente aquellos que en la 5ta columna tengan la información:
#    - 'accede a beca' Ó 'mantiene beca'
# ----------------------------------------------------------------------------------------------------


#? 1) Función EXTRA: print_datos()
print('\n1) Función EXTRA: print_datos()')

def print_datos(lista_tuplas):
    for tupla in lista_tuplas:
        print(tupla)
    # end for
# end def

# => TEST:
print('\nLISTA ESTUDIANTES - ORIGINAL:')
print_datos(estudiantes)



#? 2) Lista: estudiantes_mod => usando map
print('\n2) Lista: estudiantes_mod => usando map')
# * RECORDAR:  map(funcion, elementoS_iterableS)

# => función para calcular promedio y que devuelva un float con 2 decimales
def calcular_promedio(lista_notas):
    promedio = 0
    for nota in lista_notas:
        promedio += nota
    # end for
    
    promedio /= len(lista_notas)
    promedio = float( f'{promedio:.2f}' )
    return promedio
# end def


# => funcion determinar_beca
#    - promedio es >= 18 y el estudiante es becado: 'mantiene beca'
#    - promedio es >= 18 y el estudiante es no-becado: 'accede a beca'
#    - promedio es < 18 y el estudiante es becado: 'pierde beca'
#    - promedio es < 18 y el estudiante es no-becado: 'no accede a beca'

def determinar_beca(nota_promedio, info_beca):
    if nota_promedio >= 18 and info_beca == 'becado':
        return 'mantiene beca'
    elif nota_promedio >= 18 and info_beca == 'no-becado':
        return 'accede a beca'
    elif nota_promedio < 18 and info_beca == 'becado':
        return 'pierde beca'
    elif nota_promedio < 18 and info_beca == 'no-becado':
        return 'no accede a beca'
    # end if
# end def


# => función map
def funcion_map(x):
    return (
            x[0],
            x[1],
            calcular_promedio( x[1] ),
            x[2],
            determinar_beca( calcular_promedio( x[1] ) , x[2] )
        )
# end def


# => construyendo : estudiantes_mod
# - no olvidar el casting a lista !

estudiantes_mod = list(map(
    funcion_map,
    estudiantes
))

# => TEST:
print_datos(estudiantes_mod)



#? 3) usando filter => lista : promedio_mayor_16
print('\n3) usando filter => lista : promedio_mayor_16')
# * RECORDAR:  filter(funcion, elemento_iterable)
# - la función_filter debe retornar True o False
# - dependiendo del criterio de filtrado

# ------------------------------------------
# 3.1) Utilizando función normal
print('\n3.1) Utilizando función normal\n')
# ------------------------------------------

# => definiendo la función filter
def filter_promedio_mayor_16(info_estudiantes):
    if info_estudiantes[2] >= 16:
        return True
    else:
        return False
    # end if
# end def


# => aplicando filter
promedio_mayor_16 = list(filter(
    filter_promedio_mayor_16,
    estudiantes_mod
))

# => TEST:
print_datos(promedio_mayor_16)


# ------------------------------------------
# 3.2) Utilizando función lambda
print('\n3.2) Utilizando función lambda\n')
# ------------------------------------------

promedio_mayor_16 = list(filter(
    lambda x : x[2] >= 16, # 3ra columna, promedio
    estudiantes_mod
))

# => TEST:
print_datos(promedio_mayor_16)



#? 4) usando filter => lista: beca_disponible
print('\n4) usando filter => lista: beca_disponible')
# - 'accede a beca' Ó 'mantiene beca'

beca_disponible = list(filter(
    lambda x : (x[4] == 'accede a beca') or (x[4] == 'mantiene beca'),
    estudiantes_mod
))

# => TEST:
print_datos(beca_disponible)