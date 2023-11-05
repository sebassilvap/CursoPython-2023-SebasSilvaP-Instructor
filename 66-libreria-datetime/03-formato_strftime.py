# ===========================================================
# Formato de datetime con strftime y strptime

# - al igual que en el módulo "time"
# - un tipo de dato datetime tiene el método:

# *    fecha_datetime.strftime( formato ) => retorna un STRING

# - el formato se establece por medio de códigos de formato
# - pero como vimos, el string por defecto se forma en inglés
# - luego veremos como cambiar el idioma por defecto
# - por medio del módulo "locale"

# - https://docs.python.org/3/library/datetime.html
# ===========================================================

import datetime


#? 1) Format Codes de strftime() y strptime()
print('\n1) Format Codes de strftime() y strptime()')
# - ya habíamos visto esto en la librería "time"
# - pero lo volvemos a presentar como un recordatorio
# ! RECORDAR que por defecto nos presenta en idioma inglés

"""
%a  día de la semana abreviado (Sun, Mon, ...)
%A  día de la semana completo (Sunday, Monday, ...)
%w  día de la semana como número (0 = Domingo / 6 = Sábado)
%d  día del mes (01, 02, ..., 31)
%b  mes abreviado (Jan, Feb, ... , Dec)
%B  mes completo (January, February, ... , December)
%m  mes como número decimal (01, 02, ..., 12)
%y  año con 2 números decimales (00, 01, ... , 99)
%Y  año con 4 números decimales (0001, ... ,1999, 2000, 2001)
%H  hora en formato de 24 (00, 01, ..., 23)
%I  hora en formato de 12 (01, 02, ..., 12)
%p  expresar AM / PM  (AM, PM)
%M  minutos (00, 01, ..., 59)
%S  segundos (00, 01, ..., 59)
%j  día del año (001, ... , 366)
%W  semana del año con lunes en semana cero (00, 01, ..., 53)

%c  Representación Local de fecha/hora (Tue Aug 16 21:30:00 1988)
%x  Representación local de fecha (08/16/88)
%X  Representación local de hora (21:30:00)
"""


#? 1) Establecer 2 fechas de ejemplo
print('\n1) Establecer 2 fechas de ejemplo')

fecha_1 = datetime.datetime(2018, 3, 19, 15, 45, 23)
fecha_2 = datetime.datetime(1955, 5, 8, 7, 6, 5)

print( fecha_1 , type(fecha_1) ) # 2018-03-19 15:45:23 <class 'datetime.datetime'>
print( fecha_2 , type(fecha_2) ) # 1955-05-08 07:06:05 <class 'datetime.datetime'>



#? 2) Representación local de fecha/hora => %c
print('\n2) Representación local de fecha/hora => %c')

fecha_1_local_datetime = fecha_1.strftime('%c')
fecha_2_local_datetime = fecha_2.strftime('%c')

print( fecha_1_local_datetime , type(fecha_1_local_datetime) ) # Mon Mar 19 15:45:23 2018 <class 'str'>
print( fecha_2_local_datetime , type(fecha_2_local_datetime) ) # Sun May  8 07:06:05 1955 <class 'str'>



#? 3) Representación local de sólo fecha => %x
print('\n3) Representación local de sólo fecha => %x')
# - la representación local de fecha es:
# *     mes/día/año ==> mm/dd/yy

fecha_1_local_date = fecha_1.strftime('%x')
fecha_2_local_date = fecha_2.strftime('%x')

print( fecha_1_local_date , type(fecha_1_local_date) ) # 03/19/18 <class 'str'>
print( fecha_2_local_date , type(fecha_2_local_date) ) # 05/08/55 <class 'str'>



#? 4) Representación local de sólo hora => %X
print('\n4) Representación local de sólo hora => %X')
# - la representación local de hora es:
# *     hora:minutos:segundos ==> hh:mm:ss

fecha_1_local_time = fecha_1.strftime('%X')
fecha_2_local_time = fecha_2.strftime('%X')

print( fecha_1_local_time , type(fecha_1_local_time) ) # 15:45:23 <class 'str'>
print( fecha_2_local_time , type(fecha_2_local_time) ) # 07:06:05 <class 'str'>



#? 5) Formato Personalizado con Códigos de Formato
print('\n5) Formato Personalizado con Códigos de Formato')
# - recordar que por defecto sería en idioma inglés
# - a menos que hagamos cambio en el "locale"
# ! Librería / Módulo "locale" => lo vemos luego

# EJ: November 05th, 2023 - 20h:33m:21s

formato_personalizado = '%B %dth, %Y - %Hh:%Mm:%Ss'

fecha_1_personalizada = fecha_1.strftime(formato_personalizado)
fecha_2_personalizada = fecha_2.strftime(formato_personalizado)

print('Fecha 1 =' , fecha_1_personalizada , type(fecha_1_personalizada) )
print('Fecha 2 =' , fecha_2_personalizada , type(fecha_2_personalizada) )
# Fecha 1 = March 19th, 2018 - 15h:45m:23s <class 'str'>
# Fecha 2 = May 08th, 1955 - 07h:06m:05s <class 'str'>