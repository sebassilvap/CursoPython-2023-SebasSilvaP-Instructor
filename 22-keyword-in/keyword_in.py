# ========================================================================
# Palabra Clave / Palabra Reservada => in

# - para comprobar si un valor está dentro de una secuencia
# - devuelve un booleano => True / False
# - secuencia: listas, strings, rangos(*), etc...
# - veremos más adelante que es usada para la iteración en el bucle for

# - https://www.w3schools.com/python/ref_keyword_in.asp
# ========================================================================

#? 1) "in" + string
print('\n1) "in" + string')

cadena_1 = 'python'

print()
print('m' in cadena_1)  # False
print('o' in cadena_1)  # True
print('P' in cadena_1)  # False
print('y' in cadena_1)  # True
print('N' in cadena_1)  # False


#? 2) "in" + lista
print('\n2) "in" + lista')

lista = [100,200,True,-8.5,'nombre']

print()
print('100' in lista) # False
print('n' in lista) # False
print(1 in lista) # True => porque True es también 1
print(False in lista) # False

lista = ['','a','b']

print(False in lista) # False
print(True in lista) # False

lista = [5,6,7,0]

print(False in lista) # True => porque False es también 0
print(True in lista) # False

lista = [100,200,300]

print(False in lista) # False
print(True in lista) # False


#? 3) SALTO EN EL TIEMPO
print('\n3) SALTO EN EL TIEMPO')
# ! Bucle for con in
# - ya veremos a profundidad el tema bucles
# - pero el uso más común de for es para recorrer un elemento iterable
# - elementos iterables por el momento: listas, strings

nombre = 'sebas'
autos = ['Vitara', 'BMW', 'Ford', 'Ferrari']

# => recorrer un string
for x in nombre:
    print(x)
    
print()

# => recorrer una lista
for x in autos:
    print(x)

# - x, el nombre de la variable a recorrer es por el momento arbitrario
# - puede ser cualquier nombre
# - cuando se usa un bucle, condicional, etc, se crea un nuevo bloque de código
# - por el momento esto solo es una introducción muy breve
# - ya veremos este tema a profundidad

for n in nombre:
    print(n)