# =============================================================
# String Slicing

# - Slicing es una técnica para construir subcadenas de texto
# - substrings
# - a partir de los índices del string original

#*   string[ inicio : final ]
# => inicio - incluyente
# => final  - excluyente
# =============================================================


#? 1) Slicing con índices positivos
print('\n1) Slicing con índices positivos')

palabra = 'programa'
#(+)       01234567
#(-)       87654321

print( palabra[0:2] )
print( palabra[0:3] ) # OK
print( palabra[:3] )  # OK
print()
print( palabra[3:7] )
print( palabra[3:8] )  # OK
print( palabra[3:10] ) # OK
print( palabra[3:] )   # OK
print()
print( palabra[-1:3] ) # no funciona de esta manera
print('hola')



#? 2) Slicing con índices negativos
print('\n2) Slicing con índices negativos')
# - Recordar que aunque sea índice negativo
# - El 'END' => sigue siendo exclusivo

print( palabra[-8:-5] )
print( palabra[:-5] )

print( palabra[-5:-1] ) # el último caracter no aparece
print( palabra[-5:0] )  # no funciona de esta manera
print( palabra[-5:] )   # esta sería la manera correcta



#? 3) El Slicing no tiene Index Error
print('\n3) El Slicing no tiene Index Error')

palabra = 'Python'
#(+)       012345

print( palabra )
print( palabra[0] )  # P => el primer caracter
print( palabra[-1] ) # n => el último caracter
print( palabra[5] ) 
#print( palabra[6] ) #! Index Error => string index out of range

print( palabra[0:3] )
print( palabra[3:6] )

print( palabra[3:100] )  # índice 100 no existe, pero no da index error en el slicing
print( palabra[-100:3] ) # igual si lo hago con -100



#? 4) Pequeño adelanto => casting de variables | casting a número entero
print('\n4) Pequeño adelanto => casting de variables | casting a número entero')

num_1 = 4.2
num_2 = 4.5
num_3 = 4.9

print( num_1, type(num_1) )
print( num_2, type(num_2) )
print( num_3, type(num_3) )

# - veremos a profundidad el tema casting en la siguiente lección
# - por el momento entender que es la manera
# - como podemos transformar de un tipo de variable a otro

ent_1 = int(num_1)
ent_2 = int(num_2)
ent_3 = int(num_3)

print( ent_1, type(ent_1) )
print( ent_2, type(ent_2) )
print( ent_3, type(ent_3) )

# - en este caso los números flotantes han sido transformados a enteros
# - prácticamente la parte decimal desaparece
# - y nos quedamos con la parte entera
# - Si recordamos la función len()
# - esta nos devuelve como entero la longitud de una cadena

cadena = 'hola'
print(cadena, len(cadena))



#? 4) Dividir cualquier palabra a la mitad => slicing + len()
print('\n4) Dividir cualquier palabra a la mitad => slicing + len()')

palabra = 'programa'
#(+)       01234567

#palabra = 'sol'

#palabra = 'contextualización'

print( 'len(palabra) =', len(palabra) )


print( '\nDividiendo palabra con len()' )

final_1era_mitad = len(palabra) / 2
#palabra_1_primera_mitad = palabra[0:final_1era_mitad] #! ERROR => slicing siempre con enteros


print(final_1era_mitad) # resultado de una división nos da SIEMPRE un flotante
print( int(final_1era_mitad) )

primera_mitad = palabra[  : int(final_1era_mitad) ]
print(primera_mitad)

segunda_mitad = palabra[ int(final_1era_mitad) : ]
print(segunda_mitad)

# ==> pero en lugar de crear variables podemos poner esto directamente !!

print( '1era Mitad =' , palabra[ : int(final_1era_mitad)] )
print( '2da  Mitad =' , palabra[ int(final_1era_mitad) : ] )

# - obviamente la división de una palabra funciona al 100%
# - si el tamaño (número de caracteres) del string es PAR
# - en el segundo ejemplo como son 3 letras
# - divide en 1 y 2 letras respectivamente








