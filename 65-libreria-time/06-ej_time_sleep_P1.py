# ===========================================================
# Librería / Módulo time
# Método time.sleep()

# - para dar una dinámica a nuestro programa
# - un tiempo de sleep entre iteraciones
# ! el argumento lo recibe en segundos

# - https://docs.python.org/3/library/time.html#leap-second

# * EJERCICIO 1
# ===========================================================

#? 1) Ejercicio: Presentar un reloj en la consola
print('\n1) Ejercicio: Presentar un reloj en la consola')

import time

# ==> definir una función que me retorne la hora actual

def retornar_hora_actual():
    fecha_actual_time = time.localtime()
    formato = '%H:%M:%S'
    hora_actual = time.strftime( formato , fecha_actual_time )
    
    return hora_actual
# end def

#print( retornar_hora_actual() ) # test


# ==> definir una iteración

while True:
    print( retornar_hora_actual() )
    time.sleep(1) # se espera 1 segundo antes de siguiente iteración
# end while