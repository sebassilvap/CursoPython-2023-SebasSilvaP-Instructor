# ==============================================================
# sort / map / filter / reduce
# => filter en Python

# https://www.w3schools.com/python/ref_func_filter.asp

# ? RECORDAR: las colecciones avanzadas de casos reales:

#       * Listas de Listas (Listas 2D)
#       * Listas de Tuplas
#       * Listas de Diccionarios

# ? TIP: la función la podemos definir con lambda
# - recordar que lambda se define en una sola línea
# - si la expresión es muy complicada podemos siempre optar
# - por nuestras funciones normales

# ? RECORDAR !!!
# - la función filter nos debe retornar un patrón de filtrado
# - en True o False
# - o con lambda se define la expresión que me devuelve True

# ! PARTE 2
# => aplicando filter a una lista de DICCIONARIOS
# ==============================================================


#? Filter + Lista de DICCIONARIOS
print('\nFilter + Lista de DICCIONARIOS')

autos = [
    {
        'marca' : 'chevrolet',
        'tipo' : 'Vitara',
        'color' : 'rojo',
        'km' : 30000,
        'v_max' : 180
    },
    {
        'marca' : 'ford',
        'tipo' : 'Ranger',
        'color' : 'azul',
        'km' : 20000,
        'v_max' : 150
    },
    {
        'marca' : 'toyota',
        'tipo' : 'Land Rover',
        'color' : 'rojo',
        'km' : 115000,
        'v_max' : 195
    },
    {
        'marca' : 'chevrolet',
        'tipo' : 'Blazer',
        'color' : 'negro',
        'km' : 80000,
        'v_max' : 170
    },
    {
        'marca' : 'hyundai',
        'tipo' : 'Tucson',
        'color' : 'rojo',
        'km' : 120000,
        'v_max' : 220
    },
    {
        'marca' : 'toyota',
        'tipo' : 'Rav4',
        'color' : 'azul',
        'km' : 40000,
        'v_max' : 190
    },
    {
        'marca' : 'mitsubishi',
        'tipo' : 'Montero',
        'color' : 'rojo',
        'km' : 75000,
        'v_max' : 185
    },
]


# ------------------------------------------------------------------------------------------
# EJERCICIO
# - se presenta esta lista de diccionarios
# - cada diccionario es un auto en específico
# - se piden los siguientes filtrados

# A) filtrar los autos de color rojo
# B) filtrar los autos de color rojo con kilometraje > 40.000
# C) filtrar los autos de color rojo con kilometraje > 40.000 y velocidad máxima < 190 km/h
# ------------------------------------------------------------------------------------------


#? 1) Función EXTRA: presentar datos
print('\n1) Función EXTRA: presentar datos')

def print_datos(lista_dict):
    for i, diccionario in enumerate(lista_dict):
        print('{} => {}'.format(i + 1, diccionario))
    # end for
# end def

# => TEST:
print('\nLISTA ORIGINAL:\n')
print_datos(autos)



#? 2) Filtrado: autos color rojo
print('\n2) Filtrado: autos color rojo')

# => función de filtrado
funcion_filtrado = lambda auto : auto['color'] == 'rojo'

# => aplicando filter
filtrado_1 = list(filter(
    funcion_filtrado,
    autos
))

# => TEST:
print('\nAUTOS COLOR ROJO:\n')
print_datos(filtrado_1)



#? 3) Filtrado: autos color rojo | km > 40000
print('\n3) Filtrado: autos color rojo | km > 40000')

# => función de filtrado
def funcion_filtrado(auto):
    if auto['color'] == 'rojo' and auto['km'] > 40000:
        return True
    else:
        return False
    # end if
# end def

# => aplicando filter
filtrado_2 = list(filter(
    funcion_filtrado,
    autos
))

# => TEST:
print('\nAUTOS COLOR ROJO | KM > 40000:\n')
print_datos(filtrado_2)



#? 4) Filtrado: autos color rojo | km > 40000 | v_max < 190 km/h
print('\n4) Filtrado: autos color rojo | km > 40000 | v_max < 190 km/h') 

# => función de filtrado
def funcion_filtrado(auto):
    if auto['color'] == 'rojo' and auto['km'] > 40000 and auto['v_max'] < 190:
        return True
    else:
        return False
    # end if
# end def

# => aplicando filter
filtrado_3 = list(filter(
    funcion_filtrado,
    autos
))

# => TEST:
print('\nAUTOS COLOR ROJO | KM > 40000 | V_MAX < 190:\n')
print_datos(filtrado_3)