# =================================================================
# for para modificar un string

# - un ejercicio para ver las utilidades del for
# - vamos a modificar de manera dinámica un string
# - y vamos a solventar un problema que se presenta en el camino
# =================================================================


#? 1) Modificar string con bucle for
print('\n1) Modificar string con bucle for\n')

nombre = 'python'
nombre_modificado = ''
caracter_especial = '---'


for letra in nombre:
    #nombre_modificado = nombre_modificado + letra + caracter_especial
    nombre_modificado += letra + caracter_especial #! utilizando la concatenación en la asignación
# end for

print( 'nombre =' , nombre )
print( 'nombre_modificado =', nombre_modificado )


# - un problema si deseamos ser meticulosos en esto
# - es que el caracter especial se imprime después de la última letra
# - podríamos evitar esto
# - modificando un poco nuestro bucle


#? 2) Corrigiendo el problema
print('\n2) Corrigiendo el problema\n')

nombre = 'python'
nombre_modificado = ''
caracter_especial = '---'

index = 0

for letra in nombre:
    
    if index == len(nombre) - 1:
        nombre_modificado += letra
    else:
        nombre_modificado += letra + caracter_especial
    # end if
    
    index += 1

# end for

print( 'nombre =' , nombre )
print( 'nombre_modificado =', nombre_modificado )