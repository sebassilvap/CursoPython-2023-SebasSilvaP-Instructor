# ==========================================
# Funciones: Parámetros y Retorno

# - una función puede:
#   => tener o no parámetros
#   => tener o no retorno

# - Parámetros: variables de la función
# - Retorno: valor que devuelve la función
# ==========================================


#? 1) Función SIN parámetros y SIN retorno
print('\n1) Función SIN parámetros y SIN retorno')

# => definición
def saludar():
    print('Muy buenos días!')
# end def

def despedirse():
    print('Chao!')
# end def

# => invocación
saludar()
despedirse()



#? 2) Función CON parámetros y SIN retorno
print('\n2) Función CON parámetros y SIN retorno')

# => definición
def hola(n):
    print('Hola', n, 'que tengas un buen día!')
# end def

# => invocación
persona = 'Sebas'
hola(persona)
hola('Carlos')
#hola() #! TypeError: hola() missing 1 required positional argument: 'n'



#? 3) Función SIN parámetros y CON retorno / return
print('\n3) Función SIN parámetros y CON retorno / return')
# - ya hemos visto el retorno antes
# - en algunos métodos
# - luego veremos que los métodos son a la final funciones
# - (funciones de una clase*)
# - por ej:

lista = [1,2,3,4]

# => método .pop() devuelve / retorna el elemento eliminado
# - y por eso podíamos guardar este retorno
# - en una variable
# - o puede ir directamente en un print por ejemplo
eliminado = lista.pop()
print(eliminado)

print( lista.pop() )

# => ejemplo con función
def devolver_pi():
    return 3.14159
# end def

devolver_pi()

# - de igual manera para ver su contenido
# - guardamos en una variable y hacemos print
# - o hacemos print directamente

numero_pi = devolver_pi()
print(numero_pi)

print( devolver_pi() )



#? 4) Función CON parámetros y CON retorno / return
print('\n4) Función CON parámetros y CON retorno / return')

def suma( a, b ):
    print('La suma de', a, '+', b, '=', a + b)
    return a + b
# end def

suma(5,6)
# La suma de 5 + 6 = 11

print( suma(9,8) )
# La suma de 9 + 8 = 17
# 17

# => podemos guardar en una variable
resultado = suma(10,25)
print(resultado)