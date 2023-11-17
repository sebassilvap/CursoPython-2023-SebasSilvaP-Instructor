# ====================================================================
# Librería / Módulo - Locale

# - nos sirve para cambiar el idioma por defecto de nuestro Script
# - lo vamos a utilizar para las fechas
# - con las librerías "time" y "datetime"
# - y con el strftime + los códigos de formato
# - para expresar la fecha en formato personalizado e idioma español
# - al final el resultado va a ser lo mismo con ambas librerías
# ====================================================================


# ------------------------
# Importación de módulos
# ------------------------
import locale
import time
import datetime


# ----------------------------------
# Definir idioma español con locale
# ----------------------------------
# - con el método .setlocale

#locale.setlocale(locale.LC_ALL, 'es-ES') #? ESPAÑOL DE ESPAÑA
locale.setlocale(locale.LC_ALL, 'es')     #? ESPAÑOL GENERAL


# -------------------------
# Fecha de HOY con "time"
# -------------------------
print()

fecha_hoy_time = time.localtime()
print( fecha_hoy_time ) # time.struct_time(tm_year=2023, tm_mon=11, tm_mday=10, tm_hour=23, tm_min=28, tm_sec=44, tm_wday=4, tm_yday=314, tm_isdst=0)    
print( type(fecha_hoy_time) ) # <class 'time.struct_time'>


# -----------------------------
# Fecha de HOY con "datetime"
# -----------------------------
print()

fecha_hoy_datetime = datetime.datetime.now()
print( fecha_hoy_datetime ) # 2023-11-10 23:28:44.900527
print( type(fecha_hoy_datetime) ) # <class 'datetime.datetime'>


# ----------
# RECORDAR
# ----------

"""
time       =>   time.struct_time
datetime   =>   datetime.datetime
"""


# --------------------------------------------------
# Definir un formato con los FORMAT CODES de Fecha
# --------------------------------------------------

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

# EJ-1: viernes 11 de noviembre de 2023 - 11h:19m
f1 = '%A %d de %B de %Y - %Hh:%Mm:%Ss'

# EJ-2: noviembre 11 de 2023. Son las 11 horas y 19 minutos.
f2 = '%B %d de %Y. Son las %H horas y %M minutos'


# -----------------------------------
# Fecha "time" con formato español
# -----------------------------------
#!  => time
#*  fecha_formato = time.strftime ( formato , fecha_time )

fecha_time_f1 = time.strftime( f1 , fecha_hoy_time )
fecha_time_f2 = time.strftime( f2 , fecha_hoy_time )


# --------------------------------------
# Fecha "datetime" con formato español
# --------------------------------------
#!  => datetime
#*  fecha_formato = fecha_datetime.strftime( formato )

fecha_datetime_f1 = fecha_hoy_datetime.strftime( f1 )
fecha_datetime_f2 = fecha_hoy_datetime.strftime( f2 )


# ------------
# RESULTADOS
# ------------
print('\n\nRESULTADOS')

print('\nFecha HOY - time')
print( fecha_time_f1 )
print( fecha_time_f2 )

print('\nFecha HOY - datetime')
print( fecha_datetime_f1 )
print( fecha_datetime_f2 )