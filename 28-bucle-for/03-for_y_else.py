# =================================================
# for + else

# - al igual que en el bucle while
# - el else puede usarse dentro de un bucle for
# - siempre se ejecuta 1 vez
# - y se ejecuta al terminar la iteración
# =================================================


#? 1) for + else => Ejemplo Básico
print('\n1) for + else => Ejemplo Básico')

for x in range(1,6):
    print('El contador x =', x)
else:
    print('Al final contador x =', x)
# end for

print('fuera del bucle for')
print('x =', x)

# - NOTA: al crear un bucle for
# - la variable de recorrido se crea dentro del script
# - y la podemos usar luego de finalizado el bucle



#? 2) Ejemplo: Crear sumatoria con for
print('\n2) Ejemplo: Crear sumatoria con for')
# - EJ: dada la variable "numero"
# *     numero = 5
# *     sumatoria = 1+2+3+4+5 = 15
# *     promedio = 15/5 = 3.0

numero = 5
sumatoria = 0
counter = 0

# NOTA: al volver a utilizar x, estamos sobrescribiéndola
for x in range(1, numero + 1): # recordar (range - end - exclusivo)
    sumatoria += x
    counter += 1
else:
    promedio = sumatoria / counter
    print('sumatoria(' + str(numero) + ') =', sumatoria)
    print('counter =', counter)
    print('promedio =', promedio)
# end for


# ----------------------------------------------
# => Con una lista de números:
# - cuando tengamos lista de números sin orden
# - EJ: [5, 2, 3, 2, 4]
# - sumatoria = 5+2+3+2+4 = 16
# - promedio = 16/5 = 3.2
# - counter = 5 elementos
# ----------------------------------------------

print('\nCon lista de números:\n')

lista = [5, 2, 3, 2, 4]

sumatoria = 0
counter = 0

for x in lista:
    sumatoria += x
    counter += 1
else:
    promedio = sumatoria / counter
    print('sumatoria(' + str(numero) + ') =', sumatoria)
    print('counter =', counter)
    print('promedio =', promedio)
# end for



#? 3) Ejemplo: Crear sumatoria con for + lista
print('\n3) Ejemplo: Crear sumatoria con for + lista')

lista = [5, 2, 3, 2, 4]
sumatoria = 0

for x in lista:
    sumatoria += x
else:
    print( 'sumatoria(' + str(numero) + ') =', sumatoria )
    print( '# elementos =', len(lista) )
    print( 'promedio =', sumatoria / len(lista) )
# end for