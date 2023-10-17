# ===============================================================
# Ejercicio

# - Control Básico de Errores con Condicionales & Funciones
# - la gestión de errores es un tema avanzado
# - ya lo veremos más luego
# - sin embargo con lo aprendido hasta el momento
# - estamos en la capacidad de poder gestionar errores básicos
# - errores predecibles
# - obviamente no todos
# ===============================================================


#? 1) EJ: división para cero
print('\n1) EJ: división para cero')
# - sin necesidad de imprimir
# - o guardar en una variable
# - al poner lo siguiente en el código
# - tendremos el error de división para cero

#2 / 0 #! ZeroDivisionError: division by zero

def division(a, b):
    if b == 0:
        return 'ERROR: No existe la división para 0!!'
    else:
        return a / b
    # end if
# end def

# => TEST
print( division(2,5) )
print( division(2,0) )
print( division(12,4) )

# - lo más importante
# - es que nuestro código ya no se va a detener!



#? 2) EJ: IndexError al acceder a una lista
print('\n2) EJ: IndexError al acceder a una lista')

lista = ['A', 'B', 'C']
#(+)      0    1    2
#(-)      3    2    1

print( lista[2] )
#print( lista[3] )  #! IndexError: list index out of range
#print( lista[-4] ) #! IndexError: list index out of range
print( len(lista) ) # 3
print( -len(lista) ) # -3
print( -1 * len(lista) ) # -3

def acceder_index(lista, index):
    # evaluamos índice positivo fuera de rango
    if index >= len(lista):
        return 'ERROR: índice positivo fuera de rango'
    
    # evaluamos índice negativo fuera de rango
    elif index < -len(lista):
        return 'ERROR: índice negativo fuera de rango'
    
    # para los demás casos
    else:
        return lista[index]
    # end if
# end def

print('\nUtiizando función definida: ')

print( acceder_index(lista, 2) )
print( acceder_index(lista, 3) )
print( acceder_index(lista, -4) )



#? 3) EJ: Tipo de Dato incorrecto en función promedio
print('\n3) EJ: Tipo de Dato incorrecto en función promedio')

#* REVISAR:
# => ejemplo de función promedio


def promedio(lista):
    temp = 0
    
    for nota in lista:
        temp += nota
    # end for
    
    return temp / len(lista)
# end def

# ----------------
# TEST 1
print('\nTEST 1')
# ----------------
notas_1 = [17, 14, 16, 19, 13]
notas_2 = [15, 12, 20]
notas_3 = [18, 15, 'a']
notas_4 = 10
notas_5 = 'hola'

print( promedio(notas_1) )    
print( promedio(notas_2) )
#print( promedio(notas_3) ) #! TypeError: unsupported operand type(s) for +=: 'int' and 'str'
#print( promedio(notas_4) ) #! TypeError: 'int' object is not iterable
#print( promedio(notas_5) ) #! TypeError: unsupported operand type(s) for +=: 'int' and 'str'


# => Redefinir la función "promedio"

def calculo_promedio(lista):
    temp = 0
    
    for nota in lista:
        temp += nota
    # end for
    
    return temp / len(lista)
# end def

def promedio(lista):
    # revisar si el argumento es una lista
    if isinstance(lista, list):
        # revisar que todos los elementos de lista sean números
        for num in lista:
            if isinstance(num, int) == False and isinstance(num, float) == False:
                return 'ERROR: elementos de lista deben ser números'
        # end for
        
        # => si tenemos lista y los valores son int o float
        return calculo_promedio(lista)
    else:
        return 'ERROR: argumento de función debe ser una lista'
    # end if
# end def

# ----------------
# TEST 2
print('\nTEST 2')
# ----------------
notas_1 = [17, 14, 16, 19, 13]
notas_2 = [15, 12, 20]
notas_3 = [18, 15, 'a']
notas_4 = 10
notas_5 = 'hola'

print( promedio(notas_1) ) # 15.8
print( promedio(notas_2) ) # 15.666666666666666
print( promedio(notas_3) ) # ERROR: elementos de lista deben ser números 
print( promedio(notas_4) ) # ERROR: argumento de función debe ser una lista 
print( promedio(notas_5) ) # ERROR: argumento de función debe ser una lista 


# => Utilizando operador not para función
# - es el mismo resultado
# - solo es una opción que nos muestra varias maneras de escribir lo mismo

def promedio(lista):
    # revisar si el argumento es una lista
    if isinstance(lista, list):
        # revisar que todos los elementos de lista sean números
        for num in lista:
            if not isinstance(num, int) and not isinstance(num, float):
                return 'ERROR: elementos de lista deben ser números'
        # end for
        
        # => si tenemos lista y los valores son int o float
        return calculo_promedio(lista)
    else:
        return 'ERROR: argumento de función debe ser una lista'
    # end if
# end def

# ----------------
# TEST 3
print('\nTEST 3')
# ----------------
notas_1 = [17, 14, 16, 19, 13]
notas_2 = [15, 12, 20]
notas_3 = [18, 15, 'a']
notas_4 = 10
notas_5 = 'hola'

print( promedio(notas_1) ) # 15.8
print( promedio(notas_2) ) # 15.666666666666666
print( promedio(notas_3) ) # ERROR: elementos de lista deben ser números 
print( promedio(notas_4) ) # ERROR: argumento de función debe ser una lista 
print( promedio(notas_5) ) # ERROR: argumento de función debe ser una lista 