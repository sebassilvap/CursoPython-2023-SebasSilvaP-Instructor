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
print('1)  Backslash')
print()

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



#? 2) \' Comilla Simple  y  \" Comilla Doble
print('2) Comilla Simple y Comilla Doble')
print()

#print('la palabra 'python' va en comilla simple') #! ERROR de sintaxis

# => una solución a este erro (usar comilla doble)
# es decir, alternar el uso de comilla doble y simple
print("la palabra 'python' va en comilla simple")
print('la palabra "python" va en comilla doble')

# => otra solución es con las secuencias de escape
print('la palabra \'python\' va en comilla simple')
print("la palabra \"python\" va en comilla doble")



#? 3) \b Retroceso
print('3) Retroceso')
print()

# - elimina el caracter que tiene a la izquierda

print('palabra')
print('pala\bbra')
print('Hola Sebas Silva')
print('Hola \bSebas \bSilva')



#? 4) \f Formfeed
print('4) Formfeed')
print()

# - Para añadir nueva línea con tab secuencial
# - Puede ser que algunos editores de código no lo reconozcan

print('HolaSebasSilva')
print('Hola\fSebas\fSilva')



#? 5) \v Tab Vertical
print('5) Tab Vertical')
print()

# - Hace lo mismo que el Formfeed
# - Puede ser que algunos editores de código no lo reconozcan

print('HolaSebasSilva')
print('Hola\vSebas\vSilva')



#? 6) \t Tab Horizontal
print('6) Tab Horizontal')
print()

# - Para introducir un espaciado de tab

print('HolaSebasSilva')
print('Hola\tSebas\tSilva')
print('Hola\tSebas\t\tSilva')
print('Hola\tSebas\t\t\tSilva')



#? 7) \r Carriage Return
print('7) Carriage Return')
print()

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



#? 8) \n Nueva línea
print('8) Nueva línea')
print()

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