# ==============================================================
# Método .copy() en listas

# - Un método muy importante
# - Permite crear una copia de una lista
# - Recordar que hay métodos que modifican la lista original
# - Podemos evitar esta modificación
# - Modificando pero en la copia de la lista
# ==============================================================


#? 1) Dirección de la memoria de variables básicas
print('\n1) Dirección de la memoria de variables básicas')

num_1 = 10
print(num_1)

num_2 = num_1
print(num_1 , num_2)

num_1 = 5
# => ¿cambia num_2?
print(num_1 , num_2)


#   ¿POR QUÉ?
# - al hacer num_2 = num_1
# - asignamos el mismo valor y el mismo espacio en la memoria para ambas variables
# - pero al reasignar num_1
# num_1 = 5
# - estamos creando nuevamente la variable
# - tiene un nuevo espacio en la memoria
# - num_1 y num_2 son independientes ahora



#? 2) Dirección de la memoria en listas
print('\n2) Dirección de la memoria en listas')
# - lo mismo pasa con listas
# - RECORDAR: cuando hay reasignación
# - es como si se vuelve a crear la variable
# - se tiene entonces una nueva variable

lista_1 = [1,2,3]
print(lista_1)

lista_2 = lista_1
print(lista_1 , '|' , lista_2)

lista_1 = ['a', 'b', 'c']
print(lista_1 , '|' , lista_2)

lista_1 = [100,200,300]
print(lista_1 , '|' , lista_2)

# - sin embargo, en las listas
# - nosotros podemos modificar la lista
# - sin necesidad de volver a reasignar



#? 3) Modificando la lista
print('\n3) Modificando la lista')

lista_1 = [1,2,3]
lista_2 = lista_1
print(lista_1 , '|' , lista_2)

# => modificando lista_1
lista_1[0] = 'AAA'
print(lista_1 , '|' , lista_2)

# - los cambios se ven también en la lista_2

# => modificando lista_1
lista_1.append('ZZZ')
print(lista_1 , '|' , lista_2)

# => modificando lista_2
lista_2.append('python')
print(lista_1 , '|' , lista_2)

# - Por tanto:
# - Cuando se crea una lista a partir de otra
# - Al crear así, ambas se crean con la misma dirección en la memoria
# - Y cualquier cambio en una de ellas, afecta a ambas

# => utilizando múltiple asignación
print()
lista_1 = lista_2 = lista_3 = lista_4 = ['A', 'B', 'C']
print(lista_1, '|', lista_2, '|', lista_3, '|', lista_4)

lista_3.pop()
print(lista_1, '|', lista_2, '|', lista_3, '|', lista_4)

# - Esto puede ser un problema
# - Por tanto no es recomendable crear listas de esta manera
# - Pero si es necesario crear una lista a partir de otra
# - Podemos utilizar el método .copy()


#? 4) Utilizando .copy()
print('\n4) Utilizando .copy()')
# - Permite crear una copia de los valores de una lista
# - Sin crear el mismo espacio en la memoria

lista_1 = [1,2,3]

lista_2 = lista_1.copy() # creando copia de lista

print(lista_1, '|', lista_2)

lista_1.append('A')
lista_2.append('Z')

print(lista_1, '|', lista_2) # lista_1 y lista_2 son INDEPENDIENTES