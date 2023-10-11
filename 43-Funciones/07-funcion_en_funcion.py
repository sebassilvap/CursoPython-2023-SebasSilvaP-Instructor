# ======================================================
# Invocar una función en la definición de otra función

# - una función con retorno
# - puede ser un elemento de construcción
# - de una función más grande
# ======================================================

def elevar_al_cuadrado( num ):
    return num ** 2
# end def

def doblar_numero( num ):
    return 2 * num
# end def

# => la siguiente función invoca las otras 2
def presentar_resultados( x ):
    print( x, 'al cuadrado =', elevar_al_cuadrado(x) )
    print('el doble de', x, '=', doblar_numero(x) )
    print()
# end

presentar_resultados(5)

presentar_resultados(8)


# => como se dijo anteriormente,
# - el parámetro puede ser lo que sea
# - podemos definir el mismo nombre en todos los parámetros de una función
# - esto no tiene problema
# - aunque sería muy útil darle nombres que nos ayuden
# - a entender la funcionalidad de la función

def presentar_resultados_2( num ):
    print( num, 'al cuadrado =', elevar_al_cuadrado(num) )
    print('el doble de', num, '=', doblar_numero(num) )
    print()
# end

print('-------------------')

presentar_resultados_2(2)
