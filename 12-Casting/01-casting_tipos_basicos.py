# ==================================================================
# Casting

# - funciones internas de python
# - con el mismo nombre del tipo de variable
# - las utilizamos para transformar de un tipo de variable a otro
# ==================================================================

#? 1) Casting entre tipos básicos

var_1 = '25' # string numérico!
var_2 = 41
var_3 = -8.9
var_4 = True
var_5 = False
var_6 = 0
var_7 = 100
var_8 = None

print( var_1 , '\t|', type(var_1) )
print( var_2 , '\t|', type(var_2) )
print( var_3 , '\t|', type(var_3) )
print( var_4 , '\t|', type(var_4) )
print( var_5 , '\t|', type(var_5) )
print( var_6 , '\t|', type(var_6) )
print( var_7 , '\t|', type(var_7) )
print( var_8 , '\t|', type(var_8) )

var_1_to_int = int(var_1)
var_2_to_float = float(var_2)
var_3_to_str = str(var_3)
var_4_to_int = int(var_4)
var_5_to_float_= float(var_5)
var_6_to_bool = bool(var_6)
var_7_to_bool = bool(var_7)
var_8_to_bool = bool(var_8)

print( var_1 , '=>' , var_1_to_int , '\t|' , type(var_1_to_int) )
print( var_2 , '=>' , var_2_to_float , '\t|' , type(var_2_to_float) )
print( var_3 , '=>' , var_3_to_str , '\t|' , type(var_3_to_str) )
print( var_4 , '=>' , var_4_to_int , '\t|' , type(var_4_to_int) )
print( var_5 , '=>' , var_5_to_float_ , '\t|' , type(var_5_to_float_) )
print( var_6 , '=>' , var_6_to_bool , '\t|' , type(var_6_to_bool) )
print( var_7 , '=>' , var_7_to_bool , '\t|' , type(var_7_to_bool) )
print( var_8 , '=>' , var_8_to_bool , '\t|' , type(var_8_to_bool) )


#? 2) Si el casting no tiene sentido nos va a dar un error
#! ValueError ó TypeError

## EJEMPLO - ValueError - 1:
# - querer pasar un string de texto a int o float
# - esto nos daría un ValueError

var_1 = 'hola'
#print( int(var_1) )
#print( float(var_1) )

## EJEMPLO - ValueError - 3:
# - un valor None no puede ser convertido a número
# esto nos da un TypeError

var_1 = None
print( var_1 , type(var_1) )
#print( int(var_1) )
#print( float(var_1) )


#? 3) Todo puede ser convertible a string
var_1 = 25
var_2 = -6.33
var_3 = True
var_4 = False
var_5 = None

print( var_1 , ' => a string => ' , str(var_1) ) 
print( var_2 , ' => a string => ' , str(var_2) ) 
print( var_3 , ' => a string => ' , str(var_3) ) 
print( var_4 , ' => a string => ' , str(var_4) ) 
print( var_5 , ' => a string => ' , str(var_5) )

# => comprobamos que sea un string
cadena_3 = str(var_3) 
cadena_5 = str(var_5) 
print(cadena_3[0], cadena_3[-1])
print(cadena_5[0], cadena_5[-1])
