# =============================================
# Recorrido de Listas

# - es una de las aplicaciones de los bucles
# - especialmente la del bucle for
# - existen varias maneras de hacerlo
# =============================================

# ----------------------------------------------------------------
# EJ:
lista = [100, 200, 300, 'A', 'B', 'C', True, -10.5, 50.5, None]
# ----------------------------------------------------------------

#? 1) Recorrido con for
print('\n1) Recorrido con for')

for elemento in lista:
    print(elemento)
# end for


#? 2) for + contador externo
print('\n2) for + contador externo')

counter = 0

for elemento in lista:
    print('lista[', counter, '] =', lista[counter], '|', elemento)
    counter += 1
# end for


#? 3) for + enumerate
print('\n3) for + enumerate')

for index, elemento in enumerate(lista):
    print('Elemento Index #', index, '=', elemento)
# end for


#? 4) Recorrido con while
print('\n4) Recorrido con while')

index = 0

while index < len(lista):
    print(lista[index])
    index += 1
# end while
