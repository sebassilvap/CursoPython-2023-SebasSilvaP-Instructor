# =============================================================================
# sort / map / filter / reduce
# => reduce en Python

# https://thepythonguru.com/python-builtin-functions/reduce/

# !  Reduce sin valor inicial
# *      reduce(función , elemento_iterable)

# !  Reduce sin valor inicial
# *      reduce(función , elemento_iterable, valor_inicial)


# ! Aplicación en lista de DICCIONARIOS | PARTE 2
# =============================================================================

#? reduce + lista de DICCIONARIOS | EJERCICIO COMPLETO
print('\nreduce + lista de tuplas | EJERCICIO COMPLETO')

#           NOMBRE            PODER         VITALIDAD
guerreros_Z = [
    { 'nombre' : 'goku', 'poder' : 95, 'vitalidad' : 80},
    { 'nombre' : 'vegeta', 'poder' : 90, 'vitalidad' : 75},
    { 'nombre' : 'trunks', 'poder' : 88, 'vitalidad' : 8},
    { 'nombre' : 'gohan', 'poder' : 91, 'vitalidad' : 70},
    { 'nombre' : 'piccolo', 'poder' : 82, 'vitalidad' : 65},
    { 'nombre' : 'krilin', 'poder' : 42, 'vitalidad' : 25},
    { 'nombre' : 'chaoz', 'poder' : 12, 'vitalidad' : 11},
    { 'nombre' : 'tenshinhan', 'poder' : 45, 'vitalidad' : 21},
    { 'nombre' : 'yamcha', 'poder' : 25, 'vitalidad' : 19},
]

# -----------------------------------------------------------------------------------------------
# EJERCICIO

# Usando reduce realizar lo siguiente:

# - Calcular el nivel de poder de una Genkidama realizada por los guerreros Z
# - La Genkidama utiliza el 30% del nivel de poder de cada guerrero Z
# - Los guerreros Z que tienen una vitalidad < 20, no pueden aportar con la Genkidama
# - Definir esto como una sola función: calcular_poder_genkidama()
# - Esta función tiene 1 sólo parámetro
# - Que es la lista de diccionarios, donde cada diccionario es un guerrero Z

# * TIP: seguir el orden => filter + map + reduce
# -----------------------------------------------------------------------------------------------


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



#? 3) Función : calcular_poder_genkidama()
print('\n3) Función : calcular_poder_genkidama()')

def calcular_poder_genkidama(guerrerosZ):
    
    #! FILTER
    # => filter de guerreros_Z con vitalidad >= 20
    guerreros_genkidama_True = list(filter(
        lambda x : x['vitalidad'] >= 20,
        guerrerosZ
    ))
    
    #! MAP
    # => map para devolver solo el nivel de poder
    nivel_poder = list(map(
        lambda x : x['poder'],
        guerreros_genkidama_True
    ))
    
    #! REDUCE
    # => reduce para calcular poder_genkidama:
    # OJO: el 30% de la suma
    poder_genkidama = functools.reduce(
        lambda x,y : x + y,
        nivel_poder
    ) * 0.3
    
    return poder_genkidama
# end def

# => TEST
print('\nPODER DE LA GENKIDAMA = {}'.format( calcular_poder_genkidama(guerreros_Z) ))
    
    
    