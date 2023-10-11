# =============================================
# Ejercicio
# - lista de compras
# - agregar / eliminar compras de una lista
# - la lista de compras debe ser un set
# =============================================

lista_compras = {
    'Banana',
    'Arroz',
    'Leche',
    'Aceite',
    'Galletas',
    'Vino',
    'Café',
    'Papas'
}

agregar = ['detergente', 'Jabón']
eliminar = ['Vino', 'Galletas']

print('Lista de Compras:\n')
print( lista_compras )

# Recordar => Recorrido de Set
for compra in lista_compras:
    print(compra)
# end for


# Agregar compras
print()

for compra in agregar:
    lista_compras.add(compra)
# end for
print( lista_compras )


# Eliminar compras
print()
for compra in eliminar:
    lista_compras.discard(compra)
# end for
print( lista_compras )