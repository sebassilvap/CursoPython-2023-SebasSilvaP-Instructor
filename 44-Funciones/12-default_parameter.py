# ====================================================================
# Funciones con Parámetros por Defecto

# - es posible tener parámetros fijos
# - es decir con un valor por defecto
# - también es posible llamar la función con argumentos en desorden
# ====================================================================


#? 1) Uso básico de función con parámetro por defecto
print('\n1) Uso básico de función con parámetro por defecto')

def aprender(lenguaje='Python'):
    print('Estamos aprediendo...', lenguaje)
# end def

# TEST
aprender('Java')
aprender('HTML')
aprender()



#? 2) Posición de los parámetros - siempre al final
print('\n2) Posición de los parámetros - siempre al final')
# - los parámetros por defecto van al final de la definición
# - no les puede seguir un parámetro sin valor por defecto
# - eso nos daría un error de sintaxis

def estado_personaje(alias, poder, activo=True):
    print('Alias: ', alias)
    print('Poder:', poder, '%')
    print('¿Está activo?:', activo)
# end def

# TEST
estado_personaje('goku', 90)
print()
estado_personaje('goku', 90, False)
print()
estado_personaje('goku', 90, True) # podemos pasar el parámetro por defecto, pero no es necesario

# => redefino la función
#! SyntaxError: non-default argument follows default argument
'''
def estado_personaje(activo=True, alias, poder):
    print('Alias: ', alias)
    print('Poder:', poder, '%')
    print('¿Está activo?:', activo)
# end def
'''

#! SyntaxError: non-default argument follows default argument
'''
def estado_personaje(alias, activo=True, poder):
    print('Alias: ', alias)
    print('Poder:', poder, '%')
    print('¿Está activo?:', activo)
# end def
'''



#? 3) Podemos tener varios parámetros por defecto
print('\n3) Podemos tener varios parámetros por defecto')

def describir_persona(nombre, edad, ciudad='N/A', pais='N/A'):
    print('DATOS DE PERSONA:')
    print('Nombre', nombre)
    print('Edad:', edad)
    print('Ciudad:', ciudad)
    print('País:', pais)
# end def

# TEST
describir_persona('Sebas', 36)
print()
describir_persona('Sebas', 36, 'Quito', 'Ecuador')
print()
describir_persona('Sebas', 36, 'Quito')



#? 4) Podemos pasar argumentos en desorden pero usando el nombre del parámetro
print('\n4) Podemos pasar argumentos en desorden pero usando el nombre del parámetro')
# - por defecto 
# - los argumentos se pasan en el orden que los parámetros
# - fueron definidos
# - podemos evitar este orden llamando los nombres de los parámetros

# TEST
describir_persona('Sebas', 36, pais='Ecuador')
print()
describir_persona(nombre='Daniel', edad=45, ciudad='Hamburgo', pais='Alemania')
print()
describir_persona(pais='USA', edad=18, nombre='Andrea', ciudad='Washington DC.')