# =====================================================
# String Slicing con STEP (pasos)

# - el slicing tendría la siguiente fórmula general:
#*       variable_string[START : END : STEP]

# - START: índice de inicio => INCLUYENTE
# - END: índice de fin => EXCLUYENTE
# - STEP: salto o pasos
# =====================================================

#? 1) REPASO: Substring con índices positivos

cadena = 'superPalabraGrande'
#(+)      012345678901234567
#         0         1

sub_1 = cadena[0:5]
sub_2 = cadena[5:12]
sub_3 = cadena[12:18]

print(cadena)
print(sub_1)
print(sub_2)
print(sub_3)


#? 2) REPASO: Substring omitiendo índices redundantes

sub_1 = cadena[:5] # no necesitamos el 0
sub_2 = cadena[5:12]
sub_3 = cadena[12:] # no es necesario el final

print(cadena)
print(sub_1)
print(sub_2)
print(sub_3)


#? 3) Aplicando salto (step) 
step_1 = cadena[0:18:1] # step 1 => por default !
print( 'step_1 =' , step_1 )

step_2 = cadena[0:18:2] # nos saltamos 1 caracter
print( 'step_2 =' , step_2 )
print( 'step_2 =' , cadena[0:18:2] )
print( 'step_2 =' , cadena[:18:2] )
print( 'step_2 =' , cadena[::2] )
print( 'step_2 =' , cadena[ : : 2] ) # los espacios no nos afectan!

step_3 = cadena[ : : 3] # nos saltamos 2 caracteres
print( 'step_3 =' , step_3 )


#? 4) Salto Negativo => Revertir un String
print( cadena )
print( cadena[::1] )
print( cadena[::-1] ) # sin salto => revertir orden
print( cadena[::-2] ) # salto de 1 caracter => revertir orden
print( cadena[::-3] ) # salto de 2 caracteres => revertir orden


#? 5) Ejercicio: string & substring / normal & reverso
cadena = 'superPalabraGrande'

# cadena revertida
cadena_r = cadena[::-1]

# 3 substring orden normal
sub_1 = cadena[:5] # no necesitamos el 0
sub_2 = cadena[5:12]
sub_3 = cadena[12:] # no es necesario el final

# 3 substring orden reverso
sub_1_r = cadena[:5:-1]
sub_2_r = cadena[5:12:-1]
sub_3_r = cadena[12::-1]

print('** Orden Normal **')
print(cadena)
print(sub_1)
print(sub_2)
print(sub_3)
print('** Orden Reverso (solución errónea) **')
print(cadena_r)
print(sub_1_r)
print(sub_2_r)
print(sub_3_r)

#! Corrección
# - cuando el orden (salto) es inverso
# - la formación del substring también va en orden inverso
# - tenemos varias soluciones a este problema

## a) Solución sencilla
## --------------------
sub_1_r = sub_1[::-1]
sub_2_r = sub_2[::-1]
sub_3_r = sub_3[::-1]

print('\n** Orden Reverso (solución sencilla) **')
print(cadena_r)
print(sub_1_r)
print(sub_2_r)
print(sub_3_r)

## b) Solución complicada
## ----------------------
# - la misma regla se aplica
# - el primer índice (START) es incluyente
# - el segundo índice (END) es excluyente

cadena = 'superPalabraGrande'
#(+)      012345678901234567
#         0         1

sub_1_r = cadena[4::-1]
sub_2_r = cadena[14:4:-1]
sub_3_r = cadena[:11:-1]

print('\n** Orden Reverso (solución complicada) **')
print(cadena_r)
print(sub_1_r)
print(sub_2_r)
print(sub_3_r)