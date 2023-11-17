# ==================================================================================
# Constructor

# - método especial para definir el estado inicial de un objeto de clase
# - como su nombre lo indica, para contruir un objeto de clase
# - un objeto con sus atributos de clase
# - diferente a otro método por la utilización de __init__

# ! luego veremos que la inclusión de las 2 barras __x__ => para métodos especiales
# => __init__ => uno de estos métodos especiales => constructor de clase

# ==================================================================================


#? 1) Definición de Clase con Constructor
print('\n1) Definición de Clase con Constructor')

# --------------------------
# => clase SIN constructor
# --------------------------
"""
class Persona:
    # atributos
    nombre = 'nombre de persona'
    edad = 'edad de persona'
    
    # métodos
    def saludar(self):
        print('Hola desde la clase - soy un método!')
# end class
"""

# --------------------------
# => clase CON constructor
# --------------------------

class Persona:
    # Constructor + Atributos de Clase
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    # Métodos de Clase
    def saludar(self):
        print('Hola desde la clase - soy un método!')
# end class



#? 2) Creando Objetos / Instancias de Clase con Constructor
print('\n2) Creando Objetos / Instancias de Clase con Constructor')
# - en la parte de arriba pusimos algo como:
# *      self.nombre = nombre
# - básicamente lo que decimos es que al momento de crear un objeto
# - el valor con el que creamos, es el de ese objeto
# - vemos mejor esto en la práctica

persona_1 = Persona('Sebas' , 36)
persona_2 = Persona('Diego' , 20)

print( persona_1 , type(persona_1) , persona_1.nombre , persona_1.edad )
print( persona_2 , type(persona_2) , persona_2.nombre , persona_2.edad )

# CONSOLA:
#<__main__.Persona object at 0x000001B2C2AF8910> <class '__main__.Persona'> Sebas 36
#<__main__.Persona object at 0x000001B2C2AF88D0> <class '__main__.Persona'> Diego 20


# --------------------------------------------------------------
# => de ahora en adelante, si deseo crear un objeto de Persona
# - tengo que hacerlo pasando los valores
# - de los atributos definidos en el constructor
# --------------------------------------------------------------

#persona_3 = Persona() #! TypeError: Persona.__init__() missing 2 required positional arguments: 'nombre' and 'edad'



#? 3) Método estado_objeto()
print('\n3) Método estado_objeto()')
# - aquí vamos a redefinir la clase
# - de igual manera como redefinimos una variable o una función
# - este método para devolver el estado es una buena práctica al momento de escribir clases
# - devuelve el nombre y valor de los atributos
# ! luego veremos que este método se lo escribe como método especial __str__
# - para acceder a los valores de los atributos, lo hacemos con "self."

class Persona:
    # Constructor + Atributos
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    # Métodos
    def saludar(self):
        print('Hola desde la clase - soy un método!')
        
    def estado_objeto(self):
        print('nombre: {} | edad: {}'.format(self.nombre, self.edad))
# end class


# ======
# TEST
# ======

persona_1 = Persona('Sebas' , 36)
persona_2 = Persona('Diego' , 20)

persona_1.estado_objeto() # nombre: Sebas | edad: 36
persona_2.estado_objeto() # nombre: Diego | edad: 20



#? 4) Desventaja => podemos sobrescribir el valor de los atributos
print('\n4) Desventaja => podemos sobrescribir el valor de los atributos')
# - todavía tenemos este problema que podemos modificar el valor de los atributos
# - estas modificaciones no deberían ser posibles de esta manera
# - y fuera de la clase
# - ¿qué pasaría si la clase se tratara de una cuenta de bancos por ejemplo?
# - y cualquiera pudiese modificar el saldo de la cuenta

persona_1.nombre = 'Carlos'

persona_1.estado_objeto() # nombre: Carlos | edad: 36


# ----------------------------------------------------------------------
# - la restricción del acceso de los atributos y métodos de una clase
# - se hace con los "modificadores de acceso"
# - esto lo vemos en la siguiente lección
# ----------------------------------------------------------------------