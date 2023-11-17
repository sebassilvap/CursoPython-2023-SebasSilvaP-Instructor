# =================================================================================
# Módulos en Python

# - Módulo => un archivo con código de Python
# - puede contener variables, funciones, clases, definiciones de código Python
# - permite una estructura de programación modular
# - programación modular => permite separar un programa en partes
# - en esta primera parte enunciamos todas las maneras posibles de usar un módulo

# - básicamente tenemos las siguientes estructuras de importación

# *     import abcd
# *     import abcd as a
# *     from x import y
# *     from x import a, b, c
# *     from x import yyyy as y
# *     from x import aaaa as a, bbbb as b, cccc as c
# *     from x import *

#! NOTA:
# - en una estructura modular
# - el archivo de python principal que carga los módulos
# - recibe el nombre de "main.py"
# =================================================================================


#? 1) import de módulos / librerías internas
print('\n\n1) import de módulos / librerías internas')
# - nosotros ya habíamos visto esta estructura
# - al momento que aprendimos estas librerías internas
# - por ej: math, time, datetime, etc...
# - después aprendimos el alias => con el keyword: as 

import math

print( math.pi ) # 3.141592653589793
print( math.e ) # 2.718281828459045
print( math.log10(1000) ) # 3.0

import datetime as dt

fecha_actual = dt.datetime.now()
print(fecha_actual) # 2023-11-12 00:01:47.613850




#? 2) import de módulos creados por el usuario
print('\n\n2) import de módulos creados por el usuario')
# - básicamente la misma estructura que en los módulos / librerías internas
# - pero con archivos de python creados dentro de la misma carpeta
# - esto funciona siempre y cuando estemos en la misma carpeta
# - caso contrario debemos especificar el path => lo vemos luego

import saludos

saludos.saludo_espanol() # Hola, ¿cómo has estado?
saludos.saludo_ingles() # Hi! How are you?
saludos.saludo_aleman() # Hallo! Wie geht es dir?

print( saludos.constante ) # HOLA MUNDO




#? 3) módulos del usuario + Alias
print('\n\n3) módulos del usuario + Alias')
# - igual que con los módulos / librerías internas
# - igualmente la siguiente estructura funciona
# - siempre y cuando el módulo definido esté en la misma carpeta

import despedidas as d

d.despedida_espanol() # Adiós. Que tenga un buen día.
d.despedida_ingles() # Bye! Have a nice day!
d.despedida_aleman() # Tschuss, einen schönen Tag noch!

print( d.constante ) # ADIÓS MUNDO




#? 4) import selectivo único => from x import y
print('\n\n4) import selectivo único => from x import y')
# - from   => especifica el módulo
# - import => especifica los elementos del módulo que deseamos importar

from aritmetica import CONSTANTE_PI

print( CONSTANTE_PI ) # 3.1416
#print( GRAVEDAD ) #! NameError: name 'GRAVEDAD' is not defined




#? 5) import selectivo múltiple => from x import a, b, c, ...
print('\n\n5) import selectivo múltiple => from x import a, b, c, ...')
# - podemos seleccionar varios elementos específicos a importar
# - con from + import y separando los elementos con una coma

from aritmetica import CONSTANTE_PI, GRAVEDAD, producto
print( CONSTANTE_PI ) # 3.1416
print( GRAVEDAD ) # 9.8
producto(2,5) # Producto de 2 * 5 = 10
#aritmetica.CONSTANTE_PI #! NameError: name 'aritmetica' is not defined




#? 6) import selectivo múltiple con alias
print('\n\n6) import selectivo múltiple con alias')

from aritmetica import suma as s, resta as r, exponente
s(50,15) # Suma de 50 + 15 = 65
r(50,25) # Resta de 50 - 25 = 25
#suma(10,18) #! NameError: name 'suma' is not defined. Did you mean: 'sum'?
exponente(5,3) # Exponente de 5 ^ 3 = 125




#? 7) import universal * => NO RECOMENDADO en módulos extensos con varios elementos
print('\n\n7) import universal * => NO RECOMENDADO en módulos extensos con varios elementos')
# - con from + asterisco podemos importar todo en el módulo
# - no es recomendado en módulos extensos con varias definiciones
# - puede causar conflictos de nombres => lo veremos luego

from aritmetica import *
#aritmetica.CONSTANTE_PI #! NameError: name 'aritmetica' is not defined

suma(5,7) # Suma de 5 + 7 = 12
resta(8,3) # Resta de 8 - 3 = 5

promedio_3_numeros(10,15,18)
# Valor 1 = 10
# Valor 2 = 15
# Valor 3 = 18
# PROMEDIO = 14.33


# =================================================================
#! NOTA IMPORTANTE
# - en este script, por motivos de aprendizaje
# - se coloca los import en diferentes posiciones
# - en la realidad, los import van en la primera línea del script
# =================================================================
