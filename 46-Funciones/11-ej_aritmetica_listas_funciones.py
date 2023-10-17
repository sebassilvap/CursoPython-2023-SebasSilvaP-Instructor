# =========================================
# Ejercicio

# - Operaciones Aritméticas entre listas
# - Utilizando funciones
# =========================================

#? 1) Solución presentada en la última lección de Listas
print('\n1) Solución presentada en la última lección de Listas')

'''

array_1 = [2, 5, 6, 2, 3]
array_2 = [3, 4, 2, 5, 6]

operacion = '%'
resultado = []

if len(array_1) != len(array_2):
    print('ERROR - Ambos array tienen distinto tamaño')
else:
    i = 0
    while i < len(array_1):
        temp = str(array_1[i]) + operacion + str(array_2[i])
        resultado.append( eval(temp) )
        i += 1
    # end while
# end if

match operacion:
    case '+':
        print('SUMA =', resultado)
    case '-':
        print('RESTA =', resultado)
    case '*':
        print('PRODUCTO =', resultado)
    case '/':
        print('DIVISIÓN =', resultado)
    case '**':
        print('POTENCIA =', resultado)
    case '%':
        print('MÓDULO =', resultado)
# end match-case

'''



#? 2) Solución por medio de funciones
print('\n2) Solución por medio de funciones')
# - esta es una de las prácticas más conocidas en programación
# - se llama REFACTORIZAR el código
# - y es pan de todos los días en programación
# - consiste en mejorar nuestro código
# - adaptándolo a nuevas necesidades

def operar_arrays(array1, array2, operador):
    resultado = []
    operaciones = ['+','-','*','/','**','%']
    
    # => comprobar que ambos array tengan el mismo tamaño
    if len(array1) != len(array2):
        return 'ERROR - Ambos array tienen distinto tamaño'
        
    else:
        # => comprobar que el operador sea válido
        if operador in operaciones:
            i = 0
            while i < len(array1):
                temp = str(array1[i]) + operador + str(array2[i])
                resultado.append( eval(temp) )
                i += 1
            # end while
            
            return 'Operación ' + operador + ' ==> ' + str(resultado)
        else:
            return 'ERROR - Operación Inválida'
        # end if
# end def

# ---------------
#* TEST
print('\nTEST')
# ---------------

arr1 = [2, 5, 6, 2, 3]
arr2 = [3, 4, 2, 5, 6]
arr3 = [3, 4, 2, 5, 6, 2]

print( operar_arrays(arr1, arr2, '+') )
print( operar_arrays(arr1, arr2, '-') )
print( operar_arrays(arr1, arr2, '*') )
print( operar_arrays(arr1, arr2, '/') )
print( operar_arrays(arr1, arr2, '**') )
print( operar_arrays(arr1, arr2, '%') )
print( operar_arrays(arr1, arr2, '$') )
print( operar_arrays(arr1, arr3, '+') )