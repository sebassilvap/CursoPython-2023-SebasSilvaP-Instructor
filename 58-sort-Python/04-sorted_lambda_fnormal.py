# ===========================================================================
# Función Interna sorted()

# - función normal VS. función lambda
# - como parámetro del key
# * podemos utilizar AMBAS opciones
# - al momento de pasar la función, simplemente, no olvidar
# - que se debe pasar su firma, no ejecutada
# - en algunos casos la función lambda facilita la escritura del código
# - pero recordar que esta se hace en 1 sola línea
# - si la expresión se complica sería buena idea utilizar la función normal
# * cualquier función normal tiene su equivalente en función lambda
# ===========================================================================


# => colección de datos a ordenar
notas = {
    'Literatura' : 15,
    'Matemáticas' : 20,
    'Inglés' : 13,
    'Geometría' : 18,
    'Biología' : 14 
}


# => Función EXTRA : print_datos()
def print_datos(diccionario):
    for k, v in diccionario.items():
        print( '{} -- {}'.format(k,v) )
# end def

print('\nDATOS ORIGINALES:')
print_datos(notas)


# => ordenamiento usando función lambda:
notas_sorted = sorted(
    notas.items(),
    key = lambda x : x[1],
    reverse=True
)

notas_mayor_menor = dict(notas_sorted)

print('\nNOTAS DE MAYOR A MENOR - Función Lambda:')
print_datos(notas_mayor_menor)


# => ordenamiento usando función normal:
def mayor_a_menor(columna):
    return columna[1]
# end def

notas_sorted_2 = sorted(
    notas.items(),
    key = mayor_a_menor,
    reverse=True
)

notas_mayor_menor_2 = dict(notas_sorted_2)

print('\nNOTAS DE MAYOR A MENOR - Función Normal:')
print_datos(notas_mayor_menor_2)