# ===================================================
# Operador Walrus :=

# * una característica nueva de Python 3.8
# - también denominado asignador de expresión
# - asigna valores a las variables
# - que son parte de expresiones largas

# - https://realpython.com/python-walrus-operator/
# ===================================================


#? 1) Ejemplo Básico de uso
print('\n1) Ejemplo Básico de uso')

# => SIN Operador Walrus
nombre = 'Sebastián'
print(nombre)

# => CON Operador Walrus
print( nombre_completo := 'Sebastián Silva P.' )
print( nombre_completo )



#? 2) Ejemplo más complejo
print('\n2) Ejemplo más complejo')

# ------------------------------------
# 2.1) Usando while True
print('\n2.1) Usando while True\n')
# ------------------------------------

"""
lista_tareas = []

while True:
    tarea = input('Ingrese una tarea para hoy (o salir): ')
    tarea = tarea.strip().lower
    
    if tarea == 'salir':
        break
    else:
        lista_tareas.append(tarea)
    # end if
# end while

print('\nLista de Tareas para hoy:')
for i,value in enumerate(lista_tareas):
    print( f'Tarea {i+1}: {value}' )
# end for
"""


# -------------------------------------------
# 2.2) Usando while con condición
print('\n2.2) Usando while con condición\n')
# -------------------------------------------

"""
lista_tareas = []
opcion_user = ''

while opcion_user != 'salir':
    opcion_user = input('Ingrese una tarea para hoy (salir): ')
    opcion_user = opcion_user.strip().lower()
    lista_tareas.append(opcion_user)
# end while

print('\nLista de Tareas para hoy:')
for i,value in enumerate(lista_tareas):
    if i == len(lista_tareas) - 1: # para no imprimir salir
        break
    else:
        print( f'Tarea {i+1}: {value}' )
# end for
"""


# ------------------------------------------
# 2.3) Usando el Operador Walrus
print('\n2.3) Usando el Operador Walrus\n')
# ------------------------------------------

"""
lista_tareas = []

while (opcion_user := input('Ingrese Tarea para hoy (salir): ')) != 'salir':
    lista_tareas.append(opcion_user)
# end while

print('\nLista de Tareas para hoy:')
for i,value in enumerate(lista_tareas):
    print( f'Tarea {i+1}: {value}' )
# end for
"""

# => incluso cuando ponemos salir
# - ni siquiera se hace el append
# - en la lista_tareas


# --------------------------------------------
# 2.4) ERROR - No usar paréntesis
print('\n2.4) ERROR - No usar paréntesis\n')
# --------------------------------------------

lista_tareas = []

while opcion_user := input('Ingrese Tarea para hoy (salir): ') != 'salir':
    lista_tareas.append(opcion_user)
# end while

print('\nLista de Tareas para hoy:')
print(lista_tareas)
# EJ: [True, True, True]


# * ¿Por qué?
# opcion_user := input('Ingrese Tarea para hoy (salir): ') != 'salir'

# - opcion_user es igual a:
# input('Ingrese Tarea para hoy (salir): ') != 'salir'

# - es decir, es igual al resultado de esta comparación
# - siempre que no sea 'salir', los valores van a ser True