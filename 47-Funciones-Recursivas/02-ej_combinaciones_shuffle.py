# =======================================================
# Ejercicio

# - utilizar la librería random y su método shuffle
# - dada una lista de elementos
# - crear todas las combinaciones posibles

# EJ
# ['A', 'B', 'C']

# => todas las combinaciones posibles serían
#?  1) ['A', 'B', 'C']  => la lista original
#?  2) ['B', 'A', 'C']
#?  3) ['A', 'C', 'B']
#?  4) ['C', 'A', 'B']
#?  5) ['C', 'B', 'A']
#?  6) ['B', 'C', 'A']

# - es decir, de una lista de 3 elementos
# - tenemos 6 combinaciones posibles
# - esto obedece a una regla matemática

#* N combinaciones = (N Elementos) !

# - el operador factorial es el siguiente

# EJ
# 2! = 2 x 1 = 2
# 3! = 3 x 2 x 1 = 6
# 4! = 4 x 3 x 2 x 1 = 24

# - Crear 2 funciones:

# * generar_combinaciones(lista)
# => que reciba una lista
# => y retorne una lista con las combinaciones
# => (lista de listas)

# * mostrar_combinaciones(lista)
# => que reciba una lista de elementos
# => y muestre en la consola todas las combinaciones
# => numeradas
# =======================================================


# -------------------------
# importaciones librerías
# -------------------------
import random


# ------------------------
# definición de funciones
# ------------------------

#? 1) función => factorial(numero)

# - utilizando función normal
'''
def factorial(num):
    resultado = 1
    i = 1
    
    while i <= num:
        resultado *= i
        i += 1
    # end while
    
    return resultado
# end def

# TEST
#print( factorial(3) )
'''

# - utilizando función recursiva
def factorial(num):
    if num >= 1:
        return num * factorial(num - 1)
    else:
        return 1
# end def

# TEST
#print( factorial(3) )



#? 2) función => generar_combinaciones(lista)

def generar_combinaciones(lista):
    combinaciones = [lista] # la lista de parámetro es la 1era combinación posible
        
    # len máximo de las combinaciones
    len_max = factorial( len(lista) )
    
    # generar combinaciones
    while len(combinaciones) < len_max:
        
        lista_copia = lista.copy() # cada iteración volvemos a crear la variable, de esa manera la hacemos independiente en cada iteración
        random.shuffle(lista_copia)
        
        if lista_copia not in combinaciones:
            combinaciones.append(lista_copia)
        
    # end while
    
    return combinaciones
# end def

# TEST
'''
lista_ej = ['A', 'B', 'C']
combinaciones = generar_combinaciones(lista_ej)
print(combinaciones)
'''


#? 3) función => mostrar_combinaciones(numero)

def mostrar_combinaciones(lista):
    print('\n\nCombinaciones para la lista:')
    print('*****', lista, '*****\n')
    combinaciones = generar_combinaciones(lista)
    
    for index, combinacion in enumerate(combinaciones):
        print('Opción', index + 1, '=>', combinacion)
    # end for
# end def

# ------------
# test final
# ------------

lista_1 = ['A', 'B', 'C']
lista_2 = ['A', 'B', 'C', 'D', 'E', 'F']

mostrar_combinaciones(lista_1)
mostrar_combinaciones(lista_2)