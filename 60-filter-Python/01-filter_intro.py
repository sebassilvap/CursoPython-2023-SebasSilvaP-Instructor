# ==============================================================
# sort / map / filter / reduce
# => filter en Python

# https://www.w3schools.com/python/ref_func_filter.asp

# -   Para EXCLUIR items de un elemento / objeto iterable
# -   De igual manera es una función que recibe 2 argumentos
#     a) la función que define el filtrado (normal ó lambda)
#     b) el iterable a ser filtrado
#  
# -   la función de filter debe retornar True o False
# -   según el criterio de filtrado
#  
# !   filter => devuelve un elemento / objeto del tipo filter
# -   para verlo se debe hacer un casting a lista => list()

# *      filter(función , elemento_iterable)
# ==============================================================


#? 1) Ejemplo Básico de Funcionamiento con Función Normal
print('\n1) Ejemplo Básico de Funcionamiento con Función Normal')

calificaciones = [13, 14, 18, 10, 20, 15, 16, 14, 19, 11]

print('\nLISTADO DE CALIFICACIONES:')
print(calificaciones)

# => Función Normal para filtrar calificaciones altas (>14)
def calificaciones_altas(nota):
    if nota > 14:
        return True
    else:
        return False
    # end if
# end def

# => Función Normal para filtrar calificaciones bajas (<=14)
def calificaciones_bajas(nota):
    if nota > 14:
        return False
    else:
        return True
    # end if
# end def

# => aplicando filter para calificaciones altas:
lista_calificaciones_altas_filter = filter(
    calificaciones_altas,
    calificaciones
)

# => elemento/objeto de tipo filter
print(lista_calificaciones_altas_filter)
# EJ: <filter object at 0x000002803240BA30>

# => casting a lista
lista_calificaciones_altas = list(lista_calificaciones_altas_filter)

print('\nFILTRADO DE CALIFICACIONES ALTAS:')
print(lista_calificaciones_altas)

# => aplicando filter para calificaciones bajas:
lista_calificaciones_bajas = list(filter(
    calificaciones_bajas,
    calificaciones
))

print('\nFILTRADO DE CALIFICACIONES BAJAS:')
print(lista_calificaciones_bajas)



#? 2) Ejemplo Básico de Funcionamiento con Función Lambda
print('\n2) Ejemplo Básico de Funcionamiento con Función Lambda')

calificaciones = [13, 14, 18, 10, 20, 15, 16, 14, 19, 11]

print('\nLISTADO DE CALIFICACIONES:')
print(calificaciones)

# => Función Lambda: notas_altas
notas_altas = lambda nota : True if nota > 14 else False

# => Función Lambda: notas_bajas
notas_bajas = lambda nota : True if nota <= 14 else False

# => filter de notas_altas
lista_calificaciones_altas = list(filter(
    notas_altas,
    calificaciones
))

print('\nFILTRADO DE CALIFICACIONES ALTAS:')
print(lista_calificaciones_altas)

# => filter de notas_bajas
lista_calificaciones_bajas = list(filter(
    notas_bajas,
    calificaciones
))

print('\nFILTRADO DE CALIFICACIONES BAJAS:')
print(lista_calificaciones_bajas)



#? 3) Función lambda más corta
print('\n3) Función lambda más corta')

calificaciones = [13, 14, 18, 10, 20, 15, 16, 14, 19, 11]


# RECORDAR como se planteó antes lambda:
# notas_altas = lambda nota : True if nota > 14 else False
# todo esto puede ser resumido en 1 línea directo en filter

lista_calificaciones_altas = list(filter(
    lambda x : x > 14, 
    calificaciones
))


lista_calificaciones_bajas = list(filter(
    lambda x : x <= 14, 
    calificaciones
))

print('\nFILTRADO DE CALIFICACIONES ALTAS:')
print(lista_calificaciones_altas)

print('\nFILTRADO DE CALIFICACIONES BAJAS:')
print(lista_calificaciones_bajas)