# =========================================================================
# Función Interna input()
# PARTE 2

# - Lectura por teclado / Entrada de datos
# - Otra función interna de Python
# - De esta manera podemos almacenar entradas del usuario en la terminal
# - y adicionalmente podemos guardar este valor en una variable
#! NOTA IMPORTANTE:
# - el valor que devuelve la consola es un string
# =========================================================================

#? Script de Python para saludar e interactuar con el usuario

nombre = input('Ingrese su nombre : ')

#edad = input('Ingrese su edad : ')
#edad = int(edad)

## => podemos resumir las 2 anteriores líneas en una
# (funciones en cadena
edad = int( input('Ingrese su edad : ') )
edad_next_year = edad + 1

# Impresión en la consola:

print('-------------------')
print('Un gusto en conocerte', nombre)
print('El día de ahora tienes:', edad, 'años')
print('Pero el próximo año vas a tener', edad_next_year, 'años')
print('Me despido, fue un gusto conocerte', nombre)
print('-------------------')
