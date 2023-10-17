# =========================================================
# Función Lambda

# - también se la conoce como función anónima
# - acepta un número indefinido de argumentos
# - pero solo puede tener 1 EXPRESIÓN

# *       lambda argumentos : expresión

# - podemos pensar o verla como un shortcut
# - la usamos por un corto tiempo y luego la descartamos
# =========================================================


#? 1) Función Normal VS. Función Lambda
print('\n1) Función Normal VS. Función Lambda')

# => Función Normal
def sumar_normal(a,b):
    return a + b
# end def

print( sumar_normal(5,3) )

# => Función Lambda
sumar_lambda = lambda x,y : x + y

# - 1 sola línea
# - 1 sola expresión
# - N argumentos, en este caso x, y
# - Retorno: x + y

# => Ejecutando Función Lambda
resultado = sumar_lambda(8,9)
print(resultado)

# o directamente en el print
print( sumar_lambda(7,2) )



#? 2) Puede tener N número de argumentos
print('\n2) Puede tener N número de argumentos')
# - como observaremos
# - los argumentos pueden ser los mismos que en otras funciones lambda
# - definidas en nuestro código
# - estos argumentos EXISTEN solo dentro de la definición
# - de la función lambda donde se crean

# 1 argumento
triplicar_valor = lambda x : 3 * x

# 2 argumentos
producto = lambda x, y : x * y

# 5 argumentos
promedio_5_valores = lambda a,b,c,d,e : (a+b+c+d+e)/5

# TEST
print( triplicar_valor(100) )
print( producto(9,5) )
print( promedio_5_valores(1,2,3,4,5) )



#? 3) Lambda con argumentos de tipo String
print('\n3) Lambda con argumentos de tipo String')

# => Función Normal
def saludar(nombre, edad):
    print('Hola', nombre, 'tienes', edad, 'años!')
# end def

saludar('Carlos', 18)


# => Función Lambda

saludo = lambda nombre, edad : 'Hola ' + nombre + ' tienes ' + str(edad) + ' años!!'

print( saludo('Taty', 17) )