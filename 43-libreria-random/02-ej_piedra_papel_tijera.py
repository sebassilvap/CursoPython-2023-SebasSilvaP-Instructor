# =====================================
# Ejercicio

# - Juego de Piedra / Papel / Tijera
# - utilizando las bases de Python
# =====================================

import random

opciones_juego = ['piedra', 'papel', 'tijera']

while True:
    print('\nBienvenido al Juego: Piedra / Papel / Tijera')
    print('(1) piedra')
    print('(2) papel')
    print('(3) tijera')
    print('(4) salir / q\n')

    opcion_player = input('Ingrese su opción: ')
    opcion_player = opcion_player.strip().lower() # quitar espacios y convertir a miníscula

    opcion_computadora = random.choice(opciones_juego)
    
    # => solo si el player quiere jugar se imprime esto
    if opcion_player in opciones_juego:
        print('\n------------------------------------------------')
        print('Player ha elegido: ', opcion_player)
        print('Computadora ha elegido: ', opcion_computadora)
        print('------------------------------------------------\n')
    # end if
    
    # => Análisis
    if opcion_player == opcion_computadora:
        print('Es un EMPATE !!')
    
    elif opcion_player == 'piedra':
        if opcion_computadora == 'tijera':
            print(opcion_player, 'vence a', opcion_computadora)
            print('PLAYER GANA !!')
        elif opcion_computadora == 'papel':
            print(opcion_computadora, 'vence a', opcion_player)
            print('COMPUTADORA GANA !!')
    
    elif opcion_player == 'papel':
        if opcion_computadora == 'piedra':
            print(opcion_player, 'vence a', opcion_computadora)
            print('PLAYER GANA !!')
        elif opcion_computadora == 'tijera':
            print(opcion_computadora, 'vence a', opcion_player)
            print('COMPUTADORA GANA !!')
    
    elif opcion_player == 'tijera':
        if opcion_computadora == 'papel':
            print(opcion_player, 'vence a', opcion_computadora)
            print('PLAYER GANA !!')
        elif opcion_computadora == 'piedra':
            print(opcion_computadora, 'vence a', opcion_player)
            print('COMPUTADORA GANA !!')
    
    elif opcion_player == 'salir' or opcion_player == 'q':
        print('Gracias por su tiempo!')
        break
    
    else:
        print('ERROR - Opción Equivocada!')
# end while