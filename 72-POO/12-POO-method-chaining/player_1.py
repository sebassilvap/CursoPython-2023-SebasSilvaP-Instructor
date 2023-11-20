# ==================================
# Clase - Player_1

# - notar, ninguno de los métodos
# - va a retornar algo
# ==================================

class Player_1:
    
    # Constructor + Atributos
    def __init__(self, tipo, vida):
        self.__tipo = tipo
        self.__vida = vida
    
    # Métodos
    def saltar(self):
        print( 'Player: {} - Salta!'.format(self.__tipo) )
    
    def disparar(self):
        print( 'Player: {} - Dispara!'.format(self.__tipo) )
    
    def esquivar(self):
        print( 'Player: {} - Esquiva!'.format(self.__tipo) )
        
    def agacharse(self):
        print( 'Player: {} - Se agacha!'.format(self.__tipo) )
        
    def power_up(self):
        print( 'Player: {} - Power Up!'.format(self.__tipo) )
# end class