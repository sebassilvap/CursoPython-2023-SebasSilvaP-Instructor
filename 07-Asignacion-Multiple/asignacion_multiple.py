# =======================================================
# Asignación Múltiple de Valores

# - Formas permitidas en la SINTAXIS de Python
# - Para crear varias variables en una línea de código
# =======================================================

# 1) Asignación normal aprendida
nombre = 'Sebastián'
apellido = "Silva"
edad = 36
es_estudiante = False
es_profesor = True
nota = 75.8

print(nombre, apellido, edad, es_estudiante, es_profesor, nota)


# 2) Reasignación de valores utilizando técnica de asignación múltiple
#?  variable_1, variable_2, ... = valor_1, valor_2, ...

nombre, apellido, edad, es_estudiante, es_profesor, nota = 'Diego', 'Costa', 15, True, False, 95.5
print(nombre, apellido, edad, es_estudiante, es_profesor, nota)

# 3) Reasignación de varias variables a valor único

# => manera clásica
edad_juan = 15
edad_maria = 15
edad_santiago = 15
edad_pedro = 15
edad_andrea = 15

print( edad_juan, edad_maria, edad_santiago, edad_pedro, edad_andrea )

# => asignación múltiple

edad_juan = edad_maria = edad_santiago = edad_pedro = edad_andrea = 17

print( edad_juan, edad_maria, edad_santiago, edad_pedro, edad_andrea )

# => si deseo cambiar ahora solo 1
edad_juan = 20

print( edad_juan, edad_maria, edad_santiago, edad_pedro, edad_andrea )



