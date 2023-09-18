# =====================================
# Operadores Booleanos de Comparación
# (también: Operadores Relacionales)

# - Aplicado a valores numéricos

'''
Operador |  Definición
-------------------------------
   >     |  Mayor que
   <     |  Menor que
   >=    |  Mayor o igual que
   <=    |  Menor o igual que
   ==    |  Igual que
   !=    |  Diferente de
'''
# =====================================

num_1 = 5
num_2 = 3


print('\n1) Mayor que (>)')
print( num_1 , '>' , num_2 , ' : ' , num_1 > num_2 )  # 5 > 3  :  True
print( num_1 , '>' , num_1 , ' : ' , num_1 > num_1 )  # 5 > 5  :  False


print('\n2) Menor que (<)')
print( num_1 , '<' , num_2 , ' : ' , num_1 < num_2 )  # 5 < 3  :  False
print( num_1 , '<' , num_1 , ' : ' , num_1 < num_1 )  # 5 < 5  :  False


print('\n3) Mayor o Igual que (>=)')
print( num_1 , '>=' , num_2 , ' : ' , num_1 >= num_2 )  # 5 >= 3  :  True
print( num_1 , '>=' , num_1 , ' : ' , num_1 >= num_1 )  # 5 >= 5  :  True
#! El orden es importante
print( 20 >= 100 ) # False
#print( 20 =< 100 ) #! Error de Sintaxis


print('\n4) Menor o Igual que (<=)')
print( num_1 , '<=' , num_2 , ' : ' , num_1 <= num_2 )  # 5 <= 3  :  False
print( num_1 , '<=' , num_1 , ' : ' , num_1 <= num_1 )  # 5 <= 5  :  True


print('\n5) Igual que (==)')
print( num_1 , '==' , num_2 , ' : ' , num_1 == num_2 )  # 5 == 3  :  False
print( num_1 , '==' , num_1 , ' : ' , num_1 == num_1 )  # 5 == 5  :  True


print('\n6) Distinto de (!=)')
print( num_1 , '!=' , num_2 , ' : ' , num_1 != num_2 )  # 5 != 3  :  True
print( num_1 , '!=' , num_1 , ' : ' , num_1 != num_1 )  # 5 != 5  :  False