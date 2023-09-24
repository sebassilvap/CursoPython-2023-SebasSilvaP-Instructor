# ==========================================================
# Condicional - if
# Sentencia - if
# (if statement)

# - uno de los elementos más importantes de un programa
# - yo lo he visto en el 99% de programas
# - podemos dividir el flujo / el camino de un programa
# - se traduce al español como SI
# - le damos al programa opciones
# - al enunciarlo el bloque de código va indentado
#! - se ejecuta una instrucción cuando la condición es True
# ==========================================================

#? 1) Ejemplo básico => Análisis de una nota
print('\n1) Ejemplo básico => Análisis de una nota\n')
# - 20 es sobresaliente
# - 15 a 19 => el estudiante ha aprobado
# - 12 a 14 => el estudiante pierde el cupo
# - menor a 12 => estudiante pierde el año

nota = 18

if nota == 20:
    print('Sobresaliente!')
elif nota >= 15 and nota <= 19:
    print('El estudiante ha APROBADO!')
elif nota >= 12 and nota <= 14:
    print('El estudiante PIERDE el CUPO!')
else:
    print('El estudiante PIERDE el AÑO!')
# end if


#? 2) Explicación de los elementos del bloque if
print('\n2) Explicación de los elementos del bloque if\n')

print('''
if (condicion_1): #! => si condicion_1 se cumple:
    - entramos en modo condición
    - esto se ejecuta si condicion_1 == True
    - se crea un nuevo bloque de código
    - este nuevo bloque va indentado
    - con la indentación python sabe que estamos en un nuevo bloque
    
elif (condicion_2): #! => o en caso de que condicion_2 se cumpla:
    - pasamos a una nueva condición
    - en caso de que condicion_1 no se cumpla
    - condicion_1 == False
    - se ejecuta este bloque si condicion_2 == True
    
elif (condicion_3): #! => o en caso de que condicion_3 se cumpla:
    - si condicion_1 y condicion_2 no se cumplen
    - condicion_1 == False and condicion_2 == False
    - se ejecuta este nuevo bloque si condicion_3 es False
    
else: #! => si nada de arriba se cumple, para cualquier otro caso:
    - este bloque se ejecuta si ni if o cualquier elif se cumple
    - caso por default
    - caso por defecto
''')


#? 3) El if / elif se ejecuta cuando la condición es True
print('\n3) El if / elif se ejecuta cuando la condición es True\n')

# => ejemplo 1
print('\n=> ejemplo 1\n')
if(True):
    print('Bloque 1: hola - if')
elif(True):
    print('Bloque 2: hola - elif')
elif(True):
    print('Bloque 3: hola - elif')
else:
    print('Bloque 4: hola - else')

# => ejemplo 2
print('\n=> ejemplo 2\n')
if(False):
    print('Bloque 1: hola - if')
elif(False):
    print('Bloque 2: hola - elif')
elif(False):
    print('Bloque 3: hola - elif')
else:
    print('Bloque 4: hola - else')

# => ejemplo 3
print('\n=> ejemplo 3\n')
if(False):
    print('Bloque 1: hola - if')
elif(True):
    print('Bloque 2: hola - elif')
elif(False):
    print('Bloque 3: hola - elif')
else:
    print('Bloque 4: hola - else')
    

#? 4) Orden de ejecución del condicional if
print('\n4) Orden de ejecución del condicional if\n')

# - la ejecución del código como en un script de python
# - es de arriba hacia abajo
# - también tiene sentido trabajar con un orden en la comparación

numero = 5

if numero < 1:
    print('numero menor a 1')
elif numero < 2:
    print('numero menor a 2')
elif numero < 3:
    print('numero menor a 3')
elif numero < 4:
    print('numero menor a 4')
elif numero < 5:
    print('numero menor a 5')
elif numero < 6:
    print('numero menor a 6')

# => esto no tendría sentido si no aplico un orden en las comparaciones
#! mal ejemplo de programación del if

numero = 1

if numero < 4:
    print('numero menor a 4')
elif numero < 1:
    print('numero menor a 1')
elif numero < 2:
    print('numero menor a 2')
# número menor a 4

if numero < 1:
    print('numero menor a 4')
elif numero < 4:
    print('numero menor a 1')
elif numero < 3:
    print('numero menor a 2')
# número menor a 1

'''
- en los 2 códigos anteriores el primer if se cumple
- de hecho el if no tiene sentido 
- el sentido viene dado por el programador
- recordar al final que el computador solo interpreta las intenciones del programador
- lo anteriormente expuesto no es un error pero muy mala práctica y uso del if
'''


#? 5) Inicio y Fin de un Condicional if
print('\n5) Inicio y Fin de un Condicional if\n')

# => varias posibilidades de un bloque if
##  (A) inicia con if y termina con else
##  (B) inicia con if y termina con elif
##  (C) inicia con if y termina con el inicio de un nuevo if

print('\n(A) inicia con if y termina con else\n')

# ejemplo 5.1)
edad = 14

if edad >= 18:
    print('mayor de edad')
else: # para todo lo demás
    print('menor de edad')

print('final del if')

# ejemplo 5.2)
temp = 18

if temp < 0:
    print('frío extremo!')
elif temp >= 0 and temp < 15:
    print('está haciendo frío')
elif temp >= 15 and temp < 25:
    print('está haciendo un buen clima')
else:
    print('muy caliente!')
    
# => una buena práctica en una condición es abarcar todas las posibilidades que puedan darse!


print('\n(B) inicia con if y termina con elif')
print('(C) inicia con if y termina con el inicio de un nuevo if\n')

numero = 100
# numero = 1000

if numero > 50:
    print('numero grande')
elif numero <= 50:
    print('numero pequeño')
    
if len(str(numero)) == 1:
    print('número tiene 1 dígito')
elif len(str(numero)) == 2:
    print('numero tiene 2 dígitos')
elif len(str(numero)) == 3:
    print('numero tiene 3 dígitos')

# => con el else nos aseguramos de abarcar todas las posibilidades que pueden darse!