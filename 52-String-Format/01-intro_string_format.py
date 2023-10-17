# =============================================================
# String Format => str.format()

# - es un método de los string / cadenas de texto
# - le brinda al usuario un mejor control del texto a mostrar
# ! manera de trabajar que haremos de ahora en adelante

# https://www.w3schools.com/python/python_string_formatting.asp
# =============================================================


#? 1) Maneras de usar el print + nueva manera con .format()
print('\n1) Maneras de usar el print + nueva manera con .format()')

nombre = 'Gabriel'
edad = 18

# => print con cocatenación convirtiendo todo a string
print('Hola soy ' + nombre + ' y tengo ' + str(edad) + ' años!')

# => print con parámetros (no importa el tipo de dato)
print('Hola soy', nombre, 'y tengo', edad, 'años!')

# => usando string format
print( 'Hola soy {} y tengo {} años!'.format(nombre, edad) )


# ---------------------------------------------------------------------
# string.format() => por default
# - se expresa un string colocando llaves {}
# - en los lugares donde reemplazaremos valores directos o variables
# - el orden como son reemplazadas viene dado por el orden
# - en el cual se colocan los argumentos
# - los argumentos van dentro del método .format(arg1, arg2,....)
# * los argumentos pueden ser de cualquier tipo
# ---------------------------------------------------------------------



#? 2) Formando una variable string con format
print('\n2) Formando una variable string con format')
# - obviamente no solo podemos usar .format en un print
# - podemos crear una variable string
# - de una manera más eficiente


# --------------------------------------------------------------------------
# 2.1) El orden por default es según el orden de los argumentos
print('\n2.1) El orden por default es según el orden de los argumentos\n')
# --------------------------------------------------------------------------

n1 = 'Dani'
n2 = 'Andy'
n3 = 'Xime'

texto1 = '{} es chévere. Pero {} y {} son más chéveres!'.format(n1, n2, n3)
texto2 = '{} es chévere. Pero {} y {} son más chéveres!'.format(n2, n3, n1)
texto3 = '{} es chévere. Pero {} y {} son más chéveres!'.format(n3, n1, n2)

print( texto1, type(texto1) )
print( texto2, type(texto2) )
print( texto3, type(texto3) )


# ------------------------------------------------------
# 2.2) Podemos pasar todo tipo de variables
print('\n2.2) Podemos pasar todo tipo de variables\n')
# ------------------------------------------------------

auto = 'Vitara'
km = 200000
en_venta = True

texto = 'El auto {} tiene {} KM. ¿Está en venta? => {}'.format(auto, km, en_venta)

print(texto, type(texto))


# -----------------------------------------------
# 2.3) Podemos pasar valores directos
print('\n2.3) Podemos pasar valores directos\n')
# -----------------------------------------------

texto_1 = 'El {} cuesta {} euros...'.format('computador', 850)
texto_2 = 'El {} cuesta {} euros...'.format('PS5', 450)

print(texto_1, type(texto_1))
print(texto_2, type(texto_2))



#? 3) Podemos pasar una expresión, ejemplo un operador ternario
print('\n3) Podemos pasar una expresión, ejemplo un operador ternario')

nota1 = 13
nota2 = 16

print( 'Su nota es {}! Usted {} la materia'.format(nota1, 'HA PASADO' if nota1 >= 14 else 'NO HA PASADO') )
print( 'Su nota es {}! Usted {} la materia'.format(nota2, 'HA PASADO' if nota2 >= 14 else 'NO HA PASADO') )
print( 'El promedio de las notas es {}'.format( (nota1 + nota2)/2 ) )

# => suponiendo existe una fórmula para el cálculo de la nota
def promedio_ponderado(a,b):
    return 0.3 * a + 0.7 * b
# end def

print( 'El promedio ponderado es = {}'.format( promedio_ponderado(nota1, nota2) ) )



#? 4) string.format() + argumentos posicionales
print('\n4) string.format() + argumentos posicionales')
# - los argumentos de format => son una tupla
# - su primer argumento tiene el índice 0
# - EJ: 3 argumentos => 0,1,2
# - el orden del indexing va en el orden que se ponen los argumentos
# - si uso 1 debo LLENAR todos, pero no es necesario USAR todos

n1 = 'Dani'
n2 = 'Andy'
n3 = 'Xime'


# por default => en el orden que pongo los argumentos
print( '{} es chévere. Pero {} y {} son más chéveres!'.format(n1, n2, n3) )

# usando posiciones de argumentos en las {}
print( '{0} es chévere. Pero {1} y {2} son más chéveres!'.format(n1, n2, n3) )

# puedo poner el orden que quiera, pero una vez que los uso debo llenar todos los {}
print( '{2} es chévere. Pero {0} y {1} son más chéveres!'.format(n1, n2, n3) )

# si uso 1 debo LLENAR todos, pero no es necesario USAR todos
print( '{1} es chévere. Pero {2} y {2} son más chéveres!'.format(n1, n2, n3) )

#print( '{1} es chévere. Pero {} y {} son más chéveres!'.format(n1, n2, n3) )
#! ValueError: cannot switch from manual field specification to automatic field numbering

#print( '{1} es chévere. Pero {2} y {3} son más chéveres!'.format(n1, n2, n3) )
#! IndexError: Replacement index 3 out of range for positional args tuple



#? 5) string.format() + argumentos con keyword
print('\n5) string.format() + argumentos con keyword')
# - se los coloca directamente en el format
# - nombre keyword + valor
# - si se los define así, es obligatorio colocarlos en los {}

n1 = 'Nancy'
n2 = 'Telmo'
n3 = 'Sonia'

# => por default
print('{} es de Quito.\n{} es de Loja y {} es de Cuenca\n'.format(n1, n2, n3))


# => usando argumentos con keyword
print( '{nombre2} es de Quito.\n{nombre1} es de Loja y {nombre3} es de Cuenca\n'.format(
    nombre1 = 'Sebas',
    nombre2 = 'Ana',
    nombre3 = 'Beto') 
    )


# => una vez definidos, es obligatorio colocarlos en todos los {}

# ! IndexError: Replacement index 0 out of range for positional args tuple
'''
print( '{} es de Quito.\n{} es de Loja y {} es de Cuenca\n'.format(
    nombre1 = 'Sebas',
    nombre2 = 'Ana',
    nombre3 = 'Beto') 
    )
'''

# => no es necesario USAR todos pero si REEMPLAZAR todos los {}

# * OK => esto no es error!
print( '{nombre1} es de Quito.\n{nombre2} es de Loja y {nombre1} es de Cuenca\n'.format(
    nombre1 = 'Sebas',
    nombre2 = 'Ana',
    nombre3 = 'Beto') 
    )

# ! IndexError: Replacement index 0 out of range for positional args tuple
'''
print( '{nombre3} es de Quito.\n{nombre1} es de Loja y {} es de Cuenca\n'.format(
    nombre1 = 'Sebas',
    nombre2 = 'Ana',
    nombre3 = 'Beto') 
    )
'''



#? 6) Lo que hacíamos VS. lo que haremos
print('\n6) Lo que hacíamos VS. lo que haremos')

notas = [15, 17, 13, 20]

# ---------------------------------
# 6.1) Lo que hacíamos
print('\n6.1) Lo que hacíamos\n')
# ---------------------------------

promedio = 0

print('Notas del Estudiante :', notas)

for i, nota in enumerate(notas):
    print( 'Nota', i+1, ':', nota )
    promedio += nota
# end for

print('El promedio es =', promedio / 4)


# ----------------------------------
# 6.2) Lo que haremos!
print('\n6.2) Lo que haremos!\n')
# ----------------------------------

promedio = 0

print( 'Las notas del estudiante son: {}'.format(notas) )

for i, nota in enumerate(notas):
    print( 'Nota {}: {}'.format(i+1, nota) )
    promedio += nota
# end for
print( 'El promedio es = {}'.format(promedio/4) )