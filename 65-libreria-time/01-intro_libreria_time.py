# ==================================================
# Librería / Módulo => time

# - para trabajar hora y fecha en Python
# - no es aconsejable usarla para horas y fechas:
#   * antes del 1 de enero de 1970 (EPOCH)
#   * más allá del año 2038
# ==================================================


#? 1) importación de la librería / módulo time
print('\n1) importación de la librería / módulo time')
# - como es costumbre, al momento de usar una librería interna
# - la primera tarea es importarla

import time



#? 2) Punto / Tiempo 0 => time.ctime()
print('\n2) Punto / Tiempo 0 => time.ctime()')
# - es el punto cero para la computadora
# - en python y muchos lenguajes de programación
# - es el primer día de 1970
# - en inglés se conoce como el "epoch"
# ! time.ctime() => devuelve un string

punto_cero = time.ctime(0)

print(punto_cero) # Thu Jan  1 01:00:00 1970
print( type(punto_cero) ) # <class 'str'>



#? 3) X milisegundos a partir del punto 0
print('\n3) X milisegundos a partir del punto 0')
# ! time.ctime() => devuelve un string

"""
    1000 ms = 1 s
    60 s = 1 min
    60 min = 1 hour
    24 hour = 1 day
    30 days = 1 month
    1 year = 12 months = 360 days
"""

# ejemplo: 5 millones de ms a partir del punto 0
cinco_millones_ms_from_t0 = time.ctime(5000000)

print(cinco_millones_ms_from_t0) # Fri Feb 27 21:53:20 1970
print( type(cinco_millones_ms_from_t0) ) # <class 'str'>



#? 4) time.time() => Fecha Actual en ms desde el tiempo 0 (al momento de ejecutar el programa)
print('\n4) time.time() => Fecha Actual en ms desde el tiempo 0 (al momento de ejecutar el programa)')
# - con el método .time de time
# - ojo: sería entonces => time.time()
# ! time.time() => devuelve un float en ms

tiempo_actual_ms_from_t0 = time.time()

print(tiempo_actual_ms_from_t0) # 1699105514.1178083
print( type(tiempo_actual_ms_from_t0) ) # <class 'float'>



#? 5) Fecha Actual | con .ctime() | (al momento de ejecutar el programa)
print('\n5) Fecha Actual | con .ctime() | (al momento de ejecutar el programa)')
# - aplicamos time.time()
# - dentro de .ctime()
# ! time.ctime() => devuelve un string

fecha_actual = time.ctime(time.time()) #! IMPORTANTE

print(fecha_actual) # Sat Nov  4 14:45:45 2023
print( type(fecha_actual) ) # <class 'str'>



#? 6) Fecha Actual | con .localtime() | (al momento de ejecutar el programa)
print('\n6) Fecha Actual | con .localtime() | (al momento de ejecutar el programa)')
# - .localtime() sin argumentos devuelve la fecha actual
# - en el momento exacto de ejecutar el programa
# ! time.localtime() => devuelve un objeto de tipo "time.struct_time"

fecha_actual = time.localtime()

print(fecha_actual) # time.struct_time(tm_year=2023, tm_mon=11, tm_mday=4, tm_hour=14, tm_min=46, tm_sec=6, tm_wday=5, tm_yday=308, tm_isdst=0)     
print( type(fecha_actual) ) # <class 'time.struct_time'>



#? 7) Extrayendo elementos de un tipo time.struct_time
print('\n7) Extrayendo elementos de un tipo time.struct_time')
# - el objeto / elemento de tipo time.struct_time
# - tiene a su vez elementos / atributos 
# - mediante los cuales podemos acceder al mes, día, año, hora, etc..
# - su acceso es mediante la notación del punto
# - pero estos no son métodos
# - son ATRIBUTOS
# ! esto tendrá más sentido cuando entremos a la Programación Orientada a Objetos (POO)

"""
    ELEMENTO DE FECHA/HORA  |   NOMBRE DEL ATRIBUTO
    ------------------------|--------------------------------------------------------------
    año                     | .tm_year [número de 4 dígitos, ej: 1999]
    mes                     | .tm_mon [mes del año 1 - 12]
    dia del mes             | .tm_mday [día del mes 1 - 31]
    día de la semana        | .tm_wday [día de la semana 0 - 6 / Lunes == 0]
    día del año             | .tm_yday [día del año 1 - 366]
    hora                    | .tm_hour [0 a 23, formato 24 horas]
    minutos                 | .tm_min [0 a 59]
    segundos                | .tm_sec [0 a 61, 61 para correcciones históricas, no usado]
    horario de verano       | .tm_isdst [1 si / 0 no / -1 no sabemos ]
"""

fecha_actual = time.localtime()
anio = fecha_actual.tm_year
mes = fecha_actual.tm_mon
dia_mes = fecha_actual.tm_mday
dia_semana = fecha_actual.tm_wday
dia_anio = fecha_actual.tm_yday
hora = fecha_actual.tm_hour
minutos = fecha_actual.tm_min
segundos = fecha_actual.tm_sec
horario_verano = fecha_actual.tm_isdst

# TEST
print( 'FECHA ACTUAL =' , fecha_actual ) # FECHA ACTUAL = time.struct_time(tm_year=2023, tm_mon=11, tm_mday=5, tm_hour=14, tm_min=30, tm_sec=30, tm_wday=6, tm_yday=309, tm_isdst=0)
print( type(fecha_actual) ) # <class 'time.struct_time'>
print( 'año =' , anio ) # año = 2023
print( 'mes =' , mes ) # mes = 11
print( 'dia_mes =' , dia_mes ) # dia_mes = 5
print( 'dia_semana =' , dia_semana ) # dia_semana = 6
print( 'dia_año =' , dia_anio ) # dia_año = 309
print( 'hora =' , hora ) # hora = 14
print( 'minutos =' , minutos ) # minutos = 30
print( 'segundos =' , segundos ) # segundos = 30
print( 'horario_verano =' , horario_verano ) # horario_verano = 0



#? 8) Fijar cualquier fecha en str con formato => time.asctime()
print('\n8) Fijar cualquier fecha en str con formato => time.asctime()')
# - recibe como argumentos: un objeto time, o una tupla con los valores
# - la tupla de valores tiene 9 entradas posibles
# - retorna un string
# ! time.asctime() => devuelve un string

"""
    #* (año, mes, día, horas, minutos, segundos, día de la semana, día del año, dst)
    1)  año      => yyyy
    2)  mes      => 1 - 12
    3)  día      => 1 - 31
    4)  horas    => 0 - 23
    5)  minutos  => 0 - 59
    6)  segundos => 0 - 61 / 61 es válido por razones históricas (no usado)
    7)  día de la semana => 0 - 6 (Lunes es 0)
    8)  día del año => 1 - 366 (https://miniwebtool.com/es/day-of-the-year-calculator/?date=2024-04-24)
    9)  daylight savings time / dst => -1 ó 0
"""

# ! los 3 últimos argumentos ya veremos que no es necesario definirlos de manera exacta

# -----------------------------------------------
# EJ 1: Miércoles 24 de Abril de 2024 - 19:53:06
# -----------------------------------------------

tupla_fecha_1 = (2024, 4, 24, 19, 53, 6, 2, 115, 0)
fecha_1 = time.asctime(tupla_fecha_1)

print(fecha_1) # Wed Apr 24 19:53:06 2024
print( type(fecha_1) ) # <class 'str'>


# ------------------------------------------------------------
# EJ 2: Fijando en 0 los 3 últimos argumenos - FECHA ERRÓNEA
# => 24 de abril de 2024 es MIÉRCOLES !!
# ------------------------------------------------------------

tupla_fecha_2 = (2024, 4, 24, 19, 53, 6, 0, 0, 0)
fecha_2 = time.asctime(tupla_fecha_2)

print(fecha_2) # Mon Apr 24 19:53:06 2024
print( type(fecha_2) ) # <class 'str'>

#! después veremos que podemos corregir esto fácilmente


# ---------------------------------------------------------------
# EJ 3: Sin fijar los 3 últimos argumentos - ERROR PROGRAMACIÓN
# ---------------------------------------------------------------

tupla_fecha_3 = (2024, 4, 24, 19, 53, 6)
#fecha_3 = time.asctime(tupla_fecha_3)
#! TypeError: asctime(): illegal time tuple argument



#? 9) Transformar a milesegundos desde el tiempo 0 => time.mktime()
print('\n9) Transformar a milesegundos desde el tiempo 0 => time.mktime()')
# - de igual manera recibe el tiempo en forma de tupla
# - retorna los milisegundos desde el tiempo 0 (1 de enero de 1970)
# - no importa si el día de la semana y el día del año son incorrectos
# ! time.mktime() => devuelve un float de ms

# -------------------------------------------------
# * ==>  Miércoles 24 de Abril de 2024 - 19:53:06
# -------------------------------------------------

# ==> tuplas de fecha
tupla_fecha_1 = (2024, 4, 24, 19, 53, 6, 2, 115, 0)
tupla_fecha_2 = (2024, 4, 24, 19, 53, 6, 0, 0, 0)

# ==> fechas en milisegundos después de tiempo cero
# aquí se corrige el día de la semana, y día del año !!!
cero_a_fecha1 = time.mktime(tupla_fecha_1)
cero_a_fecha2 = time.mktime(tupla_fecha_2)

print(cero_a_fecha1, type(cero_a_fecha1)) # 1713984786.0 <class 'float'>
print(cero_a_fecha2, type(cero_a_fecha2)) # 1713984786.0 <class 'float'>

# ==> fechas en string
fecha_1_string = time.ctime(cero_a_fecha1)
fecha_2_string = time.ctime(cero_a_fecha2)

print( fecha_1_string, type(fecha_1_string) ) # Wed Apr 24 20:53:06 2024 <class 'str'>
print( fecha_2_string, type(fecha_2_string) ) # Wed Apr 24 20:53:06 2024 <class 'str'>

# ----------------------------------------------------------
# ! una versión más completa
# - de cómo generar una fecha arbitraria (pasado / futuro)
# - lo veremos en la siguiente lección
# - aquí nos falta generar la fecha en formato de tipo time
# ----------------------------------------------------------