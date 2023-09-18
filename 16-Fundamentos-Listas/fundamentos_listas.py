# ==========================================================
# Listas

# - es el tipo más fundamental de las colecciones de datos
# - el tema colecciones lo vemos a profundidad más adelante
# - pero con lo que sabemos podemos ya entender las bases
# - no son más que una lista de valores separados con coma
# - y van entre corchetes
# - pueden almacenar varios tipos de datos
# ==========================================================

#? 1) Creación de una lista
print('\n1) Creación de una lista')

letras = ['a','b','c','d','e']
numeros = [10,20,30,40,50,60]
info_persona = ['Diego','Salas', 25, True, 17.5]

print( letras, type(letras) )
print( numeros, type(numeros) )
print( info_persona, type(info_persona) )


#? 2) Index y Slicing
# - al igual que los string
# - son elementos iterables / de secuencia
# - podemos acceder a sus elementos por medio de los índices
# - y a un subgrupo de sus valores por medio del Slicing
# - RECORDAR: que el índice inicia en 0
# - RECORDAR: el último elemento tiene índice -1

# => aplicando index
print('\n2.1) Index en Listas')

print( letras[0] , numeros[-1] )

nombre = info_persona[0]
apellido = info_persona[1]
edad = info_persona[2]
es_estudiante = info_persona[3]
nota_final = info_persona[4]

print( nombre )
print( apellido )
print( edad )
print( es_estudiante )
print( nota_final )

# => aplicando slicing
print('\n2.1) Slicing en Listas')
# RECORDAR: [start , end , step]
# - start => inclusivo
# - end   => exclusivo
# - step  => salto

letras_lista = ['a','b','c','d','e']
letras_string = 'abcde'

print( letras_lista[0:2] )
print( letras_string[0:2] )

print( letras_lista[-3:] )
print( letras_string[-3:] )

# aplicando salto
print( letras_lista[::2] )
print( letras_string[::2] )


#? 3) Concatenación en Listas
print('\n3) Concatenación en Listas')
numeros_1 = [1,2,3]
numeros_2 = [10,20,30]

lista_numeros = numeros_1 + numeros_2

print(numeros_1)
print(numeros_2)
print(lista_numeros)

# similar a la concatenación de strings
string_1 = '1,2,3'
string_2 = '10,20,30'

string_resultado = string_1 + string_2
print(string_1)
print(string_2)
print(string_resultado)


#? 4) función len()
print('\n4) función len()')
# - función len se aplica a algunos elementos
# - como vimos en los string nos devuelve el tamaño del mismo
# - en listas devuelve el número de elementos de la lista

string_1 = 'Python'
print( string_1 , len(string_1) ) # Python 6

lista = ['X','Y',10,20,True,False,-100.5]
print( lista , len(lista) )
# ['X', 'Y', 10, 20, True, False, -100.5] 7


#? 5) Las listas son MUTABLES
print('\n5) Las listas son MUTABLES')
# - RECORDAR: string (cadenas de texto) => INMUTABLES
# - Pero las listas si son MUTABLES
# - es decir, podemos reasignar sus elementos

# => Inmutabilidad del String
string = 'xyz'
print(string)
print(string[0])
print(string[1])
print(string[2])

#string[0] = 'A' #! TypeError => str no soporta asignación de sus ítems

# => Mutabilidad de Listas
lista = ['x' , 'y' , 'z']
print(lista)
print(lista[0])
print(lista[1])
print(lista[2])

lista[0] = 'AAAAA'
print(lista) # ['AAAAA', 'y', 'z']


#? 6) Podemos definirlas en varias líneas de código
print('\n6) Podemos definirlas en varias líneas de código')

# => ej: lista de estudiantes
lista_estudiantes = ['Carlos' , 'Andrea' , 'Marcelo']
print(lista_estudiantes)

lista_estudiantes = [
    'Andrea', #! no olvidar la coma al final
    'Sebastián',
    'Diego',
    'Marcelo'
]
print(lista_estudiantes)


#? 7) .append() => añadir un elemento al final de la lista
print('\n7) .append() => añadir un elemento al final de la lista')
# - uno de los elementos más importantes de las listas
# - veremos a profundidad luego el tema de colecciones y listas

print( lista_estudiantes , len(lista_estudiantes) )
lista_estudiantes.append('Santiago')
print( lista_estudiantes , len(lista_estudiantes) )
lista_estudiantes.append('Carla')
print( lista_estudiantes , len(lista_estudiantes) )


#? 8) Reasignación con Slicing
print('\n8) Reasignación con Slicing')

lista = [1,2,3,4,5,6]
print( lista , len(lista) )

print( lista[0:3] )
lista[0:3] = ['X' , 'Y' , 'Z']
print( lista , len(lista) )

# => ¿qué pasa si mandamos MENOS elementos?
lista[0:3] = [100 , 200]
print( lista , len(lista) ) # se eliminan los elementos que no mandamos

# => ¿qué pasa si mandamos MÁS elementos?
lista = [1,2,3,4,5,6]
print( lista , len(lista) )

lista[:3] = [100,200,300,400]
print( lista , len(lista) ) # se añaden los nuevos elementos

# => ¿si lo hacemos con el index?
lista = [1,2,3,4,5,6]
print( lista , len(lista) )

lista[2] = [100,200,300]
print( lista , len(lista) ) # se añade la lista como un elemento => listas anidadas


#? 9) Listas Anidadas
print('\n9) Listas Anidadas')
# - como vimos anteriormente podemos almacenar listas dentro de listas

# => Creación de una lista anidada
lista_anidada_1 = [
    [100,200,300],
    [400,500,600],
    [700,800,900],
]

lista_1 = ['A','B','C']
lista_2 = ['D','E','F']
lista_3 = ['X','Y','Z']

lista_anidada_2 = [lista_1, lista_2, lista_3]

print( lista_anidada_1 , type(lista_anidada_1) , len(lista_anidada_1) )
print( lista_anidada_2 , type(lista_anidada_2) , len(lista_anidada_2) )

# => Accediendo a los elementos
print( lista_anidada_2[0] , type(lista_anidada_2[0]) , len(lista_anidada_2[0]) )
print( lista_anidada_2[1] , type(lista_anidada_2[1]) , len(lista_anidada_2[1]) )
print( lista_anidada_2[2] , type(lista_anidada_2[2]) , len(lista_anidada_2[2]) )

# => Acceso con doble índice => doble corchete

print( lista_anidada_2[0][0] , type(lista_anidada_2[0][0]) , len(lista_anidada_2[0][0]) )
print( lista_anidada_2[0][1] , type(lista_anidada_2[0][1]) , len(lista_anidada_2[0][1]) )
print( lista_anidada_2[0][2] , type(lista_anidada_2[0][2]) , len(lista_anidada_2[0][2]) )