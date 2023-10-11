# ====================================
# Concatenación y Producto en Tuplas

# - concatenación => +
# - producto => *
# ====================================

#? 1) Concatenación en Tuplas => +
print('\n1) Concatenación en Tuplas => +')

tupla_1 = (10, 'A', 5.5)
tupla_2 = tuple((50, 'M', -8.8))

tupla_resultado = tupla_1 + tupla_2

print(tupla_1, len(tupla_1))
print(tupla_2, len(tupla_2))
print(tupla_resultado, len(tupla_resultado))


#? 2) Producto en Tuplas => *
print('\n2) Producto en Tuplas => *')
# - se repite el número de veces indicado

tupla = (10, 'A', 5.5)

resultado = tupla * 3

print(tupla, len(tupla))
print(resultado, len(resultado))

#resultado = tupla * 'A'
#! TypeError: can't multiply sequence by non-int of type 'str'