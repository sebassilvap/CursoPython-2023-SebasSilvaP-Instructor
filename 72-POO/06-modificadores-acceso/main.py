# ========================================================================
# Modificadores de Acceso

# - Los atributos y métodos de una clase en Python
# - pueden ser:

#   1) Públicos => se los puede acceder dentro y fuera de la clase
#   2) Privados => no se puede acceder fuera de la definición de clase

# ! Métodos Privados => concepto de ENCAPSULACIÓN
# (esto lo veremos luego, por el momento solo atributos)

# ========================================================================


#? 1) Clase con Atributos Públicos
print('\n1) Clase con Atributos Públicos')

class Persona:
    # Constructor + Atributos de Clase
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    # Métodos de Clase
    def saludar(self):
        print('Hola desde la clase - soy un método!')
        
    def estado_objeto(self):
        print('nombre: {} | edad: {}'.format(self.nombre, self.edad))
# end class

p = Persona('Sebas' , 36)
p.estado_objeto() # nombre: Sebas | edad: 36
print( p.nombre , '|' , p.edad) # Sebas | 36
p.nombre = 'Carlos'
p.estado_objeto() # nombre: Carlos | edad: 36



#? 2) Clase con Atributos Privados
print('\n2) Clase con Atributos Privados')
# - el nombre del atributo va con => __nombre
# - esta modificación se hace en el onstructor
# - y en los métodos que utilicen los atributos (ej: estado_objeto)


class Persona:
    # Constructor + Atributos de Clase
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
        
    # Métodos de Clase
    def saludar(self):
        print('Hola desde la clase - soy un método!')
        
    def estado_objeto(self):
        print('nombre: {} | edad: {}'.format(self.__nombre, self.__edad))
# end class


p = Persona('Andrea' , 20)

# => puedo mostrar los atributos con mi método estado_objeto()

p.estado_objeto() # nombre: Andrea | edad: 20


#? 3) Acceso & Modificación de Atributos Privados
print('\n3) Acceso & Modificación de Atributos Privados')

# -----------------------
# => si intento acceder
# ERROR
# -----------------------

#print( p.nombre ) #! AttributeError: 'Persona' object has no attribute 'nombre'
#print( p.__nombre ) #! AttributeError: 'Persona' object has no attribute '__nombre'

# -----------------------------
# => si intento modificar
# NO ERROR, pero no pasa nada
# -----------------------------

p.nombre = 'Carlos'
p.estado_objeto() # nombre: Andrea | edad: 20

p.__nombre = 'Xime'
p.estado_objeto() # nombre: Andrea | edad: 20




#? 4) Conclusiones y desventajas
print('\n4) Conclusiones y desventajas')

# -------------------------------------------------------------------------------------
# - sin embargo, el problema es que ahora es muy restringido
# - no solo no puedo modificar
# - tampoco puedo ya ni mostrar
# - el acceso y modificación debe ser posible, pero no de la manera como hemos visto
# - la manera adecuada es con el uso de GETTERS y SETTERS
# - esto lo vemos en la próxima lección
# -------------------------------------------------------------------------------------
