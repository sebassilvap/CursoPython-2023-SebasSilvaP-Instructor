# ==================================================================
# Format Codes - Para representación local

"""
%c    Representación Local de fecha/hora (Tue Aug 16 21:30:00 1988)
%x    Representación local de fecha (08/16/88)
%X    Representación local de hora (21:30:00)
"""

# - con la representación local podemos dar un formato rápido
# - ya sea de fecha/hora, fecha o sólo hora
# - como vimos, lo hacemos aplicando el método .strftime

# *    time.strftime( formato , fecha_time.struct_time )
# ==================================================================

import time


#? 1) Generar 2 fechas: 1 actual y 1 en pasado/futuro
print('\n1) Generar 2 fechas: 1 actual y 1 en pasado/futuro')
# - ambas fechas deben ser de tipo "time.struct_time"

# -----------------------------
# 1.1) Fecha Actual
print('\n1.1) Fecha Actual\n')
# -----------------------------

fecha_actual_time = time.localtime()
print(fecha_actual_time) 
print( type(fecha_actual_time) ) 


# ----------------------------------
# 1.2) Fecha Arbitraria
print('\n1.2) Fecha Arbitraria\n')
# ----------------------------------

# EJ: 15 de Agosto de 2030 - 18:51:02

tupla_fecha = (2030, 8, 15, 18, 51, 2, 0, 0, 0) # 1
cero_a_fecha = time.mktime(tupla_fecha) # 2
fecha_string = time.ctime(cero_a_fecha) # 3
formato_estandar = '%a %b %d %H:%M:%S %Y' # 4
fecha_time = time.strptime( fecha_string , formato_estandar ) # 5

# => todo esto se podría hacer en una función
# - pero como solo tenemos una fecha
# - vamos a dejar así


# ----------------------------
# 1.3) Resultados
print('\n1.3) Resultados\n')
# ----------------------------

print( fecha_actual_time , type(fecha_actual_time) ) # time.struct_time(tm_year=2023, tm_mon=11, tm_mday=5, tm_hour=20, tm_min=17, tm_sec=1, tm_wday=6, tm_yday=309, tm_isdst=0) <class 'time.struct_time'>
print( fecha_time , type(fecha_time) ) # time.struct_time(tm_year=2030, tm_mon=8, tm_mday=15, tm_hour=19, tm_min=51, tm_sec=2, tm_wday=3, tm_yday=227, tm_isdst=-1) <class 'time.struct_time'>



#? 2) Representación Local
print('\n2) Representación Local')
# - RECORDAR:
# *    time.strftime( formato , fecha_time.struct_time ) => STRING

# -----------------------------------------------------
print('\n%c    Representación Local de fecha/hora\n')
# -----------------------------------------------------

fecha_hora_local_actual = time.strftime( '%c' , fecha_actual_time )
fecha_hora_local = time.strftime( '%c' , fecha_time )

print( "fecha_hora_local_actual =" , fecha_hora_local_actual , type(fecha_hora_local_actual) )
print( "fecha_hora_local =" , fecha_hora_local , type(fecha_hora_local) )
# fecha_hora_local_actual = Sun Nov  5 20:22:54 2023 <class 'str'>
# fecha_hora_local = Thu Aug 15 19:51:02 2030 <class 'str'>


# -------------------------------------------------
print('\n%x    Representación local de fecha\n')
# -------------------------------------------------

fecha_local_actual = time.strftime( '%x' , fecha_actual_time )
fecha_local = time.strftime( '%x' , fecha_time )

print( "fecha_local_actual =" , fecha_local_actual , type(fecha_local_actual) )
print( "fecha_local =" , fecha_local , type(fecha_local) )
# fecha_local_actual = 11/05/23 <class 'str'>
# fecha_local = 08/15/30 <class 'str'>


# -----------------------------------------------
print('\n%X    Representación local de hora\n')
# -----------------------------------------------

hora_local_actual = time.strftime( '%X' , fecha_actual_time )
hora_local = time.strftime( '%X' , fecha_time )

print( "hora_local_actual =" , hora_local_actual , type(hora_local_actual) )
print( "hora_local =" , hora_local , type(hora_local) )
# hora_local_actual = 20:22:54 <class 'str'>
# hora_local = 19:51:02 <class 'str'>
