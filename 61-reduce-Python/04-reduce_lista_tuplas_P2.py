# =============================================================================
# sort / map / filter / reduce
# => reduce en Python

# https://thepythonguru.com/python-builtin-functions/reduce/

# !  Reduce sin valor inicial
# *      reduce(función , elemento_iterable)

# !  Reduce sin valor inicial
# *      reduce(función , elemento_iterable, valor_inicial)


# ! Aplicación en lista de TUPLAS | PARTE 2
# =============================================================================


#? reduce + lista de tuplas | EJERCICIO COMPLETO
print('\nreduce + lista de tuplas | EJERCICIO COMPLETO')

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

# -----------------------------------------------------------------------------------------------
# EJERCICIO

# - Usando reduce realizar los siguientes cálculos:
# *    A) total a pagar por las compras, con un IVA del 12%
# *    B) total a pagar por la categoría 'ropa', con un IVA del 12%
# *    C) total a pagar por las categorías 'ropa' y 'electrodomésticos', con un IVA del 12%
# -----------------------------------------------------------------------------------------------


#? 1) Importar en 1er lugar functools
print('\n1) Importar en 1er lugar functools')
import functools



#? 2) Definir el IVA como una variable
print('\n2) Definir el IVA como una variable')

IVA = 1.12



#? 3) función : calcular_total_mas_IVA()
print('\n3) función : calcular_total_mas_IVA()')

# => definición de la función
def calcular_total_mas_IVA(lista_compras, iva):
    
    total = functools.reduce(
        lambda x,y : x + y,
        
        map(
            lambda x : x[2] * x[3],
            lista_compras
        )
    )
    
    # => agregar IVA
    total_IVA = total * iva
    
    # => redondear a 2 decimales
    total_IVA = float( f'{total_IVA:.2f}' )
    
    return total_IVA
# end def

# => TEST
print( 'Total a pagar + IVA = {} USD'.format( calcular_total_mas_IVA(compras, IVA) ) )



#? 4) función : calcular_total_ropa_mas_IVA()
print('\n4) función : calcular_total_ropa_mas_IVA()')

def calcular_total_ropa_mas_IVA(lista_compras, iva):
    # => filter de categoría ropa y electrodomésticos
    lista_filter = list(filter(
        lambda x : x[1] == 'ropa',
        lista_compras
    ))
    
    # => map a la lista filter
    lista_subtotales_por_ropa = list(map(
        lambda x : x[2] * x[3],
        lista_filter
    ))
    
    # => reduce a la lista map
    total_ropa = functools.reduce(
        lambda x,y : x + y,
        lista_subtotales_por_ropa
    )
    
    # => agregar IVA
    total_ropa *= iva
    
    # => formato de 2 decimales
    total_ropa = f'{total_ropa:.2f}'
    
    return total_ropa
# end def

# => TEST
print( 'Total a pagar por ropa + IVA = {} USD'.format(
    calcular_total_ropa_mas_IVA(compras, IVA) 
    ) 
)



#? 5) función : calcular_total_ropa_y_electrod_mas_IVA()
print('\n5) función : calcular_total_ropa_y_electrod_mas_IVA()')

def calcular_total_ropa_y_electrod_mas_IVA(lista_compras, iva):
    
    # => filter de categoría ropa y electrodomésticos
    lista_filter = list(filter(
        #lambda x : x[1] == 'ropa' or x[1] == 'electrodomésticos',
        lambda x : x[1] != 'herramientas',
        lista_compras
    ))
    
    # => map a la lista filter
    lista_subtotales_por_ropa_y_electrod = list(map(
        lambda x : x[2] * x[3],
        lista_filter
    ))
    
    # => reduce a la lista map
    total_ropa_electrod = functools.reduce(
        lambda x,y : x + y,
        lista_subtotales_por_ropa_y_electrod
    )
    
    # => agregar IVA
    total_ropa_electrod *= iva
    
    # => formato de 2 decimales
    total_ropa_electrod = f'{total_ropa_electrod:.2f}'
    
    return total_ropa_electrod
# end def

# => TEST
print( 'Total a pagar por ropa y electrodomésticos + IVA = {} USD'.format(
    calcular_total_ropa_y_electrod_mas_IVA(compras, IVA) 
    ) 
)
