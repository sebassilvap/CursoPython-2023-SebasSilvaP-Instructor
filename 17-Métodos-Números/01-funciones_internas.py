# =======================================================================
# Funciones internas para trabajar con números

# - Python ofrece por defecto funciones internas
# - Para poder trabajar y dar formato a números
# - Podemos utilizarlas sin necesidad de importar la librería math (*)
# - (*) en la siguiente lección veremos la librería math
# =======================================================================

#? 1) round() => lleva un número decimal a su inmediato superior
print('\n1) round()')

constante_pi = 3.14159

print(constante_pi) # 3.14159
print( round(constante_pi) ) # 3

num_1 = 3.2
num_2 = 3.4999
num_3 = 3.5
num_4 = 3.8
num_5 = 3.999999

# => aplicando round()
print( num_1 , ' =>' , round(num_1) )
print( num_2 , ' =>' , round(num_2) )
print( num_3 , ' =>' , round(num_3) )
print( num_4 , ' =>' , round(num_4) )
print( num_5 , ' =>' , round(num_5) )


#? 2) abs() => valor absoluto de un número
print('\n2) abs()')

num_1 = 10
num_2 = -30
num_3 = -5.555
num_4 = 4.96

# => aplicando abs()
print( num_1 , ' =>' , abs(num_1) )
print( num_2 , ' =>' , abs(num_2) )
print( num_3 , ' =>' , abs(num_3) )
print( num_4 , ' =>' , abs(num_4) )


#? 3) sum() => devuelve la suma de una lista
print('\n3) sum()')

lista_1 = [10,20,30,40]
print(lista_1 , sum(lista_1))

# => existe un problema con esta función:
lista_2 = [0.9999999, 1, 2, 3]
print(sum(lista_2))