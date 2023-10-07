# ===============================================================
# break-continue-pass

# Son sentencias para el control de un bucle
# pass => también tiene otras utilidades además de los bucles

#* pass
# => se lo utiliza como un placeholder
# => para definir algo y trabajar en eso luego

#* break
# => interrumpimos / terminamos un bucle de manera total

#* continue
# => para saltarnos a la siguiente iteración de un bucle

# ===============================================================

#? 1) break => interrumpir la ejecución del bucle y seguir ejecutando el código
# - si utilizamos else en while o for
# - si aplicamos un break
# - el else no se ejecuta

print('\n1) break => interrumpir la ejecución del bucle y seguir ejecutando el código')

print('línea de código # 1')
print('línea de código # 2')
print('línea de código # 3')

contador = 1

while contador < 10:
    print('Contador =', contador)
    
    
    if contador == 5:
        print('Salimos del bucle cuando Contador =', contador)
        break
    
    contador += 1
else:
    print('Llegamos al final del Bucle')
    print('Al final, Contador =', contador)
# end while

print('Línea de código # 4')
print('Línea de código # 5')
print('Línea de código # 6')


#? 2) break => ejemplo con for

print('\n2) break => ejemplo con for')

print('Ejecutando Instrucción # 1')
print('Ejecutando Instrucción # 2')
print('Ejecutando Instrucción # 3')

for i in range(1,11):
    print('Bucle for - Contador i =', i)
    if i == 6:
        print('*** break ***')
        print('Contador i en el break vale =', i)
        break
    # end if
else:
    print('El bucle ha terminado')
    print('Contador i al final =', i)
# end for

print('Ejecutando Instrucción # 4')
print('Ejecutando Instrucción # 5')
print('Ejecutando Instrucción # 6')
    