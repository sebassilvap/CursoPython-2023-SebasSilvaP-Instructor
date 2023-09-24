# ===================================================
# Encadenamiento de Funciones
# (Function - Chaining)

# - chaining / encadenamiento
# - es un estilo de programación
# - se invocan varias funciones de manera múltiple
# - que se ejecutan de manera secuencial
# - en las funciones => desde dentro hacia afuera
# ===================================================

#? 1) Sin usar function-chaining
print('\n1) Sin usar function-chaining\n')

print('Calcular el redondeo absoluto de un número:')

numero = input('Ingrese un Número: ') # input al usuario
numero = float(numero) # 1 - casting a float
numero = abs(numero) # 2 - obtener valor absoluto
numero = round(numero) # 3 - calcular redondeo
print(numero) # 4 - imprimir resultado

# => 4 líneas de código para hacer esto


#? 2) CON function-chaining
print('\n2) CON function-chaining\n')

print('Calcular el redondeo absoluto de un número:')

print( round(abs(float(input('Ingrese un Número: ')))) )

# => 1 línea de código para realizar todo esto


#? 3) Buenas Prácticas de Programación
# - el código debe ser legible
# - legible para el programador y cualquiera que lo lea
# - un excesivo uso de funciones encadenadas hace al código difícil de leer
# - en programas avanzados será común ver esto
# - para empezar usarlo con mesura



