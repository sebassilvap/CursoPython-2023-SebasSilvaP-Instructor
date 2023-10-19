# ====================================================================================
# Decoradores en Python

# - Decorador:
#   => patrón de diseño en Python
#   => permite añadir una nueva funcionalidad a un elemento
#   => pero sin modificar su estructura
#   => son llamados antes de la definición de una función que deseamos decorar

# - Para esto tener presente las 2 lecciones anteriores
#   => Una función puede ser almacenada en una variable (cualquier cosa en Python)
#   => Las funciones pueden ser de alto orden (high order function)
#       1) cuando reciben otra función como argumento
#       2) cuando una 1era función retorna una 2da definida en la 1era

# * Se enuncia un decorador con => @
# ====================================================================================


#? 1) Ejemplo Básico de un decorador para función
print('\n1) Ejemplo Básico de un decorador para función')

# => definición de función decoradora
def my_decorator_func(function):
    
    def wrapper_func():
        print('Hola!') # antes de ejecutar de la función que decoramos!
        function()
        print('Chao!') # después de ejecutar la función que decoramos
    # end def
    return wrapper_func
# end def


# => función normal SIN decorador
def normal_func_1():
    print('Me gusta Python!')
# end def


# => función normal CON decorador
@my_decorator_func
def normal_func_2():
    print('Me gusta javascript!')
# end def


# => TEST
normal_func_1()
print()
normal_func_2()



#? 2) Después de enunciado el decorador es obligatorio definir una función
print('\n2) Después de enunciado el decorador es obligatorio definir una función')

print('Hola Hola Mundo!!!')

#! SyntaxError: invalid syntax
"""
@my_decorator_func
print('Hola Hola Mundo desde Python!!!')
"""

#! SyntaxError: invalid syntax
"""
@my_decorator_func
x = 20
"""

@my_decorator_func
def decir_cumplido():
    print('Eres la persona más increíble del mundo!')
# end def

print()
decir_cumplido()

# => CONSOLA
# Hola!
# Eres la persona más increíble del mundo!
# Chao!