# ================================================
# Ejercicio

# - reducir los decimales de un número flotante
# - pero SIN cambiar el tipo de dato
# ================================================

nota_1 = 12
nota_2 = 16
nota_3 = 18

promedio = (nota_1 + nota_2 + nota_3) / 3
print( promedio, type(promedio) ) # recordar, al momento de dividir ya es un float

"""
promedio = '{:.2f}'.format(promedio)
print( promedio, type(promedio) ) # logramos el objetivo pero se convierte en string
"""

# => para que esto siga siendo float, la manera es la siguiente
promedio = float( '{:.2f}'.format(promedio) )

print( promedio, type(promedio) ) #* OK !!