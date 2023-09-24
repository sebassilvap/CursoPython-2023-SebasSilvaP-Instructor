# =========================================================
# Condicional if + input

# - una muy buena combinación al inicio en el aprendizaje
# - para evaluar la entrada dada por el usuario
#! RECORDAR: el input siempre devuelve un string!
# =========================================================

opcion = input('Ingrese un número del 1 al 100: ')

# => de esta manera no me va a dar error de sintaxis
# - no lo detecta el editor
# - el error se da al ejecutar e ingresar un valor
# - porque estoy evaluando un string
'''
if opcion < 50:
    print('Ingresó un número menor a 50!')
else:
    print('Ingresó un número mayor a 50!')
'''

## CORRECCIÓN & SOLUCIÓN
if int(opcion) < 50:
    print('Ingresó un número menor a 50!')
else:
    print('Ingresó un número mayor a 50!')