# =============================================================================================
# Función de Python vs. Método de Clase

# - la diferencia más obvia es el uso de self para el método de clase
# - self => hace referencia a que el método se aplica al objeto / instancia de la misma clase
# - el método no es más que una función en sí, pero que pertenece a la clase
# - dentro del ámbito de la clase
# - la función está definida dentro del ámbito global del código
# =============================================================================================


#? 1) función y método de clase
print('\n1) función y método de clase')

class Persona:
    # atributos
    nombre = 'nombre de persona'
    apellido = 'apellido de persona'
    edad = 'edad de persona'
    
    # métodos
    def saludar(self):
        print('Hola desde la clase - soy un método!')
# end class


def saludar():
    print('hola desde una función')
# end def



#? 2) Invocación de método y función
# - el método por si no puede ser llamado
# - a menos que creemos un objeto de clase

p = Persona() # creando objeto / instancia de clase

p.saludar() # Hola desde la clase - soy un método!

saludar() # hola desde una función