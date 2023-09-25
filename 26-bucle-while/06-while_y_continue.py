# =======================================================
# while + continue

# - continue => se salta la iteración donde se lo invoca
# - pero no rompe el bucle como lo hace break
# =======================================================


#? ejercicio de aplicación
# - contar del 1 al 10
# - saltarse las iteraciones 3 y 8

contador = 0

while contador < 10:
    
    contador += 1 #! Incremento
       
    if (contador == 3 or contador == 8):
        print('*** salto de bucle ***')
        continue
    # end if
    
    print('Iteración #', contador)
    
else:
    print('Final del while, contador =', contador)
    
# end while