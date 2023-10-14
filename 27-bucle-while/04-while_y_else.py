# ====================================================
# while + else

# - el else puede usarse dentro de un bucle while
# - siempre se ejecuta 1 vez
# - y se ejecuta cuando la condición ya no se cumple
# ====================================================

#? 1) Explicación básica
print('\n1) Explicación básica')

while False:
    print('nunca entramos al while')
else:
    print('pero el else siempre se ejecuta')
# end while

# => al menos 1 vez, así el while nunca se ejecute



#? 2) Ejemplo contador
print('\n2) Ejemplo contador')

contador = 5

while contador >= 2:
    print('Contador = ', contador)
    contador -= 1
else:
    print('Hemos llegado a la meta')
    print('Donde al final contador =', contador)
# end while