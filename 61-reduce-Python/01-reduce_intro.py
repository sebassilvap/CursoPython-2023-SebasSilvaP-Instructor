# =============================================================================
# sort / map / filter / reduce
# => reduce en Python

# https://thepythonguru.com/python-builtin-functions/reduce/

# *      reduce(función , elemento_iterable)

# -   reduce => acepta una función para retornar UN SOLO valor
# -   al inicio la función se llama con los primeros 2 ítems de la secuencia
# -   este resultado es retornado
# -   la función se llama de nuevo y se aplica con el valor del primer retorno
# -   y el siguiente valor de la colección (en este caso el 3er item)
# -   así sucesivamente hasta terminar los elementos de la colección

# ?   IMPORTANTE
# -   Para usarla debemos importar la librería/módulo functools
# -   RECORDAR: devuelve al final 1 SÓLO VALOR!! (reduce todo a 1 valor)

# =============================================================================


#? 1) Primer Paso: importación de functools
print('\n1) Primer Paso: importación de functools')

import functools



#? 2) Ejemplo básico con valores numéricos
print('\n2) Ejemplo básico con valores numéricos')
# - si se trata de algo tan básico como una lista de números
# - en lugar de reduce tenemos la función interna sum
# - o el fsum de la librería math
# - este ejemplo básico es más para fines demostrativos

compras_usd = [100.50, 200, 85, 15, 20.99]


# => función para reduce
funcion_suma = lambda x,y : x + y

# => aplicando functools.reduce
precio_total = functools.reduce(funcion_suma, compras_usd)
print(precio_total)


# => OTRA MANERA: función sum()
precio_total_2 = sum(compras_usd)
print(precio_total_2)


# => también podríamos hacer otras operaciones
# - y de paso demostramos la utilización de lambda
# - en la misma línea de código de la función reduce

valores = (1,2,3,4,5,6,7,8,9,10)

suma = functools.reduce(
    lambda x,y : x + y,
    valores
)

resta = functools.reduce(
    lambda x,y : x - y,
    valores
)

producto = functools.reduce(
    lambda x,y : x * y,
    valores
)

division = functools.reduce(
    lambda x,y : x / y,
    valores
)

print(valores)
print(suma, resta, producto, division)



#? 3) Fijar la colección como una expresión iterable
print('\n3) Fijar la colección como una expresión iterable')

# ------------------------------------------
# EJEMPLO: cálculo de factorial
print('\nEJEMPLO: cálculo de factorial\n')
# ------------------------------------------
# - podemos usar range por ejemplo
# - como una expresión iterable

def factorial(x):
    return functools.reduce(
        lambda x, y : x * y,
        range(1, x+1) # recordar: start - incluyente / end - excluyente
    )
# end def

# => TEST
factorial_3 = factorial(3)
factorial_5 = factorial(5)

print('factorial_3 =', factorial_3)
print('factorial_5 =', factorial_5)



#? 4) Usando valores NO numéricos => ej: string
print('\n4) Usando valores NO numéricos => ej: string')

cadena = ['p', 'y', 't', 'h', 'o', 'n']

palabra = functools.reduce(
    lambda x,y : x + y, # en este caso no es suma es concatenación
    cadena
)

print(palabra)

# => tenemos una manera más sencilla de hacer esto
palabra_2 = ''.join(cadena)
print(palabra)


# => pero con reduce podríamos jugar un poco

palabra_3 = functools.reduce(
    lambda x,y : (x + '--' + y).upper(),
    cadena
)

print(palabra_3)



#? 5) reduce | sum | fsum | bucles => perfectamente aplicable a lista | tupla | set => 1D
print('\n5) reduce | sum | fsum | bucles => perfectamente aplicable a lista | tupla | set => 1D')

import math # para utilizar fsum

# -------------------------------------------
# => ejemplo lista | tupla | set
print('\n=> ejemplo lista | tupla | set\n')
# -------------------------------------------

lista = [100, 150, 300]
tupla = (80, 50, 100, 20)
conjunto = {10, 20, 30, 40}

print('lista =', lista)
print('tupla =', tupla)
print('conjunto =', conjunto)


# -------------------------------------------------
# => aplicando función interna : sum()
print('\n=> aplicando función interna : sum()\n')
# -------------------------------------------------

print( 'sum(lista) =', sum(lista) )
print( 'sum(tupla) =', sum(tupla) )
print( 'sum(conjunto) =', sum(conjunto) )


# -------------------------------------
# => aplicando math.fsum()
print('\n=> aplicando math.fsum()\n')
# ------------------------------------
# * RECORDAR: devuelve como float

import math

print( 'math.fsum(lista) =', math.fsum(lista) )
print( 'math.fsum(tupla) =', math.fsum(tupla) )
print( 'math.fsum(conjunto) =', math.fsum(conjunto) )


# -----------------------------------
# => aplicando bucle for
print('\n=> aplicando bucle for\n')
# -----------------------------------

# suma de elementos / lista
suma_lista_for = 0
for x in lista:
    suma_lista_for += x
# end for

# suma de elementos / tupla
suma_tupla_for = 0
for x in tupla:
    suma_tupla_for += x
# end for

# suma de elementos / set
suma_conjunto_for = 0
for x in conjunto:
    suma_conjunto_for += x
# end for

print('suma_lista_for =', suma_lista_for)
print('suma_tupla_for =', suma_tupla_for)
print('suma_conjunto_for =', suma_conjunto_for)


# -------------------------------------
# => aplicando bucle while
print('\n=> aplicando bucle while\n')
# -------------------------------------

# suma de elementos / lista
suma_lista_while = 0
i = 0 # index-counter

while i < len(lista):
    suma_lista_while += lista[i]
    i += 1
# end while
    
    
# suma de elementos / tupla
suma_tupla_while = 0
i = 0 # index-counter

while i < len(tupla):
    suma_tupla_while += tupla[i]
    i += 1
# end while
    
    
# suma de elementos / set
# ! no es posible => el set no puede accederse con index
"""
suma_conjunto_while = 0
i = 0 # index-counter

while i < len(conjunto):
    suma_conjunto_while += conjunto[i]
    i += 1
# end while
"""
#! TypeError: 'set' object is not subscriptable

print( 'suma_lista_while =', suma_lista_while )
print( 'suma_tupla_while =', suma_tupla_while )


# --------------------------------
# => aplicando reduce
print('\n=> aplicando reduce\n')
# --------------------------------

suma_lista_reduce = functools.reduce(
    lambda x,y : x + y,
    lista
)

suma_tupla_reduce = functools.reduce(
    lambda x,y : x + y,
    tupla
)

suma_conjunto_reduce = functools.reduce(
    lambda x,y : x + y,
    conjunto
)

print( 'suma_lista_reduce =', suma_lista_reduce )
print( 'suma_tupla_reduce =', suma_tupla_reduce )
print( 'suma_conjunto_reduce =', suma_conjunto_reduce )