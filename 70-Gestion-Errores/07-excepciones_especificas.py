# ===================================================================================
# Excepciones Específicas

# - como buena práctica los errores se capturan / gestionan de manera específica
# - con except Exception as e => capturamos al error de manera general
# - y en todas sus formas posibles
# - por ej: ZeroDivisionError, TypeError => todo abarca Exception as e
# - también podemos definir cada excepción POR SEPARADO
# ===================================================================================


#? 1) type(e).__name__
print('\n1) type(e).__name__\n')
# - al utilizar el alias en Exception
# - por ejemplo: e
# *     e                => detalla la razón del error
# *     type(e)          => retorna el nombre del error con la palabra "class"
# *     type(e).__name__ => retorna el nombre del error


def dividir(a,b):
    try:
        resultado = a/b
    except Exception as e:
        print( 'ERROR | Lo siento, pero algo salió mal' )
        print( type(e) ) # nombre de tipo de dato + "class" => como hemos aprendido hasta el momento
        print( type(e).__name__ ) # solo el nombre del tipo de dato
        print( e ) # explicación del tipo de error
    else:
        print( 'Operación con ÉXITO | RESULTADO => {}/{} = {:.5f}'.format(a,b,resultado) )
    finally:
        print( 'FIN DEL MÉTODO DIVIDIR' )
    # end try-except-else-finally
# end def


def separador():
    print('-----------------------------')
# end def


# ------
# TEST
# ------
dividir(5,0)

separador()
dividir(5,2)

separador()
dividir(5,"a")

separador()
dividir('x','y')

separador()
dividir(20,90.5)


# => Resultado Consola:
"""

ERROR | Lo siento, pero algo salió mal
<class 'ZeroDivisionError'>
ZeroDivisionError
division by zero
FIN DEL MÉTODO DIVIDIR
-----------------------------
Operación con ÉXITO | RESULTADO => 5/2 = 2.50000
FIN DEL MÉTODO DIVIDIR
-----------------------------
ERROR | Lo siento, pero algo salió mal
<class 'TypeError'>
TypeError
unsupported operand type(s) for /: 'int' and 'str'
FIN DEL MÉTODO DIVIDIR
-----------------------------
ERROR | Lo siento, pero algo salió mal
<class 'TypeError'>
TypeError
unsupported operand type(s) for /: 'str' and 'str'
FIN DEL MÉTODO DIVIDIR
-----------------------------
Operación con ÉXITO | RESULTADO => 20/90.5 = 0.22099
FIN DEL MÉTODO DIVIDIR

"""



#? 2) Excepciones Específicas
print('\n2) Excepciones Específicas\n')
# - es tan fácil como llamar except + el nombre del Error
# - por ej: except TypeError as e: ó except ZeroDivisionError as e:
# ! no es error si el alias se repite
# - es una buena práctica el capturar los errores de manera específica
# - antes que hacerlo de manera general
# - ESTRUCTURA:
# *     iniciamos con las excepciones específicas
# *     terminamos con la excepción general


# ----------------
# BUENA PRÁCTICA 
# ----------------

def dividir(a,b):
    try:
        resultado = a/b
    except TypeError as e:
        print( type(e).__name__ , '||' , e  )
        print('ERROR - Por favor ingrese un número !')
    except ZeroDivisionError as e:
        print( type(e).__name__ , '||' , e  )
        print('ERROR - La división para CERO no existe !')
    except Exception as e: # de manera general
        print( type(e).__name__ , '||' , e  )
        print('ERROR - La división no es posible...')
    else:
        print( 'Operación con ÉXITO | RESULTADO => {}/{} = {:.5f}'.format(a,b,resultado) )
    finally:
        print( 'FIN DEL MÉTODO DIVIDIR' )
    # end try-except
# end def


# ------
# TEST
# ------
dividir(5,0)

separador()
dividir(5,2)

separador()
dividir(5,"a")

separador()
dividir('x','y')

separador()
dividir(20,90.5)


# => Resultado Consola:
"""

ZeroDivisionError || division by zero
ERROR - La división para CERO no existe !
FIN DEL MÉTODO DIVIDIR
-----------------------------
Operación con ÉXITO | RESULTADO => 5/2 = 2.50000
FIN DEL MÉTODO DIVIDIR
-----------------------------
TypeError || unsupported operand type(s) for /: 'int' and 'str'
ERROR - Por favor ingrese un número !
FIN DEL MÉTODO DIVIDIR
-----------------------------
TypeError || unsupported operand type(s) for /: 'str' and 'str'
ERROR - Por favor ingrese un número !
FIN DEL MÉTODO DIVIDIR
-----------------------------
Operación con ÉXITO | RESULTADO => 20/90.5 = 0.22099
FIN DEL MÉTODO DIVIDIR

"""