# ==================================================================
# Mutabilidad e Inmutabilidad

# - En programación muchas veces veremos el concepto
# - de elementos mutables
# - y elementos inmutables

#* Mutable   => que no se puede modificar / cambiar
#* Inmutable => que se pueden modificar

# - En Python hay algunos elementos que cumplen esta característica
# - Veremos solo algunos ejemplos básicos para entender el concepto
# ==================================================================

#? 1) Listas - Elementos Mutables
print('\n1) Listas - Elementos Mutables')

lista_letras = ['a', 'b', 'c', 'd', 'e', 'f']
print(lista_letras)

# => con acceso a index, yo puedo modificar los elementos
lista_letras[1] = 'ZZZ'
print(lista_letras)


#? 2) String - Elemento Inmutable
print('\n2) String - Elemento Inmutable')

string = 'python'
print( string )
print( string[0] )
print( string[1] )
print( string[2] )

#string[-1] = 'M'
#! TypeError: 'str' object does not support item assignment

# => Reasignar una variable no es modificarla
# la variable original se borra y se crea otra

string = 'pythoM'
print( string )

#string[0] = 'A' #! TypeError