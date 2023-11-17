# ====================
# Atributos de Clase
# ====================

#? 1) Acceso / Modificación / Creación de Atributos de Clase
print('\n1) Acceso / Modificación / Creación de Atributos de Clase')

class Persona:
    # atributos
    nombre = 'nombre de persona'
    edad = 'edad de persona'
    
    # métodos
    def saludar(self):
        print('Hola desde la clase - soy un método!')
# end class


# -------------------------------------------------
# => CREANDO objetos / instancias de clase Persona
# -------------------------------------------------
persona_1 = Persona()
persona_2 = Persona()
print( persona_1 , '|' , type(persona_1) ) # <__main__.Persona object at 0x000001C51D8D8650> | <class '__main__.Persona'>
print( persona_2 , '|' , type(persona_2) ) # <__main__.Persona object at 0x000001C51D8D8690> | <class '__main__.Persona'>

#! NOTA
# - al imprimir el objeto tenemos la dirección en la memoria
# - 2 objetos de la misma clase tienen diferentes direcciones en la memoria
# - recordar, lo mismo pasaba en listas
# - por tanto los objetos de las clases que definimos son mutables

l1 = [1,2,3]
l2 = [1,2,3]

print( hex(id(l1)) ) # 0x2a8ea935640
print( hex(id(l2)) ) # 0x2a8eab27c80


# -----------------------------------------
# => ACCEDIENDO a los atributos del objeto
# -----------------------------------------
print( persona_1.nombre , '|' , persona_1.edad ) # nombre de persona | edad de persona
print( persona_2.nombre , '|' , persona_2.edad ) # nombre de persona | edad de persona

#! NOTA
# - en un inicio son los mismos
# - porque así los hemos definido en la clase
# - con estos valores


# ------------------------------------------
# => MODIFICANDO el valor de los atributos
# ------------------------------------------
# - lo hacemos con la notación del punto
# - y como si se tratase de una variable

persona_1.nombre = 'Sebas'
persona_1.edad = 36

persona_2.nombre = 'Diego'
persona_2.edad = 21

print( persona_1.nombre , '|' , persona_1.edad ) # Sebas | 36
print( persona_2.nombre , '|' , persona_2.edad ) # Diego | 21


# -----------------------------
# => CREANDO nuevos atributos
# -----------------------------
# - tan simple como colocar el nuevo nombre después del punto

persona_1.ciudad = 'Quito'

print( persona_1.nombre , '|' , persona_1.edad , '|' , persona_1.ciudad ) # Sebas | 36 | Quito
print( persona_2.nombre , '|' , persona_2.edad ) # Diego | 21
#print( persona_2.ciudad ) #! AttributeError: 'Persona' object has no attribute 'ciudad'

# - no existe pero el atributo ciudad en persona_2



#? 2) Creación de Atributos en Clase Vacía
print('\n2) Creación de Atributos en Clase Vacía')

class Estudiante:
    pass

e = Estudiante()

e.nota = 18

print( e , '|' , type(e) ) # <__main__.Estudiante object at 0x00000172FB7F8C90> | <class '__main__.Estudiante'>
print( e.nota ) # 18



#? 3) Reflexión Final
print('\n3) Reflexión Final')
# - ¿es esta la manera adecuada de crear una clase?
# - podemos acceder a los atributos y cambiarlos cuando queramos
# - podemos crear nuevos atributos que no están en la definición de la clase
# - esto no es recomendable
# - veremos como solventar esto y muchas cosas más, a continuación