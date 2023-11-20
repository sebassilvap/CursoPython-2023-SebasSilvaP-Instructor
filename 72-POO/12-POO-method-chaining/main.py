# ==============================================
# Configurar Method Chaining en nuestras Clases
# ==============================================

from player_1 import Player_1 as P1
from player_2 import Player_2 as P2


#? 1) SIN method chaining
print('\n1) SIN method chaining')

j1 = P1('Guardián' , 80)

j1.saltar() # Player: Guardián - Salta!
j1.power_up() # Player: Guardián - Power Up!
j1.disparar() # Player: Guardián - Dispara!


# => ¿si intento hacer chaining?
#j1.saltar().power_up().disparar()  #! AttributeError: 'NoneType' object has no attribute 'power_up'

# ------------------------------------------------------------
# => ¿por qué el error?
# - cada método de Player_1 no devuelve / retorna nada
# - por defecto me retorna un "NoneType"
# - y es como si tratara de aplicar el método de la clase
# - a un objeto de tipo / clase "None"
# ------------------------------------------------------------



#? 2) CON method chaining
print('\n2) CON method chaining')
# - observar la clase Player_2
# - la única diferencia con Player_1
# - es que cada método me retorna el "self"
# - es decir, me retorna el mismo objeto

j2 = P2('Mago' , 50)

j2.disparar() # Player: Mago - Dispara!

print( j2.disparar() )
# Player: Mago - Dispara!
# <player_2.Player_2 object at 0x000001512800D8D0> #* => me retorna el mismo objeto / instancia

# => lo puedo comprobar, imprimiendo el objeto:

print( j2 ) # <player_2.Player_2 object at 0x000001512800D8D0>


# -------------------------------------------------------
# => aquí si puedo entonces aplicar el method-chaining
# - porque cada vez que aplico un método
# - estoy retornando el mismo objeto
# -------------------------------------------------------

j2.saltar().agacharse().disparar().power_up().esquivar().saltar()

# Player: Mago - Salta!
# Player: Mago - Se agacha!
# Player: Mago - Dispara!
# Player: Mago - Power Up!
# Player: Mago - Esquiva!
# Player: Mago - Salta!