# =================================
# Listas - Completo
# => Recordatorio de Fundamentos

# - Creación
# - Lista Vacía
# - Función len()
# - Concatenación
# =================================

#? 1) Creación de Listas
print('\n1) Creación de Listas')
# - una lista se crea con corchetes []
# - y separando los elementos con coma

lista_numeros = [1,2,3,4,5]
print(lista_numeros, type(lista_numeros))

# - puede albergar varios tipos de datos
lista = ['A', True, 100, 5.5, None]

print()
print( lista, type(lista) )
print( lista[0], type(lista[0]) )
print( lista[1], type(lista[1]) )
print( lista[2], type(lista[2]) )
print( lista[3], type(lista[3]) )
print( lista[4], type(lista[4]) )

# - puede albergar incluso otras listas
lista = [1,2,3, ['a', 'b', 'c']]

print()
print(lista)
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])

# - también se la puede crear de manera mucho más formal
# - utilizando la función list
# - el cual sirve también para hacer casting a lista

lista_1 = list( [1,2,3] )
lista_2 = list( range(1,11,2) )

print()
print( lista_1, type(lista_1) )
print( lista_2, type(lista_2) )


#? 2) Creación Lista Vacía
print('\n2) Creación Lista Vacía')
# - Nos sirve para iniciar un valor de lista
# - Y poder trabajarlo luego

lista_numeros = []
print(lista_numeros)

for i in range(1,6):
    lista_numeros.append(i)

print(lista_numeros)

# - podemos iniciar también con un list() vacío
lista_vacia = list()

print(lista_vacia, type(lista_vacia))


#? 3) Función len()
print('\n3) Función len()')
# - len() => devuelve el número de elementos
# - de un elemento iterable

string = 'python'
lista = [1,2,3,4,5]

print( len(string) )
print( len(lista) )


#? 4) in + Listas
print('\n4) in + Listas')
# - una manera de averiguar si un elemento está en una lista
lista = [10, True, 'hola', -5.5]

print( 20 in lista )
print( False in lista )
print( 'hola' in lista )


#? 5) Concatenación
print('\n5) Concatenación')
# - al igual que strings
# - une una lista con otra

lista_1 = ['a', 'b', 'c']
lista_2 = [100, 200, 300]

print( lista_1 + lista_2 )
print( lista_2 + lista_1 )

# => guardar en variable
resultado_1 = lista_1 + lista_2
resultado_2 = lista_2 + lista_1

print(resultado_1)
print(resultado_2)


#? 6) Operador * en listas
print('\n6) Operador * en listas')
# - repite el número de veces indicado

numeros = [100,200,300]

numeros_x_2 = numeros * 2
numeros_x_3 = numeros * 3

print(numeros, len(numeros))
print(numeros_x_2, len(numeros_x_2))
print(numeros_x_3, len(numeros_x_3))

#resultado_raro = numeros * 'A'
#! TypeError: can't multiply sequence by non-int of type 'str'
