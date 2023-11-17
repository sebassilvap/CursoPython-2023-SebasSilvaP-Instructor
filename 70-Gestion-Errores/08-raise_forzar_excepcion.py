# =====================================================================
# keyword raise => forzar el error / excepción

# - un código no se limita a las exepciones estándar que tiene Python
# - nosotros podemos definir nuestros propios errores
# - o cuándo un error ocurriría en nuestro programa
# - esto se lo hace con el keyword => raise
# - pero una vez que ocurre se la debe gestionar
# - caso contrario el flujo del programa queda interrumpido
# - podemos entonces definir nuestras propias:
#       * TypeError
#       * ValueError
#       * Exception en General
# =====================================================================


#? 1) Ejemplo: sin raise + sin try-except
print('\n1) Ejemplo: sin raise + sin try-except\n')
# - veamos como una función tan sencilla
# - puede dar tantos inconvenientes
# - cuando los argumentos dados al invocar esta función
# - son los incorrectos ó los no adecuados

def saludar(nombre):
    print( 'Hola {} es un gusto conocerte!'.format( nombre.title().strip(' ') ) )
# end def


# ------
# TEST
# ------

## => ejecución correcta (OK)
saludar('sebastian silva') # Hola Sebastian Silva es un gusto conocerte!
saludar('    carlos    ') # Hola Carlos es un gusto conocerte!

## => ejecución con error (NO OK)
#saludar(False)  #! AttributeError: 'bool' object has no attribute 'title'
#saludar(50)  #! AttributeError: 'int' object has no attribute 'title'

## => no error, pero no tiene sentido (NO OK)
saludar('') # Hola  es un gusto conocerte!  
saludar('   ') # Hola  es un gusto conocerte!  



#? 2) Ejemplo: sin raise + con try-except
print('\n2) Ejemplo: sin raise + con try-except\n')

def saludar(nombre):
    try:
        print( 'Hola {} es un gusto conocerte!'.format( nombre.title().strip(' ') ) )
    except AttributeError as e:
        print( type(e).__name__ , '|' , e , '| ERROR - Por favor ingrese un dato válido' )
    except Exception as e:
        print( type(e).__name__ , '|' , e , '| ERROR al utilizar la función saludar()' )
    # end try-except
# end def


# ------
# TEST
# ------

## => ejecución correcta (OK)
saludar('sebastian silva') # Hola Sebastian Silva es un gusto conocerte!
saludar('    carlos    ') # Hola Carlos es un gusto conocerte!

## => ejecución con error (OK)
saludar(False) # AttributeError | 'bool' object has no attribute 'title' | ERROR - Por favor ingrese un dato válido
saludar(50) # AttributeError | 'int' object has no attribute 'title' | ERROR - Por favor ingrese un dato válido

## => no error, pero no tiene sentido (NO OK)
saludar('') # Hola  es un gusto conocerte!  
saludar('   ') # Hola  es un gusto conocerte!  



#? 3) Ejemplo: con raise + con try-except
print('\n3) Ejemplo: con raise + con try-except\n')
# - no olvidar cuando se usa raise
# - tiene que ser con un try-except
# - caso contrario, se produce error y se para el flujo del programa

# -------------------------------------------
# 3.1) raise FUERA de try-except
print('\n3.1) raise FUERA de try-except\n')
# -------------------------------------------
# - cuando se invoca un error o excepción
# - si no está dentro de un try-except
# - el programa se para

def saludar(nombre):
    nombre = nombre.title().strip(' ')
    if nombre == '':
        raise Exception('ERROR - El nombre no puede estar vacío')
    else:
        print( 'Hola {} es un gusto conocerte!'.format( nombre.title().strip(' ') ) )
# end def


# ------
# TEST
# ------

saludar('   sebas ') # Hola Sebas es un gusto conocerte!
#saludar('') #! Exception: ERROR - El nombre no puede estar vacío



# -------------------------------------------
# 3.2) raise DENTRO de try-except
print('\n3.2) raise DENTRO de try-except\n')
# -------------------------------------------
# - la manera correcta de plantear el raise
# - se captura en este caso dentro la Exception general

def saludar(nombre):
    try:
        nombre = nombre.title().strip(' ')
        if nombre == '':
            raise Exception('ERROR - El nombre no puede estar vacío')
        else:
            print( 'Hola {} es un gusto conocerte!'.format( nombre.title().strip(' ') ) )
    
    except AttributeError as e:
        print( type(e).__name__ , '|' , e , '| ERROR - Por favor ingrese un dato válido' )
    except Exception as e:
        print( type(e).__name__ , '|' , e , '| ERROR al utilizar la función saludar()' )
    # end try-except
# end def


# ------
# TEST
# ------

## => ejecución correcta (OK)
saludar('sebastian silva') # Hola Sebastian Silva es un gusto conocerte!
saludar('    carlos    ') # Hola Carlos es un gusto conocerte!

## => ejecución con error (OK)
saludar(False) # AttributeError | 'bool' object has no attribute 'title' | ERROR - Por favor ingrese un dato válido
saludar(50) # AttributeError | 'int' object has no attribute 'title' | ERROR - Por favor ingrese un dato válido

## => no error, pero no tiene sentido (NO OK)
saludar('') # Exception | ERROR - El nombre no puede estar vacío | ERROR al utilizar la función saludar()
saludar('   ') # Exception | ERROR - El nombre no puede estar vacío | ERROR al utilizar la función saludar()



#? 4) raise + tipo de Error Específico => La mejor práctica
print('\n4) raise + tipo de Error Específico => La mejor práctica')
# - en cuanto a excepciones se refiere
# - mientras más específicos seamos, es mejor
# - podemos hacer un raise de un error específico

def saludar(nombre):
    try:
        nombre = nombre.title().strip(' ')
        if nombre == '':
            raise ValueError('ERROR - El nombre no puede estar vacío')
        else:
            print( 'Hola {} es un gusto conocerte!'.format( nombre.title().strip(' ') ) )
    
    except ValueError as user_e:
        print( type(user_e).__name__ , '|' , user_e )
    except AttributeError as e:
        print( type(e).__name__ , '|' , e , '| ERROR - Por favor ingrese un dato válido' )
    except Exception as e:
        print( type(e).__name__ , '|' , e , '| ERROR al utilizar la función saludar()' )
    # end try-except
# end def


# ------
# TEST
# ------

## => ejecución correcta (OK)
saludar('sebastian silva') # Hola Sebastian Silva es un gusto conocerte!
saludar('    carlos    ') # Hola Carlos es un gusto conocerte!

## => ejecución con error (OK)
saludar(False) # AttributeError | 'bool' object has no attribute 'title' | ERROR - Por favor ingrese un dato válido
saludar(50) # AttributeError | 'int' object has no attribute 'title' | ERROR - Por favor ingrese un dato válido

## => no error, pero no tiene sentido (NO OK)
saludar('') # ValueError | ERROR - El nombre no puede estar vacío
saludar('   ') # ValueError | ERROR - El nombre no puede estar vacío