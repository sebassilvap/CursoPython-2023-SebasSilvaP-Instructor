# ====================================================================
# Operaciones con el tiempo => datetime.timedelta()

# - con .timedelta() podemos definir una CANTIDAD DE TIEMPO
# - esta cantidad es del tipo "datetime.timedelta"
# - este tiempo lo podemos agregar o restar
# - a una fecha/hora de tipo "datetime"

# - https://www.geeksforgeeks.org/python-datetime-timedelta-function/

# ====================================================================

import datetime


#? 1) Argumentos de datetime.timedelta()
print('\n1) Argumentos de datetime.timedelta()')
# - los argumentos deben ser pasados con el nombre
# - por defecto si no se pasa nada son 0
# - los argumentos posibles para definir una cantidad de tiempo
# - utilizando el método datetime.timedelta() son:
# ! Retorna un tipo "datetime.timedelta"

"""
    1)     days=
    2)     seconds=
    3)     microseconds=
    4)     milliseconds=
    5)     minutes=
    6)     hours=
    7)     weeks=
"""


tiempo = datetime.timedelta(days=15, hours=20, minutes=35, seconds=3500)
print(tiempo) # 15 days, 21:33:20
print( type(tiempo) ) # <class 'datetime.timedelta'>



#? 2) Sumando & Restando timedelta a la fecha/hora actual
print('\n2) Sumando & Restando timedelta a la fecha/hora actual')

fecha_hora_actual = datetime.datetime.now()
fecha_hora_pasado = fecha_hora_actual - tiempo
fecha_hora_futuro = fecha_hora_actual + tiempo

print( 'Fecha Actual =' , fecha_hora_actual , '|' , type(fecha_hora_actual) )
print( 'Fecha Pasado =' , fecha_hora_pasado , '|' , type(fecha_hora_pasado) )
print( 'Fecha Futuro =' , fecha_hora_futuro , '|' , type(fecha_hora_futuro) )

# Resultados Consola:
# Fecha Actual = 2023-11-05 20:47:17.054191 | <class 'datetime.datetime'>
# Fecha Pasado = 2023-10-20 23:13:57.054191 | <class 'datetime.datetime'>
# Fecha Futuro = 2023-11-21 18:20:37.054191 | <class 'datetime.datetime'>
