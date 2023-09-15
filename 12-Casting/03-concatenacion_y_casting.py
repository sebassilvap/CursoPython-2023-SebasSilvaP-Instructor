# =============================================================
# Problema con la concatenación de strings

# - un problema / error común con la concatenación de strings
# - que genera muchos errores en principantes
# - es querer concatenar un dato que no sea string
# - la solución a esto es el casting
# =============================================================

#? 1) Ejemplo de Error CLÁSICO
nombre = 'sebas'
edad = 36
nota = 18.5
es_estudiante = False

# => De esta manera como conocemos no hay error
print(nombre)
print(edad)
print(nota)
print(es_estudiante)
print('----------------------')
print(nombre , edad , nota , es_estudiante)
print('----------------------')
print(nombre , type(nombre) )
print(edad , type(edad) )
print(nota , type(nota) )
print(es_estudiante , type(es_estudiante) )
print('-------CURIOSIDAD: ¿qué devuelve type?---------')
print(nombre , type(nombre) , '=>' , type( type(nombre) ) )
print(edad , type(edad) , '=>' , type( type(edad) ) )
print(nota , type(nota) , '=>' , type( type(nota) ) )
print(es_estudiante , type(es_estudiante) , '=>' , type( type(es_estudiante) ) )

# => ¿Cuál es el ERROR típico?
#print( nombre + edad + nota + es_estudiante ) #! TypeError : solo se puede concatenar entre str

# esto no solo pasa en el print, sino en un string en general
apellido = 'silva'
full_name = nombre + apellido
print(full_name)
full_name = nombre + ' ' + apellido
print(full_name)
#full_name = nombre + ' ' + apellido + es_estudiante #! TypeError
print(full_name)

## SOLUCIÓN
# - utilizar el casting
# - RECORDAR: que todo puede ser transformado a string

print( nombre + str(edad) + str(nota) + str(es_estudiante) )

#! ==> pero no olvidar los espacios

print( nombre + ' ' + str(edad) + ' ' + str(nota) + ' ' + str(es_estudiante) )

# podemos crear una variable espacio también
b = ' '

print( nombre + b + str(edad) + b + str(nota) + b + str(es_estudiante) )


#? 2) RESUMEN: Maneras correcta de utilizar print
nombre = 'Diego'
edad = 24
es_estudiante = False

print(nombre, 'tiene', edad, 'años. ¿Es estudiante? ==>', es_estudiante)
#print(nombre + ' tiene ' + edad + ' años. ¿Es estudiante? ==> ' + es_estudiante) #! TypeError
print(nombre + ' tiene ' + str(edad) + ' años. ¿Es estudiante? ==> ' + str(es_estudiante) )


