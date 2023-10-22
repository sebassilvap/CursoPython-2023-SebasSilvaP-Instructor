# ================================================================================
# Python - List Comprehension
# (Comprensión / Entendimiento de Listas)

# - básicamente es una manera corta de crear una lista
# - (se podría ver como una manera dinámica / inteligente)
# - con una sintaxis más reducida y menos líneas de código
# - se tienen 3 tipos de sintaxis que se pueden usar:

#*    A) lista = [ expresión + bucle FOR en un iterable ]
#*    B) lista = [ expresión + bucle FOR en un iterable + condicional IF ]
#*    C) lista = [ expresión + condicional IF/ELSE + bucle FOR en un ITERABLE ]

# - en esta primera introducción vamos a analizar
# - cada una de estas 3 sintaxis por medio de ejemplos sencillos

# https://www.w3schools.com/python/python_lists_comprehension.asp

# ================================================================================

# !   NOTA:
# -   para los siguientes ejemplos vamos a considerar un range
# -   como elemento iterable
# -   pero como sabemos existen varios elementos iterables en Python !!


#? A) lista = [ expresión + bucle FOR en un iterable ]
print('\nA) lista = [ expresión + bucle FOR en un iterable ]')

# -------------------------------------------
# 1.1) Planteamiento del Ejemplo
print('\n1.1) Planteamiento del Ejemplo\n')
# -------------------------------------------

# EJEMPLO:
# INICIO    =>  [1, 2, 3, 4, 5]
# RESULTADO =>  [3, 6, 9, 12, 15]

print('INICIO    =>  [1, 2, 3, 4, 5]')
print('RESULTADO =>  [3, 6, 9, 12, 15]')


# --------------------------------------
# 1.2) Solución Tradicional
print('\n1.2) Solución Tradicional\n')
# --------------------------------------

resultado_1 = []
#resultado_1 = list() # otra manera de iniciar lista vacía

for x in range(1,6):
    resultado_1.append(x * 3)
# end for

print('resultado_1 =', resultado_1)


# -------------------------------------------------
# 1.3) Solución con List Comprehension
print('\n1.3) Solución con List Comprehension\n')
# -------------------------------------------------

resultado_2 = [ 3*x for x in range(1,6) ] # 1 LÍNEA DE CÓDIGO !!!
print('resultado_2 =', resultado_2)

# => buena práctica inicial:
# poner en nuestras palabras lo que hace Python
"""
Devolver lista de 3 * x
siendo x una lista inicial
formada por un rango que va del 1 al 5
"""



#? B) lista = [ expresión + bucle FOR en un iterable + condicional IF ]
print('\nB) lista = [ expresión + bucle FOR en un iterable + condicional IF ]')

# -------------------------------------------
# 2.1) Planteamiento del Ejemplo
print('\n2.1) Planteamiento del Ejemplo\n')
# -------------------------------------------

# EJEMPLO:
# INICIO    =>  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# RESULTADO =>  [102, 104, 106, 108, 110]

print('INICIO    =>  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]')
print('RESULTADO =>  [102, 104, 106, 108, 110]')

# - básicamente, el resultado son los números pares
# - del 1 al 10
# - sumados 100


# --------------------------------------
# 2.2) Solución Tradicional
print('\n2.2) Solución Tradicional\n')
# --------------------------------------

resultado_1 = []

for x in range(1,11):
    if x % 2 == 0:
        resultado_1.append(x + 100)
    # end if
# end for

print('resultado_1 =', resultado_1)


# -------------------------------------------------
# 2.3) Solución con List Comprehension
print('\n2.3) Solución con List Comprehension\n')
# -------------------------------------------------

resultado_2 = [ 100 + x for x in range(1,11) if x % 2 == 0 ] 
print('resultado_2 =', resultado_2)

# => buena práctica inicial:
# poner en nuestras palabras lo que hace Python
"""
Devolver lista de 100 + x
siendo x una lista inicial
formada por un rango que va del 1 al 10
siempre y cuando el módulo de x para 2 sea 0
"""



#? C) lista = [ expresión + condicional IF/ELSE + bucle FOR en un ITERABLE ]
print('\nC) lista = [ expresión + condicional IF/ELSE + bucle FOR en un ITERABLE ]')
# - si utilizamos esta sintaxis con if al inicio
# ! SIEMPRE utilizar else
# - caso contrario va a dar error

# ------------------------------------------------------------
# 3.1) Ejemplo Anterior - ERROR sin utilizar else
print('\n3.1) Ejemplo Anterior - ERROR sin utilizar else\n')
# ------------------------------------------------------------

resultado = [ 100 + x for x in range(1,11) if x % 2 == 0 ] 
print('resultado_2 =', resultado_2)

#resultado = [ 100 + x if x % 2 == 0 for x in range(1,11) ]
#! SyntaxError: expected 'else' after 'if' expression


# -------------------------------------------
# 3.2) Planteamiento del Ejemplo
print('\n3.2) Planteamiento del Ejemplo\n')
# -------------------------------------------

# EJEMPLO:
# INICIO    =>  [1, 2, 3, 4, 5]
# RESULTADO =>  [impar, par, impar, par, impar]

print('INICIO    =>  [1, 2, 3, 4, 5]')
print('RESULTADO =>  [impar, par, impar, par, impar]')


# --------------------------------------
# 3.3) Solución Tradicional
print('\n3.3) Solución Tradicional\n')
# --------------------------------------

resultado_1 = []

for x in range(1,6):
    if x % 2 == 0:
        resultado_1.append('par')
    else:
        resultado_1.append('impar')
    # end if
# end for

print('resultado_1 =', resultado_1)


# -------------------------------------------------
# 3.4) Solución con List Comprehension
print('\n3.4) Solución con List Comprehension\n')
# -------------------------------------------------

resultado_2 = [ 'par' if x % 2 == 0 else 'impar' for x in range(1,6) ] 
print('resultado_2 =', resultado_2)

# => buena práctica inicial:
# poner en nuestras palabras lo que hace Python
"""
Retornar una lista con la palabra "par"
si una variable de recorrido "x" tiene un módulo
evaluado en 2 igual a 0.
Caso contrario (else) retornar la palabra "impar".
Todo esto para x que recorre un rango del 1 al 5.
"""