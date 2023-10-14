# ============================================================
# Aclaración del funcionamiento de shuffle

# - Mutabilidad de lista
# - Prevención de mutabilidad con reasignación de variable
# ============================================================

import random

#? 1) La mutabilidad afecta a la variable y las variables que la contengan
print('\n1) La mutabilidad afecta a la variable y las variables que la contengan')
# - una lista es mutable
# - sigue siendo mutable así esté contenida dentro de otra variable

lista_1 = [1,2,3]
lista_2 = ['a','b','c']

resultado = []
resultado.append(lista_1)
resultado.append(lista_2)

print(resultado)

lista_1[0] = 'Z'

print(resultado)



#? 2) De igual manera pasa con shuffle
print('\n2) De igual manera pasa con shuffle')

lista = [1,2,3]

resultado = []

resultado.append(lista)
print(resultado)

lista_copy = lista.copy()
random.shuffle( lista_copy )

resultado.append(lista_copy)
print(resultado)

random.shuffle( lista_copy )

resultado.append(lista_copy)
print(resultado) # la segunda y la tercera variable son las mismas

# => ambas son las mismas!
# - podemos prevenir esto reasignando la variable
# - y luego haciendo shuffle



#? 3) Evitar mutabilidad con reasignación
print('\n3) Evitar mutabilidad con reasignación')

lista = [1,2,3]

resultado = []

resultado.append(lista)
print(resultado)

#! => 2 pasos a hacer
lista_copy = lista.copy()
random.shuffle( lista_copy )

resultado.append(lista_copy)
print(resultado)

#! => 2 pasos a hacer
lista_copy = lista.copy()
random.shuffle( lista_copy )

resultado.append(lista_copy)
print(resultado)