# ==================================
# Optimización del Script Anterior
# => Aplicando Funciones de Python
# ==================================

#? Definición de la Función

def print_info(n, e, nota): # PARÁMETROS DE LA FUNCIÓN DEFINIDA
    print( '\nSu nombre es:', n )
    print( 'Usted tiene', e, 'años' )
    print( 'Su nota final es =', nota )
# end def

#? Invocando la Función Definida
nombre = 'Sebas'
edad = 36
nota_final = 15.5

print_info(nombre, edad, nota_final)

nombre = 'Andy'
edad = 25
nota_final = 16.8

print_info(nombre, edad, nota_final)

nombre = 'Carla'
edad = 30
nota_final = 19.9

print_info(nombre, edad, nota_final)


# ---------------------------------------------------
# - la función la defino 1 vez
# - al inicio
# - y la puedo utilizar donde sea dentro del script
# - permite la reutilización del código
# - se declara / define una función con "def"
# - el bloque de código de la función
# - va indentado dentro de def:
# ---------------------------------------------------