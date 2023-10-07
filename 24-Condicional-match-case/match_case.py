# ===============================================================================
# match-case

#! disponible a partir de python 3.10 - no en versiones anteriores
# - comportamiento de condicional del legendario switch-case
# - switch-case en otros lenguajes de programación
# - se usa cuando una condición puede tener una exagerada cantidad de if & elif

#! para los que vienen de otro lenguaje:
# => en este caso no se necesita poner 'break' al final de cada case
# ===============================================================================

print('''opción 1 - ATAQUE
opción 2 - DEFENSA
opción 3 - CURAR COMPAÑEROS
opción 4 - HUIR DE BATALLA
opción 5 - USAR ÍTEM
opción 6 - SALIR DEL JUEGO''')
print('**************************************')

player_option = input('Player 1, ingrese opción de juego (1-6): ')

print()

match player_option:
    case '1':
        print('opción 1 - ATAQUE')
    case '2':
        print('opción 2 - DEFENSA')
    case '3':
        print('opción 3 - CURAR COMPAÑEROS')
    case '4':
        print('opción 4 - HUIR DE BATALLA')
    case '5':
        print('opción 5 - USAR ÍTEM')
    case '6':
        print('opción 6 - SALIR DEL JUEGO')
    case _: # opción por defecto = else
        print('ERROR - opción incorrecta')
# end match-case
        
        
## Utilizando if-elif-else
print('\nUtilizando if-elif-else\n')

if player_option == '1':
    print('opción 1 - ATAQUE')
elif player_option == '2':
    print('opción 2 - DEFENSA')
elif player_option == '3':
    print('opción 3 - CURAR COMPAÑEROS')
elif player_option == '4':
    print('opción 4 - HUIR DE BATALLA')
elif player_option == '5':
    print('opción 5 - USAR ÍTEM')
elif player_option == '6':
    print('opción 6 - SALIR DEL JUEGO')
else:
    print('ERROR - opción incorrecta')

# - en caso de no contar con una versión de python >= 3.10
# - esta sería la manera de simular un match-case
# - usando if-elif-else