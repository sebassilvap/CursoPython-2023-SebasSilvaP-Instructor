# ========================================================
# Función Interna zip

# - acepta como argumentos 2 elementos iterables
# - y une los elementos del 1ero con los del 2do
# - el iterable de menor tamaño decide el tamaño del zip
# - los elementos sin un par quedan excluidos
# - se retorna un objeto de tipo zip

# - https://www.w3schools.com/python/ref_func_zip.asp
# ========================================================


#? 1) Ejemplo Básico de Creación de un zip
print('\n1) Ejemplo Básico de Creación de un zip')

nombres = ['Renato', 'Andrea', 'Ximena']
edades = [15, 17, 20]

nombres_edades = zip(nombres, edades)

print(nombres_edades)
# ej: <zip object at 0x00000225C8F04F00>

for i in nombres_edades:
    print(i)
# end for

"""
('Renato', 15)
('Andrea', 17)
('Ximena', 20)
"""



#? 2) Una vez recorrido el objeto zip => queda vacío
print('\n2) Una vez recorrido el objeto zip => queda vacío')

print('Antes de for')
for i in nombres_edades:
    print(i)
# end for
print('Después de for')



#? 3) Casting de zip a list
print('\n3) Casting de zip a list')
# - para evitar utilizar directamente el objeto zip
# - podemos hacer en primera instancia una transformación a lista

lista_nombres_edades = list(zip(nombres, edades))

for i in lista_nombres_edades:
    print(i)
# end for

print()

for i in lista_nombres_edades:
    print(i)
# end for



#? 4) Casting de zip a diccionario
print('\n4) Casting de zip a diccionario')
# - para zip de 2 iterables, se puede hacer casting a diccionario

dict_nombres_edades = dict(zip(nombres, edades))

for clave, valor in dict_nombres_edades.items():
    print(clave, valor)
# end for

print()

for clave, valor in dict_nombres_edades.items():
    print(clave, valor)
# end for



#? 5) zip con más iterables además de listas
print('\n5) zip con más iterables además de listas')
# - cualquier iterable puede ser usado
# - de preferencia listas y tuplas
# - porque estas 2 mantienen un orden en sus elementos
# - el resultado final siempre va a ser una tupla que una los elementos

colores = ('amarillo', 'azul', 'rojo')
codigos = [100, 200, 300]

list_colores_codigos = list(zip(colores, codigos))

print(list_colores_codigos)



#? 6) zip adopta el tamaño del iterable de menor tamaño
print('\n6) zip adopta el tamaño del iterable de menor tamaño')

colores_1 = ('amarillo', 'azul', 'rojo')
codigos_1 = [100, 200, 300, 400, 500]

colores_2 = ('amarillo', 'azul', 'rojo', 'verde', 'blanco')
codigos_2 = [100, 200, 300]

lista_zip_1 = list(zip(colores_1, codigos_1))
lista_zip_2 = list(zip(colores_2, codigos_2))

print('lista_zip_1 =', lista_zip_1)
print('lista_zip_2 =', lista_zip_2)



#? 7) zip con más de 2 iterables
print('\n7) zip con más de 2 iterables')
# - zip puede empacar en una tupla más de 2 iterables
# - la transformación de zip a lista siempre es posible
# - con más 2 iterables una transformación a diccionario NO es posible

colores = ('amarillo', 'azul', 'rojo')
codigos = [100, 200, 300]
simbolos = ('AM', 'AZ', 'RO')

list_col_cod_sim = list(zip(colores, codigos, simbolos))
print(list_col_cod_sim)

#dict_col_cod_sim = dict(zip(colores, codigos, simbolos))
#! ValueError: dictionary update sequence element #0 has length 3; 2 is required