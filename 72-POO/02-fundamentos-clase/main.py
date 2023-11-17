# ==================================================
# Clase

# - plantilla / molde / fábrica de objetos
# - define el objeto por medio de:
#   1) atributos
#   2) métodos

# - atributos: características / propiedades
# - métodos: comportamiento / ¿qué hace el objeto?
# ==================================================


#? 1) Definición Básica de una Clase
print('\n1) Definición Básica de una Clase')
# - como todo en python utilizamos una palabra clave / keyword
# - en este caso es la palabra class + nombre de clase + :
# - en este bloque de código, dentro
# - va la definición de la clase
# ! el nombre de la clase, va la primera con mayúscula => NORMA

class Persona:
    # atributos
    nombre = 'nombre de persona'
    apellido = 'apellido de persona'
    edad = 'edad de persona'
    
    # métodos
    def saludar(self): #! self => lo explicamos luego
        print('Hola!')
    
    def despedirse(self):
        print('Chao!')
# end class



#? 2) Instancia de Clase
print('\n2) Instancia de Clase')
# - una vez definida la clase
# - podemos definir objetos con la misma

# => a esto se le llama INSTANCIAR una clase
# - o crear OBJETOS de una clase
# - funciona de igual manera como si ejecutaramos una función

persona_1 = Persona()
persona_2 = Persona()

print( persona_1 ) # <__main__.Persona object at 0x000001A519A08950>
print( persona_2 ) # <__main__.Persona object at 0x000001A519A08910>

# => ¿qué nos devuelve type()?

print( type(persona_1) ) # <class '__main__.Persona'>
print( type(persona_2) ) # <class '__main__.Persona'>

# => ¿qué nos devolvía type antes?

a = 10
b = 'hola'
c = [1,2,3]

print( a , type(a) ) # 10 <class 'int'>
print( b , type(b) ) # hola <class 'str'>
print( c , type(c) ) # [1, 2, 3] <class 'list'>

# -------------------------------------------------------------------------------
#* CONCLUSIÓN
# - Todo! en Python son objetos / instancias de una clase
# - lo que hemos usado en todo este tiempo
# - son instancias / objetos de esas clases
# - type dijimos devuelve el tipo del elemento
# - en verdad lo que devuelve es la clase de la cual un elemento es instancia
# -------------------------------------------------------------------------------



#? 3) Atributos y Métodos
print('\n3) Atributos y Métodos')
# - los atributos y métodos se los accede con la nomenclatura del punto
#! RECORDAR
# - en una clase
# - los atributos definen las propiedades / características
# - los métodos definen el comportamiento / ¿qué hace?

# => atributos
print( persona_1.nombre ) # nombre de persona
print( persona_1.apellido ) # apellido de persona
print( persona_1.edad ) # edad de persona
# => métodos
persona_1.saludar() # Hola!
persona_1.despedirse() # Chao!



#? 4) self
print('\n4) self')
# - self => hace referencia al propio objeto de la clase
# - esta es la diferencia entre un método de clase y una función normal como la conocemos
# - el método no es más que una "función" especial que actúa sobre el objeto de clase
# - self => "sobre sí mismo"
# ! función vs. método => más a detalle lo vemos luego

# => recordar algunos métodos que ya vimos
# - por ejemplo de una instacia de string <str>

cadena = 'python'
print( cadena ) # python
print( cadena.upper() ) # PYTHON

persona_1.despedirse() # Chao!
persona_2.despedirse() # Chao!



#? 5) Creando Clase Vacía - Sólo Definición
print('\n5) Creando Clase Vacía - Sólo Definición')
# - ya aprendimos una palabra clave
# - que nos permite hacer esto
# - con "pass" => definimos el título / firma, y llenamos luego

class Estudiante():
    pass
# end class

# => creando un objeto de clase Estudiante
# (creando una instancia de clase Estudiante)

e = Estudiante()

print( e , '|' , type(e) ) # <__main__.Estudiante object at 0x0000019A8D7D9110> | <class '__main__.Estudiante'>