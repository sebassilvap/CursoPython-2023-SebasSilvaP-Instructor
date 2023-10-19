# ==========================================================================
# sort / map / filter / reduce
# => sort en Python

# ! PARTE 2: Intentando .sort() en colecciones distintas a LISTAS

# - son funciones MUY, MUY importantes
# - al momento de trabajar con colecciones de datos
# - nos permiten masajear los datos 
# - no solo son importantes en Python, sino en algunos lenguajes
# - por ejemplo en la programación WEB, en javascript, son muy conocidas
# - para trabajar y presentar datos de manera personalizada

# * SORT
# => Clasificar datos
# - por ejemplo:
# - ordenar de mayor a menor / menor a mayor
# - ordenar alfabéticamente (A-Z) / (Z-A)
# - ordenar en base a algún criterio especial (ej: tamaño de palabra)

# => Existen 2 maneras de hacer "sort" en Python:

# ?   A) método .sort()   => sólo funciona en listas
# ?   B) función sorted() => para cualquier colección de datos
# ==========================================================================


#? 1) Intentando .sort() en elementos no LISTAS
print('\n1) Intentando .sort() en elementos no LISTAS')

tupla = (30,10,20)

conjunto = {3,1,2}

diccionario = {
    3 : 300,
    1 : 100,
    2 : 200
}

print( tupla, type(tupla) )
print( conjunto, type(conjunto) )
print( diccionario, type(diccionario) )

#tupla.sort()
#! AttributeError: 'tuple' object has no attribute 'sort'

#conjunto.sort()
#! AttributeError: 'set' object has no attribute 'sort'

#diccionario.sort()
#! AttributeError: 'dict' object has no attribute 'sort'



#? 2) ¿Posible Solución> => Casting a Lista + .sort() + Casting a Original
print('\n2) ¿Posible Solución> => Casting a Lista + .sort() + Casting a Original')

lista_tupla = list(tupla)
lista_conjunto = list(conjunto) 
lista_diccionario = list(diccionario)

print()

print( lista_tupla, type(lista_tupla) )
print( lista_conjunto, type(lista_conjunto) ) # NO tiene sentido
print( lista_diccionario, type(lista_diccionario) ) # NO tiene sentido

# => ¿Por qué no tiene sentido?
# ! para SET: 
# - desde un inicio no tiene sentido porque son elementos desordenados
# - así los cambiemos a lista y luego a set
# - luego van a volver a ser elementos desordenados
# - desde un inicio no tiene sentido ordenar SETS

# ! para DICCIONARIOS:
# - como vemos al hacer casting a lista
# - solo las claves se transforman a lista
# - por tanto no tiene sentido

# * para TUPLA:
# - con las tuplas podríamos aplicar este método

lista_tupla.sort()
tupla = tuple(lista_tupla)

print(tupla)

# ------------------------------------------------------------------
# => CONCLUSIÓN
# - .sort() no sería una manera viable
# - nos podría servir para tuplas, pero debemos hacer este proceso
# - diccionarios & tuplas => elementos además de listas
# - que tienen sentido ordenar
# - RECORDAR: diccionarios a partir de Python 3.7 + ==> Ordenados
# - SOLUCIÓN: aplicar función interna => sort()
# ------------------------------------------------------------------