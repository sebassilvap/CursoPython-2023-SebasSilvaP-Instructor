# ===========================================================================
# Función Interna range

# - para crear una secuencia de números
#* range(start, stop, end)

# - start: parámetro opcional, 0 por default, establece inicio (inclusivo)
# - end: parámetro obligatorio, establece final (exclusivo)
# - step: prámetro opcional, establece incremento, 1 por default

#! RECORDAR: los tipos de datos en Python
'''
https://www.w3schools.com/python/python_datatypes.asp

----------------------------------------------------
Text Type:	     |    str(OK)
Numeric Types:   |    int(OK), float(OK), complex
Sequence Types:  |    list(OK), tuple, range
Mapping Type:	 |    dict
Set Types:	     |    set, frozenset
Boolean Type:	 |    bool(OK)
Binary Types:	 |    bytes, bytearray, memoryview
None Type:	     |    NoneType(OK)
----------------------------------------------------
'''

# - como vemos range es uno de los tipos de datos para secuencia
# ===========================================================================


#? 1) Creación Básica de Rangos
print('\n1) Creación Básica de Rangos\n')

# rango de 0 a 9
rango_0_9 = range(10) # recordar el end es exclusivo!

# rango de 20 a 30
rango_20_3 = range(20,31)

# rango de 50 a 100 en saltos de 10
rango_50_100_10 = range(50,101,10)

# resultados

print( 'rango_0_9 = ', rango_0_9, '|', type(rango_0_9) )
print( 'rango_20_3 = ', rango_20_3, '|', type(rango_20_3) )
print( 'rango_50_100_10 = ', rango_50_100_10, '|', type(rango_50_100_10) )

# - como vemos se imprime tal y como se crea
# - así como está posiblemente no vemos su utilidad
# - pero podemos usar casting y transformarlo a algo útil
# - ej: a una lista
# - el casting puede darse no solo como vimos sino entre algunos tipos de datos


#? 2) Casting de range a list => list()
print('\n2) Casting de range a list => list()\n')

lista_0_9 = list( rango_0_9 )
lista_20_3 = list( rango_20_3 )
lista_50_100_10 = list( rango_50_100_10 )

# imprimiendo resultados

print( 'lista_0_9 = ', lista_0_9)
print( 'lista_20_3 = ', lista_20_3)
print( 'lista_50_100_10 = ', lista_50_100_10)


#? 3) Su uso fundamental => bucle for
print('\n3) Su uso fundamental => bucle for\n')

#! IMPORTANTE: esto es un abrebocas del tema bucles (ya lo veremos a continuación)
# - el uso fundamental del range es con el bucle for
# - para crear una iteración numérica

# => por ejemplo tomando en cuenta la lista creada anteriormente => lista_0_9

for elemento in lista_0_9:
    print(elemento)
# end for

print()

# => pero antes de hacer toda esta transformación podemos usar directamente el range
for i in range(0,10):
    print(i)

