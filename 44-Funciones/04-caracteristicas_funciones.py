# ================================================================
# Características / Particularidades de las Funciones en Python
# ================================================================


#? 1) Primero se la define luego se la invoca
print('\n1) Primero se la define luego se la invoca')
# - en otros lenguajes una función puede definirse en cualquier lado
# - y al ejecutar el código las definiciones de funciones
# - se ponen arriba del código
# - este comportamiento se llama "hoisting"
# - en python TENEMOS que definirla primero

#saludar() #! NameError: name 'saludar' is not defined

def saludar():
    print('hola amigo')
# end def

saludar()



#? 2) El código que lo define va indentado
print('\n2) El código que lo define va indentado')
# - en este punto ya hemos aprendido
# - que la indentación define un nuevo bloque de código
# - este tema se explicará con más detalle más adelante
# - en lo que se refiere al scope de variables*

print('línea de código 1')

def despedirse():
    print('chao!')
    
print('línea de código 2')

despedirse()



#? 3) Se la puede redefinir N veces
print('\n3) Se la puede redefinir N veces')
# - al igual que las variables
# - que podemos reasignar cuantas veces queramos
# - la función puede redefinirse N veces a lo largo del código
# - la última definición de arriba a abajo es la que queda

def saludar():
    print('Buenos días!!')
# end def

saludar()

def saludar(n):
    print('hola', n)
    return n
# end def

saludar('Diego')



#? 4) El return marca el fin de la función
print('\n4) El return marca el fin de la función')

def sumar(a, b):
    resultado = a + b
    print('Su cálculo es:')
    print(a,'+',b,'=', resultado )
    return resultado
    print('Fin de Función')
    print('Hola')
# end def

sumar(4,5)

print( sumar(8,9) )

# - poner algo luego del return
# - no es error
# - pero nunca se ejecuta



#? 5) El return puede ser inmediato
print('\n5) El return puede ser inmediato')
# - no es necesario crear una variable extra dentro de la función
# - podemos retornar una variable o una operación

def nombre_edad(x, y):
    mensaje = 'Me llamo ' + x + ' y tengo ' + str(y) + ' años'
    return mensaje
# end def

nombre_edad('Sebas', 36)

# => RECORDAR: 
# - necesitamos imprimir o guardar en variable
# - para usar el retorno de una función

mensaje_1 = nombre_edad('Sebas', 36)
print( mensaje_1 )
print( nombre_edad('Sebas', 36) )

# => Podemos evitar la creación de la variable mensaje

def nombre_edad(x, y):
    return 'HOLA! Me llamo ' + x + ' y tengo ' + str(y) + ' años'
# end def

print( nombre_edad('Santi', 40) )



#? 5) Los parámetros existen solo en las funciones
print('\n5) Los parámetros existen solo en las funciones')
# - este tema ya veremos a profundidad en el scope de variables
# - por el momento adelantamos esto
# - estas "variables" existen solo dentro de la función
# - no importa si se repiten en otras funciones
# - no se puede acceder a ellas fuera de la funcion

def sumar(num1, num2):
    return num1 + num2
# end def

#print( num1 ) #! NameError: name 'num1' is not defined

resultado = sumar(5,2)
print(resultado)

#print(num1, num2) #! NameError: name 'num1' is not defined

# => si defino num1 y num2 aquí
# - existen aquí
# - nada tienen que ver con los parámetros
num1 = 10
num2 = 15

print(num1, num2)

resultado = sumar(20,30)
print(resultado)

# => aquí ingreso las variables creadas en el "entorno global"
# - nada tienen que ver con los parámetros de la función
resultado = sumar(num1, num2)
print(resultado)

resultado = sumar(0.5, 2.3)
print(resultado)



#? 6) Los nombres de los parámetros pueden repetirse en varias funciones
print('\n6) Los nombres de los parámetros pueden repetirse en varias funciones')
# - no existe conflicto en usar el mismo nombre en los PARÁMETROS
# - RECORDAR:
# - estas "variables" existen solo en el espectro de la función
# - donde se las crea
# - cumplen su propósito dentro de la función
# - y termina su trabajo

def sumar(a,b):
    return a + b
# end def

def restar(a,b):
    return a - b
# end def

def duplicar_numero(a):
    return a * 2
# end def

print('\nRESULTADOS:')
print( sumar(10,5) )
print( restar(20,12) )
print( duplicar_numero(6) )



#? 7) pass => para definir una función en blanco y trabajar luego
print('\n7) pass => para definir una función en blanco y trabajar luego')
# - Recordemos el pass
# - lo utilizábamos para definir algo
# - y trabajar en eso luego
# - en el if por ejemplo

x = 10

if x < 20:
    pass

# => de igual manera con las funciones

def suma(a,b):
    pass

def calcular_algo(a,b,c,d):
    pass

# => es decir,
# - es como dejar la firma de la función
# - dejamos ahí, y volveremos luego