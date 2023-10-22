# ===========================================================
# Función interna => id()

# - me devuelve un identificador único
# - de cualquier elemento creado en Python
# - este identificador, su valor
# - es la dirección en la memoria de este elemento
# - es siempre distinto cada vez que se ejecuta el programa


# https://www.w3schools.com/python/ref_func_id.asp
# ===========================================================


#? 1) Función interna => id()
print('\n1) Función interna => id()')
# - retorna un id único de un objeto en Python
# - todos los objetos en Python tienen un id único
# - este id se crea cuando el objeto es creado
# - el id es la DIRECCIÓN EN MEMORIA del objeto
# - y será distinta siempre que ejecutemos el programa

# ------------------------------------------
# - Para cualquier tipo de variable
# - Cuando se inician con valores distintos
# - Esta dirección es distinta
# ------------------------------------------

numero_1 = 10
numero_2 = 20
cadena_1 = 'hola'
cadena_2 = 'python'
lista_1 = [1,2,3]
lista_2 = [4,5,6]

# TEST:
print( numero_1, type(numero_1), id(numero_1) )
print( numero_2, type(numero_2), id(numero_2) )
print( cadena_1, type(cadena_1), id(cadena_1) )
print( cadena_2, type(cadena_2), id(cadena_2) )
print( lista_1, type(lista_1), id(lista_1) )
print( lista_2, type(lista_2), id(lista_2) )

print( id(numero_1) == id(numero_2) )
print( id(cadena_1) == id(cadena_2) )
print( id(lista_1) == id(lista_2) )



#? 2) Variables Básicas inicializadas con el mismo valor
print('\n2) Variables Básicas inicializadas con el mismo valor')
# - RECORDAR las variables básicas:
# *     int   str   float   bool
# - Si se las declara e inicializa con el mismo valor
# - Tendrán la misma dirección en la memoria


# TEST:
int_1, int_2, int_3 = 10, 10, 20
float_1, float_2, float_3 = 1.5, 1.5, 3.6
str_1, str_2, str_3 = 'A', 'A', 'Z'
bool_1, bool_2, bool_3 = True, True, False

print( id(int_1) == id(int_2), '|', id(int_1) == id(int_3) )
print( id(float_1) == id(float_2), '|', id(float_1) == id(float_3) )
print( id(str_1) == id(str_2), '|', id(str_1) == id(str_3) )
print( id(bool_1) == id(bool_2), '|', id(bool_1) == id(bool_3) )



#? 3) Variables no Básicas inicializadas con el mismo valor
print('\n3) Variables no Básicas inicializadas con el mismo valor')
# - Para listas por ejemplo
# - Si iniciamos 2 listas con los mismos valores
# - Ambas no tienen la misma dirección en la memoria

# TEST:
lista_1 = [1,2,3]
lista_2 = [4,5,6]
lista_3 = [1,2,3]
lista_4 = list([1,2,3]) # utilizando la función list*

print( id(lista_1) == id(lista_1) ) # True
print( id(lista_1) == id(lista_2) )
print( id(lista_1) == id(lista_3) )
print( id(lista_1) == id(lista_4) )

# - ya veremos luego lo que son clases y objetos
# - al utilizar list() este es un método especial llamado constructor
# - lo que hacemos es crear un objeto de la clase list
# - por el momento entender que cada objeto creado
# - tiene DIFERENTE espacio en la memoria



#? 4) Cuando una lista es creada a partir de otra lista
print('\n4) Cuando una lista es creada a partir de otra lista')

# => Recordemos la MUTABILIDAD de listas
lista_1 = [1,2,3]
lista_2 = lista_1

lista_1.append('z')

print(lista_1, '|', lista_2)

# => RECORDEMOS
# - cuando hacíamos esto decíamos
# - que al modificar 1 se afecta la otra
# - y esto pasaba porque ambas se creaban en el mismo espacio de la memoria
# - ahora lo podemos comprobar

print( id(lista_1) )
print( id(lista_2) )
print( id(lista_1) == id(lista_2) )

# => Y recordemos que esto lo evitamos con .copy()
lista_copy = lista_1.copy()

print('\nEvaluando la copia de la lista:')
print( id(lista_1) )
print( id(lista_copy) )
print( id(lista_1) == id(lista_copy) )

lista_copy.append(100)

print(lista_1, '|', lista_copy)