# ======================
# Métodos Diccionario
# ======================

# ----------------------------------
#* Métodos de Acceso a Diccionarios
#  .get()
#  .keys()
#  .values()
#  .items()
# ----------------------------------

superheroe = {
    'alias' : 'Flash',
    'nombre_real' : 'Barry Allen',
    'edad' : 30,
    'superpoder' : 'velocidad',
    'activo' : True
}

#? 1) .get()
print('\n1) .get()')
# - obtener el valor de una clave

# => sin get, con acceso de corchete
print( superheroe['superpoder'] )

# => con .get()
print( superheroe.get('activo') )
print( superheroe.get('nombre_real') )


#? 2) .keys()
print('\n2) .keys()')
# - retorna todas las claves del diccionario
# - me retorna un tipo de dato 'dict_keys'

print( superheroe.keys() )

claves = superheroe.keys()

print( claves, type(claves), len(claves) )

# => iterando las claves
print()

for clave in claves:
    print(clave, '--', type(clave))
# end for


#? 3) .values()
print('\n3) .values()')
# - retorna los valores de las claves de un diccionario
# - me retorna un tipo de dato 'dict_values'

print( superheroe.values() )

valores = superheroe.values()

print( valores, type(valores), len(valores) )

# => iterando los valores de las claves
print()

for valor in valores:
    print(valor, '--', type(valor))
# end for


#? 4) .items()
print('\n4) .items()')
# - devuelve un tipo de dato 'dict_items'
# - que es una lista de tuplas
# - cada tupla tiene la clave y el valor del diccionario

print( superheroe.items() )

claves_y_valores = superheroe.items()

print( claves_y_valores, type(claves_y_valores), len(claves_y_valores) )


# => A) una manera de iterar devolviendo las tuplas de clave y valor
print()

for clave_valor in claves_y_valores:
    print( clave_valor, '--', type(clave_valor) )
# end for


# => B) iterar devolviendo clave y valor por separado
print()

for clave, valor in claves_y_valores:
    print(clave, '=>', valor)
# end for


# => C) iteración estádar utilizada
print()

for key, value in superheroe.items():
    print(key, '--', value)
# end for

# - 1era variable de iteración => siempre el key
# - 2da variable de iteración  => siempre el value del key


# ------------------------------------
#* Método para modificar diccionarios
#  .update()
#  .setdefault()
# ------------------------------------

superheroe = {
    'alias' : 'Flash',
    'nombre_real' : 'Barry Allen',
    'edad' : 30,
    'superpoder' : 'velocidad',
    'activo' : True
}


#? 5) .update()
print('\n5) .update()')
# - tiene 2 funciones
# - modifica el valor de una clave
# - añade nuevos pares de clave-valor


# 5.1) uso básico
print('\n5.1) uso básico\n')

print( superheroe, len(superheroe) )

mod_heroe = {
    'marca': 'dc',
    'grupos': 'liga de la justicia',
    'edad': 35
}

superheroe.update(mod_heroe)

print( superheroe, len(superheroe) )


# 5.2) Manera tradicional con corchete
print('\n5.2) Manera tradicional con corchete\n')

superheroe['enemigo'] = 'Flash Reverso'
print( superheroe, len(superheroe) )

superheroe['edad'] = 40
print( superheroe, len(superheroe) )


# 5.3) pasando un diccionario de manera literal
print('\n5.3) pasando un diccionario de manera literal\n')

auto = {
    'marca': 'Chevrolet',
    'modelo': 'Vitara',
    'year': 2014,
}

print(auto, len(auto))

auto.update( {'km' : 100000, 'color' : 'rojo', 'year' : 2020} )
print(auto, len(auto))


#? 6) .setdefault()
print('\n6) .setdefault()')
# - pasamos clave y valor como argumentos del método
# - si existe la clave, NO LA MODIFICA, pero igual devuelve el valor
# - si no existe, LA CREA

auto = {
    'marca': 'Chevrolet',
    'modelo': 'Vitara',
    'year': 2014,
}

print( auto, len(auto) )

# => devuelve el valor de la clave
year = auto.setdefault( 'year', 2014 )
print()
print( auto, len(auto) )
print( year )

# => modifica el valor de la clave
auto.setdefault( 'color', 'rojo' )
print()
print( auto, len(auto) )

# => si pongo clave correcta y valor incorrecto
# - no modifica
# - devuelve el valor de la clave
modelo = auto.setdefault( 'modelo', 'Blazer' )
print()
print( auto, len(auto) )
print( modelo )



# -------------------------------------------------
#* Métodos para Eliminar Elementos de Diccionario
#  .pop()
#  .popitem()
#  .clear()
#   del
# -------------------------------------------------


#? 7) .pop()
print('\n7) .pop()')
# - elimina un elemento del diccionario
# - pasando como argumento la clave
# - si la clave no existe => Error
# - no funciona como en listas
# - no elimina el último elemento por defecto
# - siempre debemos pasar una clave
# - devuelve el valor eliminado

superheroe = {
    'alias' : 'Flash',
    'nombre_real' : 'Barry Allen',
    'edad' : 30,
    'superpoder' : 'velocidad',
    'activo' : True
}

print( superheroe, len(superheroe) )

superheroe.pop('activo')
print( superheroe, len(superheroe) )

# => devuelve el valor eliminado
valor_edad = superheroe.pop('edad')
print( superheroe, len(superheroe) )
print(valor_edad)

# => errores de uso
superheroe = {
    'alias' : 'Flash',
    'nombre_real' : 'Barry Allen',
    'edad' : 30,
    'superpoder' : 'velocidad',
    'activo' : True
}

print( superheroe, len(superheroe) )

#superheroe.pop() #! TypeError: pop expected at least 1 argument, got 0

#superheroe.pop('enemigo') #! KeyError: 'enemigo'


#? 8) .popitem()
print('\n8) .popitem()')
# - Python > 3.7 => borra el último elemento insertado (Diccionarios Ordenados)
# - Python < 3.7 => borra un elemento al azar (Diccionarios Desordenados)
# - devuelve una tupla con la clave y valor eliminado

superheroe = {
    'alias' : 'Flash',
    'nombre_real' : 'Barry Allen',
    'edad' : 30,
    'superpoder' : 'velocidad',
}

# => uso básico
print( superheroe, len(superheroe) )

superheroe.popitem()
print( superheroe, len(superheroe) )

# => retorna tupla de clave, valor eliminados
valor_eliminado = superheroe.popitem()
print( superheroe, len(superheroe) )
print( valor_eliminado, type(valor_eliminado) )


#? 9) .clear()
print('\n9) .clear()')
# - vacía por completo el diccionario
# - al final tenemos un diccionario vacío

auto = {
    'marca': 'Chevrolet',
    'modelo': 'Vitara',
    'year': 2014,
}

print( auto, len(auto) )

auto.clear()
print( auto, len(auto) )


#? 10) del diccionario['clave']
print("\n10) del diccionario['clave']")
# - del => keyword / palabra clave
# - elimina clave/valor pasando la clave
# - también elimina toda la variable del diccionario

auto = {
    'marca': 'Chevrolet',
    'modelo': 'Vitara',
    'year': 2014,
}

print( auto, len(auto) )

del auto['year']
print( auto, len(auto) )

del auto
#print( auto, len(auto) ) #! NameError: name 'auto' is not defined


# ------------------
#* Resto de Métodos
# ------------------

#? 11) .fromkeys()
print('\n11) .fromkeys()')

x = ( 'clave_1', 'clave_2', 'clave_3', 'clave_4', 'clave_5' )
y = 100

diccionario = dict.fromkeys(x, y)

print( diccionario, type(diccionario), len(diccionario) )