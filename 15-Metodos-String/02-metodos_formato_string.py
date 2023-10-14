# =======================================================
# Métodos para dar formato a un string

# - Lista de los métodos más importantes
# - No afectan la variable original
# - Transforman al string para un propósito específico
# =======================================================


#? 1) Para cambiar el tipo
print('\n1) Para cambiar el tipo')
#   .capitalize() => Primera letra con mayúscula
#   .title()      => Primera letra de cada palabra con mayúscula
#   .upper()      => Todo en mayúsculas
#   .lower()      => Todo en minúsculas
#   .swapcase()   => Invierte el case del texto

var_1 = 'Me gusta APRENDER PythoN.'

print( 'var_1 =' , var_1 )
print( 'var_1.capitalize() =' , var_1.capitalize() )
print( 'var_1.title() =' , var_1.title() )
print( 'var_1.upper() =' , var_1.upper() )
print( 'var_1.lower() =' , var_1.lower() )
print( 'var_1.swapcase() =' , var_1.swapcase() )

var_1 = 'Me gusta APRENDER PythoN.'
print(var_1)
var_1.upper()
print(var_1)

# -----------------------------------------------------------------------
#! NOTA IMPORTANTE
# - veremos más luego que algunos métodos MODIFICAN la variable original
# - en este caso los métodos de string no lo hacen
# - para ver su funcionamiento tenemos:
# - que hacer un print
# - guardarlos en otra variable
# -----------------------------------------------------------------------

var_1_upper = var_1.upper()
print(var_1)
print(var_1_upper)



#? 2) Para justificación del texto
print('\n2) Para justificación del texto')
#   .center(x) => Justificación al centro en x espacios
#   .ljust(x) => Justificación a la izquierda en x espacios
#   .rjust(x) => Justificación a la derecha en x espacios

var_1 = 'python'
#        012345

print( 'var_1 =' , var_1 , 'len =' , len(var_1) )

# .center(x)
center_10 = var_1.center(10)
center_20 = var_1.center(20)
print( 'center_10 =', center_10 , len(center_10) )
print( 'center_20 =', center_20 , len(center_20) )

# .ljust(x)
ljust_10 = var_1.ljust(10)
ljust_20 = var_1.ljust(20)
print( 'ljust_10 =', ljust_10 , len(ljust_10) )
print( 'ljust_20 =', ljust_20 , len(ljust_20) )

# .rjust(x)
rjust_10 = var_1.rjust(10)
rjust_20 = var_1.rjust(20)
print( 'rjust_10 =', rjust_10 , len(rjust_10) )
print( 'rjust_20 =', rjust_20 , len(rjust_20) )



#? 3) Conteo de caracteres repetidos
print('\n3) Conteo de caracteres repetidos')
# .count(substring, start, end) => búsqueda de izquierda a derecha con inicio y fin opcionales

var_1 = 'nunca digas nunca en esta vida.'
#(+)     0123456789012345678901234567890
#        0         1         2         3

# .count()
print(var_1.count('a')) # 5
print(var_1.count('nunca')) # 2
print(var_1.count('nunca', 2)) # 1
print(var_1.count('nunca', 2 , 10))
print(var_1.count('nunca', 2 , 18))



#? 4) Búsqueda por caracter => Retorno de índice CON ERROR
print('\n4) Búsqueda por caracter => Retorno de índice CON ERROR')
# .index(substring, start, end) => búsqueda de un caracter de izquierda a derecha
# .rindex(substring, start, end) => búsqueda de un caracter de derecha a izquierda

var_1 = 'contextualización'
#(+)     01234567890123456
#        0         1

# .index()
print('\nUtilizando .index()')
print(var_1.index('x')) # 5
print(var_1.index('ó')) # 15
#print(var_1.index('ó',10,15)) #! ValueError => índice 15 no se incluye en la búsqueda 
print(var_1.index('ó',10,16)) # 15
print(var_1.index('n')) # 2
print(var_1.index('n',10)) # 2
#print(var_1.index('n',10,16)) #! ValueError
print(var_1.index('n',10,17)) # 16 
print(var_1.index('n',10,100)) # 16
print(var_1.index('liz')) # 9
#print(var_1.index('lix')) #! ValueError => substring no encontrado

# .rindex()
print('\nUtilizando .rindex()')
print(var_1.rindex('n')) # 16
print(var_1.rindex('n', 3)) # 16
print(var_1.rindex('n', 0, 10)) # 2

var_1 = 'Xuna palabraX que se forma conX'
print(var_1.rindex('X')) # 30
print(var_1.rindex('X',0,5)) # 0
print(var_1.rindex('X',5,20)) # 12



#? 5) Búsqueda por caracter => Retorno de índice SIN ERROR
print('\n5) Búsqueda por caracter => Retorno de índice SIN ERROR')
#   .find(substring, start, end)
#   .rfind(substring, start, end)

# => básicamente lo mismo que index
# => pero no devuelve error si no encuentra
# => en su lugar devuelve -1

var_1 = 'contextualización'
#(+)     01234567890123456
#        0         1

# .find()
print(var_1.index('liz')) # 9
print(var_1.find('liz')) # 9
#print(var_1.index('lit')) #! ValueError: substring no encontrado
print(var_1.find('lit')) # -1
print(var_1.find('n')) # 2


# .rfind()

var_1 = 'Xuna palabraX que se forma conX'

print(var_1.find('X')) # 0
print(var_1.rfind('X')) # 30
print(var_1.find('X',0,20)) # 0
print(var_1.rfind('X',0,20)) # 12
print(var_1.rfind('X',2,12)) # -1



#? 6) Eliminar espaciados y caracteres
print('\n6) Eliminar espaciados y caracteres')
#   .strip()  => eliminación a ambos lados
#   .lstrip() => eliminación a la izquierda
#   .rstrip() => eliminación a la derecha

# => por defecto sin argumento elimina todo tipo de espaciado


# .strip()

var_1 = '   hola mundo   '
var_2 = 'a   hola mundo   a'
var_3 = '   hola mundo'
var_4 = '**********hola****'
var_5 = '\nhola mundo\n'

print('Variables sin aplicar .strip()')
print( var_1 )
print( var_2 )
print( var_3 )
print( var_4 )
print( var_5 )
print('Variables después de aplicar .strip()')
print( var_1.strip() )
print( var_2.strip() )
print( var_3.strip() )
print( var_4.strip('*') )
print( var_5.strip() )


# .lstrip() y .rstrip()
var_1 = '**********hola****'
print('\nUtilización de .lstrip() & .rstrip()')
print( 'var_1 =', var_1 )
print( "var_1.strip('*') =", var_1.strip('*') ) # a ambos lados
print( "var_1.lstrip('*') =", var_1.lstrip('*') ) # a la izquierda
print( "var_1.rstrip('*') =", var_1.rstrip('*') ) # a la derecha



#? 7) .join()
print('\n7) .join()')
# - Une cada caracter de una cadena
# - Con el valor de otra cadena

cadena_1 = 'X'
cadena_2 = '&&'
cadena_3 = ' xx '
cadena_4 = '   '

cadena_principal = 'Python'

print( cadena_1.join(cadena_principal) )
print( cadena_2.join(cadena_principal) )
print( cadena_3.join(cadena_principal) )
print( cadena_4.join(cadena_principal) )



#? 8) .split()
print('\n8) .split()')
# - transforma una cadena en una lista
# ! TEMA Listas: Ya lo veremos a profundidad luego
# - básicamente una lista es una colección de datos
# - cuando no se da el parámetro por defecto separa por espacios

var_1 = 'Python Java C++ Javascript'
split_1 = var_1.split()

print( var_1 , type(var_1) ) # <class 'str'>
print( split_1 , type(split_1) ) # <class 'list'>

var_1 = 'Python,Java,C++,Javascript'
split_1 = var_1.split(',')

#! Ya veremos luego => len() también se puede aplicar en listas
# - en este caso len devuelve el número de elementos en la lista

print( var_1 , type(var_1) , len(var_1) )
print( split_1 , type(split_1) , len(split_1) )

split_1 = var_1.split('*')

print( split_1 , type(split_1) , len(split_1) ) # 1 elemento de lista



#? 9) .splitlines()
print('\n9) .splitlines()')
# - transforma un string en lista
# - separando los saltos de línea (\n)

texto = 'Yo programo en Python\nEl programa en Java\nElla en C++'

print(texto)
print(texto.split())
print(texto.splitlines())

# opción: keepends = True => para conservar saltos de línea
print(texto.splitlines(keepends=True))

# - Se acopla de mejor manera a un string multilínea

poema = '''
En una noche de verano
Yo la conocí
Nunca lo olvidé
Siempre la recordaré
'''

print(poema)
print(poema.splitlines())


#? 10) .expandtabs()
print('\n10) .expandtabs()')
# - como su nombre lo indica
# - sirve para incrementar el tamaño de un tab
# - dentro de un string

var_1 = 'hola\tpython'
print(var_1)
print( var_1.expandtabs() ) # tab por defecto => nuestro caso 4 espacios
print( var_1.expandtabs(1) ) # tab = 1 espacio
print( var_1.expandtabs(2) ) # tab = 2 espacios
print( var_1.expandtabs(4) ) # tab = 4 espacios



#? 10) .replace()
print('\n10) .replace()')
#! UNO DE LOS MÁS IMPORTANTES
# - para reemplazar un caracter o subcadena
# - dentro de una cadena


# => reemplazando un caracter
var_1 = 'pXlabrX secrXtX'
print( var_1 , var_1.replace('X', '***') )

# => reemplazando una subcadena (substring)
var_1 = 'hola mundo'
print(var_1)
print( var_1.replace('mundo' , 'java') )
print( var_1.replace('mundo' , 'python') )
print( var_1.replace('Mundo' , 'python') ) # si no hay coincidencia develve el mismo