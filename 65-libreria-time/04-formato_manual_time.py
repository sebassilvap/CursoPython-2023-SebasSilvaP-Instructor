# =====================================================================================
# Dar un formato personalizado a time

# - básicamente hemos aprendido
# - que cuando tenemos un objeto de tipo time.struct_time
# - nosotros podemos acceder a todos los elementos de le fecha / hora
# - aprendimos 2 maneras de generar una fecha / hora de tipo time.struct_time

# *     A) time.localtime() => para fecha / hora actual (momento de ejecución)
# *     B) time.strptime() => transformación / parseo a de string a time.struct_time

# - también aprendimos que en un tipo time.struct_time
# - podemos acceder a sus elementos de manera fácil
# - con notación de punto + atributos (que ya veremos en POO)
# - (POO / OOP => Programación Orientada a Objetos)

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

# - con los valores de mes y día de la semana
# - (.tm_mon & .tm_wday RESPECTIVAMENTE)
# - podemos crear / generar diccionarios que permitan adaptar estos valores
# - a los nombres de los días & meses en cualquier idioma
# - también veremos otro problema
# - el valor de hora / minutos / segundos viene dado por 1 solo dígito
# - si tenemos una hora por ejemplo: 07:05:02
# - con estos valores se nos devolvería 7:5:2
# - esto lo podemos corregir con funciones y string format
# - en esta lección se detalla como podemos realizar todo esto

# =====================================================================================


import time



#? 1) Generar 3 fechas de ejemplo
print('\n1) Generar 3 fechas de ejemplo')
# - vamos a trabajar con 3 fechas de ejemplo
# - la fecha actual
# - una fecha del pasado
# - una fecha del futuro
# ! el objetivo es dejar estas fechas como tipo "time_struct.time"

fecha_actual = time.localtime()

# --------------------------------------------------------
# fechas pasado/futuro con tuplas + .asctime
# ! Recordar: que no importa si en este punto no sabemos
# ! el día exacto de la semana
# ! y el día exacto del año
# - esto será corregido luego con .mktime

#                 dd/mm/yyyy - hh:mm:ss
# fecha pasado => 21/10/1987 - 13:05:21
# fecha futuro => 02/04/2031 - 05:01:09
# --------------------------------------------------------

# => generando tuplas
# *  (año, mes, día, horas, minutos, segundos, día de la semana, día del año, dst)

tupla_fecha_pasado = (1987, 10, 21, 13, 5, 21, 0, 0, 0)
tupla_fecha_futuro = (2031, 4, 2, 5, 1, 9, 0, 0, 0)

# -----------------------------------------------
# ms desde tiempo 0 a fechas propuestas
# - utilizamos el método .mktime(tupla_fecha)
# ! los valores día semana y día año se corrigen
# -----------------------------------------------

cero_a_fecha_pasado = time.mktime(tupla_fecha_pasado)
cero_a_fecha_futuro = time.mktime(tupla_fecha_futuro)

# ------------------------------------------------------
# de ms a fecha_string FORMATO ESTÁNDAR
# - utilizamos el método .ctime(milisegundos_desde_t0)
# ------------------------------------------------------

fecha_pasado_string = time.ctime( cero_a_fecha_pasado )
fecha_futuro_string = time.ctime( cero_a_fecha_futuro )

# ------------------------------------------
# RECORDAR: el formato estándar como String
# ------------------------------------------

formato_estandar = '%a %b %d %H:%M:%S %Y'

# ------------------------------------------------------------
# parseo de string => time.struct_time
# - utilizamos el método .strptime( fecha_string , formato )
# ------------------------------------------------------------

fecha_pasado_time = time.strptime( fecha_pasado_string , formato_estandar )
fecha_futuro_time = time.strptime( fecha_futuro_string , formato_estandar )

# ----------------
# RESULTADO FINAL
# ----------------

print( 'FECHA ACTUAL =', fecha_actual, type(fecha_actual) ) # FECHA ACTUAL = time.struct_time(tm_year=2023, tm_mon=11, tm_mday=5, tm_hour=15, tm_min=59, tm_sec=57, tm_wday=6, tm_yday=309, tm_isdst=0) <class 'time.struct_time'>
print( 'FECHA PASADO =', fecha_pasado_time, type(fecha_pasado_time) ) # FECHA PASADO = time.struct_time(tm_year=1987, tm_mon=10, tm_mday=21, tm_hour=14, tm_min=5, tm_sec=21, tm_wday=2, tm_yday=294, tm_isdst=-1) <class 'time.struct_time'>
print( 'FECHA FUTURO =', fecha_futuro_time, type(fecha_futuro_time) ) # FECHA FUTURO = time.struct_time(tm_year=2031, tm_mon=4, tm_mday=2, tm_hour=6, tm_min=1, tm_sec=9, tm_wday=2, tm_yday=92, tm_isdst=-1) <class 'time.struct_time'>



#? 2) Definir Diccionarios para nombres de meses & días
print('\n2) Definir Diccionarios para nombres de meses & días')

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

dias_semana = {
    0 : 'Lunes',
    1 : 'Martes',
    2 : 'Miércoles',
    3 : 'Jueves',
    4 : 'Viernes',
    5 : 'Sábado',
    6 : 'Domingo'
}


#? 3) Función de corrección de dígito
print('\n3) Función de corrección de dígito')
# - recordemos que nuestro formato personalizado
# - pretende la inclusión SIEMPRE de 2 dígitos en la fecha mostrada
# - no importa si se trata de la fecha o la hora
# - pretendemos tener algo así:

# *     dd/mm/yyyy - hh:mm:ss

# - y como sabemos los atributos .tm_
# - nos devuelven 1 dígito
# - por tanto vamos a corregir esto con una función

def corregir_digito_fecha_hora(digito):
    if len(str(digito)) == 1: # tamaño del string == 1
        return '0{}'.format(digito)
    else:
        return '{}'.format(digito)
# end def


#? 4) Función para determinar AM / PM
print('\n4) Función para determinar AM / PM')
# - como vemos, este atributo no está presente
# - en los elementos disponibles de "time.struct_time"
# - pero podemos generarlo fácilmente con una función
# - y el valor del atributo tm_hour
# - (0 a 11 => AM | 12 a 23 => PM)

def am_pm(fecha_time):
    hora = fecha_time.tm_hour
    
    if hora >= 0 and hora <= 11:
        return 'AM'
    else:
        return 'PM'
# end def



#? 5) Definir formatos personalizados
print('\n5) Definir formatos personalizados')
# - vamos a definir formatos personalizados 
# - para presentar las fechas en idioma español
# - y maneras generales

# ----------------------------------------------
# EJ: Lunes 20 de Noviembre de 2023 - 15:25:18
# ----------------------------------------------
print('Fecha Ejemplo:', 'Lunes 20 de Noviembre de 2023 - 15:25:18')


# ------------------------
# *   Formato 1
# 20/11/2023 - 15h:25m:18s
# ------------------------
print('Ejemplo Formato 1:', '20/11/2023 - 15h:25m:18s')


# --------------------------------------------
# *   Formato 2
# Lunes 20 de Noviembre de 2023 | 15h:25m PM
# --------------------------------------------
print('Ejemplo Formato 2:', 'Lunes 20 de Noviembre de 2023 | 15h:25m PM')



#? 6) Ajustar formatos personalizados por medio de funciones
print('\n6) Ajustar formatos personalizados por medio de funciones')
# - vamos a construir funciones
# - que nos permitan ajustar estos formatos definidos
# - de manera personalizada

def aplicar_formato_1(fecha_time):
    return '{}/{}/{} - {}h:{}m:{}s'.format(
        corregir_digito_fecha_hora(fecha_time.tm_year),
        corregir_digito_fecha_hora(fecha_time.tm_mon),
        corregir_digito_fecha_hora(fecha_time.tm_mday),
        corregir_digito_fecha_hora(fecha_time.tm_hour),
        corregir_digito_fecha_hora(fecha_time.tm_min),
        corregir_digito_fecha_hora(fecha_time.tm_sec),
    )
# end def

def aplicar_formato_2(fecha_time):
    return '{} {} de {} de {} | {}h:{}m {}'.format(
        dias_semana[ fecha_time.tm_wday ],
        corregir_digito_fecha_hora(fecha_time.tm_mday),
        meses[ fecha_time.tm_mon ],
        corregir_digito_fecha_hora(fecha_time.tm_year),
        corregir_digito_fecha_hora(fecha_time.tm_hour),
        corregir_digito_fecha_hora(fecha_time.tm_min),
        am_pm(fecha_time)
    )
# end def



#? 7) Aplicando FORMATO 1
print('\n7) Aplicando FORMATO 1')

print( 'FECHA ACTUAL =', aplicar_formato_1(fecha_actual) ) # FECHA ACTUAL = 2023/11/05 - 16h:39m:37s
print( 'FECHA PASADO =', aplicar_formato_1(fecha_pasado_time) ) # FECHA PASADO = 1987/10/21 - 14h:05m:21s
print( 'FECHA FUTURO =', aplicar_formato_1(fecha_futuro_time) ) # FECHA FUTURO = 2031/04/02 - 06h:01m:09s



#? 8) Aplicando FORMATO 2
print('\n7) Aplicando FORMATO 2')

print( 'FECHA ACTUAL =', aplicar_formato_2(fecha_actual) ) # FECHA ACTUAL = Domingo 05 de Noviembre de 2023 | 16h:39m PM
print( 'FECHA PASADO =', aplicar_formato_2(fecha_pasado_time) ) # FECHA PASADO = Miércoles 21 de Octubre de 1987 | 14h:05m PM
print( 'FECHA FUTURO =', aplicar_formato_2(fecha_futuro_time) ) # FECHA FUTURO = Miércoles 02 de Abril de 2031 | 06h:01m AM
