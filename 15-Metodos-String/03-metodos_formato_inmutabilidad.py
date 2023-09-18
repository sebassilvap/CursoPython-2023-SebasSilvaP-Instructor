# =======================================
# RECORDEMOS: Los String son inmutables
# =======================================

cadena = 'hola python'
print(cadena)
print(cadena[0]) 
#cadena[0] = 'H' #! TypeError: str no soporta asignación

cadena[0].upper()
print(cadena)

print( cadena[0].upper() )

#cadena[0] = cadena[0].upper() #! TypeError: str no soporta asignación

# - la asignación se da al momento que ponemos variable =
# - ya sea con un método o sobreescribiendo
# - no podemos hacer esto con strings

# => pero recordemos el truco
# - si bien es cierto
# - no podemos cambiar un índice
# - pero podemos reasignar la variable entera

cadena = 'hola python'
print(cadena)

cadena = cadena[0].upper() + cadena[1:]
print(cadena)