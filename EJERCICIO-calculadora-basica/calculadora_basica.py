# ===========================================================
## EJERCICIO
# - Realizar una calculadora básica con lo aprendido
# - Básicamente el usuario debe ingresar 2 números
# - Por la terminal con el teclado
# - Efectuar las operaciones aritméticas básicas aprendida
# - Mostrar los resultados al usuario utilizando print
# ===========================================================

print('**** Calculadora Básica realizada en Python ****')
n1 = float( input('Ingrese un PRIMER número : ') )
n2 = float( input('Ingrese un SEGUNDO número : ') )

# Operaciones y almacenamiento de Variables
suma = n1 + n2
resta = n1 - n2
producto = n1 * n2
division = n1 / n2
exponente = n1 ** n2
modulo = n1 % n2

print('**** Los resultados son los siguientes ****')
print('1) SUMA :', n1, '+', n2, '=', suma)
print('2) RESTA :', n1, '-', n2, '=', resta)
print('3) PRODUCTO :', n1, '*', n2, '=', producto)
print('4) DIVISIÓN :', n1, '/', n2, '=', division)
print('5) EXPONENTE :', n1, '**', n2, '=', exponente)
print('6) MÓDULO :', n1, '%', n2, '=', modulo)
print('**** FIN DE LOS CÁLCULOS ****')