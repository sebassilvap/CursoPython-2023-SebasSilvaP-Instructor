# =================================================================
# Bucle while

# - bucle / loop => bloque de código que se ejecuta varias veces
# - se ejecuta siempre y cuando la condición que se evalúa es True
# - cada que vez que se ejecuta => se llama iteración
# - while == MIENTRAS
# - mientras una condición sea True => se ejecuta por siempre
#! tener cuidado de caer en un bucle infinito

'''
while (condicion):
    bloque de código
'''

#* NOTA:
# - los bucles nos permiten sacar el mayor provecho a nuestro computador
# - podemos realizar una serie de cálculos en fracciones de segundo
# - en cada iteración
# - aquí empieza lo bueno de esto :)
# =================================================================


#? 1) ERROR común siempre a evitar
print('\n1) ERROR común siempre a evitar')
#! IMPORTANTE

'''
while True:
    print('Lo siento :( bucle infinito')
# end while
'''



#? 2) La condición debe cambiar algún momento a False
print('\n2) La condición debe cambiar algún momento a False')

iterador = 0

#! ERROR Fatal => no incrementar el iterador
# => tranquilos :) siempre al inicio!
'''
while iterador <= 10:
    print(iterador)
# end while
'''

# => Corrigiendo el error
# - el iterador cambia en cada iteración

while iterador <= 10:
    print(iterador)
    iterador += 1 # de esta manera cada iteración tenemos un incremento
# end while



#? 3) Bucle while básico para incremento & decremento
print('\n3) Bucle while básico para incremento & decremento')

contador_a = 0 # para contar del 0 al 5
contador_b = 5 # para contar del 5 al 0


# ---------------------------
# 3.1) Incremento
print('\n3.1) Incremento\n')
# ---------------------------

while contador_a <= 5:
    print('Contador_A =', contador_a)
    contador_a += 1 #! no olvidar esto!!
# end while


# ---------------------------
# 3.2) Decremento 
print('\n3.2) Decremento\n')
# ---------------------------

while contador_b >= 0:
    print('Contador_B =', contador_b)
    contador_b -= 1 #! IMPORTANTE
# end while

# => los valores quedan alterados / modificados al final del bucle
print()
print('contador_a =', contador_a) # 6
print('contador_b =', contador_b) # -1


# * NOTA:
# - al poner <= y >= con el igual incluimos el valor límite
# - esto pasaría al no incluirlo

contador_a = 0
contador_b = 5


# ---------------------------------------
# 3.3) Incremento - Ejemplo 2
print('\n3.3) Incremento - Ejemplo 2\n')
# ---------------------------------------

while contador_a < 5: # quitamos =
    print('Contador_A =', contador_a)
    contador_a += 1 #! no olvidar esto!!
# end while


# ----------------------------------------
# 3.4) Decremento - Ejemplo 2
print('\n3.4) Decremento - Ejemplo 2\n')
# ----------------------------------------

while contador_b > 0: # quitamos =
    print('Contador_B =', contador_b)
    contador_b -= 1 #! IMPORTANTE
# end while