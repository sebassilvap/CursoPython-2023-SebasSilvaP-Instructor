# ==========================================================================
# Palabra Clave / Keyword => is

# - es básicamente una comprobación
# - más fuerte y estricta que el "=="

# *   ==    |    comprueba si 2 variables tienen el mismo valor
# *   is    |    tienen el mismo valor y la misma dirección de la memoria


# https://www.w3schools.com/python/ref_keyword_is.asp#:~:text=Definition%20and%20Usage,if%20two%20variables%20are%20equal.

# ==========================================================================


#? 1) Con variables Básicas => ninguna diferencia
print('\n1) Con variables Básicas => ninguna diferencia')
# - Variables Básicas
# *      int  float  bool  str
# - aquí da lo mismo usar "=="  ó  "is"

# -------------------------------------------------------------------
# (A) Si se crean con distinto valor - diferente espacio de memoria
# (B) Si se crean con el mismo valor - igual espacio de memoria
# -------------------------------------------------------------------

num_1 = 10
num_2 = 20
num_3 = 10
num_4 = num_1

print( hex(id(num_1)) )
print( hex(id(num_2)) ) # este es el único distinto
print( hex(id(num_3)) )
print( hex(id(num_4)) )

# TEST
print('\nTEST:')
print( num_1 == num_2, '|', num_1 is num_2 ) # False
print( num_1 == num_3, '|', num_1 is num_3 ) # True
print( num_1 == num_4, '|', num_1 is num_4 ) # True



#? 2) Con variables MUTABLES => es distinto
print('\n2) Con variables MUTABLES => es distinto')
# - nuestro ejemplo clásico de elemento MUTABLE => lista

lista_1 = [1,2,3]
lista_2 = [1,2,3]
lista_3 = lista_1
lista_4 = [10,20,30]

# TEST
print('\nTEST:')
print( lista_1 == lista_2, '|', lista_1 is lista_2 ) # True | False
print( lista_1 == lista_3, '|', lista_1 is lista_3 ) # True | True
print( lista_1 == lista_4, '|', lista_1 is lista_4 ) # False | False



#? 3) Ejemplos que podemos ver en algunos códigos:
print('\n3) Ejemplos que podemos ver en algunos códigos:')

# ----------------------------
# 3.1) Ejemplo 1:
print('\n3.1) Ejemplo 1:\n')
# ----------------------------
# => RECORDAR:
# - con variables básicas no habría problema
edad = 14

if edad == 18:
    print('Tiene 18 años!')
else:
    print('No tiene 18 años')
# end if

if edad is 18:
    print('Tiene 18 años!')
else:
    print('No tiene 18 años')
# end if


# ----------------------------
# 3.2) Ejemplo 2:
print('\n3.2) Ejemplo 2:\n')
# ----------------------------

a = 2
b = 10
#b = 2


if a != b:
    print('a y b NO son iguales')
else:
    print('a es igual a b')
# end if


if a is not b:
    print('a y b NO son iguales')
else:
    print('a es igual a b')
# end if