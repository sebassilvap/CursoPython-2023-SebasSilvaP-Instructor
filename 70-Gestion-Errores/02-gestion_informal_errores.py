# =================================================
# Gestión Informal de Errores

# - habíamos hablado ya de este tema
# - podemos simular la gestión de errores
# - con un condicional
# - y podemos añadir también funciones
# - sin necesidad de utilizar un bloque try...catch

# *    try...catch => a continuación !!
# =================================================


#? 1) Ejemplo de gestión informal - ZeroDivisionError
print('\n1) Ejemplo de gestión informal - ZeroDivisionError')

def operacion_division(a, b):
    if b == 0:
        return 'ERROR - divisor no puede ser CERO !!'
    else:
        return a / b
# end def

print( operacion_division(5,2) ) # 2.5
print( operacion_division(5,0) ) # ERROR - divisor no puede ser CERO !!



#? 2) Ejemplo de gestión informal - ValueError
print('\n2) Ejemplo de gestión informal - ValueError')

# => Código susceptible a errores
"""
edad_usuario = input('Ingrese su edad: ')

print( 'Usted tiene {} años!'.format(edad_usuario) )
print( 'En 5 años usted tendrá {} años...'.format( int(edad_usuario) + 5 ) )
"""
#! ValueError: invalid literal for int()


# => Con gestión informal
edad_usuario = input('Ingrese su edad: ')
edad_usuario = edad_usuario.strip(' ')

if edad_usuario.isdigit():
    edad_usuario = int(edad_usuario)
    print( 'Usted tiene {} años!'.format(edad_usuario) )
    print( 'En 5 años usted tendrá {} años...'.format( edad_usuario + 5 ) )
else:
    print('ERROR - Usted debe poner un número ENTERO !')
# end if
    