# ==============================================================
# sort / map / filter / reduce
# => map en Python

# https://www.w3schools.com/python/ref_func_map.asp

# - con map() podemos ejecutar una función
# - que se aplica a cada ítem de un elemento iterable
# - cada ítem se envía entonces como un argumento a la función
# - elemento iterable => colección de datos en Python
# - la función se envía como firma, es decir no se ejecuta
# - map => retorna un objeto / elemento de tipo map
# - para ver su resultado debemos hacer un casting a lista

# *      map(función , elementos_iterables)

# * NOTA: puede ser 1 o más ELEMENTOS ITERABLES
# ==============================================================


#? 1) Ejemplo Básico de Funcionamiento
print('\n1) Ejemplo Básico de Funcionamiento')

# => función
def doblar_numero(x):
    return 2 * x
# end def

# => elemento iterable, ej: lista
lista_numeros = [15, 2, 12, 8]

# => variable de tipo map
resultado_map = map(doblar_numero, lista_numeros) # función como argumento, sin invocar

# => ¿qué es map?
print( resultado_map, type(resultado_map) )

# => casting a lista
map_a_lista = list(resultado_map)
print( map_a_lista, type(map_a_lista) )



#? 2) Ejemplo con más de una colección como argumento
print('\n2) Ejemplo con más de una colección como argumento')

# => función
def calcular_nota_final(nota1, nota2, nota3):
    return 0.2*nota1 + 0.3*nota2 + 0.5*nota3
# end def

# => colecciones
# A) nota_deberes
nota_deberes = [15, 13, 12, 18, 20]

# B) nota_proyecto
nota_proyecto = [14, 13, 20, 19, 16]

# C) nota_examen
nota_examen = [14, 18, 19, 20, 13]

# => aplicando map
nota_final_map = map(calcular_nota_final, nota_deberes, nota_proyecto, nota_examen)
nota_final = list(nota_final_map)

print(nota_final)



#? 3) Ejemplo Map con strings
print('\n3) Ejemplo Map con strings')

# => función
def presentacion(nombre, edad):
    return 'Usted se llama {} y tiene {} años'.format(nombre, edad)
# end def

# => colecciones
nombres = ['Sebas', 'Xime', 'Andrea', 'Santi']
edades = [29, 18, 20, 15]

# => aplicando map
info_map = map(presentacion, nombres, edades)
info_list = list(info_map)

for i in info_list:
    print(i)
# end for



#? 4) También funciona con función lambda
print('\n4) También funciona con función lambda')

# => función lambda
presentación_lambda = lambda nombre, edad : f'Usted se llama {nombre} y tiene {edad} años!!'

# => colecciones
nombres = ['Sebas', 'Xime', 'Andrea', 'Santi']
edades = [29, 18, 20, 15]

# => aplicando map
info_map = map(presentación_lambda, nombres, edades)
info_list = list(info_map)

for i in info_list:
    print(i)
# end for


#? 5) Una vez consumido el recurso map => ya no queda nada por iterar
print('\n5) Una vez consumido el recurso map => ya no queda nada por iterar')

# EJ
# y(x) = 2*x - 5

valores_x = [10, 15, 20, 8, 6, 12]

funcion_y_de_x = lambda x : 2*x - 5

valores_y_map = map(
    funcion_y_de_x,
    valores_x
)

print(valores_y_map)

valores_y = list(valores_y_map)

print(valores_y)

# => si intento una vez más
valores_y = list(valores_y_map)

print(valores_y) # []

#! OJO
# - una vez consumido el recurso de map
# - a través de un casting a lista por ejemplo
# - ese objeto nos queda vacío
# - es decir con el casting se modifica, se queda sin elementos
# - una buena práctica es hacer al mismo tiempo list(map(....))

valores_y = list(map(
    funcion_y_de_x,
    valores_x
))

print(valores_y)