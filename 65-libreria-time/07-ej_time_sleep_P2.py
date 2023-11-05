# ===========================================================
# Librería / Módulo time
# Método time.sleep()

# - para dar una dinámica a nuestro programa
# - un tiempo de sleep entre iteraciones
# ! el argumento lo recibe en segundos

# - https://docs.python.org/3/library/time.html#leap-second

# * EJERCICIO 2
# ===========================================================

import time

#? 1) Ejercicio: Definir un contador de año nuevo
print('\n1) Ejercicio: Definir un contador de año nuevo')

contador = 5

while True:
    if contador > 0:
        print( 'Faltan {} segundos para que sea Año Nuevo!'.format(contador) )
        contador -= 1
        time.sleep(1) # 1 segundo antes de nueva iteración
    else:
        print('FELIZ AÑO NUEVO !!')
        break
# end while