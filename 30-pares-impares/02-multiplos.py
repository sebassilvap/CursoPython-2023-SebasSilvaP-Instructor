# ================================================
# Recorriendo los múltiplos

# - Como vimos con el módulo podemos identificar
# - Fácilmente pares e impares
# - Pero no solo eso
# - También podemos identificar los múltiplos

# EJ: cualquier número múltiplo de 5

#   25 |___ 5
#  -25      5
#*   0
# ================================================

#? 1) EJ: Múltiplos de 7 en lista del 1 al 100
print('\n1) EJ: Múltiplos de 7 en lista del 1 al 100')

multiplos_siete = []

for i in range(1,101):
    if i % 7 == 0:
        multiplos_siete.append(i)
    # => else es innecesario, con if basta
# end for

print(multiplos_siete)


#? 2) EJ: Múltiplos del 8 en lista del 1 al 100
print('\n2) EJ: Múltiplos del 8 en lista del 1 al 100')

multiplos_ocho = []

contador = 1

while contador <= 100:
    if contador % 8 == 0:
        multiplos_ocho.append(contador)
    contador += 1
# end while

print(multiplos_ocho)