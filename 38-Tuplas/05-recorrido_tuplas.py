# ==========================================
# Recorrido de Tuplas

# - los mismos fundamentos que con listas
# ==========================================


# ----------------------------------------------
# EJ:
tupla = ('A', 'B', -100, 500, True, -8.8, None)
# ----------------------------------------------

#? 1) Recorrido con for
print('\n1) Recorrido con for')

for elemento in tupla:
    print(elemento)
# end for


#? 2) for + contador externo
print('\n2) for + contador externo')

counter = 0

for elemento in tupla:
    print('tupla[', counter, '] =', tupla[counter], '|', elemento)
    counter += 1
# end for


#? 3) for + enumerate
print('\n3) for + enumerate')

for index, elemento in enumerate(tupla):
    print('Elemento Index #', index, '=', elemento)
# end for


#? 4) Recorrido con while
print('\n4) Recorrido con while')

index = 0

while index < len(tupla):
    print(tupla[index])
    index += 1
# end while

