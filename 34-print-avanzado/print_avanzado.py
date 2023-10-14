# ====================================================================
# print avanzado

# - print es una función interna de python
# - recibe argumentos
#*  print( arg1, arg2, arg3, .... , argN, end='' )

# - los argumentos que mandemos se imprimen en la terminal
# - el end es un argumento opcional
# - con el indicamos como deseamos terminar la línea de impresión
# ====================================================================


#? 1) Recordatorio de las maneras de usar print
print('\n1) Recordatorio de las maneras de usar print')

nombre = 'Sebastián'
edad = 36
nota_final = 18.5
es_profesor = True
es_estudiante = False


# ----------------------------------------
# 1.1) print() con argumentos
print('\n1.1) print() con argumentos\n')
# ----------------------------------------
# - cuando se manda argumentos
# - no importa el tipo de dato

print(nombre, edad, nota_final, es_profesor, es_estudiante)

# - puedo ordenar las impresiones en diferentes líneas
print(
    '\nNombre :', nombre,
    '\nEdad :', edad,
    '\n¿Es profesor? :', es_profesor,
    '\n¿Es estudiante? :', es_estudiante
)


# ------------------------------------------------------
# 1.2) print() con concatenación y casting
print('\n1.2) print() con concatenación y casting\n')
# ------------------------------------------------------
# - concatenación + casting para formar un solo string
# - y poder imprimir ese string

print( nombre + str(edad) + str(nota_final) + str(es_profesor) + str(es_estudiante) )

print()

print( nombre + '\n' +
       str(edad) + '\n' + 
       str(nota_final) + '\n' + 
       str(es_profesor) + '\n' +
       str(es_estudiante) 
     )

cadena_imprimir = nombre + str(edad) + str(nota_final) + str(es_profesor) + str(es_estudiante)

print( cadena_imprimir )



#? 2) Parámetro opcional end
print('\n2) Parámetro opcional end')
# - especificamos la manera de terminar un print
# - por defecto, end = nueva línea = \n

cadena_1 = 'Hola'
cadena_2 = 'Mundo'

print(cadena_1)
print(cadena_2)

print()

print(cadena_1, end='')
print(cadena_2)

print()

print(cadena_1, end='\n') # por defecto
print(cadena_2)

print()

print(cadena_1, end='---')
print(cadena_2)



#? 3) Aplicación en bucles
print('\n3) Aplicación en bucles')

for x in range(1,11):
    print(x, end='---')
# end for


# => eliminando último end
print()
for x in range(1,11):
    if x == 10:
        print(x)
    else:
        print(x, end='---')
# end for