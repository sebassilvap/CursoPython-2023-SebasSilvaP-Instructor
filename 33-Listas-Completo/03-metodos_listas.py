# ==============================================================
# Métodos de Listas
# - Python tiene elementos internos
# - para poder trabajar con listas
#! OJO: muchos de estos modifican la lista original

# https://www.w3schools.com/python/python_lists_methods.asp
# ==============================================================

#? 1) .index()
print('\n1) .index()')
# - devuelve el índice de una búsqueda

# EJ:
lista = ['x', 'y', 'z', 100, 200, 300, True]
#         0    1    2     3   4    5    6

print( lista.index('z') )
print( lista.index(True) )
print( lista.index(200) )

# => si la búsqueda no existe - ValueError
#print( lista.index('SEBAS') )
#! ValueError: 'SEBAS' is not in list


#? 2) .append()
print('\n2) .append()')
# - para agregar elemento
# - al FINAL de la lista
#* modifica la lista original

lista = ['x', 'y', 'z', 100, 200, 300, True]

print(lista, len(lista))

lista.append('sebas')

print(lista, len(lista))


#? 3) .insert()
print('\n3) .insert()')
# - para insertar un elemento en una posición exacta
# - recibe 2 argumentos
# .insert(index, elemento)
#* modifica la lista original

lista = ['x', 'y', 'z', 100, 200, 300, True]
#(+)      0    1    2    3    4    5    6
#(-)      7    6    5    4    3    2    1

print(lista, len(lista))

lista.insert(2,'hola')
print(lista, len(lista))

lista.insert(-3,'python')
print(lista, len(lista))

# => inserta y desplaza a la derecha el resto

# insertando en un índice que no existe
print()
lista = ['x', 'y', 'z', 100, 200, 300, True]
#(+)      0    1    2    3    4    5    6
#(-)      7    6    5    4    3    2    1

lista.insert(20,'python')
print(lista, len(lista)) # => no da error pero inserta al final

lista.insert(-10,'python')
print(lista, len(lista)) # => no da error pero inserta al inicio


#? 4) del lista[indice]
print('\n4) del lista[indice]')
# - eliminar un elemento de la lista
# - proporcionando la lista y el índice
# - el índice entre corchetes
#* modifica la lista original

lista = ['x', 'y', 'z', 100, 200, 300, True]
#(+)      0    1    2    3    4    5    6

print(lista, len(lista))

del lista[3]
print(lista, len(lista))

# => si tratamos de eliminar un índice que no existe
'''
del lista[100]
print(lista, len(lista))
'''
#! IndexError: list assignment index out of range


#? 5) .pop()
print('\n5) .pop()')
# - por defecto: elimina último elemento de la lista
# - también se puede especificar el índice del elemento a eliminar
# - devuelve el elemento eliminado
#* modifica la lista original

# -------------
# por defecto
print('\npor defecto')
# -------------
lista = ['x', 'y', 'z', 100, 200, 300, True]
#         0    1    2     3   4    5    6

print(lista, len(lista))

lista.pop()

print(lista, len(lista))

# ---------------------
# especificando index
print('\nespecificando index')
# ---------------------
lista = ['x', 'y', 'z', 100, 200, 300, True]
#         0    1    2     3   4    5    6
print(lista, len(lista))

lista.pop(4)
print(lista, len(lista))

# -------------------------------
# retorna el elemento eliminado
print('\nretorna el elemento eliminado')
# -------------------------------

lista = ['x', 'y', 'z', 100, 200, 300, 'AAA', 'BBB']
#         0    1    2     3   4    5    6      7

print(lista, len(lista))

elemento_eliminado = lista.pop()
print(lista, len(lista))
print(elemento_eliminado)

elemento_eliminado = lista.pop()
print(lista, len(lista))
print(elemento_eliminado)

# sin guardarlo en una variable
print(lista.pop())


lista = ['x', 'y', 'z', 100, 200, 300, 'AAA', 'BBB']
#         0    1    2     3   4    5    6      7

#lista.pop(9) # un índice que no existe -> me da error
#! IndexError: pop index out of range


#? 6) .remove()
print('\n6) .remove()')
# - elimina un elemento de la lista
# - el elemento lo pasamos como parámetro
#* modifica la lista original

lista = ['x', 'y', 'z', 100, 200, 300, 'AAA', 'BBB']
#         0    1    2     3   4    5    6      7

print(lista, len(lista))

lista.remove('AAA')
print(lista, len(lista))

#lista.remove('ZZZ') # cuando no existe el elemento me da error
#! ValueError: list.remove(x): x not in list

# ------------------------------------------
#* RECORDAR
# 3 maneras de eliminar elementos en listas:

# 1)  del lista[indice]
# 2)  .pop()
# 3)  .remove()
# ------------------------------------------


#? 7) .sort()
# - para ordenar listas
# - recibe 2 argumentos: reverse & key
#* modifica la lista original

lista_1 = ['Sebas', 'Ximena', 'Daniel', 'Mauro', 'Beto']
lista_2 = [10, -80, 0, 6.5, -8.9, -20, 15]

print(lista_1)
print(lista_2)


# 7.1) sort por defecto
print('\n7.1) sort por defecto')
# - por defecto: orden ascendente
# - (A-Z) & menor a mayor

lista_1.sort()
lista_2.sort()

print(lista_1)
print(lista_2)


# 7.2) sort con reverse True
print('\n7.2) sort con reverse True')
# - orden descendente
# - (Z-A) & mayor a menor

lista_1.sort(reverse=True)
lista_2.sort(reverse=True)

print(lista_1)
print(lista_2)

# - reverse=False => por defecto
# - o también no se lo pone
print()

lista_1.sort(reverse=False)
lista_2.sort(reverse=False)

print(lista_1)
print(lista_2)

# 7.3) sort con key
print('\n7.3) sort con key')
# - key permite un ordenado especial
# - en función a una característica de la lista

lista = ['superPalabraGrande', 'sol', 'amigos', 'palabra']
print(lista)

lista.sort()
print(lista)

lista.sort(reverse=True)
print(lista)

lista.sort(key=len) # ordena en función al tamaño del string
# => palabra más pequeña a más grande
print(lista)

lista.sort(key=len, reverse=True)
# => palabra más grande a más pequeña
print(lista)


#? 8) sorted()
print('\n8) sorted()')
# - a diferencia de sort no me afecta la lista original
# sorted( lista , reverse, key )

# 8.1) sorted() por defecto
print('\n8.1) sorted() por defecto')
# - por defecto: orden ascendente
# - (A-Z) & menor a mayor

lista_1 = ['Andres', 'Carlos', 'Ximena', 'Karla']
lista_2 = [10, -80, 0, 6.5, -8.9, -20, 15]

# aplicando sorted()
sorted(lista_1)
sorted(lista_2)

print('\nlistas originales:\n')
print(lista_1)
print(lista_2)

print('\nlistas con sorted():\n')
print( sorted(lista_1) )
print( sorted(lista_2) )

# => por tanto tendría más sentido guardar en una variable

lista_1_ordenada = sorted(lista_1)
lista_2_ordenada = sorted(lista_2)

print('\nlistas originales:\n')
print(lista_1)
print(lista_2)

print('\nlistas creadas:\n')
print( lista_1_ordenada )
print( lista_2_ordenada )

# => de igual manera funciona si ponemos el reverse en False

lista_1_ordenada = sorted(lista_1 , reverse=False)
lista_2_ordenada = sorted(lista_2 , reverse=False)

print('\nlistas originales:\n')
print(lista_1)
print(lista_2)

print('\nlistas creadas con reverse=False:\n')
print( lista_1_ordenada )
print( lista_2_ordenada )


# 8.2) sorted() con reverse True
print('\n8.2) sorted() con reverse True')
# - orden descendente
# - (Z-A) & mayor a menor

lista_1 = ['Andres', 'Carlos', 'Ximena', 'Karla']
lista_2 = [10, -80, 0, 6.5, -8.9, -20, 15]

lista_1_sorted = sorted(lista_1, reverse=True)
lista_2_sorted = sorted(lista_2, reverse=True)

print('\nlistas originales:\n')
print(lista_1)
print(lista_2)

print('\nlistas creadas con reverse=True:\n')
print( lista_1_sorted )
print( lista_2_sorted )


# 8.3) sorted() con key
print('\n8.3) sorted() con key')
# - key permite un ordenado especial
# - en función a una característica de la lista

lista = ['superPalabraGrande', 'sol', 'amigos', 'palabra']


print('\nsorted() + key + reverse=False\n')

lista_orden_len = sorted(lista, key=len)

print('ORIGINAL =', lista)
print(lista_orden_len)

lista_orden_len = sorted(lista, key=len, reverse=False)
print(lista_orden_len)


print('\nsorted() + key + reverse=True\n')

print('ORIGINAL =', lista)
lista_orden_len = sorted(lista, key=len, reverse=True)
print(lista_orden_len)


#? 9) .split()
print('\n9) .split()')
# - para dividir un string
# - en elementos de lista

# => por defecto divide tomando en cuenta los espacios

mensaje = 'Queridos estudiantes les saludo desde Alemania'
print(mensaje, type(mensaje))

lista_palabras = mensaje.split()
print(lista_palabras, type(lista_palabras), len(lista_palabras))


# => podemos especificar el caracter a dividir
print()
texto_1 = 'python,java,javascript,c++,pascal'
print(texto_1)
print(texto_1.split(','))

print()
texto_2 = 'manzana/banana/pera/durazno*sandia'
print(texto_2)
print(texto_2.split('/'))


#? 10) .join()
print('\n10) .join()')
# - para formar un string
# - aplicable a lista o string

# => aplicado a un string
caracter = '*'
palabra = 'python'

print( caracter.join(palabra) )


# => aplicado a listas
lista = ['Carlos','Andres','Sebas','Karla']

caracter = '--'

print(caracter.join(lista))
print('***'.join(lista))

# guardando en una variable
cadena = caracter.join(lista)
print(cadena, type(cadena))


#? 11) .list()
print('\n11) .list()')
# - casting a lista
# - también: para crear lista o lista vacía

# => crear lista / crear lista vacía
lista = list([1,2,3,4,5])
lista_vacia = list()

print(lista, len(lista))
print(lista_vacia, len(lista_vacia))

# => casting de string a lista
print()
cadena = 'python'
lista = list(cadena)
print(cadena)
print(lista)

# => casting de range a lista
print()
rango = range(1,11)
lista = list(rango)

print( rango, type(rango) )
print( lista, type(lista) )


#? 12) .clear()
print('\n12) .clear()')
# - deja la lista en blanco
#* modifica la lista original

lista = ['Carlos','Andres','Sebas','Karla']
print(lista, len(lista))

lista.clear()
print(lista, len(lista))

lista.append('A')
print(lista, len(lista))


#? 13) .count()
print('\n13) .count()')
# - para contar coincidencias
# - de un elemento en la lista

numeros = [1,2,3,4,5,1,6,9,8,1,2]

print(numeros)

print(numeros.count(1))
print(numeros.count(2))


#? 14) .extend()
print('\n14) .extend()')
# - otra manera de concatenar
# - pero modifica la lista original

lista_1 = ['A', 'B', 'C']
lista_2 = [100, 200, 300]

print('lista_1 =', lista_1)
print('lista_2 =', lista_2)

# extend a lista_1
print('\nextend a lista_1\n')

lista_1.extend(lista_2)
print('lista_1 =', lista_1)
print('lista_2 =', lista_2)

# extend a lista_2
print('\nextend a lista_2\n')

lista_1 = ['A', 'B', 'C']
lista_2 = [100, 200, 300]

lista_2.extend(lista_1)
print('lista_1 =', lista_1)
print('lista_2 =', lista_2)

# usando concatenacion
print('\nusando concatenacion\n')

lista_1 = ['A', 'B', 'C']
lista_2 = [100, 200, 300]

lista_1 = lista_1 + lista_2
print('lista_1 =', lista_1)
print('lista_2 =', lista_2)


#? 15) .reverse()
print('\n15) .reverse()')
# - para revertir el orden de la lista
# * modifica la lista original

lista_1 = [1,2,3,4,5]
lista_2 = ['python', 'java', 'c++', 'pascal']

print('\nListas Originales\n')
print(lista_1)
print(lista_2)

print('\nAplicando .reverse()\n')
lista_1.reverse()
lista_2.reverse()

print(lista_1)
print(lista_2)