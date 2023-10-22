# =============================================================================
# sort / map / filter / reduce
# => reduce en Python

# https://thepythonguru.com/python-builtin-functions/reduce/

# !  Reduce sin valor inicial
# *      reduce(función , elemento_iterable)

# !  Reduce sin valor inicial
# *      reduce(función , elemento_iterable, valor_inicial)


# ! Aplicación en lista de DICCIONARIOS | PARTE 1
# - de igual manera en esta primera lección
# - vamos a observar las generalidades de esto
# - los errores y el procedimiento correcto a seguir
# - para aplicar reduce en una lista de diccionarios

# =============================================================================

#? reduce + lista de DICCIONARIOS | Explicación & Generalidades
print('\nreduce + lista de DICCIONARIOS | Explicación & Generalidades')

#           NOMBRE            PODER         VITALIDAD
guerreros_Z = [
    { 'nombre' : 'goku', 'poder' : 95, 'vitalidad' : 80},
    { 'nombre' : 'vegeta', 'poder' : 90, 'vitalidad' : 75},
    { 'nombre' : 'gohan', 'poder' : 91, 'vitalidad' : 70},
    { 'nombre' : 'piccolo', 'poder' : 82, 'vitalidad' : 65},
    { 'nombre' : 'krilin', 'poder' : 42, 'vitalidad' : 32},
    { 'nombre' : 'chaoz', 'poder' : 12, 'vitalidad' : 11},
    { 'nombre' : 'trunks', 'poder' : 88, 'vitalidad' : 8},
]


#? 1) Importar en 1er lugar functools
print('\n1) Importar en 1er lugar functools')

import functools



#? 2) Función EXTRA: print_datos()
print('\n2) Función EXTRA: print_datos()')

def print_datos(lista_dict):
    for x in lista_dict:
        print(x)
    # end for
# end def

print_datos(guerreros_Z)



#? 3) Ejemplo de Acceso a un valor específico en una lista de DICCIONARIOS
print('\n3) Ejemplo de Acceso a un valor específico en una lista de DICCIONARIOS')

# => ¿cómo obtendría el poder de goku con una línea de código?
print( guerreros_Z[0] )
print( guerreros_Z[0].values() )
print( list( guerreros_Z[0].values() ) )
print( list( guerreros_Z[0].values() )[1] )



#? 4) ERROR - Al usar este concepto dentro de reduce
print('\n4) ERROR - Al usar este concepto dentro de reduce')
# * vamos a tener el mismo error que teníamos en la lista de tuplas
# - por tanto sería conveniente
# - primero con un map obtener todos los poderes
# - en una lista
# - y con esto, podríamos aplicar reduce


#! AttributeError: 'int' object has no attribute 'values'
"""
poder_genkidama = functools.reduce(
    
    lambda x, y : list(x.values())[1] + list(y.values())[1],
    guerreros_Z
)
"""



#? 5) Procedimiento Correcto para utilizar reduce
print('\n5) Procedimiento Correcto para utilizar reduce')

# => map : para obtener una lista de los poderes
poderes_guerreros_Z = list(map(
    lambda x : x['poder'] ,
    guerreros_Z,
))

print( poderes_guerreros_Z, type(poderes_guerreros_Z) )


# => reduce : aplicado a la lista de poderes
poder_genkidama = functools.reduce(
    lambda x, y : x + y,
    poderes_guerreros_Z
)

print( poder_genkidama, type(poder_genkidama) )

# => en la siguiente lección:
# - definimos el mismo ejemplo pero como ejercicio más real
# - definiendo todo esto en funciones