# =============================================================
# Diccionarios en Python

# - Junto con las listas
# - Los diccionarios son de las colecciones más importantes
# - Se los denomina estructura mapeada (mapping)
# - Son estructuras de clave & valor (key & value)
# - la clave es única
# - no puede existir un diccionario con 2 claves iguales
# - en otros lenguajes se denominan => arreglos asociativos
# - asociamos una clave a un valor

#* Python 3.6 y < ==> Desordenados
#* Python 3.7 +   ==> Ordenados

# => se los escribe entre llaves {} y key : value

#* RECORDAR tipos de datos

'''
https://www.w3schools.com/python/python_datatypes.asp

----------------------------------------------------
Text Type:	     |    str
Numeric Types:   |    int, float, complex
Sequence Types:  |    list, tuple, range
Mapping Type:	 |    dict
Set Types:	     |    set, frozenset
Boolean Type:	 |    bool
Binary Types:	 |    bytes, bytearray, memoryview
None Type:	     |    NoneType
----------------------------------------------------
'''

# =============================================================

#? 1) Creación Básica de un Diccionario
print('\n1) Creación Básica de un Diccionario')
# - 2 maneras
# - con la notación {} y key : value
# - con el constructor => dict()
# - len() => para los elementos iterables

# => diccionario con notación
monedas_1 = {
    'usa' : 'dólar',
    'alemania' : 'euro',
    'mexico' : 'peso'
}

# => diccionario a partir de constructor
monedas_2 = dict( usa='dólar', alemania='euro', mexico='peso' )

print( monedas_1, type(monedas_1), len(monedas_1) )
print( monedas_2, type(monedas_2), len(monedas_2) )

# => cada key : value, es un elemento!


#? 2) Iniciar diccionario vacío
print('\n2) Iniciar diccionario vacío')

# => con la notación
dict_vacio_1 = {}

# => con el constructor dict()
dict_vacio_2 = dict()

print( dict_vacio_1, type(dict_vacio_1), len(dict_vacio_1) )
print( dict_vacio_2, type(dict_vacio_2), len(dict_vacio_2) )


#? 3) Técnica de Indexing & Slicing => No aplicable a diccionarios
print('\n3) Técnica de Indexing & Slicing => No aplicable a diccionarios')

print('\n3.1) Recordar Indexing & Slicing en Listas\n')
lista = [1,2,3]

# indexing
print( lista[1] )

# slicing
print( lista[1:3] )

print('\n3.2) Intentando esto en diccionarios\n')

monedas = {
    'usa' : 'dólar',
    'alemania' : 'euro',
    'mexico' : 'peso'
}

#print( monedas[0] ) #! KeyError: 0
#print( monedas[1:3] ) #! TypeError: unhashable type: 'slice'


#? 4) Acceder a valor de diccionario con clave
print('\n4) Acceder a valor de diccionario con clave')
# - parecido al indexing
# - pero en lugar de la posición
# - pasamos el nombre de la clave

monedas = {
    'usa' : 'dólar',
    'alemania' : 'euro',
    'mexico' : 'peso'
}

print( monedas['usa'] )
print( monedas['mexico'] )


#? 5) Crear una nueva clave valor
print('\n55) Crear una nueva clave valor')
# - se utiliza el acceso con clave
# - y se asigna nuevo valor

monedas = {
    'usa' : 'dólar',
    'alemania' : 'marco',
    'mexico' : 'peso',
}

print(monedas)

monedas['alemania'] = 'euro'

print(monedas)


#? 5) Podemos tener 2 valores iguales pero nunca 2 mismas claves
print('\n4) Podemos tener 2 valores iguales pero nunca 2 mismas claves')
# - Recordar:
# { key : value }

# - Una clave duplicada sobreescribe el diccionario

monedas = {
    'usa' : 'dólar',
    'alemania' : 'euro',
    'mexico' : 'peso',
    'ecuador' : 'sucre',
    'ecuador' : 'dólar' # establece la última definida
}

print( monedas, type(monedas), len(monedas) )


#? 6) Un diccionario puede contener todo tipo de datos
print('\n6) Un diccionario puede contener todo tipo de datos')

estudiante = {
    'nombre': 'Sebastián',
    'apellido': 'Silva',
    'edad' : 36,
    'es_estudiante' : True,
    'calificaciones': [8, 9.5, 10]
}

print(estudiante)


#? 7) Keyword 'in' => para averiguar una CLAVE
print('\n7) Keyword 'in' => para averiguar una CLAVE')
# - 'in' en un diccionario me averigua la clave
# - no el valor

print( 'nombre' in estudiante )
print( 'calificaciones' in estudiante )
print( 'nota_final' in estudiante )


#? 8) Valores enteros como claves
print('\n8) Valores enteros como claves')

codigos_colores = {
    100 : 'amarillo',
    200 : 'azul',
    300 : 'rojo',
    400 : 'blanco',
    500 : 'negro'
}

print( codigos_colores, len(codigos_colores) )
print( codigos_colores[100] )
print( codigos_colores[500] )


