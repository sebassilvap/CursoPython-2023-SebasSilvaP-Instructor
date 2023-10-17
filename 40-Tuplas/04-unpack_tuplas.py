# =============================================
# Desempaquetar / Unpack - Tuplas

# - hablamos de desempaquetar
# - cuando extraemos el valor a una variable
# - esto es posible hacerlo en tuplas
# =============================================


#? 1) Desempaquetando Valores de Tupla
print('\n1) Desempaquetando Valores de Tupla')

heroes = ('goku', 'superman', 'ironman')
print(heroes, type(heroes), len(heroes))

(heroe_db, heroe_dc, heroe_marvel) = heroes

# - cada valor de la tupla queda guardado
# - en las variables anteriores

print(heroe_db)
print(heroe_dc)
print(heroe_marvel)


#? 2) Operador Asterisco *
print('\n2) Operador Asterisco *')
# - cuando el número de variables
# - no coincide con el número de valores en la tupla
# - el resto de variables se guarda en la variable con asterisco
# - en forma de lista
# - * => a la izquierda de la variable

heroes = (
    'goku',
    'superman',
    'hulk',
    'thor',
    'spiderman'
)

(heroe_db, heroe_dc, *heroes_marvel) = heroes

print( heroe_db, type(heroe_db) )
print( heroe_dc, type(heroe_dc) )
print( heroes_marvel, type(heroes_marvel) )



#? 3) Operador Asterisco * en otra posición
print('\n3) Operador Asterisco * en otra posición')

# ------------------------
# EJEMPLO 1
print('\nEJEMPLO 1:\n')
# ------------------------

heroes = (
    'goku',
    'hulk',
    'thor',
    'spiderman',
    'batman'
)

(heroe_db, *heroes_marvel, heroe_dc) = heroes

print( heroe_db, type(heroe_db) )
print( heroes_marvel, type(heroes_marvel) )
print( heroe_dc, type(heroe_dc) )


# ------------------------
# EJEMPLO 2
print('\nEJEMPLO 2:\n')
# ------------------------

# => lo siguiente ya sería un error en Python
#!SyntaxError: multiple starred expressions in assignment

'''
heroes = (
    'goku',
    'hulk',
    'thor',
    'spiderman',
    'batman',
    'superman',
    'wonderwoman'
)

(heroe_db, *heroes_marvel, *heroes_dc) = heroes

print( heroe_db, type(heroe_db) )
print( heroes_marvel, type(heroes_marvel) )
print( heroes_dc, type(heroes_dc) )
'''