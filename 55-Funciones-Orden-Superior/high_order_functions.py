# =============================================================
# Funciones de Orden Superior
# (en inglés: High Order Functions)

# - Una función de orden superior
# - o función de alto orden, es aquella 
# - que cumple 1 de estas 2 características:

# *   A) puede aceptar otra función como ARGUMENTO
# *   B) puede RETORNAR una 2da función definida en la 1era

# - como vimos en la lección pasada
# - las funciones, y todo en Python
# - es una variable con dato (un objeto*)
# ! Una definición podría ser: Son como funciones anidadas
# =============================================================


#? 1) High Order Function: Función como Argumento
print('\n1) High Order Function: Función como Argumento')

# ---------------------------
# 1.1) Ejemplo 1
print('\n1.1) Ejemplo 1\n')
# ---------------------------

# => funciones normales
def gritar(msg):
    return msg.upper()
# end def

def en_voz_baja(msg):
    return msg.lower()
# end def

# => función de alto grado
# (high order function)
def saludar(funcion):
    saludo = funcion('Hola mi Estimado! Saludos!')
    print(saludo)
# end def

# => Invocando high order function
# - las funciones de argumento no se invoca
# - pasa solo su nombre, su firma

saludar(gritar) # HOLA MI ESTIMADO! SALUDOS!
saludar(en_voz_baja) # hola mi estimado! saludos!

#saludar(gritar())
#! TypeError: gritar() missing 1 required positional argument: 'msg'


# ---------------------------
# 1.2) Ejemplo 2
print('\n1.2) Ejemplo 2\n')
# ---------------------------

# => funciones normales
def mover_robot_en_X():
    return('Robot avanza en coordenada X')
# end def

def mover_robot_en_Y():
    return('Robot avanza en coordenada Y')
# end def

def mover_robot_en_XY():
    return('Robot avanza en coordenadas XY')
# end def

# => high order function
def operar_robot(funcion):
    print( 'Robot en Movimiento | {}'.format(funcion()) )
# end def

# TEST
operar_robot(mover_robot_en_X)
operar_robot(mover_robot_en_Y)
operar_robot(mover_robot_en_XY)



#? 2) High Order Function: 2da Función como RETORNO de 1era
print('\n2) High Order Function: 2da Función como RETORNO de 1era')
# - vamos a ver un ejemplo básico
# - simulando una división
# - cada uno de sus elementos de operación

# ---------------------------
# 2.1) Ejemplo 1
print('\n2.1) Ejemplo 1\n')
# ---------------------------
# - ejemplo más básico 
# - ver esta high order function
# - como una función externa, y la de dentro
# - como una función interna

def funcion_externa():
    def funcion_interna():
        print('Hola desde dentro!')
    # end def
    funcion_interna()
# end def


funcion_externa() # Hola desde dentro!
#funcion_interna() #! NameError: name 'funcion_interna' is not defined.

# - igual que las variables
# - la función interna se encuentra en un ambiente local
# - no puede ser accedida desde el global


# ---------------------------
# 2.2) Ejemplo 2
print('\n2.2) Ejemplo 2\n')
# ---------------------------

"""
7  |___ 3
-6      2
1

7 => dividendo
3 => divisor
2 => cociente
1 => residuo

"""

# => definición de la high order function

def divisor(a):
    def dividendo(b):
        return b/a
    # end def
    return dividendo
# end def


# 1era Manera de Invocar la función
print('\n1era Manera de Invocar la función\n')

resultado_division = divisor(3) # pasamos el divisor

print(resultado_division)
# <function divisor.<locals>.dividendo at 0x000001E7F21EA3E0>

print( resultado_division(7) ) # pasamos el dividendo
# 2.3333333333333335


# 2da manera de Invocar la función
print('\n2da manera de Invocar la función\n')

resultado = divisor(3)
resultado = resultado(7)
print(resultado) # 2.3333333333333335


# 3era manera de Invocar la función
print('\n3era manera de Invocar la función\n')
# - una manera un poco más abstracta de entender
# - pero también lo podríamos hacer de esta manera
# - doble paréntesis ()()
# - hacer una analogía al doble index de listas 2D [][]

resultado_1 = divisor(3)(7)
resultado_2 = divisor(4)(10)
resultado_3 = divisor(3)(15)

print( f'{resultado_1:.2f}' )
print( f'{resultado_2:.2f}' )
print( f'{resultado_3:.2f}' )


# ---------------------------
# 2.3) Ejemplo 3
print('\n2.3) Ejemplo 3\n')
# ---------------------------

# velocidad = distancia / tiempo

# => Fórmula de Velocidad con Función Normal
print('\n=> Fórmula de Velocidad con Función Normal\n')

def calcular_velocidad(distancia, tiempo):
    return distancia / tiempo
# end def

d = 10 # 10 metros
t = 60  # 1 minuto

print( calcular_velocidad(d,t) )


# => Fórmula de Velocidad con High Order Function
print('\n=> Fórmula de Velocidad con High Order Function\n')

def distancia(d):
    def tiempo(t):
        return d/t
    # end def
    return tiempo
# end def

velocidad_distancia = distancia(10)
velocidad_distancia_tiempo = velocidad_distancia(60)

# TEST:
print(velocidad_distancia_tiempo)
print( distancia(10)(60) )