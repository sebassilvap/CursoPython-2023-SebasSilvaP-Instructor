# =======================================================
# Gestión de Errores / Manejo de Excepciones
# Introducción

# - a lo largo de este camino hemos visto
# - que se pueden generar errores en el código
# - esto no solo pasa en Python
# - sino también en cualquier lenguaje de programación

# - Básicamente tenemos 3 tipos de errores

#*    a) Errores de Sintaxis Directos
#*    b) Errores de Sintaxis Indirectos
#*    b) Errores de Ejecución
# =======================================================


#? 1) Errores de Sintaxis Directos
print('\n1) Errores de Sintaxis Directos')
# - cuando se escribe mal el código de Python
# - el IDE los detecta automáticamente
# - antes de ejecutar el script

"""
numero_a = 1
#numero b = 2 #! SyntaxError: invalid syntax

#print(numero_a , numero_b, ,) #! SyntaxError: invalid syntax
"""



#? 2) Errores de Sintaxis Indirectos
print('\n2) Errores de Sintaxis Indirectos')
# - son aquellos que no los identifica el IDE de manera directa
# - es decir, antes de ejecutar el script
# - pero se generan en la ejecución del mismo
# - el ejemplo típico: eval() + una expresión incorrecta
# - es en si un error de ejecución, pero al ser de sintaxis
# - es especial y se lo pone en esta categoría

expresion_matematica_1 = '2 + 10 / 2'
expresion_matematica_2 = '2 + 10 /* 2'

# calcular expresión con eval y mostrar en pantalla
print( eval(expresion_matematica_1) ) # 7.0
#print( eval(expresion_matematica_2) ) #! SyntaxError: invalid syntax



#? 3) Errores de Ejecución
print('\n3) Errores de Ejecución')
# - los hemos visto a lo largo de este camino
# - hay varios
# - el IDE no los identifica a primera vista
# - ocurren al momento que intentamos ejecutar el script
# - vamos a citar los más típicos

# ---------------------------------
# 3.1) ZeroDivisionError
print('\n3.1) ZeroDivisionError')
# ---------------------------------
# - uno de los más típicos
# - no solo de python u otro lenguaje de programación
# - típico de las mismas calculadoras

def division(a,b):
    return a / b
# end def

r1 = division(4,5)
#r2 = division(4,0) #! ZeroDivisionError: division by zero


# --------------------------
# 3.2) IndexError
print('\n3.2) IndexError')
# --------------------------
# - lo hemos visto varias veces
# - cuando intentamos acceder a un índice/posición que no existe
# - en una colección de datos

cadena = 'hola'
lista = [1,2,3]

#cadena[10] #! IndexError: string index out of range
#lista[4] #! IndexError: list index out of range


# ------------------------
# 3.3) TypeError
print('\n3.3) TypeError')
# ------------------------
# - al intentar por ejemplo 
# - sumar un string y un entero

numero = 100
palabra = 'python'

#resultado = numero + palabra #! TypeError: unsupported operand type(s) for +: 'int' and 'str'


# --------------------------
# 3.4) ValueError
print('\n3.4) ValueError')
# --------------------------
# - cuando un valor erróneo es asignado a un objeto
# - a una operación / función / etc..


#*  EJ 1: intentar casting de str a int
palabra = 'hola'
#numero = int(palabra) #! ValueError: invalid literal for int() with base 10: 'hola'


#* EJ 2: raíz cuadrada de número negarivo con math

# => con el operador **
def calcular_raiz_cuadrada(numero):
    return numero ** 0.5
# end def

r1 = calcular_raiz_cuadrada(4)
r2 = calcular_raiz_cuadrada(-9)

print(r1) # 2.0
print(r2) # (1.8369701987210297e-16+3j)

# => con math.sqrt()
import math
#r2 = math.sqrt(-9) #! ValueError: math domain error


# ------------------------------
# 3.5) AttributeError
print('\n3.5) AttributeError')
# ------------------------------
# - cuando por ejemplo queremos ejecutar un método
# - que no existe en un tipo de date

var_1 = 'sebas'
var_2 = 36

var_1.upper()
#var_2.upper() #! AttributeError: 'int' object has no attribute 'upper'


# ====================================================================
#? Conclusión
# - los errores de Sintaxis son manejables
# - y corregibles al momento de escribir el código
# - los errores de ejecución
# - ZeroDivisionError / IndexError / TypeError / ValueError / etc...
# ! NO SON INDENTIFICABLES A SIMPLE VISTA POR EL IDE
# - cuando se producen, se corta la ejecución del código
# - a menos que podamos anticiparnos a ellos
# - o capturarlos
# - a esto se llama la gestión / manejo de errores
# - y se lo hace con un bloque de código especial
# *     try...except
# ====================================================================