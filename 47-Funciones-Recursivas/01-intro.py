# ==================================================================
# Funciones Recursivas

# - Python acepta la recursión de funciones
# - Básicamente es cuando una función se llama a sí misma
# - Es un concepto matemático y de programación
# ! Tener cuidado
# ! Es fácil quedar en una función que nunca va a terminar

# * IMPORTANTE
# - cualquier cosa que se pueda hacer con función recursiva
# - también puede ser hecha con bucle, condicional y función normal
# - la función recursiva es una forma más científica
# - de expresar nuestras funciones
# - y más elegante
# ==================================================================

#? 1) Ejemplo Básico de Función Recursiva
print('\n1) Ejemplo Básico de Función Recursiva')

# => contador de 1 a X

# -------------------------
# 1.1) Con Función normal
# -------------------------
print('\n1.1) Con Función normal\n')

def contador(x):
    lista = list( range(1,x+1) )
    lista.reverse()
    
    for i in lista:
        print(i)
    # end for
# end def

# -- TEST --
contador(10)


# ----------------------------
# 1.2) Con Función Recursiva
# ----------------------------
print('\n1.2) Con Función Recursiva\n')

def contador(x):
    if x > 0:
        print(x)
        contador(x-1)
    # end if
# end def

# -- TEST --
contador(10)



#? 2) Ejemplos Clásico: Sumatorio
print('\n2) Ejemplos Clásico: Sumatorio')

# EJ:
# sumatorio(4) = 1 + 2 + 3 + 4 = 10
# sumatorio(5) = 1 + 2 + 3 + 4 + 5 = 15 = sumatorio(4) + 5


# ------------------------
# 2.1) Con Función normal
# ------------------------
print('\n2.1) Con Función normal\n')

def sumatorio(num):
    resultado = 0
    i = 1
    while i <= num:
        resultado += i
        i += 1
    # end while
    return resultado
# end def

# -- TEST --
print( sumatorio(4) )
print( sumatorio(5) )


# ---------------------------
# 2.2) Con Función Recursiva
# ---------------------------
print('\n2.2) Con Función Recursiva\n')

# sumatorio(4) = 4 + 3 + 2 + 1 = 10

def sumatorio(num):
    if num > 0:
        return num + sumatorio(num-1)
    else:
        return 0
    # end if
# end def

# -- TEST --
print( sumatorio(4) )
print( sumatorio(5) )
        

#? 3) Ejemplos Clásico: Factorial
print('\n3) Ejemplos Clásico: Factorial')

# EJ:
# factorial(3) = 3! = 3 x 2 x 1 = 6
# factorial(4) = 4! = 4 x 3 x 2 x 1 = 24 = 4 * factorial(3)


# -------------------------
# 3.1) Con Función normal
# -------------------------
print('\n3.1) Con Función normal\n')

def factorial(num):
    i = 1
    resultado = 1
    
    while i <= num:
        resultado *= i
        i += 1
    # end while
    
    return resultado
# end def

# -- TEST --
print( factorial(3) )
print( factorial(4) )


# ---------------------------
# 3.2) Con Función Recursiva
# ---------------------------
print('\n3.2) Con Función Recursiva\n')

def factorial(num):
    if num >= 1:
        return num * factorial(num-1)
    else:
        return 1
    # end if
# end def

# -- TEST --
print( factorial(3) )
print( factorial(4) )



#? 4) Evitar Recursión ETERNA
print('\n4) Evitar Recursión ETERNA')
# - la mejor manera de evitar esto
# - es siempre fijar un condicional
# - que en algún momento termine la recursión


# ------------------------------------------
# 4.1) Ejemplo de error de recursión eterna
# ------------------------------------------
print('\n4.1) Ejemplo de error de recursión eterna\n')

# cuenta_regresiva(3) => 3...2...1...0...

'''
def cuenta_regresiva(num):
    return str(num) + '...' + cuenta_regresiva(num-1)
# end def

cuenta_regresiva(3)
'''
#! RecursionError: maximum recursion depth exceeded while getting the str of an object


# ------------------------
# 4.2) Corrigiendo Error
# ------------------------
print('\n4.2) Corrigiendo Error\n')

def cuenta_regresiva(num):
    if num >= 0:
        return str(num) + '...' + cuenta_regresiva(num-1)
    else:
        return ''
# end def

# -- TEST --
print( cuenta_regresiva(3) )

# - el else es importante
# - y retornar algo compatible al final de la recursión
# - que no nos afecte el resultado final


# -------------------------
# 4.3) Mejorando el código
# -------------------------
print('\n4.3) Mejorando el código\n')
# - podemos añadir más condicionales
# - y retornos
# - para mejorar el resultado de la función

# cuenta_regresiva(3) = 3...2...1...0 => FELIZ AÑO NUEVO

def cuenta_regresiva(num):
    if num > 0:
        return str(num) + '...' + cuenta_regresiva(num-1)
    elif num == 0:
        return '0 => FELIZ AÑO NUEVO!'
# end def


# -- TEST --
print( cuenta_regresiva(5) )
print( cuenta_regresiva(10) )