# ===============================================================
# sort / map / filter / reduce
# => reduce con valor inicial

# https://thepythonguru.com/python-builtin-functions/reduce/

# !  Reduce sin valor inicial
# *      reduce(función , elemento_iterable)

# !  Reduce sin valor inicial
# *      reduce(función , elemento_iterable, valor_inicial)

# - el valor incial es un parámetro opcional
# - también se lo puede llamar como valor offset
# - cuando lo definimos, el resultado del reduce se adiciona
# - a este valor inicial
# ===============================================================


#? 1) Importación de functools
print('\n1) Importación de functools')

import functools



#? 2) Ejemplo con lista de números
print('\n2) Ejemplo con lista de números')

# => lista de números
lista = [1,2,3,4,5]
print('lista =', lista)

# => reduce normal sin valor inicial
suma_valores = functools.reduce(
    lambda x,y : x + y,
    lista
)

print('\nSuma de Valores sin Valor Inicial:')
print( suma_valores, type(suma_valores) )

# => reduce con valor inicial
suma_valores_mas_100 = functools.reduce(
    lambda x,y : x + y,
    lista,
    100 # valor inicial para el reduce
)

print('\nSuma de Valores con Valor Inicial = 100:')
print( suma_valores_mas_100, type(suma_valores_mas_100) )



#? 3) Ejemplo con string - cadena de texto
print('\n3) Ejemplo con string - cadena de texto')

nombres = ['Santi', 'Edu', 'Martín', 'Paola']

saludo = functools.reduce(
    lambda x, y : x + ', ' + y,
    nombres,
    'HOLA!'
)

print(saludo)