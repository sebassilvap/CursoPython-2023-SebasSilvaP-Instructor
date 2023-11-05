# =======================================================================================
# UTC => Universal Coordinated Time
# método time.gmtime()

# - UTC == Estádar Primario para la Definición del Tiempo
# - de esta manera se regula la hora en todo el mundo
# ! NO está regulado para el cambio horario de invierno en Europa
# - time.localtime() => si regula esto
# ! time.gmtime() y time.localtime() => devuelven un objeto de tipo "time.struct_time"
# =======================================================================================


import time


#? 1) Recordar el formato estándar del string time presentado en Python
print('\n1) Recordar el formato estándar del string time presentado en Python')

formato_estandar = '%d of %B of %Y %Hh:%Mm'



#? 2) Generar fecha actual con .localtime & .gmtime()
print('\n2) Generar fecha actual con .localtime & .gmtime()')
# - tanto time.localtime() como time.gmtime()
# - nos generan la fecha / hora actual al momento de ejecución
# - la única diferencia es dst
# - dst => daylight saving time
# - https://en.wikipedia.org/wiki/Daylight_saving_time
# - esto ocurre generalmente el último día de octubre en Europa
# - donde los relojes retroceden una hora para tener más luz del día
# - durante el período entre octubre y marzo del próximo año
# - PRACTICAMENTE:

# *     time.localtime() => toma en cuenta este cambio de horario
# *     time.gmtime() => no toma en cuenta este cambio de horario

# - en mi caso personal
# - al momento que redacto esto
# - es el 5 de Noviembre de 2023 => este cambio de horario ha sido aplicado
# - y al correr / ejecutar este script en python
# - con time.localtime() veremos la diferencia

fecha_actual_local = time.localtime()
fecha_actual_utc = time.gmtime()

print( fecha_actual_local , type(fecha_actual_local) ) 
print( fecha_actual_utc , type(fecha_actual_utc) ) 

# --------------------
# RESULTADO CONSOLA:
# --------------------
# time.struct_time(tm_year=2023, tm_mon=11, tm_mday=5, tm_hour=16, tm_min=54, tm_sec=29, tm_wday=6, tm_yday=309, tm_isdst=0) <class 'time.struct_time'>
# time.struct_time(tm_year=2023, tm_mon=11, tm_mday=5, tm_hour=15, tm_min=54, tm_sec=29, tm_wday=6, tm_yday=309, tm_isdst=0) <class 'time.struct_time'>



#? 3) Pasar a formato string para una mejor lectura de la fecha
print('\n3) Pasar a formato string para una mejor lectura de la fecha')
# - utilizamos el time.strftime(formato , fecha_time)
# - RECORDAR: nos devuelve un string en el formato establecido arriba
# - con los códigos de formato
# - '%d of %B of %Y %Hh:%Mm'

fecha_actual_local_str = time.strftime( formato_estandar , fecha_actual_local )
fecha_actual_utc_str = time.strftime( formato_estandar , fecha_actual_utc )

print( fecha_actual_local_str , type(fecha_actual_local_str) )
print( fecha_actual_utc_str , type(fecha_actual_utc_str) )

# --------------------
# RESULTADO CONSOLA:
# --------------------
# 05 of November of 2023 16h:58m <class 'str'>
# 05 of November of 2023 15h:58m <class 'str'>