# =================================================================================================
# Aritmética Básica en Python

# - Python es como una calculadora / súper calculadora
# - Sin necesidad de bibliotecas externas podemos hacer operaciones matemáticas básico-avanzadas
# - Las siguientes operaciones pueden ser realizadas en Python

#?      suma       =>   +
#?      resta      =>   -
#?      producto   =>   *
#?      división   =>   /
#?      potencia   =>   **
#?      módulo     =>   %

# módulo % => devuelve el resto de una división
# EJ:
#      10   /    3
#      -9        3
#*      1

# => Por tanto:  10 % 3 = 1
# =================================================================================================


#? 1) Aritmética Directa
print('1) Aritmética Directa')
print()
# - lo siguiente NO ES ERROR
# - pero no lo podemos visualizar
# - a menos que lo pongamos en un print
#!  pero esto se puede ver en otros editores como Jupyter Notebook sin necesidad de print()


5 + 5
5 * 8
15 / 3
35 - 9
2 ** 3
10 % 3

print('OPERACIONES:')
print(  5 + 5  )
print(  5 * 8  )
print(  15 / 3 )
print(  35 - 9 )
print(  2 ** 3 )
print(  10 % 3 )
print('----------------')
print(  5 + 5  , type(5 + 5)   )
print(  5 * 8  , type(5 * 8)   )
print(  15 / 3 , type(15 / 3)  ) # así sea la división exacta => devuelve un flotante (float)
print(  35 - 9 , type(35 - 9)  )
print(  2 ** 3 , type(2 ** 3) )
print(  10 % 3 , type(10 % 3) )



#? 2) Reglas Matemáticas
print('2) Reglas Matemáticas')
print()
# - Python respeta la JERARQUÍA de las operaciones matemáticas

# - primero *, / LUEGO +,-
# - primero ** LUEGO *,/ LUEGO +,-
# - primero () LUEGO ** LUEGO *,/ LUEGO +,-


#? EJ 1:
print( 3 * 3 + 2 ) 
# 9 + 2
# 11

#? EJ 2:
print( 3 * 2 + 15 / 5 + 1 )
# 6 + 3.0 + 1
# 9.0 + 1
# 10.0



