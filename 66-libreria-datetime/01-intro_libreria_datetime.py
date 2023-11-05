# ==========================================================
# Librería / Módulo => datetime

# - una librería más detallada para trabajar fecha y hora
# - para trabajar de una manera más fácil
# ==========================================================

#? 1) importación del módulo datetime
print('\n1) importación del módulo datetime')

import datetime



#? 2) datetime.datetime.now() => fecha / hora actual (momento de ejecución)
print('\n2) datetime.datetime.now() => fecha / hora actual (momento de ejecución)')
# - para obtener la fecha y hora actuales
# - al momento justo de la ejecución del programa
# ! se devuelve un objeto de tipo datetime.datetime

fecha_actual = datetime.datetime.now()

print(fecha_actual) # 2023-11-04 18:01:21.142989
print( type(fecha_actual) ) # <class 'datetime.datetime'>

# => el resultado se presenta en este orden:
# año-mes-día hora:minutos:segundos:microsegundos



#? 3) Acceder a los elementos de datetime
print('\n3) Acceder a los elementos de datetime')
# - podemos acceder a los elementos de este elemento / objeto datetime
# - ya veremos que estos elementos reciben el nombre de "atributos"
# - al momento de su acceso, NO debemos invocar los paréntesis ()
# - se accede con un punto . + el nombre de estos atributos
# - los elementos aquí presentados se devuelven en int
# ! el nombre de estos elementos / atributos son los nombres de los elementos de fecha en inglés
# ! este acceso a los elementos tendrá más sentido cuando veamos POO (Programación Orientada a Objetos)

"""
Elemento de Acceso          |  Manera de Acceder
-----------------------------------------------------------
acceder al año              |  fecha_datetime.year 
acceder al mes              |  fecha_datetime.month 
acceder al día              |  fecha_datetime.day 
acceder a la hora           |  fecha_datetime.hour
acceder a los minutos       |  fecha_datetime.minute
acceder a los segundos      |  fecha_datetime.second
acceder a los microsegundos |  fecha_datetime.microsecond
"""

fecha_actual = datetime.datetime.now()
anio = fecha_actual.year
mes = fecha_actual.month
dia = fecha_actual.day
hora = fecha_actual.hour
minutos = fecha_actual.minute
segundos = fecha_actual.second
microsegundos = fecha_actual.microsecond


print( fecha_actual, '|', type(fecha_actual) ) # 2023-11-04 18:18:04.222986 | <class 'datetime.datetime'>
print( anio, '|', type(anio) ) # 2023 | <class 'int'>
print( mes, '|', type(mes) ) # 11 | <class 'int'>
print( dia, '|', type(dia) ) # 4 | <class 'int'>
print( hora, '|', type(hora) ) # 18 | <class 'int'>
print( minutos, '|', type(minutos) ) # 18 | <class 'int'>
print( segundos, '|', type(segundos) ) # 4 | <class 'int'>
print( microsegundos, '|', type(microsegundos) ) # 222986 | <class 'int'>



#? 4) Formato Personalizado Fácil para Fecha/Hora Actual
print('\n4) Formato Personalizado Fácil para Fecha/Hora Actual')
# - debido al fácil acceso de estos elementos de la fecha/hora
# - se puede presentar la fecha/hora fácilmente
# - incluso se podría presentar los meses en español
# - por medio de un diccionario


fecha_actual = datetime.datetime.now()

anio = fecha_actual.year
mes = fecha_actual.month
dia = fecha_actual.day
hora = fecha_actual.hour
minutos = fecha_actual.minute
segundos = fecha_actual.second
microsegundos = fecha_actual.microsecond

meses = {
    1 : 'Enero',
    2 : 'Febrero',
    3 : 'Marzo',
    4 : 'Abril',
    5 : 'Mayo',
    6 : 'Junio',
    7 : 'Julio',
    8 : 'Agosto',
    9 : 'Septiembre',
    10 : 'Octubre',
    11 : 'Noviembre',
    12 : 'Diciembre'
}

print( '{}/{}/{}'.format(anio, mes, dia) ) # 2023/11/4
print( '{}h:{}m:{}s'.format(hora, minutos, segundos) ) # 22h:52m:22s
print( '{} de {} de {} y son las {}:{}'.format(dia, meses[mes], anio, hora, minutos) ) # 4 de Noviembre de 2023 y son las 22:52



#? 5) Crear una fecha (pasado / futuro) => datetime.datetime()
print('\n5) Crear una fecha (pasado / futuro) => datetime.datetime()')
# - se crea de una manera más flexible que en "time"
# - podemos pasar solo valores de año, mes y día
# - o también los 6 valores de año, mes, día, hora, minutos, segundos

# EJ: 20 de Julio de 2001
fecha_1 = datetime.datetime(2001, 7, 20)
print( fecha_1, type(fecha_1) ) # 2001-07-20 00:00:00 <class 'datetime.datetime'>

# EJ: 19 de Diciembre de 2025 - 19:52:23
fecha_2 = datetime.datetime(2025, 12, 19, 19, 52, 23)
print( fecha_2, type(fecha_2) ) # 2025-12-19 19:52:23 <class 'datetime.datetime'>



#? 6) .replace() => cambiar un valor de una fecha
print('\n6) datetime.replace() => cambiar un valor de una fecha')

fecha = datetime.datetime(2022, 6, 18, 7, 35, 15)
print( fecha, type(fecha) ) # 2022-06-18 07:35:15 <class 'datetime.datetime'>

# -----------------------------------------------------------------
# 6.1) ERROR al tratar de reemplazar sin método replace
print('\n6.1) ERROR al tratar de reemplazar sin método replace\n')
# -----------------------------------------------------------------

#fecha.year = 2019
#! AttributeError: attribute 'year' of 'datetime.date' objects is not writable


# --------------------------------------------------------
# 6.2) Corrección => usando datetime.replace()
print('\n6.2) Corrección => usando .replace()\n')
# --------------------------------------------------------
# - pero la variable original no se modifica
# - debemos guardar en una variable nueva
# - o sobreescribir la anterior


# => reemplazando sin guardar o sobrescribir / SIN EFECTO
fecha.replace(year=2019, month=2)
print( fecha, type(fecha) ) # 2022-06-18 07:35:15 <class 'datetime.datetime'>


# => Sobrescribiendo variable original
fecha = fecha.replace(year=2019, month=2)
print( fecha, type(fecha) ) # 2019-02-18 07:35:15 <class 'datetime.datetime'>


# => Guardando en una nueva variable
fecha_2 = fecha.replace(year=2005, month=4)
print( fecha_2, type(fecha_2) ) # 2005-04-18 07:35:15 <class 'datetime.datetime'>



#? 7) Métodos .iso => Formato ISO de una fecha
print('\n7) Métodos .iso => Formato ISO de una fecha')
# - ISO => International Standard Organization
# - Código Internacional de la Normalización
# - dispone de una formato estádar para la presentación de una fecha

# ---------------------------------
# 7.1) fecha de ejemplo
print('\n7.1) fecha de ejemplo\n')
# ---------------------------------

fecha = datetime.datetime(2022, 6, 18, 7, 35, 15)
print( fecha, type(fecha) ) # 2022-06-18 07:35:15 <class 'datetime.datetime'>


# ---------------------------------------------------------------
# 7.2) .isoformat() => presentar fecha en formato ISO
print('\n7.2) .isoformat() => presentar fecha en formato ISO\n')
# ---------------------------------------------------------------
# - método que devuelve una fecha "datetime" en formato ISO como string

fecha_ISO = fecha.isoformat()
print( fecha_ISO, type(fecha_ISO) ) # 2022-06-18T07:35:15 <class 'str'>


# ----------------------------------------------------------------------
# 7.3) .isocalendar() => tupla (año, semana, día de semana)
print('\n7.3) .isocalendar() => tupla (año, semana, día de semana)\n')
# ----------------------------------------------------------------------

calendario_ISO = fecha.isocalendar()
print( calendario_ISO, type(calendario_ISO) )
# datetime.IsoCalendarDate(year=2022, week=24, weekday=6) <class 'datetime.IsoCalendarDate'>

# => accediendo a los valores de la tupla
print(calendario_ISO.year) # 2022
print(calendario_ISO.week) # 24
print(calendario_ISO.weekday) # 6


# -------------------------------------------------------------
# 7.4) .isoweekday() => retorna el día de la semana
print('\n7.4) .isoweekday() => retorna el día de la semana\n')
# -------------------------------------------------------------
"""
1 == Lunes
7 == Domingo
"""

dia_semana = fecha.isoweekday()
print(dia_semana)



#? 8) Fechas más atrás del punto cero
print('\n8) Fechas más atrás del punto cero')
# - Recordar el punto 0
# - 1 de enero de 1970
# - con librería "time" no era posible manejar fechas más antiguas que este punto
# - con "datetime" si lo podemos hacer

fecha_pasado = datetime.datetime(1913, 5, 20, 15, 25, 30)
print( fecha_pasado, type(fecha_pasado) ) # 1913-05-20 15:25:30 <class 'datetime.datetime'>

# => ¿que día era en esta fecha?
dia = fecha_pasado.isoweekday()
print( dia ) # 2 == Martes