# =================================
# Variables

# - una variable es un CONTENEDOR
# - para almacenar un VALOR
# =================================


# 1) Crear una variable en python
x = 'Hola Mundo'
# Aquí suceden dos cosas:
# 1) x              => declarando una variable con el nombre 'x'
# 2) = 'Hola Mundo' => asignamos un valor a la variable de nombre 'x'
print()
print('------------------- (1) -------------------')

print('Hola Mundo')
print(x)


# 2) Por el momento conocemos 2 tipos de datos
#   - cadena de texto (string - str)
#   - número entero   (int)
#! La siguiente lección hablamos en profundidad de los tipos de datos en Python
print()
print('------------------- (2) -------------------')

# nombre_variable = valor

nombre = 'Sebastián'
apellido = "Silva" # recordar '' ó "" es igual
edad = 36
es_estudiante = False # tipo de dato booleano - False (Falso)
es_profesor = True # tipo de dato booleano - True (Verdadero)

# impresión en la consola
print(nombre)
print(apellido)
print(edad)
print(es_estudiante)
print(es_profesor)


# 3) Normas de buena escritura en Python
# - nombre de la variable en minúsculas
# - cuando son varias palabras => separadas con guión bajo => _
# - se utiliza mayúculas para constantes
# - no iniciar con mayúsculas => eso se hace en clases (tema que veremos luego)
# - recomendaciones para buena práctica de programación en python
# - su nombre tiene que ser descriptivo de lo que es la variable
print()
print('------------------- (3) -------------------')

Saludo = 'hola' # X
letra = 'A' # OK
numeroDeTelefono = 123456789 # X (nomenclatura usada en otros lenguajes)
numero_de_telefono = 123456789 # OK

# RECORDAR: Recomendaciones de buena práctica / más no ERROR

print(Saludo)
print(letra)
print(numeroDeTelefono)
print(numero_de_telefono)



# 4) Impresión de variables en print
# 1 FORMA ==> pasarlos como PARÁMETROS de la función print / separados con una coma
print()
print('------------------- (4) -------------------')

# el espacio después de la coma, no afecta la impresión en consola
print(nombre, apellido, edad, es_estudiante, es_profesor)
print(nombre,apellido,edad,es_estudiante,es_profesor)
print(nombre,   apellido, edad,es_estudiante, es_profesor)

# podemos pasar valores sin ser declarados como variable también
print() # técnica sencilla para espacio en blanco

#      1      2      3       4     5        6        7       8
print(nombre,'A', apellido, 2222, edad, es_estudiante,'XYZ', es_profesor)

#! hay otras maneras pero veremos luego !


# 5) Ejercicio Básico - print() de variables y valores 
# Podemos utilizar lo aprendido para imprimir información de manera más estructurada
print()
print('------------------- (5) -------------------')

print()
print('*********************************')
print('Su nombre es:', nombre, apellido)
print('Tiene', edad, 'años')
print('¿Es estudiante? :', es_estudiante)
print('¿Es profesor? :', es_profesor)
print('*********************************')


# 6) DATO CURIOSO
# - en otros lenguajes de programación para declarar una variable
# - se debe especificar el tipo de dato
# - en python no
# - en python el tipado es asumido por python mismo

# EJ en JAVA:
# int edad = 36;

# En Python:
# edad = 36