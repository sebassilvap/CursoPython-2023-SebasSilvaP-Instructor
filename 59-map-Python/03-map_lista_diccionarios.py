# ==============================================================
# sort / map / filter / reduce
# => map en Python

# https://www.w3schools.com/python/ref_func_map.asp

# ? RECORDAR: las colecciones avanzadas de casos reales:

#       * Listas de Listas (Listas 2D)
#       * Listas de Tuplas
#       * Listas de Diccionarios

# ? TIP: la función la podemos definir con lambda
# - de esta manera incluso podemos definir el tipo de colección
# - que map nos va a devolver
# - recordar que lambda se define en una sola línea
# - si la expresión es muy complicada podemos siempre optar
# - por nuestras funciones normales

# ! PARTE 2
# => aplicando map a una lista de DICCIONARIOS

# ==============================================================


#? Map + Lista de DICCIONARIOS
print('\nMap + Lista de DICCIONARIOS')
# - REFERENCIA: https://www.pokemon.com/us/pokedex

# EJERCICIO:
# - se tiene la siguiente lista de diccionarios
# - cada diccionario es un pokemon
# - las claves son: nombre, categoría, ataque, defensa
# - se pide lo siguiente:
#
#   a) crear una función: power_up() que devuelva una lista de diccionarios reducida con:
#       => nombre
#       => ataque = ataque * 1.2
#       => defensa = defensa * 1.1
#   - los valores de ataque y defensa deben ser enteros redondeados
#
#   b) crear una función: fire_shield() que devuelva:
#       => lista original con todas las claves (nombre, categoría, ataque, defensa) pero
#       => defensa de pokemons de categoría 'fuego' = 1.5 * defensa_actual
#       => ataque sigue siendo el mismo para todos
#
#   c) crear una función: air_power() que devuelva una lista reducida:
#       => nombre del pokemon
#       => ataque de pokemon ave = 1.5 * ataque_actual
#       => ataque de resto de pokemons igual
#       => defensa de todos igual


lista_pokemons = [
    {
        'nombre' : 'charizard',
        'categoría' : 'fuego',
        'ataque' : 92,
        'defensa' : 75
    },
    {
        'nombre' : 'charmander',
        'categoría' : 'fuego',
        'ataque' : 65,
        'defensa' : 52
    },
    {
        'nombre' : 'pidgeot',
        'categoría' : 'ave',
        'ataque' : 76,
        'defensa' : 62
    },
    {
        'nombre' : 'rapidash',
        'categoría' : 'fuego',
        'ataque' : 82,
        'defensa' : 72
    },
    {
        'nombre' : 'staraptor',
        'categoría' : 'ave',
        'ataque' : 90,
        'defensa' : 79
    },
]


#? 1) Función EXTRA: print_lista()
print('\n1) Función EXTRA: print_lista()')

# => definición de la función
def print_lista(lista):
    for item in lista:
        print(item)
    # end for
# end def

# => TEST
print('\n LISTA POKEMONS ORIGINAL:')
print_lista(lista_pokemons)



#? 2) Función power_up()
print('\n2) Función power_up()')

# => definición de la función
def power_up(lista):
    power_up_function = lambda x : { 'nombre' : x['nombre'], 'ataque' : round(x['ataque'] * 1.2), 'defensa' : round(x['defensa'] * 1.1) }
    
    return list(map(
        power_up_function,
        lista
    ))
# end def

# => aplicando función
lista_power_up = power_up(lista_pokemons)

# => TEST
print('\n LISTA POWER-UP:')
print_lista(lista_power_up)



#? 3) Función fire_shield()
print('\n3) Función fire_shield()')

# => definición de la función
def fire_shield(lista):
    
    # => definir lambda para map (atención: fijarse en la expresión booleana para defensa)
    fire_shield_function = lambda x : { 'nombre' : x['nombre'], 'categoría' : x['categoría'], 'ataque' : x['ataque'], 'defensa' : round(1.5*x['defensa']) if x['categoría'] == 'fuego' else x['defensa'] }
    
    return list(map(
        fire_shield_function,
        lista
    ))
# end def

# => aplicando función
lista_fire_shield = fire_shield(lista_pokemons)

# => TEST
print('\n LISTA FIRE-SHIELD:')
print_lista(lista_fire_shield)



#? 4) Función air_power()
print('\n4) Función air_power()')

# => definición de la función
def air_power(lista):
    
    # => definir lambda para map (atención: fijarse en la expresión booleana para defensa)
    air_power_function = lambda x : { 'nombre' : x['nombre'], 'ataque' : round(1.5*x['ataque']) if x['categoría'] == 'ave' else x['ataque'], 'defensa' : x['defensa'] }
    
    return list(map(
        air_power_function,
        lista
    ))
# end def

# => aplicando función
lista_air_power = air_power(lista_pokemons)

# => TEST
print('\n LISTA AIR-POWER:')
print_lista(lista_air_power)



#? 5) ALTERNATIVA: Doble Función Normal => air_power()
print('\n5) ALTERNATIVA: Doble Función Normal => air_power()')
# - como vemos la función lambda me ahorra muchas líneas extra de código
# - sin embargo, recordemos que es una expresión de 1 sola línea
# - si la lectura del código se dificulta
# - podemos siempre recurrir a la función normal


# => definir función map:
def map_function(x):
    if x['categoría'] == 'ave':
        return {
            'nombre' : x['nombre'],
            'ataque' : round(1.5*x['ataque']),
            'defensa' : x['defensa']
        }
    else:
        return {
            'nombre' : x['nombre'],
            'ataque' : x['ataque'],
            'defensa' : x['defensa']
        }
    # end if
# end def


# => definir función air_power():
def air_power(lista):
    return list(map(
        map_function,
        lista
    ))
# end def


# => aplicando función
lista_air_power = air_power(lista_pokemons)


# => TEST
print('\n LISTA AIR-POWER / SOLUCIÓN ALTERNATIVA:')
print_lista(lista_air_power)