# ==========================================
# Módulo Funciones y Constantes Aritméticas
# ==========================================

# --------------
# => Constantes
# --------------

CONSTANTE_PI = 3.1416
GRAVEDAD = 9.8


# --------------
# => Funciones
# --------------

def suma(a,b):
    print( 'Suma de {} + {} = {}'.format(a, b, a+b) )
# end def


def resta(a,b):
    print( 'Resta de {} - {} = {}'.format(a, b, a-b) )
# end def


def producto(a,b):
    print( 'Producto de {} * {} = {}'.format(a, b, a*b) )
# end def


def exponente(a,b):
    print( 'Exponente de {} ^ {} = {}'.format(a, b, a**b) )
# end def


def promedio_3_numeros(a,b,c):
    print( 'Valor 1 =', a )
    print( 'Valor 2 =', b )
    print( 'Valor 3 =', c )
    print( 'PROMEDIO = {:.2f}'.format( (a+b+c) / 3 ) )
# end def