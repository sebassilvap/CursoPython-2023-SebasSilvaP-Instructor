# ================================================================================
# Métodos booleanos de los String

# - Se llaman métodos booleanos
# - Porque al aplicarlos devuelven un valor booleano
# - Es decir, True o False

'''
Método        |  Descripción
--------------|----------------------------------------------------------------
.isalpha()    |  True si todos los caracteres son alfabéticos (A-Z)
.isalnum()    |  True si los caracteres son sólo letras y/o números (A-Z) (0-9)
.isdigit()    |  True si el string es numérico - entero
.islower()    |  True si todos los caracteres son minúsculas
.isupper()    |  True si todos los caracteres son mayúsculas
.istitle()    |  True si el string tiene formato de título
.startswith() |  True si el string comienza con caracter o substring indicado
.endswith()   |  True si el string finaliza con caracter o substring indicado
.isspace()    |  True si el string tiene solo espacios vacíos
'''
# ================================================================================

#? 1) .isalpha()
print('\n1) .isalpha()')

var_1 = 'abcde'
var_2 = 'XYZabc'
var_3 = 'abc1'
var_4 = 'a bcde'
var_5 = ''
var_6 = ' '
var_7 = 'abc#'

print( var_1 , '|' , var_1.isalpha() ) # True 
print( var_2 , '|' , var_2.isalpha() ) # True
print( var_3 , '|' , var_3.isalpha() ) # False
print( var_4 , '|' , var_4.isalpha() ) # False
print( var_5 , '|' , var_5.isalpha() ) # False
print( var_6 , '|' , var_6.isalpha() ) # False
print( var_7 , '|' , var_7.isalpha() ) # False



#? 2) .isalnum()
print('\n2) .isalnum()')

var_1 = '12345'
var_2 = 'ABCdef'
var_3 = '123XYZ'
var_4 = '123 XYZ'
var_5 = 'abc$123'

print( var_1 , '|' , var_1.isalnum() ) # True 
print( var_2 , '|' , var_2.isalnum() ) # True
print( var_3 , '|' , var_3.isalnum() ) # True
print( var_4 , '|' , var_4.isalnum() ) # False
print( var_5 , '|' , var_5.isalnum() ) # False



#? 3) .isdigit()
print('\n3) .isdigit()')

var_1 = '123'
var_2 = '123.56'
var_3 = '123,56'
var_5 = '123a'
var_6 = '12 3'
var_7 = '0'
var_8 = ' 0'

print( var_1 , '|' , var_1.isdigit() ) # True
print( var_2 , '|' , var_2.isdigit() ) # False
print( var_3 , '|' , var_3.isdigit() ) # False 
print( var_4 , '|' , var_4.isdigit() ) # False 
print( var_5 , '|' , var_5.isdigit() ) # False 
print( var_6 , '|' , var_6.isdigit() ) # False 
print( var_7 , '|' , var_7.isdigit() ) # True 
print( var_8 , '|' , var_8.isdigit() ) # False 



#? 4) .islower()
print('\n4) .islower()')

var_1 = 'hola sebastián'
var_2 = 'Hola mundo'
var_3 = '  hola mundo'

print( var_1 , '|' , var_1.islower() ) # True
print( var_2 , '|' , var_2.islower() ) # False
print( var_3 , '|' , var_3.islower() ) # True



#? 5) .isupper()
print('\n5) .isupper()')

var_1 = 'hOLA'
var_2 = 'Hola Mundo'
var_3 = 'PYTHON'
var_4 = 'PYTHON  '
var_5 = 'PYTHON  a'

print( var_1 , '|' , var_1.isupper() ) # False
print( var_2 , '|' , var_2.isupper() ) # False
print( var_3 , '|' , var_3.isupper() ) # True
print( var_4 , '|' , var_4.isupper() ) # True
print( var_5 , '|' , var_5.isupper() ) # False



#? 6) .istitle()
print('\n6) .istitle()')

var_1 = 'Hola'
var_2 = 'Hola Mundo'
var_4 = 'Hola mundo'
var_5 = 'hola mundo'
var_6 = 'hola Mundo'
var_7 = 'holaMundo'
var_8 = 'HolaMundo'

print( var_1 , '|' , var_1.istitle() ) # True 
print( var_2 , '|' , var_2.istitle() ) # True 
print( var_3 , '|' , var_3.istitle() ) # False 
print( var_4 , '|' , var_4.istitle() ) # False 
print( var_5 , '|' , var_5.istitle() ) # False 
print( var_6 , '|' , var_6.istitle() ) # False 
print( var_7 , '|' , var_7.istitle() ) # False 
print( var_8 , '|' , var_8.istitle() ) # False



#? 7) .startswith()
print('\n7) .startswith()')

var_1 = 'aprendiendo python'
print( "var_1.startswith('a') =>" , var_1.startswith('a') ) # True
print( "var_1.startswith('') =>" , var_1.startswith('') ) # True
print( "var_1.startswith(' ') =>" , var_1.startswith(' ') ) # False
print( "var_1.startswith('A') =>" , var_1.startswith('A') ) # False

var_2 = ' HEllo World'
print( "var_2.startswith('H') =>" , var_2.startswith('H') ) # False
print( "var_2.startswith(' H') =>" , var_2.startswith(' H') ) # True
print( "var_2.startswith(' HE') =>" , var_2.startswith(' HE') ) # True
print( "var_2.startswith(' HELLO') =>" , var_2.startswith(' HELLO') ) # False
print( "var_2.startswith(' HEllo W') =>" , var_2.startswith(' HEllo W') ) # True
print( "var_2.startswith('') =>" , var_2.startswith('') ) # True



#? 8) .endswith()
print('\n8) .endswith()')

var_1 = 'aprendo PythON'
print( "var_1.endswith('') =>" , var_1.endswith('') ) # True
print( "var_1.endswith('N') =>" , var_1.endswith('N') ) # True
print( "var_1.endswith('ON') =>" , var_1.endswith('ON') ) # True
print( "var_1.endswith('ON ') =>" , var_1.endswith('ON ') ) # False
print( "var_1.endswith('on') =>" , var_1.endswith('on') ) # False
print( "var_1.endswith('o PythON') =>" , var_1.endswith('o PythON') ) # True


#? 9) .isspace()
print('\n9) .isspace()')

var_1 = ''
var_2 = ' '
var_3 = '\t'
var_4 = '\n'
var_5 = ' 1'
var_6 = 'XYZ'

print( var_1 , '|' , var_1.isspace() ) # False
print( var_2 , '|' , var_2.isspace() ) # True 
print( var_3 , '|' , var_3.isspace() ) # True 
print( var_4 , '|' , var_4.isspace() ) # True
print( var_5 , '|' , var_5.isspace() ) # False 
print( var_6 , '|' , var_6.isspace() ) # False 