# =============================================================================
# sort / map / filter / reduce
# => reduce en Python

# https://thepythonguru.com/python-builtin-functions/reduce/

# !  Reduce sin valor inicial
# *      reduce(función , elemento_iterable)

# !  Reduce sin valor inicial
# *      reduce(función , elemento_iterable, valor_inicial)


# ! Aplicación en lista de TUPLAS | PARTE 1
# - vamos a ver en primer lugar las generalidades de aplicar reduce
# - a una lista de tuplas
# - los errores que se presentan, y como solventarlos
# - luego haremos este mismo ejercicio
# - pero con las bases aprendidas aquí
# =============================================================================


#? reduce + lista de TUPLAS | Explicación & Generalidades
print('\nreduce + lista de TUPLAS | Explicación & Generalidades')

#     0     ,     1     ,    2   ,        3
#  artículo , categoría , unidad , precio unitario
compras = [
    ('camiseta', 'ropa', 1, 15.00),
    ('pantalón', 'ropa', 3, 25.99),
    ('licuadora', 'electrodomésticos', 1, 79.50),
    ('martillo', 'herramientas', 2, 18.65),
    ('microondas', 'electrodomésticos', 1, 186.45),
    ('destornillador', 'herramientas', 3, 6.99),
    ('par de zapatos', 'ropa', 1, 45.35),
    ('corbata', 'ropa', 3, 12.55),
    ('taladro', 'herramientas', 1, 125.69),
]


#? 1) Importar en 1er lugar functools
print('\n1) Importar en 1er lugar functools')
import functools



#? 2) ERROR - Aplicando Reduce directamente
print('\n2) ERROR - Aplicando Reduce directamente')
# - lastimosamente de esta manera nos da error
# - para demostrar este error voy a tratar de sumar todos los precios unitarios
# - reduce => funciona perfectamente en una lista / tupla 1D

def test_error(lista_tuplas):
    suma = functools.reduce(
        lambda x,y : x[3] + y[3],
        lista_tuplas
    )
    
    return suma
# end def

#print( test_error(compras) )
#! TypeError: 'float' object is not subscriptable



#? 3) Solución Larga: Map + Reduce => por separado
print('\n3) Solución Larga: Map + Reduce => por separado')
# - vamos a hacer primero map para obtener un iterable con la cantidad * precio_unitario
# - luego el casting de map a lista
# - y el reduce vamos a aplicar a esta lista resultante

subtotales_map = map(
    lambda x : x[2] * x[3],
    compras
)

print(subtotales_map) # ej: <map object at 0x00000205DBEBB490>

subtotales = list(subtotales_map) # una vez hecho esto recordar, map queda vacío!!
print(subtotales)

precio_total = functools.reduce(
    lambda x,y : x + y,
    subtotales
)

print('Precio Total =', precio_total)



#? 4) Solución Corta y Elegante => Map dentro de Reduce
print('\n4) Solución Corta y Elegante => Map dentro de Reduce')

# --------------------------------------------
# 4.1) Con casting de map a lista
print('\n4.1) Con casting de map a lista\n')
# --------------------------------------------
# - básicamente lo que hicimos arriba
# - pero en una sola instrucción

precio_total = functools.reduce(
    lambda x,y : x + y,
    list(map(
        lambda x : x[2] * x[3],
        compras
    ))
)

print(precio_total)


# --------------------------------------------
# 4.2) Sin casting de map a lista
print('\n4.2) Sin casting de map a lista\n')
# --------------------------------------------
# - el casting a lista para el map interno
# - NO es necesario
# - reduce me recibe una función y un iterable
# - no necesariamente debe ser SIEMPRE lista
# - el map es un objeto/elemento iterable también


precio_total = functools.reduce(
    lambda x,y : x + y,
    
    map(
        lambda x : x[2] * x[3],
        compras
    )
)

print(precio_total)



#? 5) Solución IDEAL: función con reduce + map
print('\n5) Solución IDEAL: función con reduce + map')

def calcular_total(lista_compras):
    total = functools.reduce(
        lambda x,y : x + y,
        
        map(
            lambda z : z[2] * z[3],
            lista_compras
        )
    )
    
    # => acortamos a 2 decimales
    total = float(f'{total:.2f}')
    
    return total
# end def

print( 'Total a pagar = {} USD'.format(calcular_total(compras)) )