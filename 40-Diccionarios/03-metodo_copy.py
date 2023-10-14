# =================================
# Método .copy() en Diccionarios

# - al igual que en listas, sets
# - permite una forma segura
# - de crear un diccionario
# - a partir de otro diccionario
# =================================


#? 1) Problema General de Creación a partir de otra Variable
print('\n1) Problema General de Creación a partir de otra Variable')

lista_1 = [1,2,3]
set_1 = { 'a', 'b', 'c' }
dict_1 = {
    10 : 'python',
    20 : 'java'
}

# => Creando a partir de una variable
# - practicamos la asignación múltiple!

lista_2, set_2, dict_2 = lista_1, set_1, dict_1

print( lista_1, '|', lista_2 )
print( set_1, '|', set_2 )
print( dict_1, '|', dict_2 )

# => modificando
# - ya sea en la variable original
# - o en la nueva
lista_1.append('S')
set_2.add(100)
dict_1[20] = 'C++'

print()
print( lista_1, '|', lista_2 )
print( set_1, '|', set_2 )
print( dict_1, '|', dict_2 )



#? 2) Utilizando .copy()
print('\n2) Utilizando .copy()')

# => variables originales
lista_1 = [1,2,3]
set_1 = { 'a', 'b', 'c' }
dict_1 = {
    10 : 'python',
    20 : 'java'
}

# => asignando copia de manera múltiple
lista_2, set_2, dict_2 = lista_1.copy(), set_1.copy(), dict_1.copy()

print( lista_1, '|', lista_2 )
print( set_1, '|', set_2 )
print( dict_1, '|', dict_2 )

# => modificando
# - ahora las modificaciones
# - son donde las he realizado
lista_1.append('S')
set_2.add(100)
dict_1[20] = 'C++'

print()
print( lista_1, '|', lista_2 )
print( set_1, '|', set_2 )
print( dict_1, '|', dict_2 )