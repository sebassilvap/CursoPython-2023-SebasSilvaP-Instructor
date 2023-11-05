# ================================================================================
# Python - Dictionary Comprehension
# (Comprensión / Entendimiento de Diccionarios)

# - al igual que en las listas
# - es una manera dinámica / inteligente
# - para crear un diccionario a partir de otro diccionario

#*  A) dict = {KEY: expresión + bucle FOR (KEY, VALUE) + in + ITERABLE}
#*  B) dict = {KEY: expresión + bucle FOR (KEY, VALUE) + in + ITERABLE + condicional IF}
#*  C) dict = {KEY: condicional IF/ELSE + bucle FOR (KEY, VALUE) + in + ITERABLE}
#*  D) dict = {KEY: función(VALOR) + bucle FOR (KEY, VALUE) + in + ITERABLE}

# https://www.datacamp.com/tutorial/python-dictionary-comprehension

# ================================================================================


#? 1) dict = {KEY: expresión + bucle FOR (KEY, VALUE) + in + ITERABLE}
print('\n1) dict = {KEY: expresión + bucle FOR (KEY, VALUE) + in + ITERABLE}')

pesos_personas_kg = {
    'Juan' : 80,
    'Andrea' : 55,
    'Carlos' : 75,
    'Ximena' : 60
}

pesos_personas_lb = { key: (value * 2.2046) for(key, value) in pesos_personas_kg.items() }

print(pesos_personas_kg)
print(pesos_personas_lb)

# NOTA:
# - los nombres key, value pueden ser cualquier cosa
# - recordar que al momento que iteramos un diccionario.items()
# - la primera variable hace referencia a las CLAVES / KEYS
# - la segunda variable hace referencia a los VALORES / VALUES

pesos_personas_lb = { clave: f'{valor * 2.2046:.2f} lb' for(clave, valor) in pesos_personas_kg.items() }

print(pesos_personas_lb)



#? 2) dict = {KEY: expresión + bucle FOR (KEY, VALUE) + in + ITERABLE + condicional IF}
print('\n2) dict = {KEY: expresión + bucle FOR (KEY, VALUE) + in + ITERABLE + condicional IF}')

notas = {
    'Daniel' : 16,
    'Pedro' : 14,
    'Sebastián' : 13,
    'Santiago' : 19,
    'Eduardo' : 11,
    'Rodrigo' : 20,
    'Francisco' : 12,
    'María' : 14,
}

estudiantes_aprobados = { key: value for (key, value) in notas.items() if value > 14 }

estudiantes_reprobados = { key: value for (key, value) in notas.items() if value <= 14 }

print(notas)
print(estudiantes_aprobados)
print(estudiantes_reprobados)



#? 3) dict = {KEY: condicional IF/ELSE + bucle FOR (KEY, VALUE) + in + ITERABLE}
print('\n3) dict = {KEY: condicional IF/ELSE + bucle FOR (KEY, VALUE) + in + ITERABLE}')

aprobado_reprobado = { key: ('aprobado' if value > 14 else 'reprobado') for(key, value) in notas.items() }

print(aprobado_reprobado)



#? 4) dict = {KEY: función(VALOR) + bucle FOR (KEY, VALUE) + in + ITERABLE}
print('\n4) dict = {KEY: función(VALOR) + bucle FOR (KEY, VALUE) + in + ITERABLE}')
# - este último se usa cuando la condición es muy difícil de expresar
# - en una sola línea
# - en este caso, utilizamos una función

notas = {
    'Daniel' : 16,
    'Pedro' : 14,
    'Sebastián' : 13,
    'Santiago' : 19,
    'Eduardo' : 11,
    'Rodrigo' : 20,
    'Francisco' : 12,
    'María' : 14,
}

def check_estudiante(nota):
    if nota > 14 and nota <= 20:
        return 'Aprobado'
    elif nota == 14:
        return 'Supletorio'
    elif nota >= 12 and nota < 14:
        return 'Pierde el Cupo'
    elif nota >= 0 and nota < 12:
        return 'Pierde el Año'
    else:
        return 'ERROR - Nota'
# end def

analisis_estudiante = { key: check_estudiante(value) for(key, value) in notas.items() }

print(notas)
print(analisis_estudiante)