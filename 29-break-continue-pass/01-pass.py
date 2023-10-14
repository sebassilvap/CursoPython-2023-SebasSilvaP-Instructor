# ===============================================================
# break-continue-pass

# Son sentencias para el control de un bucle
# pass => también tiene otras utilidades además de los bucles

#* pass
# => se lo utiliza como un placeholder
# => para definir algo y trabajar en eso luego

#* break
# => interrumpimos / terminamos un bucle de manera total

#* continue
# => para saltarnos a la siguiente iteración de un bucle

# ===============================================================


#? 1) pass => definir una firma y trabajar en eso luego
print('\n1) pass => definir una firma y trabajar en eso luego')
# - escribo su definición pero voy a trabajar luego
# - si ejecuto, no pasa nada, ni error
# - se utiliza en if, funciones*, clases* (temas que veremos luego)

num = 5

if num > 3:
    pass

#! => pero cuidado
# - si lo utilizamos con un bucle while
# - quedará atrapado en un bucle infinito
'''
while True:
    pass
'''

# => en un bucle for
# - la iteración se da
# - pero no pasa nada
# - si se trata de una iteración muy grande
# - se va a consumir memoria
# - no sería conveniente utilizar pass en bucles

lista = [1,2,3,4,5]

for elemento in lista:
    pass
# end for


#? 2) Dentro de un bucle => pass funcionaría como un continue
print('\n2) Dentro de un bucle => pass funcionaría como un continue\n')

# EJ: imprimir solo los múltiplos de 5 

print('\nUtilizando pass:')

lista_pares = [] # lista vacía

for i in range(1,101):
    if i % 5 == 0:
        lista_pares.append(i)
    else:
        pass
    # end if
# end for

print(lista_pares)

print('\nUtilizando continue:')

lista_pares = []

for i in range(1,101):
    if i % 5 == 0:
        lista_pares.append(i)
    else:
        continue
    # end if
# end for

print(lista_pares)