# ==============================================================
# sort / map / filter / reduce
# => map en Python

# https://www.w3schools.com/python/ref_func_map.asp

# Aplicando map en colecciones avanzadas
# - como se explicó anteriormente, tenemos colecciones más reales
# - de las que se encuentran en la práctica

# ? RECORDAR:

#       * Listas de Listas (Listas 2D)
#       * Listas de Tuplas
#       * Listas de Diccionarios

# ? TIP: la función la podemos definir con lambda
# - de esta manera incluso podemos definir el tipo de colección
# - que map nos va a devolver
# - recordar que lambda se define en una sola línea
# - si la expresión es muy complicada podemos siempre optar
# - por nuestras funciones normales

# ! PARTE 1
# => aplicando map a una lista de TUPLAS
# ==============================================================


#? Map + Lista de TUPLAS
print('\nMap + Lista de TUPLAS')

tienda_juegos = [
    ('PlayStation 5', 580.95),
    ('XBox', 495.58),
    ('PSVita', 150.69),
    ('PlayStation 2', 110.25),
    ('Nintendo Switch', 350.99),
]

# EJERCICIO
# - la tienda aplica un 15% de descuento a todos los productos
# *      nuevo_precio = precio - 0.15 * precio = 0.85 * precio
# - aplicar map para devolver una nueva lista de consolas con el descuento en el precio


# ---------------------------
# => fijando función lambda
# ---------------------------
# - como retorno de lambda fijamos una tupla
# - básicamente decimos que la primera columna nos deje tal y como está
# - y la segunda que se refiere al precio, lo modificamos
# - esto lo hacemos con el acceso a índice

descuento_15 = lambda valor : (valor[0], valor[1] * 0.85)


# -------------------
# => aplicando map
# -------------------
precios_descuento_map = map(descuento_15, tienda_juegos)
precios_descuento = list(precios_descuento_map)

print('\nPrecios con descuento del 15%:')
for x in precios_descuento:
    print(x)
# end for


# -------------------------------
# => mejora: fijar 2 decimales
# -------------------------------
descuento_15_2d = lambda valor : ( valor[0] , float('{:.2f}'.format(valor[1] * 0.85)) )

precios_descuento_map = map(descuento_15_2d, tienda_juegos)
precios_descuento = list(precios_descuento_map)

print('\nPrecios con descuento del 15% - versión mejorada:')
for x in precios_descuento:
    print(x)
# end for


# -------------------------------------------------------------------------------
# => OJO: la función lambda nos puede cambiar la estructura de datos resultante
# -------------------------------------------------------------------------------
# - por ejemplo en lugar de fijar una tupla resultante
# - podemos fijar una lista

descuento_15_2d_lista = lambda valor : [ valor[0] , float('{:.2f}'.format(valor[1] * 0.85)) ]

precios_descuento_map = map(descuento_15_2d_lista, tienda_juegos)
precios_descuento = list(precios_descuento_map)

print('\nCambiando estructura de datos con map:')
for x in precios_descuento:
    print(x)
# end for
