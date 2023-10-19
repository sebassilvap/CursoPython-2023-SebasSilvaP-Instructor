# ===============================
# Decoradores con Argumentos
# ===============================

#? 1) ¿Qué pasa si la función decorada tiene argumentos?
print('\n1) ¿Qué pasa si la función decorada tiene argumentos?')

# => definición de función decoradora
def my_decorator_func(function):
    
    def wrapper_func():
        print('Hola!') # antes de ejecutar de la función que decoramos!
        function()
        print('Chao!') # después de ejecutar la función que decoramos
    # end def
    return wrapper_func
# end def

@my_decorator_func
def sumar(a,b):
    print( 'La SUMA de {} + {} = {}'.format(a, b, a+b) )
# end def

#sumar(5,6)
#! TypeError: my_decorator_func.<locals>.wrapper_func() takes 0 positional arguments but 2 were given

# -----------------------------------------------------------------------
# - si la función decorada tiene argumentos
# - estos argumentos deben estar también en la función wrapper
# - función wrapper => la función interna dentro de función decoradora
#     * función decoradora = my_decorator_func = outter function
#     * función wrapper = wrapper_func = inner function
# -----------------------------------------------------------------------


#? 2) Función decoradora para función con argumentos
print('\n2) Función decoradora para función con argumentos')
# - una manera de evitar este error
# - es definiendo de manera general *args y **kwargs
# - dentro de la función wrapper


# => Redefiniendo función decoradora

def my_decorator_func(function):
    
    def wrapper_func(*args, **kwargs):
        print('Hola!') 
        function(*args, **kwargs)
        print('Chao!')
    # end def
    return wrapper_func
# end def

# => Función con decorador
@my_decorator_func
def sumar(a,b):
    print( 'La SUMA de {} + {} = {}'.format(a, b, a+b) )
# end def

# TEST
print()
sumar(5,6)
sumar(10,15)


# => Podemos volver a usar el decorador en otra función
@my_decorator_func
def restar(a,b):
    print( 'La RESTA de {} - {} = {}'.format(a, b, a-b) )
# end def

# TEST
print()
restar(8,20)
restar(15,6)


# => ¿y si con esto definimos una función decorada SIN argumentos?
@my_decorator_func
def decir_algo():
    print('Hey! Aquí estoy!!')
# end def

# TEST
print()
decir_algo() # también funciona!