# =================================================================
# Funciones con Argumentos Arbitrarios asociados a Clave
# (Keyword Arguments / *kwargs)

# - para crear una función
# - con número indeterminado de parámetros
# - asociados a una clave
# - y que pueden ser empacados en un DICCIONARIO

#   * args    => Número indeterminado de argumentos empacados en TUPLA
#   ** kwargs => Número indeterminado de argumentos empacados en DICCIONARIO

# - al igual que en *args
# - el nombre "kwargs" es irrelevante
# - lo importante son los 2 asteriscos => **

#   https://www.w3schools.com/python/python_functions.asp
# =================================================================


#? 1) Recordatorio Fundamentos de Diccionario
print('\n1) Recordatorio Fundamentos de Diccionario')

persona = {
    'nombre' : 'Sebas',
    'edad' : 36,
    'es_profesor' : True
}

print( persona, type(persona), len(persona) )

# => para acceder a los valores del diccionario usando las claves
print()
print( persona['nombre'], type(persona['nombre']) )
print( persona['edad'], type(persona['edad']) )
print( persona['es_profesor'], type(persona['es_profesor']) )

# => Recorrido de diccionarios con .items()
print()
for clave, valor in persona.items():
    print(clave, '--', valor)
# end for


#? 2) Función Básica con *args y **kwargs
print('\n2) Función Básica con *args y **kwargs')

def mostrar_args(*args):
    print(args, type(args), len(args))
# end def

def mostrar_kwargs(**kwargs):
    print(kwargs, type(kwargs), len(kwargs))
# end def

# ----------------------
# TEST *args
print('\nTEST *args\n')
# ----------------------

mostrar_args('Sebas', 36, True)

# -------------------------
# TEST **kwargs
print('\nTEST **kwargs\n')
# -------------------------
mostrar_kwargs(nombre='Sebas', edad=36, es_profesor=True)



#? 3) Ejemplo: función para describir persona
print('\n3) Ejemplo: función para describir persona')
# - Recordar, como se dijo
# - el nombre "kwargs" es un estándar, pero no una obligación
# - siempre y cuando definamos los 2 asteriscos **
# - los parámetros son de número indeterminado
# - asociados a una clave y valor
# - que se empacan en un DICCIONARIO

def describir_persona(**caracteristicas):
    for clave, valor in caracteristicas.items():
        print(clave, '==>', valor)
    # end for
# end def

# TEST
describir_persona(nombre='Carlos', apellido='Salas', ciudad='Quito', profesion='Doctor')



#? 4) En la definición de la función podemos ya establecer las claves
print('\n4) En la definición de la función podemos ya establecer las claves')
# - en lugar de que sean definidas de manera arbitraria 
# - al momento de invocar la función
# - podemos también crear las claves que tendrán los kwargs

def describir_persona(**kwargs):
    print('Su nombre es', kwargs['nombre'])
    print('Tiene', kwargs['edad'], 'años')
    print('Es', kwargs['ocupacion'])
# end def

# TEST
describir_persona(nombre='Daniel', edad=15, ocupacion='estudiante')
print()
describir_persona(nombre='Ana', edad=22, ocupacion='contadora')



#? 5) ERROR => si pasamos menos claves/valores de los definidos
print('\n5) ERROR => si pasamos menos claves/valores de los definidos')

print()
#describir_persona(nombre='Ana', edad=22)
#! KeyError: 'ocupacion'



#? 6) NO ERROR => si pasamos más claves/valores de los definidos
print('\n6) NO ERROR => si pasamos más claves/valores de los definidos')
# - no hay error
# - pero si no se usa este parámetro de alguna manera 
# - en la definición de la función
# - no tiene uso ni sentido

print()
describir_persona(nombre='Ana', edad=22, ocupacion='contadora', ciudad='Riobamba')