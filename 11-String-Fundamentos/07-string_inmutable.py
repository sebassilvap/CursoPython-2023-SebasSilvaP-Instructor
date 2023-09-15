# ===================================================
# Inmutabilidad de los String

# - las cadenas de texto = String => son INMUTABLES
# - es decir, una vez definidos
# - no podemos modificar alguno de sus caracteres
# ===================================================

#? 1) Error al tratar de modificar un índice del string

cadena_1 = 'sebas'
#(+)        01234 

print(cadena_1)
print( cadena_1[0] )

#cadena_1[0] = 'X'
#! Type ERROR: string no soporta asignación de ítem

#? 2) Una solución a este problema
# - como se ha mencionado varias veces
# - el secreto de python es que podemos encontrar varias maneras
# - de poder dar solución a un problema
# - en este caso utilizamos la REASIGNACIÓN
# - como una alternativa

cadena_1 = 'X' + cadena_1[1:]
print(cadena_1)


