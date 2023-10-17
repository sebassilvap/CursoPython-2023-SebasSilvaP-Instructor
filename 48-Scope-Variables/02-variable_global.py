# ========================================
# Variables Globales

# - existen en el ambiente global y local
# - podemos acceder a ellas en ambos
# ========================================

#? 1) Podemos ACCEDER a las variables globales dentro del ambiente local
print('\n1) Podemos ACCEDER a las variables globales dentro del ambiente local')

a = 100

print(a)

def mostrar_variable():
    a
    print(a)
    print( a * 2 )
# end def

mostrar_variable()



#? 2) No podemos MODIFICAR DIRECTAMENTE una variable global dentro del ambiente local
print('\n2) No podemos MODIFICAR DIRECTAMENTE una variable global dentro del ambiente local')


# ------------------------------------------------------
# 2.1) Intento 1: Cambio directo en función
print('\n2.1) Intento 1: Cambio directo en función\n')
# ------------------------------------------------------

# a = 100
print(a)

def cambiar_variable():
    a = 150
# end def

print(a)

cambiar_variable()
print(a)


# ---------------------------------------------------------------
# 2.2) Intento 2: Cambio directo en función + return
print('\n2.2) Intento 2: Cambio directo en función + return\n')
# ---------------------------------------------------------------

# a = 100
print(a)

def cambiar_variable():
    a = 150
    print(a)
    return a
# end def

print(a)

print('----')
cambiar_variable()
print('----')

print(a)


# -----------------------------------------------------
# - esta variable a que declaro dentro de la función
# - y le asigno un valor
# - no tiene nada que ver con la a global
# -----------------------------------------------------


# ------------------------------------------------------------------------
# 2.3) Intento 3: Cambio en función con operador en asignación
print('\n2.3) Intento 3: Cambio en función con operador en asignación\n')
# ------------------------------------------------------------------------

# a = 100
print(a)

def cambiar_variable():
    a += 50
# end def

#cambiar_variable()
#! UnboundLocalError: cannot access local variable 'a' where it is not associated with a value

def cambiar_variable_2():
    z += 10
# end def

#cambiar_variable_2()
#! UnboundLocalError: cannot access local variable 'z' where it is not associated with a value

def mostrar_variables():
    print(a)
    #print(z)
# end def

#mostrar_variables()
#! NameError: name 'z' is not defined

# -----------------------------------------------------------------------
# - no puedo modificar una variable global dentro de un ambiente local
# - puedo acceder
# - puedo utilizarla
# - no puedo modificarla DIRECTAMENTE
# -----------------------------------------------------------------------



#? 3) Podemos MODIFICAR variable global dentro de local con keyword "global"
print('\n3) Podemos MODIFICAR variable global dentro de local con keyword "global"')
# - keyword global
# - para acceder y modificar una variable global
# - dentro de una función
# - dentro del ambiente local


# -------------------------------------------
# 3.1) Con operador y asignación
print('\n3.1) Con operador y asignación\n')
# -------------------------------------------

# a = 100
print(a)


def cambiar_variable():
    global a
    a += 150
# end def

print(a)

cambiar_variable()

print(a)


# ----------------------------------------
# 3.2) Con simple asignación
print('\n3.2) Con simple asignación\n')
# ----------------------------------------

m = 10
print(m)

def cambiar_valor():
    global m
    m = 55
# end def

print(m)

cambiar_valor()
print(m)


# -----------------------------------------------------
# - la función existe cuando se la invoca
# - una definición de una función no altera el código
# - si nunca se la invoca / llama
# -----------------------------------------------------