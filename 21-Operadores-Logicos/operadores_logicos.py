# =================================================================
# Operadores Booleanos de Lógica

# - Existen algunos
# - Se van a analizar los 3 más básicos

'''
Operador |  Ejemplo  |  Descripción
----------------------------------------------------------------
not      |  X and Y  |  True si todos son True
and      |  X or Y   |  Basta que 1 sea True, resultado es True
or       |  not X    |  Niega al booleano
'''
# =================================================================


#? 1) Operador not
print('\n1) Operador not')
# - realiza una negación lógica
# - niega / dice que no

verdadero = True
falso = False

print('verdadero =', verdadero , '|', not verdadero)
print('falso =', falso , '|', not falso)

pregunta = 10 < 5
print(pregunta)
print(not pregunta)

print()

print(True == True)
print(False == False)
print(True == False)
print(False == True)
print(True == (not False) )

#! negación con números ?
print('\nnegación con números ?')
print(5) # 5
print(not 5) # False

# -----------------------------------------------------
# => RECORDAR el valor booleano de las variables
# 0 => False
# cualquier otro número positivo o negativo => True
# -----------------------------------------------------

print(0) # False
print(not 0) # True

print(-8.5) # -8.5
print(not -8.5) # False

#! negación de un string ?
print('\nnegación de un string ?')
cadena_1 = 'sebas'
cadena_2 = " "
cadena_3 = ''
print(cadena_1, cadena_2, cadena_3)
print(not cadena_1, not cadena_2, not cadena_3) 

# ----------------------------------------------------
# => RECORDAR el valor booleano de las variables
# string vacío => False
# cualquier otro string así sea un espacio => True
# ----------------------------------------------------



#? 2) Operador and
print('\n2) Operador and')
#  - operador de conjunción
#  - viene de la palabra conjunto => unido, contiguo, cercano
#  - agrupa valores booleanos UNIENDO
#  ! unión lógica (Y)
#  - basta que uno sea False => el resultado es False

print('\nTabla lógica de and (Y)\n')

print( 'True and True =' , True and True ) # True
print( 'True and False =' , True and False ) # False
print( 'False and True =' , False and True ) # False
print( 'False and False =' , False and False ) # False

print('\nEjemplo práctico => analizar número en rango\n')

temp_1 = 25
temp_2 = 10
temp_3 = 40
# entre 20 y 30 => buen clima

print( 'temperatura_1, ¿buen clima? =', temp_1 >= 20 and temp_1 <= 30  )
print( 'temperatura_2, ¿buen clima? =', temp_2 >= 20 and temp_2 <= 30  )
print( 'temperatura_3, ¿buen clima? =', temp_3 >= 20 and temp_3 <= 30  )

print('\nEjemplo práctico => comprobar una cadena de texto\n')

nombre_user_1 = 'Sebas'
nombre_user_2 = 'dan'

# comprobar:
# - al menos 5 caracteres
# - que empiece con mayúscula
# - que sean sólo letras

# comprobación 1
print(nombre_user_1.istitle(),
      len(nombre_user_1) >= 5,
      nombre_user_1.isalpha(),
      '=>',
      nombre_user_1.istitle() and len(nombre_user_1) >= 5 and nombre_user_1.isalpha() )

# comprobación 2
print(nombre_user_2.istitle(),
      len(nombre_user_2) >= 5,
      nombre_user_2.isalpha(),
      '=>',
      nombre_user_2.istitle() and len(nombre_user_2) >= 5 and nombre_user_2.isalpha() )



#? 3) Operador and
print('\n3) Operador and')
#  - operador de disyunción
#  - viene de la palabra disyunto => separado, apartado, distante
#  - agrupa valores booleanos SEPARANDO
#  ! separación lógica (O) 
#  - basta que uno sea True => el resultado es True

print('\nTabla lógica de or (O)\n')

print( 'True or True =' , True or True ) # True
print( 'True or False =' , True or False ) # True
print( 'False or True =' , False or True ) # True
print( 'False or False =' , False or False ) # False

print('\nEjemplo práctico => analizar número en rango\n')
# una medida debe estar entre 12 y 15
# si no está, entonces está fuera del rango

medida_1 = 10
medida_2 = 13
medida_3 = 15
medida_4 = 50

print('¿Medidas fuera del Rango?')
print( medida_1, medida_1 < 12 or medida_1 > 15 ) # True
print( medida_2, medida_2 < 12 or medida_2 > 15 ) # False
print( medida_3, medida_3 < 12 or medida_3 > 15 ) # False
print( medida_4, medida_4 < 12 or medida_4 > 15 ) # True


print('\nEjemplo práctico => analizar comandos en un programa\n')
# tenemos 3 comandos posibles
# - añadir
# - eliminar
# - salir

comando_1 = 'añadir'
comando_2 = 'hola'
comando_3 = 'eliminar'
comando_4 = 'mi_nombre'
comando_5 = 'salir'

print('¿Existe el comando en el programa?')
print( 'comando_1 =>', comando_1 == 'añadir' or comando_1 == 'eliminar' or comando_1 == 'salir' ) # True
print( 'comando_2 =>', comando_2 == 'añadir' or comando_2 == 'eliminar' or comando_2 == 'salir' ) # False
print( 'comando_3 =>', comando_3 == 'añadir' or comando_3 == 'eliminar' or comando_3 == 'salir' ) # True
print( 'comando_4 =>', comando_4 == 'añadir' or comando_4 == 'eliminar' or comando_4 == 'salir' ) # False
print( 'comando_5 =>', comando_5 == 'añadir' or comando_5 == 'eliminar' or comando_5 == 'salir' ) # True

#! Salto en el tiempo
# => veremos que esto es más fácil con listas
# utilizando palabra clave in
print()

lista_comandos = ['añadir' , 'eliminar' , 'salir']
print(lista_comandos, '\n')

print('comando_1 =>', comando_1 in lista_comandos) # True
print('comando_2 =>', comando_2 in lista_comandos) # False
print('comando_3 =>', comando_3 in lista_comandos) # True
print('comando_4 =>', comando_4 in lista_comandos) # False
print('comando_5 =>', comando_5 in lista_comandos) # True