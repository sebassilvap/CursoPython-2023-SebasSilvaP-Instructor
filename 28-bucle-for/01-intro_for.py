# =====================================================================================================
# Bucle for

# - se lo utiliza para iterar una SECUENCIA
# - En Python una secuencia de datos puede ser:

##  1) string
##  2) lista - list
##  3) rango - range
#!  4) tupla - tuple
#!  5) diccionario - dictionary
#!  6) conjunto - set

# - estos 3 últimos no los hemos visto todavía
# - pero los hemos mencionado desde un inicio


'''
Por DEFAULT Python tiene los siguientes tipos de datos que vienen internamente al momento de instalar

----------------------------------------------------
Text Type:	     |    str
Numeric Types:   |    int, float, complex
Sequence Types:  |    list, tuple, range
Mapping Type:	 |    dict
Set Types:	     |    set, frozenset
Boolean Type:	 |    bool
Binary Types:	 |    bytes, bytearray, memoryview
None Type:	     |    NoneType
----------------------------------------------------

https://www.w3schools.com/python/python_datatypes.asp
'''

# - por el momento vamos a ver su uso y aplicación en las sencuencias que ya conocemos

#* ESTRUCTURA BÁSICA
'''
for elemento in secuencia:
    print(elemento)
'''

# - elemento => variable de iteración / puede tener cualquier nombre

# =====================================================================================================


#? 1) for + string
print('\n1) for + string')

cadena = 'ecuador'

print( cadena, type(cadena) )

for letra in cadena:
    print(letra)
# end for



#? 2) for + string + index
print('\n2) for + string + index')

# - podemos usar un contador externo que interactúe con el for como índice

cadena = 'ecuador'
index = 0

for letra in cadena:
    print('cadena[' + str(index) + '] =', letra)
    index += 1
# end for

# => es decir podríamos iterar de 2 maneras
print()

index = 0

for letra in cadena:
    print(cadena[index], '--', letra)
    index += 1    
# end for



#? 3) Uso más común => for + range
print('\n3) Uso más común => for + range')

# - iterar números del 1 al 10

for x in range(1,11):
    print('Número =', x)
# end for



#? 4) Repaso: range con salto
print('\n4) Repaso: range con salto')

# - contar del 1 al 20 en saltos de 3

for x in range(1,21,3):
    print('Número =', x)
# end for



#? 5) for + listas
print('\n5) for + listas')

heroes = ['superman', 'goku', 'batman', 'spiderman']

for heroe in heroes:
    print(heroe)
# end for

#* NOTA:
# - muchas veces se suele usar el singular de la variable a recorrer
# - como una recomendación de legibilidad de nuestro código
# - sin embargo podemos usar cualquier nombre



#? 6) for + listas + index
print('\n6) for + listas + index')

# - igualmente podemos valernos de un contador externo que funcione como index
# - de esta manera podemos complementar la iteración de una secuancia

index = 0
heroes = ['superman', 'goku', 'batman', 'spiderman']

for heroe in heroes:
    print('heroe[' + str(index) + '] =', heroe)
    index += 1
# end for

# => al igual que el string, entonces podemos iterar de 2 maneras:
print()

index = 0

for heroe in heroes:
    print(heroes[index], '--', heroe)
    index += 1
# end for



#? 8) range vs. list
print('\n8) range vs. list')

# - en python 2 el range se traducía a una lista
# - range(5) = [0,1,2,3,4]
# - el range no existe en memoria, se interpreta cuando la instrucción se ejecuta
# - si se creara en memoria => ocuparía espacio
# - por tanto es más óptimo utilizar range para la iteración