
class Estudiante:
    
    # Atributo de Clase - Privado
    __nota_minima = 16
    
    # Constructor + Atributos
    def __init__(self, nombre, edad, nota_examen, nota_deberes):
        self.__nombre = nombre
        self.__edad = edad
        self.__nota_examen = nota_examen
        self.__nota_deberes = nota_deberes
    
    # Métodos Especiales  
    def __str__(self): #! RETORNAR UN STR
        return( 'Estudiante: {} / {} años | Nota Examen: {} | Nota Deberes: {}'.format(
            self.get_nombre(),
            self.get_edad(),
            self.get_nota_examen(),
            self.get_nota_deberes()) 
            )
    
    def __len__(self): #! RETORNAR UN INT
        return self.get_edad()
        
    def __del__(self):
        print( 'El estudiante {} ha sido eliminado del registro!'.format(self.__nombre) )
    
    # Getters
    def get_nombre(self):
        return self.__nombre
    
    def get_edad(self):
        return self.__edad
    
    def get_nota_examen(self):
        return self.__nota_examen
    
    def get_nota_deberes(self):
        return self.__nota_deberes
    
    def get_nota_minima(self):
        return self.__nota_minima # atributo de clase es también de cada instancia
       
    # Setters
    def set_nombre(self, nombre):
        self.__nombre = nombre
        
    def set_edad(self, edad):
        self.__edad = edad
        
    def set_nota_examen(self, nota_examen):
        self.__nota_examen = nota_examen
        
    def set_nota_deberes(self, nota_deberes):
        self.__nota_deberes = nota_deberes
        
    # Métodos Privados / Encapsulados           
    def __calculo_nota_final(self):
        ex = self.__nota_examen
        db = self.__nota_deberes
        
        nota_final = 0.6 * ex + 0.4 * db
        return nota_final
    
    def __ayuda_profesor(self):
        nota_final = self.__calculo_nota_final()
        
        if nota_final < self.get_nota_minima():
            nota_final *= 1.05
            return nota_final
        else:
            return nota_final
        
    def __pasa_no_pasa(self):
        if self.__ayuda_profesor() >= self.get_nota_minima():
            return 'PASA LA MATERIA'
        else:
            return 'NO PASA LA MATERIA'
    
    # Métodos Públicos    
    def analisis_estudiante(self):
        print( 
            "Estudiante: {}, su nota final es = {:.2f} | {}".format(
            self.get_nombre(),
            self.__ayuda_profesor(),
            self.__pasa_no_pasa()) 
        )
# end class
