# ======================================================================
# try-except

# - de esta manera convertimos los errores de ejecución en excepciones
# - excepción 
#       => un bloque excepcional que nos permite la ejecución
#       => incluso cuando se da el error
#       => no se interrumpe el flujo del programa

# - try-except => envuelve un bloque de código peligroso
# - que puede producir un error de ejecución
# ======================================================================


#? 1) Ejemplo Básico 1: try-except
print('\n1) Ejemplo Básico 1: try-except')

def dividir(a,b):
    try:
        return a/b
    except:
        # cualquier tipo de error
        return 'ERROR al usar la división'
    # end try-except
# end def

# TEST
print('línea de código') # línea de código
print( dividir(10,3) ) # 3.3333333333333335
print( dividir(5,2) ) # 2.5
print( dividir(5,0) ) # ERROR al usar la división
print( dividir('10',5) ) # ERROR al usar la división
print('línea de código') # línea de código



#? 2) Ejemplo Básico 2: try-except
print('\n2) Ejemplo Básico 2: try-except')

"""

lista = ['manzana', 'lapiz', 'toalla']

def presentacion_inicial(lista_compras):
    print('\nPrograma de Manejo de Lista de Compras')
    print('Su lista actual:')
    print(lista_compras)
    print('----------------------------------------')
    print('Opciones:')
    print('(1) Añadir compra')
    print('(2) Eliminar último elemento')
    print('(3) Salir del programa')
    print('----------------------------------------')
# end def

while True:
    presentacion_inicial(lista)
        
    opcion_user = input('Seleccione opcion (1,2,3) : ').strip(' ')
    
    if opcion_user == '1':
        add_compra = input('Ingrese ítem: ').strip(' ').title()
        lista.append(add_compra)
    elif opcion_user == '2':
        #! si la lista ya está vacía => no hay como hacer .pop()
        try:
            lista.pop()
        except:
            print('No hay nada que eliminar !!!')
    elif opcion_user == '3':
        print('Gracias por usar nuestro programa')
        break
    else:
        print('ERROR - Opción Incorrecta')
# end while

"""



#? 3) try-except Exception
print('\n3) try-except Exception')
# - Básicamente try-except => captura cualquier excepción que se pueda dar
# - De igual manera si lo especificamos como try-except Exception

def dividir_A(a,b):
    try:
        return a/b
    except:
        return 'ERROR al usar la división'
    # end try-except
# end def

def dividir_B(a,b):
    try:
        return a/b
    except Exception:
        return 'ERROR'
    # end try-except
# end def

# ------
# TEST
# ------
print( dividir_A(10,0) ) # ERROR al usar la división
print( dividir_B(10,0) ) # ERROR



#? 4) try-except Exception con ALIAS
print('\n4) try-except Exception con ALIAS')
# - al utilizar un alias para Exception
# - podemos acceder exactamente al tipo de error que se produce

def dividir(a,b):
    try:
        print( '{:.4f}'.format(a/b) )
    except Exception as e:
        print('ERROR | Lo siento, pero algo salió mal |', e)
    # end try-except
# end def

# ------
# TEST
# ------
print('******* línea de código *******')
dividir(5,0) # ERROR | Lo siento, pero algo salió mal | division by zero
dividir(5,2) # 2.5000
dividir(5,"a") # ERROR | Lo siento, pero algo salió mal | unsupported operand type(s) for /: 'int' and 'str'
print('******* línea de código *******')



#? 5) RECORDAR => el alias puede ser cualquier nombre
print('\n5) RECORDAR => el alias puede ser cualquier nombre')
#! IMPORTANTE
# - el alias puede ser cualquier nombre
# - no necesariamente e

def dividir(a,b):
    try:
        print( '{:.4f}'.format(a/b) )
    except Exception as muestrame_el_error:
        print('ERROR | Lo siento, pero algo salió mal |', muestrame_el_error)
    # end try-except
# end def

# ------
# TEST
# ------
dividir(5,0)
dividir(5,2)
dividir(5,"a")
