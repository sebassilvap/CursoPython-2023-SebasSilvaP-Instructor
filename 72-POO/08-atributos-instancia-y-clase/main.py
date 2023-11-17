# ========================================================
# Atributos de Instancia / Atributos de Clase

# - atributos dentro del constructor => atributos de la instancia / objeto de clase
# - atributos fuera del constructor => atributos de la clase / constantes para todos los objetos / instancias
# ========================================================


#? 1) Definiendo una constante | Dentro del Constructor | Mala Práctica
print('\n1) Definiendo una constante | Dentro del Constructor | Mala Práctica')
# - mala práctica, pero no error, igual funciona
# - si va a ser una constante
# - es mejor definirla como un atributo de la clase
# - cuando se hace así, esta va dentro del constructor, pero no como parámetro

class Estudiante:
    # Constructor + Atributos de Clase
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
        self.__nota_minima = 15
    
    # Getters
    def get_nombre(self):
        return self.__nombre
    
    def get_edad(self):
        return self.__edad
    
    def get_nota_minima(self):
        return self.__nota_minima
    
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

e_1 = Estudiante('Marcelo' , 28)
e_2 = Estudiante('Juana' , 18)

e_1.estado_objeto() # nombre: Marcelo | edad: 28
e_2.estado_objeto() # nombre: Juana | edad: 18
print( e_1.get_nota_minima() ) # 15
print( e_2.get_nota_minima() ) # 15



#? 2) Constante como Atributo de Clase
print('\n2) Constante como Atributo de Clase')

class Estudiante:
    
    nota_minima = 16
    
    # Constructor + Atributos
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
        
    # Métodos
    def saludar(self):
        print('Hola desde la clase - soy un método!')
        
    def estado_objeto(self):
        print( 'nombre: {} | edad: {}'.format( self.get_nombre(), self.get_edad() ) )
# end class


# =======
# TEST
# =======

e_1 = Estudiante('Marcelo' , 28)
e_2 = Estudiante('Juana' , 18)

e_1.estado_objeto() # nombre: Marcelo | edad: 28
e_2.estado_objeto() # nombre: Juana | edad: 18


# => Acceso a las variables de Clase
# - aquí decimos: para todo estudiante => la nota mínima es de 15

print( Estudiante.nota_minima ) # 15


# => ¿Lo notaron?
# - los métodos públicos
# - también pueden ser accedidos desde la clase
# - al hacerlo de esta manera, se debe mandar como parámetro el objeto / la instancia

#Estudiante.estado_objeto() #! TypeError: Estudiante.estado_objeto() missing 1 required positional argument: 'self'

Estudiante.estado_objeto(e_1) # nombre: Marcelo | edad: 28
Estudiante.estado_objeto(e_2) # nombre: Juana | edad: 18


# => igualmente el atributo de clase puede ser accedido desde las instancias
print( Estudiante.nota_minima ) # 16
print( e_1.nota_minima ) # 16
print( e_2.nota_minima ) # 16



#? 3) Modificación del Atributo de Clase
print('\n3) Modificación del Atributo de Clase')
# - con un atributo de clase en la definición de la clase
# - al crear objetos => todos tienen este atributo
# - si este atributo de clase es público
# - podemos acceder y cambiarlo desde la clase o desde la instancia

#   * si lo cambiamos desde la clase => cambia en todas las instancias
#   * si lo cambiamos desde la instancia => cambia solo para esa instancia

# - si volvemos a cambiar desde la clase => ya no cambia en la instancia donde la cambiamos


Estudiante.nota_minima = 12
print( Estudiante.nota_minima ) # 12
print( e_1.nota_minima ) # 12
print( e_2.nota_minima ) # 12

e_1.nota_minima = 18
print( Estudiante.nota_minima ) # 12
print( e_1.nota_minima ) # 18
print( e_2.nota_minima ) # 12


Estudiante.nota_minima = 13
print( Estudiante.nota_minima ) # 13
print( e_1.nota_minima ) # 18
print( e_2.nota_minima ) # 13



#? 4) Atributo de Clase Privado
print('\n4) Atributo de Clase Privado')
# - obviamente lo observado anteriormente es algo que posiblemente
# - deseemos evitar => no sería una buena idea tener una constante de clase
# - que podamos cambiar desde cualquier instancia / objeto de clase
# - por lo tanto podemos definir atributos de clase PRIVADOS

class Estudiante:
    
    __nota_minima = 16
    
    # Constructor + Atributos
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
    
    # Getters
    def get_nombre(self):
        return self.__nombre
    
    def get_edad(self):
        return self.__edad
    
    def get_nota_minima(self):
        return self.__nota_minima
       
    # Setters
    def set_nombre(self, nombre):
        self.__nombre = nombre
        
    def set_edad(self, edad):
        self.__edad = edad
        
    # Métodos
    def saludar(self):
        print('Hola desde la clase - soy un método!')
        
    def estado_objeto(self):
        print( 'nombre: {} | edad: {}'.format( self.get_nombre(), self.get_edad() ) )
# end class

e_1 = Estudiante('Marcelo' , 28)
e_2 = Estudiante('Juana' , 18)

#print( Estudiante.__nota_minima ) 
# #! AttributeError: type object 'Estudiante' has no attribute '__nota_minima'. Did you mean: 'get_nota_minima'?

print( e_1.get_nota_minima() ) # 16
print( e_2.get_nota_minima() ) # 16

# => si intentamos esto no es error, pero no podemos modificar
Estudiante.__nota_minima = 20

print( e_1.get_nota_minima() ) # 16
print( e_2.get_nota_minima() ) # 16