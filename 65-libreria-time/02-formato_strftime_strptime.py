# =========================================================================
# Formato de time con strftime y strptime

#   * strftime => transformar una fecha a un formato estándar de string
#   * strptime => parsear / transformar de un string a time.struct_time

# - el formato se establece por medio de format codes
# - los format codes pueden ser encontrados en la guía oficial de Python

# - https://docs.python.org/3/library/time.html
# =========================================================================

import time


#? 1) Format Codes de strftime() y strptime()
print('\n1) Format Codes de strftime() y strptime()')
# - los siguientes son códigos de formato
# - mediante los cuales podemos generar un formato específico
# - con el cual podemos presentar una fecha / hora
# - esta simbología se encuentra presente en la documentación oficial de Python
# - la información por defecto nos devuelve en idioma INGLÉS
# - luego veremos que podemos cambiar el idioma
# - utilizando el módulo "locale"
# - esto lo veremos luego

"""
%a    día de la semana abreviado (Sun, Mon, ...)
%A    día de la semana completo (Sunday, Monday, ...)
%w    día de la semana como número (0 = Domingo / 6 = Sábado)
%d    día del mes (01, 02, ..., 31)
%b    mes abreviado (Jan, Feb, ... , Dec)
%B    mes completo (January, February, ... , December)
%m    mes como número decimal (01, 02, ..., 12)
%y    año con 2 números decimales (00, 01, ... , 99)
%Y    año con 4 números decimales (0001, ... ,1999, 2000, 2001)
%H    hora en formato de 24 (00, 01, ..., 23)
%I    hora en formato de 12 (01, 02, ..., 12)
%p    expresar AM / PM  (AM, PM)
%M    minutos (00, 01, ..., 59)
%S    segundos (00, 01, ..., 59)
%j    día del año (001, ... , 366)
%W    semana del año con lunes en semana cero (00, 01, ..., 53)
  
%c    Representación Local de fecha/hora (Tue Aug 16 21:30:00 1988)
%x    Representación local de fecha (08/16/88)
%X    Representación local de hora (21:30:00)
"""



#? 2) .strftime(formato, fecha_time.struct_time) => para pasar de un objeto time a string con formato
print('\n2) .strftime(formato, fecha_time.struct_time) => para pasar de un objeto time a string con formato')
# - vamos a utilizar .localtime()
# - para retornar la fecha actual como tipo de dato "time.struct_time"
# - con los códigos de formato presentados, vamos a generar un formato
# - y vamos a transformar esta fecha a un string con este formato

# ------------------------------
# fecha actual con .localtime()
# ------------------------------
fecha_actual = time.localtime()
print(fecha_actual) # time.struct_time(tm_year=2023, tm_mon=11, tm_mday=5, tm_hour=14, tm_min=55, tm_sec=33, tm_wday=6, tm_yday=309, tm_isdst=0)
print( type(fecha_actual) ) # <class 'time.struct_time'>


# --------------------
# generando formatos
# --------------------

# * EJ 1: November 05 2023 14:52:25
formato_1 = '%B %d %Y %H:%M:%S'

# * EJ 2: 05 of November, 2023 - 14h:53m
formato_2 = '%d of %B, %Y - %Hh:%Mm'

# -----------------------------------------
# aplicando .strftime(formato, fecha_time)
# ! RETORNA un string
# -----------------------------------------

fecha_actual_formato1 = time.strftime(formato_1 , fecha_actual)
fecha_actual_formato2 = time.strftime(formato_2 , fecha_actual)

# ------
# TEST
# ------

print( fecha_actual_formato1 , type(fecha_actual_formato1) ) # November 05 2023 14:55:33 <class 'str'>
print( fecha_actual_formato2 , type(fecha_actual_formato2) ) # 05 of November, 2023 - 14h:55m <class 'str'>



#? 3) .strptime(fecha_string, formato) => pasar de una fecha en string a tipo time
print('\n3) .strptime(fecha_string, formato) => pasar de una fecha en string a tipo time')
# - podemos expresar una fecha como un string
# - y por medio de este método strptime
# - podemos parsear / transformar a un objeto de tipo time
# - es necesario que el string esté en idioma inglés y correctamente escrito
# - de otra manera no funcionaría
# ! RETORNA un "time.struct_time"


# * EJ: 18 de Febrero de 1999 - 20:53:12
# => en inglés: February 18th, 1999 - 20:53:12

# ----------------------------------------------
# definir el formato según el string presentado
# ----------------------------------------------

formato = '%B %dth, %Y - %H:%M:%S'

# --------------------------------
# definir la fecha como un string
# --------------------------------

fecha_string = 'February 18th, 1999 - 20:53:12'

# ------------------------------------------------------------
# transformación / parseo => .strptime(fecha_string, formato)
# ------------------------------------------------------------

fecha_time = time.strptime(fecha_string , formato)

# -----
# TEST
# -----

print(fecha_time) # time.struct_time(tm_year=1999, tm_mon=2, tm_mday=18, tm_hour=20, tm_min=53, tm_sec=12, tm_wday=3, tm_yday=49, tm_isdst=-1)
print( type(fecha_time) ) # <class 'time.struct_time'>



#? 4) Generar cualquier fecha (pasado/futuro) en ms / string / time
print('\n4) Generar cualquier fecha (pasado/futuro) en ms / string / time')
# - recordar la última parte del script anterior
# - vamos a retomar el mismo ejemplo
# - pero ahora vamos a realizar el trabajo completo
# - generalmente cuando definimos una fecha
# - sabemos año, mes, día, hora, minuto, segundo
# - es la información que tenemos a la mano
# - mediante consulta podemos saber que día exactamente (Lunes, Martes, etc...)
# - o peor aún el número del día en el año (1 - 366)
# ! RECORDAR: no funciona para fechas anteriores al punto 0 (1 de Enero de 1970)

# ------------------------------------------------
# * EJ: Miércoles 24 de Abril de 2024 - 19:53:06
# ------------------------------------------------
# - esta fecha con anticipación sabemos que el 24 de abril de 2024
# - es un miércoles
# - pero generalmente no tenemos esto a la mano
# - aquí detallamos el proceso para generar esta fecha

# -----------------------------------------------------------------------------
# PASO 1:
# generar tuplas de la fecha
# RECORDAR:
# (año, mes, día, horas, minutos, segundos, día de la semana, día del año, dst)
# -----------------------------------------------------------------------------
tupla_fecha_1 = (2024, 4, 24, 19, 53, 6, 2, 115, 0) # si supiéramos exactamente que día de la semana y qué día del año
tupla_fecha_2 = (2024, 4, 24, 19, 53, 6, 0, 0, 0) # cuando no lo sabemos / lo que pasa generalmente


# ----------------------------------------------------
# PASO 2:
# transformar a milisegundos después del tiempo cero
# esto lo hacemos con .mktime(tupla_fecha)
# - en este punto, los datos incorrectos para
# - día de la semana y día del año
# ! SE CORRIGEN AUTOMÁTICAMENTE
# ----------------------------------------------------

cero_a_fecha1 = time.mktime(tupla_fecha_1)
cero_a_fecha2 = time.mktime(tupla_fecha_2)

print(cero_a_fecha1, type(cero_a_fecha1)) # 1713984786.0 <class 'float'>
print(cero_a_fecha2, type(cero_a_fecha2)) # 1713984786.0 <class 'float'>


# ------------------------------------------------------
# PASO 3:
# pasar de milisegundos a fecha string formato estándar
# esto lo hacemos con .ctime(milisegundos_desde_t0)
# ------------------------------------------------------
fecha_1_string = time.ctime(cero_a_fecha1)
fecha_2_string = time.ctime(cero_a_fecha2)

print( fecha_1_string, type(fecha_1_string) ) # Wed Apr 24 20:53:06 2024 <class 'str'>
print( fecha_2_string, type(fecha_2_string) ) # Wed Apr 24 20:53:06 2024 <class 'str'>


# ------------------------------------------------------
# PASO 4:
# formato estándar
# - como vemos .ctime() nos ofrece un formato estándar
# - que lo podemos definir con format codes
# ------------------------------------------------------

formato_estandar = '%a %b %d %H:%M:%S %Y' #! de esta manera estándar nos presenta Python la fecha en string


# ---------------------------------------------------
# PASO 5:
# transformar / parsear de string a time
# - definido el formato estándar
# - y teniendo en mano la fecha en formato string
# - utilizamos: .strptime( fecha_string , formato )
# - y tenemos la fecha en formato time.struct_time
# ---------------------------------------------------

fecha_1_time = time.strptime( fecha_1_string , formato_estandar )
fecha_2_time = time.strptime( fecha_2_string , formato_estandar )

print( fecha_1_time , type(fecha_1_time) ) # time.struct_time(tm_year=2024, tm_mon=4, tm_mday=24, tm_hour=20, tm_min=53, tm_sec=6, tm_wday=2, tm_yday=115, tm_isdst=-1) <class 'time.struct_time'>
print( fecha_2_time , type(fecha_2_time) ) # time.struct_time(tm_year=2024, tm_mon=4, tm_mday=24, tm_hour=20, tm_min=53, tm_sec=6, tm_wday=2, tm_yday=115, tm_isdst=-1) <class 'time.struct_time'>
