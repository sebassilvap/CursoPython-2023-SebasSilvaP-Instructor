# ========================================================================
# Parámetro VS. Argumento

#* PARÁMETRO => variable en la definición de una función
#* ARGUMENTO => variable durante la ejecución / invocación de una función
# ========================================================================


#? 1) Diferencia ente Parámetro y Argumento
print('\n1) Diferencia ente Parámetro y Argumento')

def multiplicar(a, b): # => parámetros a y b
    return a * b
# end def

a, b = 2, 3
num_1, num_2 = 8, 5

resultado_1 = multiplicar(a, b) # argumentos a y b
resultado_2 = multiplicar(num_1, num_2) # argumentos num_1 y num_2
resultado_3 = multiplicar(5, 4) # argumentos 5 y 4

print('resultado 1 =', resultado_1)
print('resultado 2 =', resultado_2)
print('resultado 3 =', resultado_3)



#? 2) El parámetro puede ser cualquier tipo de dato
print('\n2) El parámetro puede ser cualquier tipo de dato')
# - RECORDAR: Python no trabaja con tipado de datos
# - Al igual que las variables
# - Los parámetros y los argumentos pueden tener cualquier tipo
# - Esto puede resultar en errores
# - Si la función no se define correctamente
# - Por defecto VS Code no me identifica métodos
# - Porque no sabemos que tipo de dato es

def ingresar_registro(dato, registro):
    registro.append(dato)
# end def

lista_nombres = ['Carlos', 'Andrea', 'Sebas']
nuevo_estudiante = 'Daniel'

print( lista_nombres, len(lista_nombres) )

ingresar_registro(nuevo_estudiante, lista_nombres)

print( lista_nombres, len(lista_nombres) )

# => si yo ingreso parámetros que no tienen sentido con la función
lista = 'Carlos, Andrea, Sebas'
nuevo = 'Daniel'

#ingresar_registro(nuevo, lista) #! AttributeError: 'str' object has no attribute 'append'



#? 3) Solución al ingreso de un argumento con tipo de dato incorrecto
print('\n3) Solución al ingreso de un argumento con tipo de dato incorrecto')
# - con lo aprendido hasta el momento
# - podemos hacer una pequeña gestión de errores
# - la gestión de errores como tal es un tema avanzado
# * (try-except)
# - pero con funciones y condicionales 
# - podemos hacer un control básico
# - más adelante veremos un ejercicio práctico de esto

def ingresar_registro(dato, registro):
    if isinstance(registro, list):
        registro.append(dato)
        print('Registro Actualizado! =>', registro)
    else:
        print('ERROR: registro debe ser una lista')
# end def

# TEST:

lista = 'Carlos, Andrea, Sebas'
nuevo = 'Daniel'

ingresar_registro(nuevo, lista)

lista = [1,2,3]
nuevo = 100

ingresar_registro(nuevo, lista)



#? 4) RECORDAR: Los parámetros existen solo en la función donde se definen
print('\n4) RECORDAR: Los parámetros existen solo en la función donde se definen')

a = 10

def doblar_numero(a):
    print(a * 2)
# end def

def triplicar_numero(z):
    print(z * 3)
# end def

print(a)
#print(z) # NameError: name 'z' is not defined

doblar_numero(a)


# * IMPORTANTE RECORDAR
# ------------------------------------------------------------------------
# => esto veremos a profundidad en el SCOPE de variables!
# - por el momento solo recordar
# - que el nombre de los parámetros
# - y los parámetros en sí, existen dentro de la definición de la función
# - y SOBREESCRIBEN cualquier otra variable con el mismo nombre
# ------------------------------------------------------------------------