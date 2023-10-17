# ==========================================================
# Palabra Clave / Keyword => Return

# - return => devuelve un valor de la función
# - ya hemos visto esto antes
# - EJ: el método .pop() en listas
# - una vez que se lo define => marca el fin de la función
# * una función con condicional puede tener varios return
# ==========================================================

#? 1) Función Básica con return
print('\n1) Función Básica con return')

def retornar_algo():
    return 'Hola Mundo'
# end

# => ejecutando de esta manera no pasa nada
retornar_algo()

# - podemos guardar en una variable e imprimir
# - o podemos imprimir directamente

resultado = retornar_algo()
print(resultado)

print( retornar_algo() )



#? 2) Varios return => función + condicional if
print('\n2) Varios return => función + condicional if')

def analizar_1_al_10(numero):
    if numero >= 1 and numero <= 5:
        return 'Numero del 1 al 5'
    elif numero > 5 and numero <= 10:
        return 'Número del 6 al 10'
    else:
        return 'Número fuera de rango 1 al 10'
# end def

# TEST:
print( analizar_1_al_10(4) )
print( analizar_1_al_10(6) )
print( analizar_1_al_10(20) )



#? 3) Cuando no defino todos los return posibles => None
print('\n3) Cuando no defino todos los return posibles => None')

def analizar_1_al_10(numero):
    if numero >= 1 and numero <= 5:
        return 'Numero del 1 al 5'
    elif numero > 5 and numero <= 10:
        return 'Número del 6 al 10'
# end def

# TEST:
r1 = analizar_1_al_10(4)
r2 = analizar_1_al_10(6)
r3 = analizar_1_al_10(20)

print( r1, type(r1) )
print( r2, type(r2) )
print( r3, type(r3) ) # None <class 'NoneType'>

# - en otros lenguajes, al definir una función con return
# - y utilizar condicionales
# - estamos obligados a retornar algo
# - python retorna siempre algo de una función
# - en este caso retorna un dato de tipo NoneType
# * Recordar el None



#? 4) Por defecto toda función retorna un None
print('\n4) Por defecto toda función retorna un None')

def saludar():
    print('Hola amigo!')
# end def

saludar()

print( saludar() ) # ejecuta el print, pero me devuelve un None!