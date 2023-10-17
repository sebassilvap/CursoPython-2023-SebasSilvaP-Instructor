# =============================================================
# ¿Qué es el Scope / Entorno de Variables?

# - scope = entorno = ambiente = espectro 
# - el lugar donde existen las variables

# - tenemos 2
#*      a) variables globales - global
#*      b) variables locales  - local

# - global => toda variable creada en indentación 0
# - local  => toda variable creada dentro de una función
# =============================================================


#? 1) global vs. local
print('\n1) global vs. local')

a = 10  #! variable global


def hacer_algo():
    b = 20  #! variable local
    print(b)
# end def

print(a)
#print(b) #! NameError: name 'b' is not defined


# => ¿ejecutamos función y se crea b AFUERA?
# NO
hacer_algo()
#print(b) #! #! NameError: name 'b' is not defined


# => dentro de otro tipo de indentación
# - if
# - for
# - while
# - siguen siendo variables globales
if True:
    c = 30
    

for x in range(5):
    d = 40
    

print(c)
print(d)


# => la variable creada en un for también se crea como global
print(x)

# -------------------------------------------------------------
#* RECORDAR
# - cualquier variable creada dentro de una función => LOCAL
# - el resto de variables => GLOBAL
# -------------------------------------------------------------