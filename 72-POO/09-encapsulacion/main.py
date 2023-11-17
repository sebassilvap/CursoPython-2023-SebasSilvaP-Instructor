# ===========================================================================
# Encapsulación
# (Métodos Privados)

# - recordemos, tenemos 2 modificadores de acceso posibles
# - cuando hablamos de clases en Python: públicos & privados
# - ya vimos los atributos privados
# - de igual manera podemos tener métodos privados
# - también se los llama métodos encapsulados
# - y esto genera el concepto de "encapsulación"
# - cuando tenemos comportamiento de la clase, al cual no podemos acceder
# - desde fuera de la clase
# - de igual manera que los atributos se los define con " __nombre_metodo"
# ===========================================================================


#? 1) Clase SIN Métodos Privados / Encapsulados
print('\n1) Clase SIN Métodos Privados / Encapsulados')

class Estudiante:
    
    __nota_minima = 16
    
    # Constructor + Atributos
    def __init__(self, nombre, nota_examen, nota_deberes):
        self.__nombre = nombre
        self.__nota_examen = nota_examen
        self.__nota_deberes = nota_deberes
    
    # Getters
    def get_nombre(self):
        return self.__nombre
    
    def get_nota_examen(self):
        return self.__nota_examen
    
    def get_nota_deberes(self):
        return self.__nota_deberes
    
    def get_nota_minima(self):
        return self.__nota_minima # atributo de clase es también de cada instancia
       
    # Setters
    def set_nombre(self, nombre):
        self.__nombre = nombre
        
    def set_nota_examen(self, nota_examen):
        self.__nota_examen = nota_examen
        
    def set_nota_deberes(self, nota_deberes):
        self.__nota_deberes = nota_deberes
        
    # Métodos       
    def estado_objeto(self):
        print( 'Estudiante: {} | Nota Examen: {} | Nota Deberes: {}'.format(
            self.get_nombre(),
            self.get_nota_examen(),
            self.get_nota_deberes()) 
            )
        
    def calculo_nota_final(self):
        # => con getters
        #ex = self.get_nota_examen()
        #db = self.get_nota_deberes()
        
        # => con acceso dentro de clase
        ex = self.__nota_examen
        db = self.__nota_deberes
        
        nota_final = 0.6 * ex + 0.4 * db
        return nota_final
    
    def ayuda_profesor(self):
        nota_final = self.calculo_nota_final()
        
        if nota_final < self.get_nota_minima():
            nota_final *= 1.05
            return nota_final
        else:
            return nota_final
        
    def pasa_no_pasa(self):
        if self.ayuda_profesor() >= self.get_nota_minima():
            return 'PASA LA MATERIA'
        else:
            return 'NO PASA LA MATERIA'
        
    def analisis_estudiante(self):
        print( 
            "Estudiante: {}, su nota final es = {:.2f} | {}".format(
            self.get_nombre(),
            self.ayuda_profesor(),
            self.pasa_no_pasa()) 
        )
# end class


# ======
# TEST
# ======

estudiante_1 = Estudiante('Juan' , 13 , 17)
estudiante_2 = Estudiante('Xime' , 15 , 17)

#! esto necesito que vea el estudiante
estudiante_1.estado_objeto() # Estudiante: Juan | Nota Examen: 13 | Nota Deberes: 17
estudiante_2.estado_objeto() # Estudiante: Xime | Nota Examen: 15 | Nota Deberes: 17

print( estudiante_1.calculo_nota_final() ) # 14.600000000000001
print( estudiante_2.calculo_nota_final() ) # 15.8

print( estudiante_1.ayuda_profesor() ) # 15.330000000000002
print( estudiante_2.ayuda_profesor() ) # 16.59

print( estudiante_1.pasa_no_pasa() ) # NO PASA LA MATERIA
print( estudiante_2.pasa_no_pasa() ) # PASA LA MATERIA

#! esto necesito que vea el estudiante
estudiante_1.analisis_estudiante() # Estudiante: Juan, su nota final es = 15.33 | NO PASA LA MATERIA
estudiante_2.analisis_estudiante() # Estudiante: Xime, su nota final es = 16.59 | PASA LA MATERIA


# -----------------------------------------------------------------------------
# CONCLUSIÓN
# - ¿Necesito que desde fuera, el estudiante acceda a todos los métodos?
# - Por ej: calculo_nota_final, ayuda_profesor, pasa_no_pasa
# - Lo más importante para el estudiante es el método "analisis_estudiante()"
# - Lo demás no necesito que vea el estudiante
# - Estos métodos no deben ser públicos
# - Deben ser privados
# -----------------------------------------------------------------------------



#? 2) Clase CON Métodos Privados / Encapsulados
print('\n2) Clase CON Métodos Privados / Encapsulados')

class Estudiante:
    
    __nota_minima = 16
    
    # Constructor + Atributos
    def __init__(self, nombre, nota_examen, nota_deberes):
        self.__nombre = nombre
        self.__nota_examen = nota_examen
        self.__nota_deberes = nota_deberes
    
    # Getters
    def get_nombre(self):
        return self.__nombre
    
    def get_nota_examen(self):
        return self.__nota_examen
    
    def get_nota_deberes(self):
        return self.__nota_deberes
    
    def get_nota_minima(self):
        return self.__nota_minima # atributo de clase es también de cada instancia
       
    # Setters
    def set_nombre(self, nombre):
        self.__nombre = nombre
        
    def set_nota_examen(self, nota_examen):
        self.__nota_examen = nota_examen
        
    def set_nota_deberes(self, nota_deberes):
        self.__nota_deberes = nota_deberes
        
    # Métodos              
    def __calculo_nota_final(self):
        # => con getters
        #ex = self.get_nota_examen()
        #db = self.get_nota_deberes()
        
        # => con acceso dentro de clase
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
        
    def analisis_estudiante(self):
        print( 
            "Estudiante: {}, su nota final es = {:.2f} | {}".format(
            self.get_nombre(),
            self.__ayuda_profesor(),
            self.__pasa_no_pasa()) 
        )
    
    def estado_objeto(self):
        print( 'Estudiante: {} | Nota Examen: {} | Nota Deberes: {}'.format(
            self.get_nombre(),
            self.get_nota_examen(),
            self.get_nota_deberes()) 
            )
# end class


# ======
# TEST
# ======

estudiante_1 = Estudiante('Juan' , 13 , 17)
estudiante_2 = Estudiante('Xime' , 15 , 17)

#! esto necesito que vea el estudiante
estudiante_1.estado_objeto() # Estudiante: Juan | Nota Examen: 13 | Nota Deberes: 17
estudiante_2.estado_objeto() # Estudiante: Xime | Nota Examen: 15 | Nota Deberes: 17

# => ningún método privado / encapsulado se puede acceder desde fuera de la clase

#print( estudiante_1.calculo_nota_final() ) #! AttributeError: 'Estudiante' object has no attribute 'calculo_nota_final'
#print( estudiante_2.__pasa_no_pasa() ) #! AttributeError: 'Estudiante' object has no attribute '__pasa_no_pasa'


#! esto necesito que vea el estudiante
estudiante_1.analisis_estudiante() # Estudiante: Juan, su nota final es = 15.33 | NO PASA LA MATERIA
estudiante_2.analisis_estudiante() # Estudiante: Xime, su nota final es = 16.59 | PASA LA MATERIA
