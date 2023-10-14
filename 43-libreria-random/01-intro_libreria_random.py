# =====================================================
# Librería Random

# - Una de las más importantes que tiene Python
# - Nos permite generar elementos aleatorios
# - Para usarlos de varias maneras
# - Una gran aplicación es en los juegos

# https://www.w3schools.com/python/module_random.asp
# =====================================================


#? 1) Importación de librería
print('\n1) Importación de librería')

import random

# - RECORDAR: la importación siempre va en la primera parte del código
# - una vez importado, podemos hacer uso de los métodos que ofrece
# - no vamos a ver todos
# - pero si los más relevantes
# - en la página de arriba se encuentran detallados todos los métodos de esta librería



#? 2) Método .random()
print('\n2) Método .random()')
# - genera un número aleatorio entre 0 y 1
# - sin incluir el 1

x = random.random()
print(x)
# => cada vez que ejecutamos el script, tenemos un número diferente



#? 3) Truco para tener un número entero aleatorio
print('\n3) Truco para tener un número entero aleatorio')
# - para generar un número ENTERO aleatorio entre 0 y X
# - podemos utilizar un pequeño truco


# --------------------------------------------------------
# 3.1) Ejemplo: Número Aleatorio entre 0 y 10
print('\n3.1) Ejemplo: Número Aleatorio entre 0 y 10\n')
# --------------------------------------------------------

x = round( random.random() * 10 )
print(x)


# ----------------------------------------------------------------------
# 3.2) Ejemplo: Lista de 100 números aleatorios del 1 al 100
print('\n3.2) Ejemplo: Lista de 100 números aleatorios del 1 al 100\n')
# ----------------------------------------------------------------------

lista_aleatoria = []

for i in range(1,101):
    lista_aleatoria.append( round( random.random() * 100 ) )
# end for

print(lista_aleatoria)



#? 4) Método .randint(x,y)
print('\n4) Método .randint(x,y)')
# - para generar un número aleatorio en un rango entre x, y
# - el número generado es ENTERO

# -------------------------------------------------------------
# 4.1) Ejemplo: Entero Aleatorio entre 300 y 800
print('\n4.1) Ejemplo: Enteros Aleatorios entre 300 y 800\n')
# -------------------------------------------------------------

lista_aleatoria = []

for i in range(1,21):
    lista_aleatoria.append( random.randint(300,800) )
# end for

print(lista_aleatoria)



#? 5) Método .choice(lista)
print('\n5) Método .choice(lista)')
# - devuelve un elemento aleatorio
# - de una lista

nombres = ['Daniel', 'Ana', 'Carlos', 'Sebas', 'Xime', 'Beto']

print( nombres )
print( random.choice(nombres) )
print( random.choice(nombres) )



#? 6) Método .shuffle(lista)
print('\n6) Método .shuffle(lista)')
# ! IMPORTANTE
# - me "baraja" una lista
# - pone los elementos de una lista al azar
# - OJO: modifica la lista original

cartas = ['A', 'B', 'X', 'Y', 'Z']
print(cartas)

# => aplicando shuffle
random.shuffle(cartas)
print(cartas)

random.shuffle(cartas)
print(cartas)



#? 7) Método .shuffle(lista) sin afectar lista original
print('\n7) Método .shuffle(lista) sin afectar lista original')
# - como hemos visto antes
# - una manera de solventar este problema
# - es creando una copia de la lista original
# - con el método .copy()
# - y a esa copia podemos usar el random.shuffle(lista_copia)

cartas = ['A', 'B', 'X', 'Y', 'Z']

cartas_copy = cartas.copy()
random.shuffle(cartas_copy)

print('\nORIGINAL =', cartas)
print('SHUFFLE 1 =', cartas_copy)

random.shuffle(cartas_copy)

print('SHUFFLE 2 =', cartas_copy)