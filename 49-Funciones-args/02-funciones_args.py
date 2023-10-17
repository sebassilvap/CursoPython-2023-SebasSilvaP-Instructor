# =================================================================
# Funciones con Argumentos Arbitrarios
# (Arbitrary Arguments / *args)

# - para crear una función
# - que acepte un número indefinido de parámetros
# - todos los parámetros que pongamos se guardan como una tupla

#   https://www.w3schools.com/python/python_functions.asp
# =================================================================


#? 1) ¿Qué retorna *args?
print('\n1) ¿Qué retorna *args?')

def investigar_1(*args):
    return args
# end def

def investigar_2(*args):
    return type(args)
# end def

print( investigar_1(1,2,3,4,5) )
print( investigar_2(1,2,3,4,5) )

# ----------------------------------------------------
# - me duevelve una tupla
# - con todos los elementos que pase como parámetros
# ----------------------------------------------------



#? 2) La palabra *args es un estándar, puede ser cualquier otro nombre
print('\n2) La palabra *args es un estándar, puede ser cualquier otro nombre')

def mostrar_args(*elementos):
    print(elementos, type(elementos))
# end def

mostrar_args(1,2,3)
mostrar_args('a', 2, True, -100.5)



#? 3) Ejemplo: sumatoria de números
print('\n3) Ejemplo: sumatoria de números')

def sumatoria(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    # end for
    return resultado
# end def

# TEST
print( sumatoria(1,2,3,4,5) )



#? 4) Ejemplo: numerar estudiantes
print('\n4) Ejemplo: numerar estudiantes')

def numerar_estudiantes(*estudiantes):
    for index, estudiante in enumerate(estudiantes):
        print( index+1, '--', estudiante )
    # end for
# end def

# TEST
numerar_estudiantes('Sebas', 'Andrea', 'Valeria', 'Carlos')



#? 5) Ejemplo: Sumar 100 a un indeterminado número de parámetros
print('\n5) Ejemplo: Sumar 100 a un indeterminado número de parámetros')
# - por defecto no lo vamos a poder hacer
# - ¿Por qué?
# - RECORDAR: la tupla es INMUTABLE


tupla = (1,2,3)
#tupla[0] = 5 #! TypeError: 'tuple' object does not support item assignment


# => truco para modificar tupla
# - haciendo casting a list
# - modificar
# - y volver a hacer casting a tupla

lista = list(tupla)
lista[0] = 5

tupla = tuple(lista)
print(tupla)


# => ahora veamos el error que se produciría
# - al intentar cambiar algún valor de *args

def aumentar_cien(*valores):
    i = 0
    while i < len(valores):
        valores[i] += 100   
        i += 1 
    # end while
    
    return valores
# end def        
        
#aumentar_cien(1,2,3)
#! TypeError: 'tuple' object does not support item assignment


# => corrigiendo el valor con el truco de tupla a lista

def aumentar_cien(*valores):
    # reasignación y casting en 1 línea
    valores = list(valores)
    
    i = 0
    while i < len(valores):
        valores[i] += 100
        i += 1 
    # end while
    
    return tuple(valores)
# end def  

# TEST
resultado = aumentar_cien(1,2,3)
print( resultado, type(resultado) )