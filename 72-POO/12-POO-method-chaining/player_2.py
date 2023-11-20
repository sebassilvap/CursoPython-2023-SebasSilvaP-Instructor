# ==================================
# Clase - Player_2

# - todos los métodos retornan
# - el objeto / instancia
# ==================================

class Player_2:
    
    # Constructor + Atributos
    def __init__(self, tipo, vida):
        self.__tipo = tipo
        self.__vida = vida
    
    # Métodos
    def saltar(self):
        print( 'Player: {} - Salta!'.format(self.__tipo) )
        return self
    
    def disparar(self):
        print( 'Player: {} - Dispara!'.format(self.__tipo) )
        return self
    
    def esquivar(self):
        print( 'Player: {} - Esquiva!'.format(self.__tipo) )
        return self
        
    def agacharse(self):
        print( 'Player: {} - Se agacha!'.format(self.__tipo) )
        return self
        
    def power_up(self):
        print( 'Player: {} - Power Up!'.format(self.__tipo) )
        return self
# end class