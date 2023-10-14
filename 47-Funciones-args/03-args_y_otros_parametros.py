# ============================================================================
# args + otros parámetros

# - yo puedo plantear mi función
# - combinando todo tipo de parámetros
# - pero si es muy complicada de entender
# - al momento de llamar la función
# - estoy en la obligación de poner el nombre del parámetro
# * básicamente python lanza error cuando la función no puede ser entendida
# ============================================================================

#? 1) Ejemplo de función combinada
print('\n1) Ejemplo de función combinada')
# - aunque en teoría yo puedo hacer esto
# - es decir, todos los tipos de parámetros pueden coexistir en la función
# - una buena práctica es definir funciones
# - que no requieran obligatoriamente (en la medida de lo posible)
# - durante su llamada o ejecución, el nombrar a los parámetros
# - más que nada para no complicar la definición de una función

def funcion_combinada(a,b,*args,c='hola',d):
    print(a)
    print(b)
    print(args)
    print(c)
    print(d)
# end def

funcion_combinada(1,2,3,4,5,6,c='hi',d=100)



#? 2) Ejemplo de buen práctica: parámetros normales + *args
print('\n2) Ejemplo de buen práctica: parámetros normales + *args')
# - en la siguiente función
# - ingreso un número multiplicador
# - y un número divisor
# - el resto es una tupla de números
# - y su objetivo es retornar los valores de la lista
# - afectados por el multiplicador y por el divisor

def producto_y_cociente(multiplicador, divisor, *valores):
    lista_multiplicada = []
    lista_dividida = []
    
    for valor in valores:
        lista_multiplicada.append(valor * multiplicador)
        lista_dividida.append(valor / divisor)
    # end for
    
    # print de resultados antes de return
    print('Lista Original =', list(valores))
    print('Producto x', multiplicador, '=', lista_multiplicada)
    print('Cociente /', divisor, '=', lista_dividida)
    
    return [lista_multiplicada, lista_dividida]
# end def

# TEST
print()
print( producto_y_cociente(3,2,100,200,300,400,500) )



#? 3) Ahora podemos entender la función interna => print()
print('\n3) Ahora podemos entender la función interna => print()')

print('sebas')
print('sebas', 36)
print('sebas', 36, 17.5)
print('sebas', 36, 17.5, end='***\n')

# - print recibe parámetros como *args
# - el end es un parámetro por defecto que imprime nueva línea
# - si no deseamos nueva línea tenemos que nombrarlo obligatoriamente
# - en la llamada de la función