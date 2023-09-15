# =========================================================================================
# Secuencias de Escape

# SECUENCIA  NOMBRE           DEFINICIÓN
#   \\       Backslash        Para insertar el caracter \ en un String
#   \'       Comilla Simple   Para insertar la comilla simple en un String
#   \"       Comilla doble    Para insertar la comilla doble en un String
#   \b       Retroceso        Elimina un caracter del String al momento de aparecer en el output de la consola.
#   \f       Formfeed         Imprime una nueva línea indentada al final de la línea anterior.
#   \v       Tab Vertical     Realiza lo mismo que el Formfeed
#   \t       Tab Horizontal   Inserta un espaciado de tabulación
#   \r       Carriage return  Inserta los caracteres después de \r al inicio del String
#   \n       Nueva Línea      Inserta un salto del línea en tabulación 0
# =========================================================================================

#? 1)  \\ Backslash
print('Este es un backslash \ lo podemos poner así')
print('Esta secuencia \n es para poner una nueva línea')
print('Esta secuencia \\n es para poner una nueva línea')
print('Por tanto \\ es una manera segura de poner backslash')
print('---------')
var_1 = 'Este es un backslash \ lo podemos poner así'
var_2 = 'Esta secuencia \n es para poner una nueva línea'
var_3 = 'Esta secuencia \\n es para poner una nueva línea'
var_4 = 'Por tanto \\ es una manera segura de poner backslash'

print(var_1)
print(var_2)
print(var_3)
print(var_4)


#? 2) \' Comilla Simple
#? 3) \" Comilla Doble
#print('la palabra 'python' va en comilla simple') #! ERROR de sintaxis

# => una solución a este erro (usar comilla doble)
# es decir, alternar el uso de comilla doble y simple
print("la palabra 'python' va en comilla simple")
print('la palabra "python" va en comilla doble')

# => otra solución es con las secuencias de escape
print('la palabra \'python\' va en comilla simple')
print("la palabra \"python\" va en comilla doble")


#? 4) \b Retroceso
# - elimina el caracter que tiene a la izquierda

print('palabra')
print('pala\bbra')
print('Hola Sebas Silva')
print('Hola \bSebas \bSilva')

#? 5) \f Formfeed
# - Para añadir nueva línea con tab secuencial
# - Puede ser que algunos editores de código no lo reconozcan

print('HolaSebasSilva')
print('Hola\fSebas\fSilva')

#? 6) \v Tab Vertical
# - Hace lo mismo que el Formfeed
# - Puede ser que algunos editores de código no lo reconozcan

print('HolaSebasSilva')
print('Hola\vSebas\vSilva')

#? 7) \t Tab Horizontal
# - Para introducir un espaciado de tab

print('HolaSebasSilva')
print('Hola\tSebas\tSilva')
print('Hola\tSebas\t\tSilva')
print('Hola\tSebas\t\t\tSilva')

#? 8) \r Carriage Return
# - Básicamente toma lo que tiene a la derecha
# - Y lo pone al inicio
# - Ocupando el número de caracteres de lo que hay a la derecha

print('abcdef xyz')
print('abcdef\rxyz')
print('abcdef\r123')

# - Se ejecuta de izquierda a derecha (?)
print('abcdef\rxyz\r12')
# xyzdef\r12
# 12zdef

#? 9) \n Nueva línea
#! IMPORTANTE

# - Inserta un nuevo salto de línea

print('HolaSebasSilva')
print('Hola\nSebas\nSilva')
print('Hola\nSebas\n\nSilva')

# - ahora podremos olvidarnos de esta técnica
print('Línea 1')
print('Línea 2')
print('Línea 3')
print()
print('Línea 4')

print('Línea 1')
print('Línea 2')
print('Línea 3')
print('') # o también print("")
print('Línea 4')

print('\nLínea 1')
print('Línea 2')
print('Línea 3\n')
print('Línea 4')
