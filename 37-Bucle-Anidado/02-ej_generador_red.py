# ======================================
# Ejercicio: Generador de Red

# - Un ejercicio para poner en práctica
# - El bucle anidado
# ======================================


print('*********************************************')
print('Bienvenido al Generador de Telaraña\n')
num_filas = int( input('Ingrese Número de Filas: ') )
num_cols = int( input('Ingrese Número de Columnas: ') )
caracter = input('Ingrese un Caracter: ')
print()

for i in range(0, num_filas):
    for j in range(0, num_cols):
        print( caracter , end=' ' )
    # end for
    print()
# end for
print('\n*********************************************')



