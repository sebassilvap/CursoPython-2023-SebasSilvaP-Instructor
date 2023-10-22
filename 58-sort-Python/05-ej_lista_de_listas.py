# ===========================================================
# Ejercicio
# En casos reales y prácticos tenemos lo siguiente:

#       * Listas de Listas (Listas 2D)
#       * Listas de Tuplas
#       * Listas de Diccionarios

# PERO:
# - Básicamente, lo que aprendimos en la lección anterior
# - sobre la clasificación de diccionarios
# - utilizando key y la función lambda
# - se aplica en estos casos para permitirnos el orden
# - en el caso de diccionarios, es un poco especial
# - porque no podemos acceder con indexing normal
# - por lo cual como ya aprendimos podemos trasnformar
# - a lista de tuplas y luego a diccionario con dict()
# ===========================================================


#? EJERCICIO - Lista de Listas
print('\nEJERCICIO - Lista de Listas\n')

# -------------------------------------------------
# - en la siguiente colección de datos
# - presentar 3 ordenamientos en nuevas variables
#   * orden por ID
#   * orden por valor de x
#   * orden por valor de y
# -------------------------------------------------


#    ID ,  x   , y
mediciones = [
    ['A', 15.7, 102],
    ['B', 19.5, 90],
    ['C', 20.2, 108],
    ['D', 17.4, 99],
    ['E', 12.2, 105],
]

# => parámetros lambda para ordenamiento
por_id = lambda id : id[0] # para ordenamiento por id
por_x = lambda x : x[1] # por ordenamiento en valor x
por_y = lambda y : y[2] # por ordenamiento en valor y

# => ordenamiento con sorted()
mediciones_sort_id = sorted(
    mediciones,
    key=por_id,
    reverse=True
)

mediciones_sort_x = sorted(
    mediciones,
    key=por_x,
)

mediciones_sort_y = sorted(
    mediciones,
    key=por_y,
)

# => función para imprimir datos en consola
def print_datos(lista):
    for sublista in lista:
        print(sublista)
    # end for
# end def

# TEST
print_datos(mediciones_sort_id)
print()
print_datos(mediciones_sort_x)
print()
print_datos(mediciones_sort_y)