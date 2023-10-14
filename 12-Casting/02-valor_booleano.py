# =============================================================
# Valor Booleano de los Datos

# - como vimos cualquier dato puede ser transformado a string
# - de igual manera cualquier dato tiene un valor booleano
# - como veremos prácticamente
# - un valor vacío, cero, nulo nos da False
# - cualquier otro valor diferente nos da True
# =============================================================

var_1 = 1
var_2 = 0 #!
var_3 = -1
var_4 = 100
var_5 = 0.01
var_6 = -0.0002
var_7 = -0.00 #!
var_8 = 'a'
var_9 = ' '
var_10 = " "
var_11 = '' #!
var_12 = None

print( 'var_1 =' , var_1 , ' => a bool => ' , bool(var_1) )
print( 'var_2 =' , var_2 , ' => a bool => ' , bool(var_2) )
print( 'var_3 =' , var_3 , ' => a bool => ' , bool(var_3) )
print( 'var_4 =' , var_4 , ' => a bool => ' , bool(var_4) )
print( 'var_5 =' , var_5 , ' => a bool => ' , bool(var_5) )
print( 'var_6 =' , var_6 , ' => a bool => ' , bool(var_6) )
print( 'var_7 =' , var_7 , ' => a bool => ' , bool(var_7) )
print( 'var_8 =' , var_8 , ' => a bool => ' , bool(var_8) )
print( 'var_9 =' , var_9 , ' => a bool => ' , bool(var_9) )
print( 'var_10 =' , var_10 , ' => a bool => ' , bool(var_10) )
print( 'var_11 =' , var_11 , ' => a bool => ' , bool(var_11) )
print( 'var_12 =' , var_12 , ' => a bool => ' , bool(var_12) )


# -------------------------------------------------------------
# => Conclusión
# - si el valor es 0 (entero o flotante) => esto es un False
# - diferente de 0 (positivo o negativo) => True
# - un string vacío => False
# - un solo caracter, así sea 1 espacio en blanco => True
# - un valor nulo (None) => False
# -------------------------------------------------------------