# =======================================================
# librería / módulo math de python

# - no necesitamos instalarla con pip
#! - pip => asistente de instalación de librerías y módulos en Python
# - ya viene por defecto al momento de instalar python
# - pero debemos importarla para poder usarla
# =======================================================


#? 1) Importación del módulo
print('\n1) Importación del módulo')
# - las importaciones siempre son la 1era línea de código

import math



#? 2) Constantes Matemáticas
print('\n2) Constantes Matemáticas')
# - math.pi
# - math.e

constante_pi = math.pi
constante_e = math.e

print('constante_pi =' , constante_pi)
print('constante_e =' , constante_e)



#? 3) Representación Numérica
print('\n3) Representación Numérica')

# ------------------------------------------------
# 3.1) math.ceil() & math.floor()
print('\n3.1) math.ceil() & math.floor()')
# - math.ceil()  => devuelve el entero superior
# - math.floor() => devuelve el entero inferior
# ------------------------------------------------

#    ENTERO SUPERIOR         |      ENTERO INFERIOR
print( math.ceil(5.0001) , ' | ' , math.floor(5.0001) )
print( math.ceil(5.5) , ' | ' , math.floor(5.5) )
print( math.ceil(5.99999) , ' | ' , math.floor(5.99999) )

print('\nRecordar round()')
# => round devuelve el inmediato superior
print( round(5.0001) )
print( round(5.5) )
print( round(5.99999) )


# --------------------------------
# 3.2) math.fabs()
print('\n3.2) math.fabs()')
# - igual que abs()
# - devuelve el valor absoluto
# ! pero lo devuelve como float
# --------------------------------

print( math.fabs(-10) , '|', abs(-10) )
print( math.fabs(-55.999996) , '|', abs(-55.999996) )



#? 4) Mínimo Común Múltiplo & Máximo Común Divisor
print('\n4) Mínimo Común Múltiplo & Máximo Común Divisor')
# - math.lcm() => mínimo común múltiplo
# - math.gcd() => máximo común divisor

print( 'math.lcm(6,4) =' , math.lcm(6,4) ) # 12
print( 'math.gcd(6,4) =' , math.gcd(6,4) ) # 2
print()
print( 'math.lcm(8,3) =' , math.lcm(8,3) ) # 24
print( 'math.gcd(8,3) =' , math.gcd(8,3) ) # 1
print()
print( 'math.lcm(9,3) =' , math.lcm(9,3) ) # 24
print( 'math.gcd(9,3) =' , math.gcd(9,3) ) # 1



#? 5) Raíces y Potencia
print('\n5) Raíces y Potencia')

# -------------------------------------
# 5.1) math.sqrt()
print('\n5.1) math.sqrt()')
# - raíz cuadrada
# - sqrt = square root
# - IMPORTANTE: devuelve un flotante
# -------------------------------------
print( 'math.sqrt(25) =' , math.sqrt(25) )
print( 'math.sqrt(81) =' , math.sqrt(81) )
print( 'math.sqrt(10) =' , math.sqrt(10) )


# ---------------------------------------
# 5.2) math.cbrt()
print('\n5.2) math.cbrt()')
# - raíz cúbica
# - cbrt = cubic root
# - IMPORTANTE: devuelve un flotante
# ---------------------------------------
print( 'math.cbrt(8) =' , math.cbrt(8) )
print( 'math.cbrt(30) =' , math.cbrt(30) )


# -----------------------
# 5.3) Potencia
print('\n5.3) Potencia')
# -----------------------

# operador interno **
print( 3 ** 2 )

# math.pow()
print( math.pow(3,2) ) # devuelve flotante


# -----------------------------------------
# 5.4) Truco para raíces
print('\n5.4) Truco para raíces')
# math.sqrt(25) = 25 ** 0.5 = 25 ** (1/2)
# -----------------------------------------

# raíz cuadrada
print( math.sqrt(25) )  # 5.0
print( 25 ** 0.5 )  # 5.0
print( 25 ** (1/2) )  # 5.0
print( math.pow(25, 1/2) )  # 5.0

# raíz cúbica
print( math.cbrt(64) )  # 4
print( 64 ** (1/3) )  # 3.99999996
print( math.pow(64, 1/3) )  # 3.99999996

# raíz de cualquier valor
print( 32 ** (1/5) )  # raíz quinta de 32 = 2
print( math.pow(32, 1/5) )  # 2



#? 6) Logaritmos
print('\n6) Logaritmos')
# - math.log()   => logaritmo base e (logaritmo natural ln)
# - math.log10() => logaritmo base 10
# => devuelven valor flotante

# (pequeña explicación)
# log10 1000 => 10 ** x = 1000 => a qué número debo elevar 10 para que me de 1000
# ln 8 => e ** x = 8 => a qué número debo elevar constante e para que me de 8

num_1 = math.e ** 2
num_2 = 1000

print( math.log(num_1) ) # 2.0
print( math.log10(num_2) ) # 3.0



#? 7) Exponencial e
print('\n7) Exponencial e')
# - math.exp()
# - constante e ** valor = 2.71.. ^ x

print( math.exp(3) ) # 20.085536923187668
print( math.e ** 3 ) # 20.085536923187664
print( 2.718 ** 3 ) # 20.079290231999998



#? 8) Conversión de Ángulos
print('\n8) Conversión de Ángulos')
# - math.degrees(x)  => convierte x de radianes a grados
# - math.radians(x)  => convierte x de grados a radianes
# => devuelven valor flotante

# (pequeña explicación)
# 360 (grados) = 2 * pi (radianes)
# 180 (grados) = pi (radianes)
#  90 (grados) = (1/2) * pi (radianes)
#  60 (grados) = (1/3) * pi (radianes)
#  45 (grados) = (1/4) * pi (radianes)
#  30 (grados) = (1/6) * pi (radianes)

#* cuando se trata de una constante
#* es una buena práctica poner el nombre de la variable en mayúsculas
CONST_PI = math.pi

print( '2 * CONST_PI =', 2 * CONST_PI )  # 6.283185307179586
print( 'CONST_PI =', CONST_PI )  # 3.141592653589793
print( '(1/2) * CONST_PI =', (1/2) * CONST_PI )  # 1.5707963267948966
print( '(1/3) * CONST_PI =', (1/3) * CONST_PI )  # 1.0471975511965976
print( '(1/4) * CONST_PI =', (1/4) * CONST_PI )  # 0.7853981633974483
print( '(1/6) * CONST_PI =', (1/6) * CONST_PI )  # 0.5235987755982988

print('\nDe radianes a grados:')
print( '2 PI rad =', math.degrees(2*CONST_PI) ) # 360.0
print( 'PI rad =', math.degrees(CONST_PI) ) # 180.0
print( '(1/2) PI rad =', math.degrees(1/2*CONST_PI) ) # 90.0
print( '(1/3) PI rad =', math.degrees(1/3*CONST_PI) ) # 59.99999999
print( '(1/4) PI rad =', math.degrees(1/4*CONST_PI) ) # 45.0
print( '(1/6) PI rad =', math.degrees(1/6*CONST_PI) ) # 29.99999996

print('\nDe grados a radianes:')
print( '360 grados =' , math.radians(360) )  # 6.283185307179586
print( '180 grados =' , math.radians(180) )  # 3.141592653589793
print( '90 grados =' , math.radians(90) )  # 1.5707963267948966
print( '60 grados =' , math.radians(60) )  # 1.0471975511965976
print( '45 grados =' , math.radians(45) )  # 0.7853981633974483
print( '30 grados =' , math.radians(30) )  # 0.5235987755982988



#? 9) Funciones Trigonométricas
print('\n9) Funciones Trigonométricas')
# - los valores deben darse en RADIANES !!

'''
seno          coseno        tangente
math.sin()    math.cos()    math.tan()
math.asin()   math.acos()   math.atan() => arco funciones 
'''

# => ejemplos básicos de comprobación
# seno 30 grados = 0.5
# tangente 45 grados = 1
# arco coseno 0.5 = 60 grados

# => seno de 30 grados
print( math.sin( math.radians(30) ) ) # 0.49999994
print( math.sin( 1/6*math.pi ) ) # 0.49999994

# => tangente de 45 grados
print( math.tan( math.radians(45) ) ) # 0.9999999
print( math.tan( 1/4*math.pi ) ) # 0.9999999

# => arco coseno de 0.5
print( math.acos(0.5) , 'RADIANES' ) # 1.0471975511965979 RADIANES
print( math.acos(0.5) * (180 / math.pi) , 'GRADOS' ) # 60.00000000000001 GRADOS
print( math.degrees( math.acos(0.5) ) , 'GRADOS' ) # 60.00000000000001 GRADOS



#? 10) Truncate => Eliminando parte decimal
print('\n10) Truncate => Eliminando parte decimal')
# - math.trunc(x)
# - no redondea
# - sólo elimina todos los decimales y el punto

print( math.trunc(2.5569) ) # 2
print( math.trunc( math.pi ) ) # 3
print( math.trunc( math.e ) ) # 2
print( math.trunc( 2.9999999 ) ) # 2



#? 11) sum() & math.fsum()
print('\n11) sum() & math.fsum()')
# - al igual que sum()
# - math.fsum() => determina el sumatorio de los valores de una lista

# => Recordemos el problema que teníamos
lista_2 = [0.9999999, 1, 2, 3]
print(sum(lista_2)) # 6.999999900000001

# => math.fsum() resuelve este problema
print(math.fsum(lista_2)) # 6.9999999



#? 12) Funciones Hiperbólicas (*)
print('\n12) Funciones Hiperbólicas (*)')
# - (*) Tema de matemática avanzado
# - Utilizado más en temas de ingeniería
# - No los vamos a profundizar
# - Pero es bueno que sepan que hay como hacer esto

'''
seno hiperbólico     coseno hiperbólico     tangente hiperbólica
math.sinh()          math.cosh()            math.tanh()
math.asinh()         math.acosh()           math.atanh()    => arco funciones 
'''

# ejemplos
print( math.cosh(2.5) ) # 6.132289479663687
print( math.sinh(2.5) ) # 6.0502044810397875