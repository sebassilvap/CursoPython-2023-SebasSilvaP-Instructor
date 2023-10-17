# ============================================
# Ejercicio

# - dado un número por el usuario
# - dibujar una rampa que siga una secuencia
# - por ejemplo si el usuario proporciona

# *       num = 5

# - el resultado en la consola sería

"""
            1 
            1 2 
            1 2 3 
            1 2 3 4 
            1 2 3 4 5 

"""
# ============================================


# ----------------------------------
#? Definir Función => dibujar_rampa
# ----------------------------------

def dibujar_rampa(numero):
    for i in range(1, numero + 1):
        for j in range(1 , i + 1):
            print( f'{j:<2d}' , end=' ' )
        # end for
        print()
    # end for
# end def


# ----------------------------
#? Interacción con el usuario
# ----------------------------

num = int( input('\n\nIngrese un número entero: ') )

print('\nDibujando rampa con el número {}!\n'.format(num))

dibujar_rampa(num)