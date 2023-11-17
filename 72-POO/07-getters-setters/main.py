# ===========================================================
# GETTERS & SETTERS

# GETTER => Para retornar el valor del atributo
# SETTER => Para modificar el valor del atributo

# => si pudiésemos platear esto como una fórmula:

"""

#* CONSTRUCTOR
def __init__(self, x):
    self.__x = x

#* GETTER
def get_x(self):
    return self.__x

#* SETTER
def set_x(self, x):
    self.__x = x

"""
# ===========================================================


#? 1) Implementando GETTERS & SETTERS en nuestra clase
print('\n1) Implementando GETTERS & SETTERS en nuestra clase')


class Persona:
    # Constructor + Atributos de Clase
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
    
    # Getters
    def get_nombre(self):
        return self.__nombre
    
    def get_edad(self):
        return self.__edad
    
    # Setters
    def set_nombre(self, nombre):
        self.__nombre = nombre
        
    def set_edad(self, edad):
        self.__edad = edad
        
    # Métodos de Clase
    def saludar(self):
        print('Hola desde la clase - soy un método!')
        
    def estado_objeto(self):
        print('nombre: {} | edad: {}'.format(self.__nombre, self.__edad))
# end class

# =======
# TEST
# =======

p = Persona('Mario' , 25)

p.estado_objeto() # nombre: Mario | edad: 25
print( p.get_nombre() , '|' , p.get_edad() ) # Mario | 25

p.set_nombre('Xime')
p.set_edad(40)

print( p.get_nombre() , '|' , p.get_edad() ) # Xime | 40



#? 2) Podemos reescribir estado_objeto => utilizando los getters
print('\n2) Podemos reescribir estado_objeto => utilizando los getters')
# - RECORDEMOS: un método si se lo define como público
# - puede usarse dentro y fuera de la clase

class Persona:
    # Constructor + Atributos de Clase
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
    
    # Getters
    def get_nombre(self):
        return self.__nombre
    
    def get_edad(self):
        return self.__edad
    
    # Setters
    def set_nombre(self, nombre):
        self.__nombre = nombre
        
    def set_edad(self, edad):
        self.__edad = edad
        
    # Métodos de Clase
    def saludar(self):
        print('Hola desde la clase - soy un método!')
        
    def estado_objeto(self):
        print( 'nombre: {} | edad: {}'.format( self.get_nombre(), self.get_edad() ) )
# end class


# =======
# TEST
# =======

p = Persona('Mario' , 25)

p.estado_objeto() # nombre: Mario | edad: 25
print( p.get_nombre() , '|' , p.get_edad() ) # Mario | 25

p.set_nombre('Xime')
p.set_edad(40)

print( p.get_nombre() , '|' , p.get_edad() ) # Xime | 40
