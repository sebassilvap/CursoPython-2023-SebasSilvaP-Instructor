# ==============================================================
# Bucles Anidados

# - Básicamente es un bucle dentro de otro bucle
# - Podemos anidar cuantos bucles queramos
# - Pero hacer esto aumenta la complejidad de nuestro código
# - Recordar que nuestro código siempre debe ser fácil de leer
# ==============================================================


#? 1) Ejemplo Básico: Bucle for anidado
print('\n1) Ejemplo Básico: Bucle for anidado')

for i in range(1,4):
    for j in range(1,6):
        print(j)
    # end for
# end for

# => podemos mejorar la lectura de esto en la consola
# - utilizando end en el print
# - y simular una especie de matriz
print('\n-----------------------\n')

for i in range(1,4): # 3 iteraciones
    for j in range(1,6): # 5 iteraciones
        print(j, end='  ')
    # end for
    print()
# end for



#? 2) Ejemplo Básico: Bucle while anidado
print('\n2) Ejemplo Básico: Bucle while anidado')

i = 0
j = 0

while i < 3:
    while j < 5:
        print(j)
        j += 1
    # end while
    i += 1
    j = 0 # resetear j para la siguiente vez que entremos al segundo bucle
# end while

#print(i,j) # test para ver que pasa al final del bucle

# => utilizando end= para simular una matriz
print('\n-----------------------\n')

i = 0
j = 0

while i < 3:
    while j < 5:
        print(j, end=' ')
        j += 1
    # end while
    i += 1
    j = 0 
    print()
# end while

# => truco para evitar el 0 en la impresión
print('\n-----------------------\n')

i = 0
j = 0

while i < 3:
    while j < 5:
        print(j + 1, end=' ')
        j += 1
    # end while
    i += 1
    j = 0 
    print()
# end while

# ------------------------------------------------------
#*  CONCLUSIÓN
# - los bucles anidados nos ayudan a simular una matriz
# - la primera iteración simula la creación de filas
# - la segunda la creación de columnas
# ------------------------------------------------------



#? 3) Bucle anidado for: Coordenadas de filas y columnas
print('\n3) Bucle anidado for: Coordenadas de filas y columnas')

for i in range(1,4): # 3 filas
    for j in range(1,6): # 5 columnas
        temp = '('+str(i)+','+str(j)+')'
        print( temp , end='  ' )
    # end for
    print()
# end for

# => concatenación directamente en el print
print('\n-----------------------\n')

for i in range(1,4): # 3 filas
    for j in range(1,6): # 5 columnas
        print( '('+str(i)+','+str(j)+')' , end='  ' )
    # end for
    print()
# end for



#? 4) Bucle anidado while: Coordenadas de filas y columnas
print('\n4) Bucle anidado while: Coordenadas de filas y columnas')

i = 0
j = 0

while i < 3:
    while j < 5:
        print( '('+str(i+1)+','+str(j+1)+')' , end='  ')
        j += 1
    # end while
    i += 1
    j = 0 
    print()
# end while