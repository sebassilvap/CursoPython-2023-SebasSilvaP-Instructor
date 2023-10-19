# =====================================================
# Función Lambda como Retorno de Función

# - función lambda => función anónima
# - no es obligatorio que se almacene en una variable
# - o en una definición
# - puede ser una expresión resultante
# - y el retorno de una función
# =====================================================


#? 1) Lambda como variable
print('\n1) Lambda como variable')

multiplicar_numero = lambda num, multiplicador : num * multiplicador

print( multiplicar_numero(5,2) ) # 10
print( multiplicar_numero(5,3) ) # 15
print( multiplicar_numero(5,4) ) # 20



#? 2) Lambda como retorno de función
print('\n2) Lambda como retorno de función')

def multiplicador(multiplicador):
    return lambda numero : numero * multiplicador
# end def

# => definir variables en base al multiplicador
doblar_numero = multiplicador(2)
triplicar_numero = multiplicador(3)
quintuplicar_numero = multiplicador(5)

# => si deseamos saber que retorna esto
print( doblar_numero, type(doblar_numero) )
print( triplicar_numero, type(triplicar_numero) )
print( quintuplicar_numero, type(quintuplicar_numero) )

# EJ de respuesta de la consola:
# <function multiplicador.<locals>.<lambda> at 0x00000280BD57A200> <class 'function'>
# <function multiplicador.<locals>.<lambda> at 0x00000280BD57A2A0> <class 'function'>
# <function multiplicador.<locals>.<lambda> at 0x00000280BD57A160> <class 'function'>

# => Utilizando este retorno para un número en específico:
# EJ: con el número 10
print( doblar_numero(10) ) # 20
print( triplicar_numero(10) ) # 30
print( quintuplicar_numero(10) ) # 50