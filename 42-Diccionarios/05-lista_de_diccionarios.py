# ====================================================
# Ejercicio
# Lista de Diccionarios

# - nosotros podemos crear colección de colecciones
# - una muy útil es la lista de diccionarios
# - un recurso muy usado en muchos programas
# ====================================================

# => creando 3 diccionarios con un pokemon distinto
pikachu = {
    'nombre': 'pikachu',
    'vitalidad': 50,
    'poder': 80,
    'defensa': 75,
    'ataque_especial': 'Impact Trueno'
}

bulbasaur = {
    'nombre': 'bulbasaur',
    'vitalidad': 80,
    'poder': 70,
    'defensa': 80,
    'ataque_especial': 'Razor Leaf'
}

charizard = {
    'nombre': 'charizard',
    'vitalidad': 90,
    'poder': 95,
    'defensa': 85,
    'ataque_especial': 'Blast Burn'
}


# => manera básica de imprimir cada diccionario
print( pikachu, type(pikachu), len(pikachu))
print( bulbasaur, type(bulbasaur), len(bulbasaur))
print( charizard, type(charizard), len(charizard))


# => crear una lista de pokemons con cada diccionario
pokemons = [pikachu, bulbasaur, charizard]


# => recorriendo lista de pokemones
print()
for pokemon in pokemons:
    print(pokemon)
# end for


# => podría imprimir la información o usarla de una manera distinta
print()
for pokemon in pokemons:
    for clave, valor in pokemon.items():
        print(clave, '=', valor, end=' | ')
    # end for
    print()
# end for


# => podría filtar la información que deseo

# Mostrar nombre y poder especial de pokemones
print('\nMostrar nombre y poder especial de pokemones')

print()
for pokemon in pokemons:
    for clave, valor in pokemon.items():
        if clave == 'nombre' or clave == 'ataque_especial':
            print(clave,'=',valor, end=' | ')
    # end for
    print()
# end for

