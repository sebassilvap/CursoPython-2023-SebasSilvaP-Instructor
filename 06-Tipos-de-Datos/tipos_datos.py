# ===========================================================================================================
# Tipos de Datos / Tipado de Datos / Data Types

#! IMPORTANTE
# - de manera incorrecta muchos cursos / videos / tutoriales
# - dicen al estudiante que Python tiene solo 4 tipos de datos

'''
Tipo de Dato     |  Denominación  |  Ej:
---------------------------------------------------------
Entero           |  int           |  -20, 0, 5
Punto Flotante   |  float         |  2.5, 0.669, -89.52
Cadena de Texto  |  str           |  'Hola', "Python"
Booleano         |  bool          |  True, False
'''

#! Estos son los tipos BÁSICOS

# Aunque es un poco avanzado nombrar todos los tipos de datos, es importante conocerlos
# saber que existen y son los siguientes:

# Por DEFAULT Python tiene los siguientes tipos de datos que vienen internamente al momento de instalar

'''
https://www.w3schools.com/python/python_datatypes.asp

----------------------------------------------------
Text Type:	     |    str
Numeric Types:   |    int, float, complex
Sequence Types:  |    list, tuple, range
Mapping Type:	 |    dict
Set Types:	     |    set, frozenset
Boolean Type:	 |    bool
Binary Types:	 |    bytes, bytearray, memoryview
None Type:	     |    NoneType
----------------------------------------------------
'''
# => Como nuestro estudio de Python es progresivo
# - no vamos a ver todos y cada uno en este momento
# - vamos a ver los básicos
# - pero siempre tener en cuenta esta INFO

# ===========================================================================================================

#? 1) type()
# - para averiguar el tipo de dato
# - función interna de python / built-in function
# - función interna como por ejemplo: print()
# - nos va a salir una palabrita "class" => no prestar atención por el momento
# - hacer de cuenta que nos dice el tipo / ¿qué tipo de dato es?
#! RECORDAR: tema funciones & clases lo veremos luego
print()
print('-------- 1) type() --------')

nombre = 'Sebas'
print(nombre)
print(type(nombre))

# como aprendimos la anterior clase, podemos imprimir esto de una manera más elegante
#        1          2
print(nombre, type(nombre))


#? 2) string - str
# - string / cadena de texto / serie, cadena de caracteres
# - se definen con:
#   #  A) Con comilla simple => ''
#   #  B) Con comilla doble   => ""
#   #  C) Con 6 comillas dobles o simples => para textos largos (lo usamos para comentarios multilínea)

# - puede ser 1 o más caracteres
# - (en otros lenguajes cuando solo es uno se tiene el tipo char)
print()
print('-------- 2) string - str --------')

string_1 = 'hola mundo'
string_2 = '   hola mundo   '
string_3 = 'A'
string_4 = '12345' # string numérico
string_5 = ' '
string_6 = ""
string_7 = ''
string_8 = 'Texto con "comillas dobles" @$#*'
string_9 = "Texto con 'comillas simples' @$#*"
string_10 = '''hola
este es un string muy largo
compuesto por
6 comillas SIMPLES
y varias líneas de texto
'''
string_11 = """hola de nuevo
este es un string muy largo
compuesto por
6 comillas DOBLES
y varias líneas de texto
"""

# impresión en la consola:

print( string_1,  type(string_1) )
print( string_2,  type(string_2) )
print( string_3,  type(string_3) )
print( string_4,  type(string_4) )
print( string_5,  type(string_5) )
print( string_6,  type(string_6) )
print( string_7,  type(string_7) )
print( string_8,  type(string_8) )
print( string_9,  type(string_9) )
print( string_10,  type(string_10) )
print( string_11,  type(string_11) )


#? 3) int
# - int viene del inglés INTEGER / número entero (sin decimales)
# - números positivos
# - números negativos
# - números CERO
# - SIN DECIMALES
print()
print('-------- 3) int --------')

entero_1 = 20
entero_2 = -2
entero_3 = +2 # no es necesario
entero_4 = 0

print( entero_1 , type(entero_1) )
print( entero_2 , type(entero_2) )
print( entero_3 , type(entero_3) )
print( entero_4 , type(entero_4) )


#? 4) float
# - float => punto flotante / número decimal
# - números decimales positivos
# - números decimales negativos
# - CERO decimal => 0.0
print()
print('-------- 4) float --------')

decimal_1 = 10.5
decimal_2 = 5.888888888888888888888
decimal_3 = -100000.9999
decimal_4 = 0.0000000001 # python lo imprime con notación científica => pero sigue siendo float
decimal_5 = 0.0
decimal_6 = 0.0000000
decimal_7 = -0.0
decimal_8 = -0.00000 # python reduce decimales redundantes

print( decimal_1 , type(decimal_1) )
print( decimal_2 , type(decimal_2) )
print( decimal_3 , type(decimal_3) )
print( decimal_4 , type(decimal_4) )
print( decimal_5 , type(decimal_5) )
print( decimal_6 , type(decimal_6) )
print( decimal_7 , type(decimal_7) )
print( decimal_8 , type(decimal_8) )


#? 5) bool
# - bool => del inglés BOOLEAN
# - valor booleano => Verdadero o Falso
# - Los valores en inglés con la primera letra en mayúscula
##  => True
##  => False
print()
print('-------- 5) bool --------')

boolean_verdadero = True
boolean_falso = False

print( boolean_verdadero, type(boolean_verdadero) )
print( boolean_falso, type(boolean_falso) )

#? 6) None
# - None => nada
# - es muy útil para SIMULAR la creación de una variable "sin asignación"
# - porque a la final le asignamos el valor None
# - para declarar / crear una variable y ponerle un valor luego
# - cambiar el valor a la variable => REASIGNAR VALOR DE VARIABLE
#!  REASIGNAR VALOR DE VARIABLE => veremos a continuación
print()
print('-------- 6) None --------')

variable = None
print( variable, type(variable) )
variable = 'texto'
print( variable, type(variable) )
variable = 123
print( variable, type(variable) )
variable = -55.88
print( variable, type(variable) )
variable = True
print( variable, type(variable) )






