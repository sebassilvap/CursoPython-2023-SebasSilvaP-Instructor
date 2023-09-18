# =====================================
# Operadores Booleanos de Comparación
# (también: Operadores Relacionales)

# - Aplicado a strings
# - Se analiza por orden alfabético
# - ej: Z es mayor a A
# =====================================

letra_1 = 'c'
letra_2 = 'x'

#? 1) Comparación entre 2 letras distintas
print('Comparación entre',letra_1,'y',letra_2,':')
print( letra_1 , '>' , letra_2 , ' : ' , letra_1 > letra_2 ) # c > x  :  False
print( letra_1 , '>=' , letra_2 , ' : ' , letra_1 >= letra_2 ) # c >= x  :  False
print( letra_1 , '<' , letra_2 , ' : ' , letra_1 < letra_2 ) # c < x  :  True
print( letra_1 , '<=' , letra_2 , ' : ' , letra_1 <= letra_2 ) # c <= x  :  True
print( letra_1 , '==' , letra_2 , ' : ' , letra_1 == letra_2 ) # c == x  :  False
print( letra_1 , '!=' , letra_2 , ' : ' , letra_1 != letra_2 ) # c != x  :  True


#? 2) Comparación entre 2 letras iguales
print('\nComparación entre',letra_1,'y',letra_1,':')
print( letra_1 , '>' , letra_1 , ' : ' , letra_1 > letra_1 ) # c > c  :  False
print( letra_1 , '>=' , letra_1 , ' : ' , letra_1 >= letra_1 ) # c >= c  :  True
print( letra_1 , '<' , letra_1 , ' : ' , letra_1 < letra_1 ) # c < c  :  False
print( letra_1 , '<=' , letra_1 , ' : ' , letra_1 <= letra_1 ) # c <= c  :  True
print( letra_1 , '==' , letra_1 , ' : ' , letra_1 == letra_1 ) # c == c  :  True
print( letra_1 , '!=' , letra_1 , ' : ' , letra_1 != letra_1 ) # c != c  :  False


#? 3) Comparación entre 2 cadenas

c_1 = 'AA'
c_2 = 'AAA'

print('\nComparación entre',c_1,'y',c_2,':')
print( c_1 , '>' , c_2 , ' : ' , c_1 > c_2 ) # AA > AAA  :  False
print( c_1 , '>=' , c_2 , ' : ' , c_1 >= c_2 ) # AA >= AAA  :  False
print( c_1 , '<' , c_2 , ' : ' , c_1 < c_2 ) # AA < AAA  :  True
print( c_1 , '<=' , c_2 , ' : ' , c_1 <= c_2 ) # AA <= AAA  :  True
print( c_1 , '==' , c_2 , ' : ' , c_1 == c_2 ) # AA == AAA  :  False
print( c_1 , '!=' , c_2 , ' : ' , c_1 != c_2 ) # AA != AAA  :  True


c_1 = 'amigo'
c_2 = 'amiga'

print('\nComparación entre',c_1,'y',c_2,':')
print( c_1 , '>' , c_2 , ' : ' , c_1 > c_2 ) # amigo > amiga  :  True
print( c_1 , '>=' , c_2 , ' : ' , c_1 >= c_2 ) # amigo >= amiga  :  True
print( c_1 , '<' , c_2 , ' : ' , c_1 < c_2 ) # amigo < amiga  :  False
print( c_1 , '<=' , c_2 , ' : ' , c_1 <= c_2 ) # amigo <= amiga  :  False
print( c_1 , '==' , c_2 , ' : ' , c_1 == c_2 ) # amigo == amiga  :  False
print( c_1 , '!=' , c_2 , ' : ' , c_1 != c_2 ) # amigo != amiga  :  True


c_1 = 'Z'
c_2 = 'AAAAAAAAA'

print('\nComparación entre',c_1,'y',c_2,':')
print( c_1 , '>' , c_2 , ' : ' , c_1 > c_2 ) # Z > AAAAAAAAA  :  True
print( c_1 , '>=' , c_2 , ' : ' , c_1 >= c_2 ) # Z >= AAAAAAAAA  :  True
print( c_1 , '<' , c_2 , ' : ' , c_1 < c_2 ) # Z < AAAAAAAAA  :  False
print( c_1 , '<=' , c_2 , ' : ' , c_1 <= c_2 ) # Z <= AAAAAAAAA  :  False
print( c_1 , '==' , c_2 , ' : ' , c_1 == c_2 ) # Z == AAAAAAAAA  :  False
print( c_1 , '!=' , c_2 , ' : ' , c_1 != c_2 ) # Z != AAAAAAAAA  :  True


#? 4) Comparación entre 2 símbolos

c_1 = '@'
c_2 = '%'

print('\nComparación entre',c_1,'y',c_2,':')
print( c_1 , '>' , c_2 , ' : ' , c_1 > c_2 )  #     @ > %  :  True
print( c_1 , '>=' , c_2 , ' : ' , c_1 >= c_2 )  #   @ >= %  :  True
print( c_1 , '<' , c_2 , ' : ' , c_1 < c_2 )  #     @ < %  :  False
print( c_1 , '<=' , c_2 , ' : ' , c_1 <= c_2 )  #   @ <= %  :  False
print( c_1 , '==' , c_2 , ' : ' , c_1 == c_2 )  #   @ == %  :  False
print( c_1 , '!=' , c_2 , ' : ' , c_1 != c_2 )  #   @ != %  :  True

# => ¿Por qué?
# código hexadecimal de caracteres: https://www.ascii-code.com/
# @ ===> DEC = 64
# % ===> DEC = 37