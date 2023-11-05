# ============================================================
# Formato Manual de Fechas datetime

# - con lo aprendido anteriormente
# - y estableciendo valores de diccionarios
# - podemos dar un formato manual a las fechas
# - incluso cambiar manualmente el idioma

# ! RECORDAR: algo parecido hicimos en formato_manual_time.py
# ============================================================


import datetime


#? 1) Establecer la fecha actual, fecha en pasado & fecha en futuro
print('\n1) Establecer la fecha actual, fecha en pasado & fecha en futuro')
# - RECORDAR que datetime devuelve un objeto
# ! del tipo datetime.datetime
# - RECORDAR también => la tupla de valores para fechas fijas
# * datetime.datetime(año, mes, día, hora, minutos, segundos)


fecha_actual = datetime.datetime.now()
fecha_pasado = datetime.datetime(1913, 8, 30, 15, 5, 9)
fecha_futuro = datetime.datetime(2065, 2, 9, 7, 6, 5)

print( fecha_actual , type(fecha_actual) ) # 2023-11-05 17:11:11.366028 <class 'datetime.datetime'>
print( fecha_pasado , type(fecha_pasado) ) # 1913-08-30 15:05:09 <class 'datetime.datetime'>
print( fecha_futuro , type(fecha_futuro) ) # 2065-02-09 07:06:05 <class 'datetime.datetime'>



#? 2) Establecer valores de diccionario para meses y días
print('\n2) Establecer valores de diccionario para meses y días')
# - tal y como lo hicimos la anterior vez
# - establecemos diccionarios para los días de la semana
# - y los nombres de los meses
# - y de esta manera poder darun formato en español de las fechas

dias_spanish = {
    1 : 'Lunes',
    2 : 'Martes',
    3 : 'Miércoles',
    4 : 'Jueves',
    5 : 'Viernes',
    6 : 'Sábado',
    7 : 'Domingo'
}

meses_spanish = {
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



#? 3) Funciones para corrección de 1 a 2 dígitos en fecha/hora
print('\n3) Funciones para corrección de 1 a 2 dígitos en fecha/hora')
# - ya habíamos visto este problema
# - si deseamos por ejemplo una hora: 07:05:09
# - por defecto vamos a tener: 7:5:9
# - por tanto vamos a establecer unas funciones de corrección para esto
# - y una función adicional para expresar AM o PM
# ! vamos a plantear una correccion de dígito distinta a la planteada en el capítulo de time


def correccion_digito(unidad):
    if unidad >= 0 and unidad <= 9: # RECORDAR: la otra vez jugamos con el tamaño del dígito transformado a STRING
        return '0{}'.format(unidad)
    else:
        return '{}'.format(unidad)
# end def


def am_pm(hora):
    if hora >= 12 and hora <= 23:
        return 'PM'
    else:
        return 'AM'
# end def



#? 4) Establecer formatos personalizados
print('\n4) Establecer formatos personalizados')
# - podemos hacerlo por medio de funciones
# - que van a retornar un string
# - para esto utilizamos el string format
# ! IMPORTANTE: estas funciones reciben un tipo de dato "datetime.datetime"


# -----------------------------------------------------------------
# *  FORMATO 1 => EJ: Domingo 10 de Diciembre de 2023 - 18h:20m:25s
# -----------------------------------------------------------------
def aplicar_formato1(fecha_datetime):
    return '{} {} de {} de {} - {}h:{}m:{}s'.format(
        dias_spanish[fecha_datetime.isoweekday()],
        correccion_digito(fecha_datetime.day),
        meses_spanish[fecha_datetime.month],
        fecha_datetime.year,
        correccion_digito(fecha_datetime.hour),
        correccion_digito(fecha_datetime.minute),
        correccion_digito(fecha_datetime.second)
    )
# end def


# ---------------------------------------------------- 
# *  FORMATO 2 => EJ: Diciembre 10 de 2023 - 18:20 pm
# ----------------------------------------------------
def aplicar_formato2(fecha_datetime):
    return '{} {} de {} - {}:{} {}'.format(
        meses_spanish[fecha_datetime.month],
        correccion_digito(fecha_datetime.day),
        fecha_datetime.year,
        correccion_digito(fecha_datetime.hour),
        correccion_digito(fecha_datetime.minute),
        am_pm(fecha_datetime.hour)
    )
# end def



#? 5) Aplicando formatos
print('\n4) Aplicando formatos')
# - se muestra en esta sección los resultados generados
# - la fecha tal y como se presenta en el formato "datetime.datetime"
# - el fomato personalizado 1
# - el fomato personalizado 2


print('\nFECHA ACTUAL (momento de ejecución del script):')

print(fecha_actual) # 2023-11-05 00:17:40.087102
print( aplicar_formato1(fecha_actual) ) # Domingo 5 de Noviembre de 2023 - 00h:17m:40s
print( aplicar_formato2(fecha_actual) ) # Noviembre 5 de 2023 - 00:17 AM

print('\nFECHA DEL PASADO:')

print(fecha_pasado) # 2018-03-19 15:45:23
print( aplicar_formato1(fecha_pasado) ) # Lunes 19 de Marzo de 2018 - 15h:45m:23s
print( aplicar_formato2(fecha_pasado) ) # Marzo 19 de 2018 - 15:45 PM

print('\nFECHA DEL FUTURO:')

print(fecha_futuro) # 1955-05-08 07:06:05
print( aplicar_formato1(fecha_futuro) ) # Domingo 8 de Mayo de 1955 - 07h:06m:05s
print( aplicar_formato2(fecha_futuro) ) # Mayo 8 de 1955 - 07:06 AM