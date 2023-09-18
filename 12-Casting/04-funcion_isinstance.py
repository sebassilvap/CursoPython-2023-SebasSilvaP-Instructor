# ====================================
# Función Interna => .ininstance()

# - devuelve un valor booleano
# - para confirmar el tipo del dato
# - RECORDAR: el tipo lo sabemos con type()
# ====================================

var_1 = 10
var_2 = 'hola'
var_3 = -50.6
var_4 = True

print('\nVariables y tipos')
print( var_1 , type(var_1) ) # 10 <class 'int'>
print( var_2 , type(var_2) ) # hola <class 'str'>
print( var_3 , type(var_3) ) # -50.6 <class 'float'>
print( var_4 , type(var_4) ) # True <class 'bool'>

# => utilizando isinstance( valor , tipo )
print('\nvar_1 => isinstance()')
print( isinstance(var_1 , int) )  # True
print( isinstance(var_1 , str) )  # False
print( isinstance(var_1 , float) )  # False
print( isinstance(var_1 , bool) )  # False

print('\nvar_2 => isinstance()')
print( isinstance(var_2 , int) )  # False
print( isinstance(var_2 , str) )  # True
print( isinstance(var_2 , float) )  # False
print( isinstance(var_2 , bool) )  # False

print('\nvar_3 => isinstance()')
print( isinstance(var_3 , int) )  # False
print( isinstance(var_3 , str) )  # False
print( isinstance(var_3 , float) )  # True
print( isinstance(var_3 , bool) )  # False

print('\nvar_4 => isinstance()')
print( isinstance(var_4 , int) )  # True (*)
print( isinstance(var_4 , str) )  # False
print( isinstance(var_4 , float) )  # False
print( isinstance(var_4 , bool) )  # True 

# True = 1
# False = 0
