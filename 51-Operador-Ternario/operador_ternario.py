# =================================================================
# Operador Ternario en Python

# - también se los llama "expresión condicional"
# - es una versión abreviada de un condicional if
# - se puede usar en expresiones sencillas
# - que generalmente impliquen un if y un else

# - En otros lenguajes, por ejemplo JavaScript se lo escribe así:

'''
let nota = 13

let decision = nota <= 14 ? "ha reprobado" : "ha pasado"

console.log("El estudiante", decision)
'''

# - En Python se escribe de esta manera

# *   <valor cuando True> if <condicion> else <valor cuando False>
# =================================================================


#? 1) Ejemplo Básico de Operador Ternario
print('\n1) Ejemplo Básico de Operador Ternario')

# -------------------
# => condicional if
# -------------------
edad = 14
resultado = ''

if edad >= 18:
    resultado = 'Mayor de Edad'
else:
    resultado = 'Menor de Edad'
# end if

print(resultado)

# ----------------------
# => operador ternario
# ----------------------
edad = 19

resultado = 'Mayor de Edad' if edad >= 18 else 'Menor de Edad'
print(resultado)



#? 2) Operador Ternario con Operadores Lógicos y Operadores Booleanos de Comparación
print('\n2) Operador Ternario con Operadores Lógicos y Operadores Booleanos de Comparación')
# - Operadores Lógicos: not , and , or
# - Operadores de Comparación: > , < , >= , <= , == , !=

# -------------------
# => condicional if
# -------------------

temperatura = 45
clima = ''

if  not (temperatura > 30 or temperatura < 10):
    clima = 'Buen Clima!'
else:
    clima = 'Mal Clima...'
# end if

print(clima)

# => RECORDAR / Traducción:
# - una buena práctica es pasar una expresión condicional a las palabras propias
# - en este caso sería:
'''
Si la temperatura no es mayor a 30
ni tampoco menor a 10
tenemos un "Buen Clima!"
Caso contrario, tenemos un "Mal Clima..."
'''
    
# ----------------------
# => operador ternario
# ----------------------

clima = 'Buen Clima' if not (temperatura > 30 or temperatura < 10) else 'Mal Clima...'
print(clima)

#? 3) Ejemplo no Recomendado => Operador Ternario Complejo
print('\n3) Ejemplo no Recomendado => Operador Ternario Complejo')
# - cuando la escritura del operador ternario se vuelve compleja
# - es preferible utilizar el condicional if
# - RECORDAR, el código no debe ser complejo de leer o entender
# ! NO RECOMENDADO

opcion = 2
comando = ''

# -------------------
# => condicional if
# -------------------

if opcion == 1:
    comando = 'Comprar'
elif opcion == 2:
    comando = 'Vender'
elif opcion == 3:
    comando = 'Salir'
else:
    comando = 'Error'
# end if

print(comando)


# ----------------------
# => operador ternario
# ----------------------

orden = 'Comprar' if opcion == 1 else 'Vender' if opcion == 2 else 'Salir' if opcion == 3 else 'Error'

print(orden)

