# ==============================================================
# Interacción con while

# - con el conocimiento de while ya podemos hacer varias cosas
# - ej: una interacción dinámica con el usuario
# - while + if ya nos permiten hacer muchas cosas
# ==============================================================

#? 1) Forzar al usuario ingresar siempre un valor
print('\n1) Forzar al usuario ingresar siempre un valor\n')

'''
nombre = '' # una manera de inicializar una variable string

while len(nombre) == 0:
    nombre = input('Ingrese su nombre: ')
# end while

print('Su nombre es:', nombre)
'''

#? 2) Otra manera => con operador lógico not
print('\n2) Otra manera => con operador lógico not\n')
#! Tema un poco avanzado

'''
#! RECORDAR: valor booleano en las variables
cadena_1 = 'A'
cadena_2 = ' '
cadena_3 = ''
val_1 = None

print( 'cadena_1 =' , cadena_1 , '|', type(cadena_1), bool(cadena_1) )
print( 'cadena_2 =' , cadena_2 , '|', type(cadena_2), bool(cadena_2) )
print( 'cadena_3 =' , cadena_3 , '|', type(cadena_3), bool(cadena_3) )
print( 'val_1 =' , val_1 , '|', type(val_1), bool(val_1) )

# - Recordar que una cadena vacía (sin ni siquiera espacios)
# - Y un valor de tipo None
# - entre muchos otros casos
# - nos dan un valor booleano False

#nombre = ' ' # => ni siquiera entra a while
nombre = ''

while not nombre:
    nombre = input('Ingrese por favor su nombre: ')
# end while

print('Su nombre es:', nombre)

#* NOTA:
# - al poner variable dentro de while
# - se está analizando su valor booleano
'''


#? 3) Error a evitar => usando comparación ==
print('\n3) Error a evitar => usando comparación ==\n')
#! No utilizar la comparación para esto

# ej:
nombre = ''

# si hacemos lo siguiente:
print( "nombre = ''" )
print( nombre == False ) # False
print( nombre == True ) # False

nombre = 'A'

print( "\nnombre = 'A'" )
print( nombre == False ) # False
print( nombre == True ) # False

# => lo que evaluamos con '==' => es el valor de la variable
# '==' => es un operador booleano de comparación
# por tanto esta manera en el bucle while es errónea

nombre = ''

while nombre == False:
    nombre = input('Ingrese su nombre: ')
# end while

# => ni siquiera entramos en bloque while
# una manera correcta sería con casting bool()

while bool(nombre) == False:
    nombre = input('Ingrese su nombre: ')


