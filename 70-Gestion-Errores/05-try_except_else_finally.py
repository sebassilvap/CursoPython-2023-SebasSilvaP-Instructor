# ==============================================================
# try-except-else-finally

# - representa la estructura completa de la gestión de error
# - cada uno constituye un bloque de código
# ! try-except es obligatorio
# - si se usa un try => obligatoriamente necesitamos except
# * else & finally => son opcionales

"""
try:     aquí va el código que tiene el riesgo de producir error
except:  bloque que se ejecuta en caso de error sin interrumpir el flujo del programa
else:    bloque que se ejecuta cuando no se da error
finally: bloque que se ejecuta SIEMPRE, haya error o no
"""
# ==============================================================


def dividir(a,b):
    try:
        resultado = a/b
    except Exception as e:
        print( 'ERROR | Lo siento, pero algo salió mal |', e )
    else:
        print( 'Operación con ÉXITO | RESULTADO => {}/{} = {:.5f}'.format(a,b,resultado) )
    finally:
        print( 'FIN DEL MÉTODO DIVIDIR' )
    # end try-except-else-finally
# end def


# ------
# TEST
# ------
dividir(5,0)
print()
dividir(5,2)
print()
dividir(5,"a")
print()
dividir('x','y')
print()
dividir(20,90.5)


# => Resultado Consola:
"""
ERROR | Lo siento, pero algo salió mal | division by zero
FIN DEL MÉTODO DIVIDIR

Operación con ÉXITO | RESULTADO => 5/2 = 2.50000
FIN DEL MÉTODO DIVIDIR

ERROR | Lo siento, pero algo salió mal | unsupported operand type(s) for /: 'int' and 'str'
FIN DEL MÉTODO DIVIDIR

ERROR | Lo siento, pero algo salió mal | unsupported operand type(s) for /: 'str' and 'str'
FIN DEL MÉTODO DIVIDIR

Operación con ÉXITO | RESULTADO => 20/90.5 = 0.22099
FIN DEL MÉTODO DIVIDIR
"""
