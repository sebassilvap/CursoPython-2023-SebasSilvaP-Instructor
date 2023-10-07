# ===============================================
# Función enumerate

# - una manera sencilla de devolver el índice
# - de los elementos de una lista
# - en lugar de crear un contador externo
# ===============================================

#? 1) bucle for sin enumerate
print('\n1) bucle for sin enumerate')

# - normalmente si deseamos el índice de los elementos que recorremos
# - al utilizar for tenemos que crear un contador extra
# - ej:

lista = [100, 'manzana', True, -8.5, 'python']

for elemento in lista:
    print(elemento)
# end for

# => si deseamos contar los elementos
print()

index = 0

for elemento in lista:
    print('Index =', index, '|', lista[index], '|', elemento)
    index += 1 # pero necesitamos el incremento
# end for


#? 2) Utilizando enumerate
print('\n2) Utilizando enumerate')

lista = [100, 'manzana', True, -8.5, 'python']

for i, elemento in enumerate(lista):
    print('Elemento', i, '=', elemento)
# end for