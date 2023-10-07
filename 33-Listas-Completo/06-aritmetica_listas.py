# ======================================================
# Aritmética con listas numéricas

#! OJO: existen librerías especializadas para esto
# ej: numpy

# - Sin embargo, con lo aprendido hasta el momento
# - Podemos emular estas operaciones
# - y trabajar arrays numéricos (listas con números)
# ======================================================

array_1 = [10, 20, 30, 40, 50]
array_2 = [50, 70, 10, 20, 30]

#? 1) concatenación y producto funcionan de otra manera
print('\n1) concatenación y producto funcionan de otra manera')

resultado_1 = array_1 + array_2
resultado_2 = 2 * array_1

print(resultado_1)
print(resultado_2)


#? 2) Suma de Listas Numéricas
print('\n2) Suma de Listas Numéricas')
# - para que funcione, ambas listas deben tener el mismo tamaño

resultado = []

if len(array_1) != len(array_2):
    print('ERROR - Ambos array tienen distinto tamaño')
else:
    i = 0
    while i < len(array_1):
        resultado.append( array_1[i] + array_2[i] )
        i += 1
    # end while
# end if

print('SUMA =', resultado)


#? 3) Resto de Operaciones para Listas Numéricas
print('\n3) Resto de Operaciones para Listas Numéricas')
# - Básicamente el resto de operaciones sería igual
# - Al código expuesto arriba
# - Cambiaría la operación
# - Pero, podríamos utilizar lo aprendido con eval()

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

# => mostrar los resultados en función a la operación
# - podemos utilizar un condicional
# - por ejemplo el match-case

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

# => podemos mejorar más este código
# - lo veremos luego en el tema de funciones
# - cuando podamos crear nuestras propias funciones en python