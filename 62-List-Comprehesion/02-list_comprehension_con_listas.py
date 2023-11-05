# ================================================================================
# Python - List Comprehension
# (Comprensión / Entendimiento de Listas)

# - creando listas a partir de otros iterables

#*    A) lista = [ expresión + bucle FOR en un iterable ]
#*    B) lista = [ expresión + bucle FOR en un iterable + condicional IF ]
#*    C) lista = [ expresión + condicional IF/ELSE + bucle FOR en un ITERABLE ]

# https://www.w3schools.com/python/python_lists_comprehension.asp
# ================================================================================

#? A) lista = [ expresión + bucle FOR en un iterable ]
print('\nA) lista = [ expresión + bucle FOR en un iterable ]')

# y = 2*x^2 + 5*x - 10

valores_x = [-10.5, 2.8, 6.9, -2.3, 3.66]

valores_y = [ 2*(x**2) + 5*x - 10 for x in valores_x ]

print('valores x =', valores_x)
print('valores y =', valores_y)

# => utilizando una función para la expresión

def funcion_y(x):
    return 2*(x**2) + 5*x - 10

valores_y = [funcion_y(x) for x in valores_x]

print()
print('valores x =', valores_x)
print('valores y =', valores_y)



#? B) lista = [ expresión + bucle FOR en un iterable + condicional IF ]
print('\nB) lista = [ expresión + bucle FOR en un iterable + condicional IF ]')

# y = x * 0.75 | x >= 50

valores_x = [15.5, 80.6, 50.9, 25.7, 18.4, 75.3]

valores_y = [ x*0.75 for x in valores_x if x >= 50 ]

print('valores x =', valores_x)
print('valores y =', valores_y)



#? C) lista = [ expresión + condicional IF/ELSE + bucle FOR en un ITERABLE ]
print('\nC) lista = [ expresión + condicional IF/ELSE + bucle FOR en un ITERABLE ]')

# y = x * 0.75 | x >= 50
# y = x * 0.6  | x < 50

valores_x = [15.5, 80.6, 50.9, 25.7, 18.4, 75.3]

valores_y = [ x*0.75 if x >= 50 else x*0.6 for x in valores_x ]

print('valores x =', valores_x)
print('valores y =', valores_y)