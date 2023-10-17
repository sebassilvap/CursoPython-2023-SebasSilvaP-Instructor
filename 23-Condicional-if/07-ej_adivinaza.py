# ===============================================
# Ejercicio

# - juego de adivinanza múltiple
# - 3 posibilidades de premio
# - depende de si el número que de el usuario
# - esté dentro de los rangos establecidos
# ===============================================

print('\n***********************************')
print('Bienvenido al Juego de Adivinanza\n')

opcion_user = int( input('Adivine el número especial: ') )

# => Premios
premio_1 = [1,5,8,15,19]
premio_2 = [3,9,12]
premio_3 = 11

print()

if opcion_user in premio_1:
    print('Usted ha ganado el premio 1')
elif opcion_user in premio_2:
    print('Usted ha ganado el premio 2')
elif opcion_user == premio_3:
    print('HA GANADO EL PREMIO MAYOR!')
else:
    print('Lo siento, no ha ganado nada...')
# end if
print('\n***********************************')