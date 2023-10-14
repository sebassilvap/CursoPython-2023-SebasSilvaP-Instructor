# ==============================================================================
# Scope / Ambiente de Parámetros y Argumentos

# * RECORDAR:
# - Parámetros => variables en la definición de la función
# - Argumentos => variables / valores con los que se llama / invoca la función
# ==============================================================================


#? 1) Parámetros: Existen solo en el ambiente local
print('\n1) Existen solo en el ambiente local')

def mostrar_numero(x):
    print(x)
# end def

#print(x) #! NameError: name 'x' is not defined



#? 2) Parámetros: Sobrescriben cualquier variable global con el mismo nombre
print('\n2) Parámetros: Sobrescriben cualquier variable global con el mismo nombre')

nombre = 'Sebas'

# => RECORDAR:
# - dentro de una función / ambiente local
# - podemos acceder a una variable local
# - más no modificarla a menos que usemos "global"

def mostrar():
    print(nombre)
# end def

mostrar()


# => el parámetro sobreescribe cualquier variable global
# - que tenga el mismo nombre del parámetro
# - en este caso nombre existe solo dentro de la función
# - no tiene nada que ver con la variable global nombre

def mostrar(nombre):
    print(nombre)
# end def

#mostrar()
#! TypeError: mostrar() missing 1 required positional argument: 'nombre'

mostrar(nombre) # el argumento es la variable global creada antes



#? 3) Una variable no puede ser declarada global y ser parámetro al mismo tiempo
print('\n3) Una variable no puede ser declarada global y ser parámetro al mismo tiempo')
# - sin necesidad de invocar la función esto nos da un error
# - es un error de sintaxis hacer esto

numero = 10

'''
def doblar_numero(numero):
    global numero
    return numero * 2
# end def
'''
#! SyntaxError: name 'numero' is parameter and global



#? 4) RECORDAR: Pueden haber varias funciones que tengan el mismo nombre del parámetro
print('\n4) RECORDAR: Pueden haber varias funciones que tengan el mismo nombre del parámetro')

num = 10

def sumar10(num):
    return num + 10
# end def

def sumar20(num):
    return num + 20
# end def

def cambiar_num(num):
    num = 100
    return num 
# end def

r1 = sumar10(num)
r2 = sumar20(num)
r3 = cambiar_num(num)

print(num, r1, r2, r3)



#? 5) Parámetro por defecto no afecta avariable global
print('\n5) Parámetro por defecto no afecta avariable global')
# - posiblemente esté de más aclarar esto
# - pero es importante hacerlo
# - si asignamos con = un parámetro por defecto
# - esto no afecta a una variable global
# - si la variable global y el parámetro tienen el mismo nombre
# - o cuando asignamos el argumento por nombre

p = 9

def imprimir_num(p = 0):
    print(p)
# end def

print(p)
print('-----------')
imprimir_num()
imprimir_num(p = 50)
imprimir_num(p = 50)
imprimir_num(p)
imprimir_num(5)
print('-----------')
print(p)