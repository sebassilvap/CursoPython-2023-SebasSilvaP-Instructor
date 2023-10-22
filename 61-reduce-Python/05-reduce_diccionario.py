# =============================================================================
# sort / map / filter / reduce
# => reduce en Python

# https://thepythonguru.com/python-builtin-functions/reduce/


# !  Reduce sin valor inicial
# *      reduce(función , elemento_iterable)

# !  Reduce sin valor inicial
# *      reduce(función , elemento_iterable, valor_inicial)


# ? Aplicando reduce a un diccionario
# =============================================================================

#? 1) import de functools
print('\n1) import de functools')

import functools


#? 2) Ejemplo de diccionario
print('\n2) Ejemplo de diccionario')

notas = {
    'álgebra' : 15,
    'química' : 17,
    'física' : 14,
    'inglés' : 19,
    'geometría' : 18
}

print(notas, type(notas))
print( keys := notas.keys(), type(keys) ) # RECORDAR: operador walrus
print( values := notas.values(), type(values) ) # RECORDAR: operador walrus



#? 3) Reduce para promedio de notas
print('\n3) Reduce para promedio de notas')
# - la manera más fácil entonces
# - sería tomanddo el diccionario, pero sus values
# - que a la final sigue siendo un elemento iterable
# - no es necesario hacer casting a lista

promedio = functools.reduce(
    lambda x,y : x + y,
    notas.values()
) / len(notas)

print('\nPROMEDIO DE NOTAS:')
print(promedio)