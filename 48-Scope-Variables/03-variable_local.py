# =====================================================
# Variables Locales & Ambiente Local

# - una variable creada en el ambiente local
# - es decir en una función
# - existe solo dentro de esta función
# - y no podemos ni acceder desde afuera en el global
# - o en otras funciones
# =====================================================


#? 1) Cada variable local creada existe SÓLO dentro de la función donde se la crea
print('\n1) Cada variable local creada existe SÓLO dentro de la función donde se la crea')

a = 10

def funcion1():
    b = 20
# end def

def funcion2():
    c = 30
# end def

def funcion3():
    print(b)
    print(c)
# end def

#funcion3()
#! NameError: name 'b' is not defined



#? 2) Tampoco funciona si hacemos return e invocamos dentro de otra función
print('\n2) Tampoco funciona si hacemos return e invocamos dentro de otra función')

def funcion_4():
    d = 40
    return d
# end def

def funcion_5():
    funcion_4()
    print(d)
# end def

#funcion_5()
#! NameError: name 'd' is not defined.



#? 3) No podemos declarar global de una variable local en el ambiente global
print('\n3) No podemos declarar global de una variable local en el ambiente global')

global d
#print(d) #! NameError: name 'd' is not defined.



#? 4) No podemos definir global de una variable global en al ambiente global
print('\n4) No podemos definir global de una variable global en al ambiente global')
# - no tiene sentido hacer esto

e = 8
print(e)

#global e #! SyntaxError: name 'e' is used prior to global declaration



#? 5) No sirve de nada declarar una variable como global en el ambiente global
print('\n5) No sirve de nada declarar una variable como global en el ambiente global')

global f
f = 55

def cambiar_valor():
    f += 10
# end def

#cambiar_valor()
#! UnboundLocalError: cannot access local variable 'f' where it is not associated with a value