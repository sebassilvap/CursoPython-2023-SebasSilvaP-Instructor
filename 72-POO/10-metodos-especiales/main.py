# ==================================================
# Métodos Especiales en las Clases

# => Hay más, pero estos son los más importantes

# 1) __init__
# - para definir el constructor

# 2) __del__
# - destructor => para eliminar el objeto
# - podemos redefinirlo para que haga algo más
# - a parte eliminar el objeto

# 3) __str__
# - retorna una referencia del objeto
# - podemos redefinirlo para que muestre algo más

# 4) __len__
# - por defecto nos devuelve un longitud o tamaño
# - pero si no lo definimos / sobrescribimos
# - nos va a dar un error

#!  => este concepto de sobrescribir un método
# - lo veremos a más profundidad luego
# ==================================================


#? 1) Tratando de aplicar por defecto sin sobrescribir ningún método
print('\n1) Tratando de aplicar por defecto sin sobrescribir ningún método')

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

estudiante = Estudiante('Sebas' , 14 , 16) # => método constructor

estudiante.estado_objeto() # Estudiante: Sebas | Nota Examen: 14 | Nota Deberes: 16
estudiante.analisis_estudiante() # Estudiante: Sebas, su nota final es = 15.54 | NO PASA LA MATERIA

# => str, hace lo mismo que imprimir la variable con la instancia de clase
print( str(estudiante) ) # <__main__.Estudiante object at 0x000001A0433F8E90>
print(estudiante) # <__main__.Estudiante object at 0x000001A0433F8E90>

#len(estudiante) #! TypeError: object of type 'Estudiante' has no len()

del(estudiante) # => método destructor por defecto
#print(estudiante) #! NameError: name 'estudiante' is not defined. Did you mean: 'Estudiante'?




#? 2) Sobrescribiendo / Redefiniendo Métodos Especiales dentro de la Clase
print('\n2) Sobrescribiendo / Redefiniendo Métodos Especiales dentro de la Clase')
# - al usar __str__ vamos a eliminar ahora el método "estado_objeto"
# - IMPORTANTE:
# *      __str__ => debe retornar un <str>
# *      __len__ => debe retornar in <int>


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
        
    # Métodos              
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
        
    def analisis_estudiante(self):
        print( 
            "Estudiante: {}, su nota final es = {:.2f} | {}".format(
            self.get_nombre(),
            self.__ayuda_profesor(),
            self.__pasa_no_pasa()) 
        )
# end class


# ======
# TEST
# ======

# --------------------------------------------------------------------
# => Creando Estudiantes / aplicando método constructor
print('\n=> Creando Estudiantes / aplicando método constructor\n')
# --------------------------------------------------------------------

e_1 = Estudiante('Sebas', 36 , 14 , 16) 
e_2 = Estudiante('Ana' , 15 , 18 , 14) 
e_3 = Estudiante('Gabriel' , 20 , 10 , 20)


# -----------------------------
# => método str()
print('\n=> método str()\n')
# -----------------------------

print( str(e_1) ) # Estudiante: Sebas / 36 años | Nota Examen: 14 | Nota Deberes: 16
print( str(e_2) ) # Estudiante: Ana / 15 años | Nota Examen: 18 | Nota Deberes: 14
print( str(e_3) ) # Estudiante: Gabriel / 20 años | Nota Examen: 10 | Nota Deberes: 20


# -----------------------------
# => print(objeto)
print('\n=> print(objeto)\n')
# -----------------------------
# - lo siguiente pasa por haber redefinido str()

print( e_1 ) # Estudiante: Sebas / 36 años | Nota Examen: 14 | Nota Deberes: 16
print( e_2 ) # Estudiante: Ana / 15 años | Nota Examen: 18 | Nota Deberes: 14
print( e_3 ) # Estudiante: Gabriel / 20 años | Nota Examen: 10 | Nota Deberes: 20


# -----------------------------
# => método len()
print('\n=> método len()\n')
# -----------------------------

print( len(e_1) ) # 36
print( len(e_2) ) # 15
print( len(e_3) ) # 20


print('\n')
print('------------------------------------------')

# - al final vemos que los estudiantes se eliminan del registro
# - por defecto esto siempre pasa con estos y todos los objetos creados en Python
# - al momento que se termina la ejecución del script
# - ese es el ciclo de vida de estos elementos
# - como redefinimos __del__ pues este siempre se aplica al final de la ejecución del script

