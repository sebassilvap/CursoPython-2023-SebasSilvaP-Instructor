# =========================================================================
# Función Interna input()
# PARTE 1

# - Lectura por teclado / Entrada de datos
# - Otra función interna de Python
# - De esta manera podemos almacenar entradas del usuario en la terminal
# - y adicionalmente podemos guardar este valor en una variable
#! NOTA IMPORTANTE:
# - el valor que devuelve la consola es un string
# =========================================================================

#? 1) Ejemplo básico de input() y tipo de dato
#input('Escriba algo : ')

# => tiene más sentido sin guardamos esto en una variable

#? 2) Guardando el valor de input
'''
nombre = input('Su nombre : ')
print(nombre)
print( type(nombre) ) # el tipo siempre va a ser un string
'''

#? 3) Si deseo ingresar un número => casting
#! Clásico error en un inicio

edad = input('¿Cuántos años tiene? : ')
print(edad , '|' , type(edad))
#print('El próximo año tendrá: ' , edad + 1) #! TypeError

print('El próximo año tendrá :', int(edad) + 1 , 'años')
