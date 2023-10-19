# =======================================================================
# De Funciones a Variables

# - en Python todo puede ser tratado como una variable
# - que tiene un tipo de dato
# - de manera precisa se dice

# * En Python todo es un "objeto"

# - el concepto de objeto / clase => lo veremos muy pronto !!
# - (POO => Programación Orientada a Objetos)
# - pero esto lo hemos visto desde un inicio
# - al averiguar el tipo de dato con type()

# - todo es una variable con dato => las funciones no son excepción
# =======================================================================

#? 1) Las funciones y todo en Python es una variable con dato
print('\n1) Las funciones y todo en Python es una variable con dato')

def saludar(nombre):
    print('Hola {}, es un gusto!'.format(nombre))
# end def

def sumar(a,b,c):
    return a + b + c
# end def


# => ¿Qué pasa si las imprimimos sin invocar?
# - también podemos incluir el type
print( saludar , type(saludar) )
print( sumar , type(sumar) )

# EJ de respuesta en consola:
# <function saludar at 0x000001AA2EE004A0> <class 'function'>
# <function sumar at 0x000001AA2F028FE0> <class 'function'>

# -----------------------------------------------------------------------------
# - después veremos el concepto clase / objeto
# - como hemos dicho desde el inicio
# - type devuelve el tipo del elemento / ¿a qué clase pertenece?
# - se nos imprime también la dirección en la memoria del elemento (objeto*)
# ! los términos clase / objeto tendrán sentido cuando veamos POO
# ! POO => Programación Orientada a Objetos
# - otra manera de saber la dirección en memoria es con id()
# - y el valor hexadecimal de la memoria como se recordará => hex(id())
# ! cada vez que ejecutamos el programa, esta información será distinta
# -----------------------------------------------------------------------------

print()
print( saludar , '|' , hex(id(saludar)) )
print( sumar , '|' , hex(id(sumar)) )



#? 2) Asignando la función a una variable
print('\n2) Asignando la función a una variable')
# - cuando hacemos esto
# - como ya hemos aprendido
# - asignamos la dirección de una variable en otra


# => tal como lo hacíamos con las otras variables
numero_1 = 20
numero_2 = numero_1

lista_1 = [1,2,3]
lista_2 = lista_1 # RECORDAR: aquí aplicaba la mutabilidad!


# => también lo podemos hacer con las funciones
mi_variable_1 = saludar
mi_variable_2 = sumar


# => estas variables actuarían de igual manera que las funciones
# - es decir, podemos invocarlas
# - de igual manera que las funciones definidas

saludar('Juan')
mi_variable_1('Andy')

print()

print( sumar(1,2,3) )
print( mi_variable_2(1,2,3) )



#? 3) Funciona también con las funciones internas (built-in functions)
print('\n3) Funciona también con las funciones internas (built-in functions)')
# - de manera sencilla se puede ver
# - como una manera de cambiarle el nombre a las funciones que conocemos
# ! pero no invocar o usar los ()

# ---------------------------------
# 3.1) Ejemplo con print
print('\n3.1) Ejemplo con print\n')
# ---------------------------------

imprimir_en_consola = print
imprimir_en_consola_2 = print() #! NO

print( imprimir_en_consola, type(imprimir_en_consola) )
print( imprimir_en_consola_2, type(imprimir_en_consola_2) )

# => Invocando
# - funcionará de la misma manera que un print
# - todo lo que tiene print lo tendría este nuevo nombre
imprimir_en_consola() # generar espacio
imprimir_en_consola('hola mundo', end=' ') # parámetro end
imprimir_en_consola('python')


# ----------------------------------
# 3.2) Ejemplo con type
print('\n3.2) Ejemplo con type\n')
# ----------------------------------

# => cambiando el nombre de las funciones internas
# - en realidad lo que hacemos
# - es asignarles una variable creada por nosotros

imprimir_en_consola = print
mostrar_tipo_dato = type

num = 50
cadena = 'python'

# => de la manera tradicional
print( num, '|', type(num) )
print( cadena, '|', type(cadena) )

# => usando nuestras variables
imprimir_en_consola( num, '|', mostrar_tipo_dato(num) )
imprimir_en_consola( cadena, '|', mostrar_tipo_dato(cadena) )