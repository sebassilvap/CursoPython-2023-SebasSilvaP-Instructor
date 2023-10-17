# =====================================================
#   Expresiones Lógicas

# - Uniendo todos los elementos vistos anteriormente
# - Podemos crear expresiones lógicas
# - Debemos recordar siempre la filosofía de Python:

# ?     "El código debe ser fácil de leer y entender
# ?      para cualquier persona que lo lea,
# ?      no solo para el autor del código"

'''
   #* Operadores de Comparación:
    >   <   >=   <=   ==   !=
     
   #* Operadores Lógicos:
   not   and  or
   
   #* Keyword in
   EJ:   'p' in 'python' => True
   
   #* Condicional if
'''

# - Una muy buena práctica
# - Antes de empezar temas más complicados 
# - Es tratar de interpretar el código de Python
# - Con nuestras propias palabras

# =====================================================


#? 1) Ejemplo: Análisis de in / elemento y lista
print('\n1) Ejemplo: Análisis de in / elemento y lista')

lista_1 = [1,2,3,4,5]
lista_2 = [1,8,6,5,7]
lista_3 = []

n1 = 3


# ----------------------------------------------
# 1.1) elemento dentro de una lista
print('\n1.1) elemento dentro de una lista\n')
# ----------------------------------------------
print( n1 in lista_1 ) # True
print( n1 in lista_2 ) # False

print( n1 not in lista_1 ) # False
print( n1 not in lista_2 ) # True

# Traducción:
# "¿Se encuentra n1 dentro la lista_1?"
# "¿Se encuentra n1 dentro la lista_2?"

# "¿Es verdad que n1 NO ESTÁ en la lista_1?"
# "¿Es verdad que n1 NO ESTÁ en la lista_2?"


# ----------------------------------------------------
# 1.2) Otra alternativa: not + paréntesis
print('\n1.2) Otra alternativa: not + paréntesis\n')
# ----------------------------------------------------
# - otra manera de usar el not
# - pero más lógica y sentido tiene el "not in"

print( not(n1 in lista_1) ) # False
print( not(n1 in lista_2) ) # True

# Traducción:
# "¿No es CIERTO que n1 se encuentra en lista_1? => Falso porque si es CIERTO"
# "¿No es CIERTO que n1 se encuentra en lista_2? => Verdadero porque no es CIERTO"


# ---------------------------------------------------------
# 1.3) not al inicio sin paréntesis => puede confundir
print('\n1.3) not al inicio sin paréntesis => puede confundir\n')
# ---------------------------------------------------------
# - también podemos prescindir de los paréntesis
# - pero la lectura se dificulta
# - y esto puede tender a errores luego
# ! No recomendable

print( not(n1 in lista_1) ) # False
print( not(n1 in lista_2) ) # True
print('----------')
print( not n1 in lista_1 ) # False
print( not n1 in lista_2 ) # True

# Traducción:
# "¿No es CIERTO que n1 se encuentra en lista_1? => Falso porque si es CIERTO"
# "¿No es CIERTO que n1 se encuentra en lista_2? => Verdadero porque no es CIERTO"

# "¿No está n1 dentro de lista_1?" => Falso porque si está
# "¿No está n1 dentro de lista_2?" => Verdadero porque no está


# -------------------------------------------------
# 1.4) Manera redundante, no recomendable
print('\n1.4) Manera redundante, no recomendable\n')
# -------------------------------------------------
# - no olvidar envolver la expresión en ()
# - antes de hacer la comparación
# - caso contrario nos da una respuesta equivocada
# ! No recomendable

print( (n1 in lista_1) == True ) # True
print( (n1 in lista_2) == True ) # False

print( (n1 in lista_1) == False ) # False
print( (n1 in lista_2) == False ) # True

# Traducción:
# "¿Se encuentra n1 dentro la lista_1?"
# "¿Se encuentra n1 dentro la lista_2?"

# "¿Es verdad que n1 NO ESTÁ en la lista_1?"
# "¿Es verdad que n1 NO ESTÁ en la lista_2?"


# ! ERROR
print('\nERROR !!!\n')
print( (n1 in lista_2) == False ) # True
print( n1 in lista_2 == False ) # False


# * ¿Qué pasa aquí?

'''
n1 in lista_2 == False

=> se opera como una COMPARACIÓN EN CADENA
es decir:

n1 in lista_2 == False  ---> (n1 in lista_2) and (lista_2 == False)
n1 in lista_2 == False  --->  False and False
n1 in lista_2 == False  --->  False
'''


# -----------------------------------------------------------------------
# 1.5) Análizar de manera equivocada que una lista está vacía
print('\n1.5) Análizar de manera equivocada que una lista está vacía\n')
# -----------------------------------------------------------------------
# - cuando comparamos una lista directamente a False o True
# - lo que hacemos aquí es comparar el valor de un elemento y otro
# - de una manera literal
# - daría False por el simple hecho que una lsita no es igual a un booleano
# ! Uso ERRÓNEO de la comparación

print( lista_1 == False ) # False
print( lista_3 == False ) # False


# -----------------------------------------------------
# 1.6) Correción del uso de la comparación
print('\n1.6) Correción del uso de la comparación\n')
# -----------------------------------------------------
# - si lo que deseamos es evaluar si una lista está vacía
# - si está vacía esto es False
# - si tiene algo esto es True
# - podemos hacer un casting primero a bool()
# - una lista vacía tiene un VALOR BOOLEANO de False
# * RECORDAR: valor booleano de las variables !

print( bool(lista_1) == False ) # False
print( bool(lista_3) == False ) # True

# Traducción:
# "¿El valor booleano de lista_1 es False?"
# "¿El valor booleano de lista_3 es False?"



#? 2) Ejemplo: Analizar la temperatura / clima
print('\n2) Ejemplo: Analizar la temperatura / clima')

temperatura = 15
clima = ''

if not (temperatura < 10 or temperatura > 30):
    clima = 'Buen Clima'
else:
    clima = 'Mal Clima'
# end if

print(clima)

# => Traducción:

'''
Si la temperatura NO es menor a 10
o mayor a 30 grados,
tenemos un buen clima,
caso contrario, tenemos un mal clima.
'''



#? 3) Ejemplo: Control Básico de Asistencia
print('\n3) Ejemplo: Control Básico de Asistencia')

estudiante_1 = 'Fernando'
estudiante_2 = 'Francisco'
estudiante_3 = 'Sebastián'

clase_geometria = ['Andrés', 'Sebastián', 'Carlos', 'Ximena']
clase_ingles = ['Fernando', 'Tania', 'Eduardo', 'Carla', 'Sebastián']

estudiante = estudiante_1

if not (estudiante in clase_geometria or estudiante in clase_ingles):
    print('El estudiante no asiste a ninguna clase')
else:
    print('El estudiante asiste al menos a 1 clase!')
# end def


# => Traducción:

'''
Si el estudiante no está en la lista de la clase de geometría,
o en la lista de la clase de inglés,
entonces el estudiante no asiste a ninguna clase.
Caso contrario, el estudiante está asistiendo al menos
a 1 de las 2 clases.
'''



#? 4) Ejemplo: Análisis de notas sobre 20
print('\n4) Ejemplo: Análisis de notas sobre 20')
# - Básicamente si el promedio es de 15 para arriba, el estudiante aprueba
# - si es de 14 para abajo, el estudiante reprueba

nota_1 = 15
nota_2 = 14
nota_3 = 14

if not ( (nota_1 + nota_2 + nota_3)/3 >= 15 ):
    print('El estudiante ha reprobado')
else:
    print('El estudiante ha pasado!')
# end if

# => Traducción:

'''
Si el promedio de las 3 notas del estudiante
NO es mayor o igual a 15, entonces el estudiante reprueba.
Caso contrario, el estudiante aprueba la materia!
'''


#? 5) Comprobar un elemento dentro de lista
print('\n5) Comprobar un elemento dentro de lista')
# - veremos aquí maneras correctas e incorrectas
# - de formular una expresión lógica

var = 2

l1 = [1,2,3]
l2 = [10,11,12]


# ----------------------------------------------
# 5.1) Ejemplo # 1: Manera Correcta
print('\n5.1) Ejemplo # 1: Manera Correcta\n')
# ----------------------------------------------
# * MANERA CORRECTA !

if var in l1 and var in l2:
    print('En AMBAS listas')
else:
    print('No está en ambas pero puede que esté en 1 o ninguna!')
# end if

# Traducción
# "Si var se encuentra en l1 Y en l2..."


# ----------------------------------------------
# 5.2) Ejemplo # 2: Manera Correcta
print('\n5.2) Ejemplo # 2: Manera Correcta\n')
# ----------------------------------------------
# * MANERA CORRECTA !

if not(var in l1 and var in l2):
    print('No está en ambas pero puede que esté en 1 o ninguna!')
else:
    print('En AMBAS listas')
# end if

# Traducción
# "Si NO ES CIERTO que var se encuentra en l1 y l2..."


# ----------------------------------------------
# 5.3) Ejemplo # 3: Manera Incorrecta
print('\n5.3) Ejemplo # 3: Manera Incorrecta\n')
# ----------------------------------------------
# ! MANERA INCORRECTA !

if not(var in l1) and not(var in l2):
    print('No está en ambas pero puede que esté en 1 o ninguna!')
else:
    print('En AMBAS listas')
# end if

# ¿QUÉ OCURRE AQUÍ?
# var in l1 = True
# not(var in l1) = False

# var in l2 = False
# not(var in l2) = True

# False and True = False

# => Ocurre que la lógica incorrecta se aplica!


# ----------------------------------------------
# 5.4) Ejemplo # 4: Manera Incorrecta
print('\n5.4) Ejemplo # 4: Manera Incorrecta\n')
# ----------------------------------------------
# ! MANERA INCORRECTA !

if var not in l1 and var not in l2:
    print('No está en ambas pero puede que esté en 1 o ninguna!')
else:
    print('En AMBAS listas')
# end if