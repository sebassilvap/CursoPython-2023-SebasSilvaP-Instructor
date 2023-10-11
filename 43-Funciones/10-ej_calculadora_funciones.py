# ================================
# Ejercicio

# - Calculadora en Python
# - Que reciba input
# - Ejecute operaciones básicas
# ================================

# --------------------------
#? Definición de funciones
# --------------------------

def suma(a, b):
    return a + b
# end def

def resta(a, b):
    return a - b
# end def

def producto(a, b):
    return a * b
# end def

def division(a, b):
    return a / b
# end def

def potencia(a, b):
    return a ** b
# end def

def modulo(a, b):
    return a % b
# end def

def presentar_titulo():
    print('\n\n=====================================')
    print('Bienvenidos al Programa - Calculadora')
    print('=====================================')
# end def

def presentar_opciones():
    print()
    print('(1) Ejecutar Operaciones')
    print('(2) Salir / Quit / Q')
# end def

def presentar_resultados(a, b):
    print()
    print('Número 1 =', a)
    print('Número 2 =', b)
    print( a, '+', b, '=', suma(a,b) )    
    print( a, '-', b, '=', resta(a,b) )    
    print( a, '*', b, '=', producto(a,b) )    
    print( a, '/', b, '=', division(a,b) )    
    print( a, '**', b, '=', potencia(a,b) )    
    print( a, '%', b, '=', modulo(a,b) )    
# end def

# -----------------------
#? Bucle del Programa
# -----------------------

presentar_titulo()

opcion = ''

while True:
    
    presentar_opciones()
    
    opcion = input('Seleccione la opción del programa: ')
    opcion = opcion.strip().title()
    
    
    if opcion == '1':
        print()
        num_1 = float( input('Ingrese el 1er número: ') )
        num_2 = float( input('Ingrese el 2do número: ') )
        presentar_resultados(num_1, num_2)
    elif opcion == '2' or opcion == 'Salir' or opcion == 'Quit' or opcion == 'Q':
        print('Gracias por usar la calculadora')
        break
    else:
        print('ERROR: Opción Inválida')
    # end if
    
# end while
    