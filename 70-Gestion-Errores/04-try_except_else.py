# =====================================================================
# try-except-else

# - ya hemos visto que el "else" complementa algunos bloques de código
# - no solo al if
# - por ejemplo: while, for
# - igualmente lo hace con el try-except
# - aquí se ejecuta SIEMPRE Y CUANDO la excepción no ocurra
# =====================================================================


def dividir(a,b):
    try:
        print( '{:.4f}'.format(a/b) )
    except Exception as e:
        print('ERROR | Lo siento, pero algo salió mal |', e)
    else:
        print('Operación realizada con ÉXITO !!!')
    # end try-except-else
# end def


# ------
# TEST
# ------
dividir(5,0)
print()
dividir(5,2)
print()
dividir(5,"a")

# => EJ consola:
"""
ERROR | Lo siento, pero algo salió mal | division by zero

2.5000
Operación realizada con ÉXITO !!!

ERROR | Lo siento, pero algo salió mal | unsupported operand type(s) for /: 'int' and 'str'
"""