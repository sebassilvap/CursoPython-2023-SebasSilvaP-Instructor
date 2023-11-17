# =======================================================================
# Módulos + POO

# - hemos aprendido ya el tema de módulos
# - y como organizar nuestro código de python en una estructura modular
# - es momento de ponerla en práctica con la definición de las clases
# - y separar las clases dentro de módulos
# - para poderlas importar en nuestro archivo principal
# ! mientas más organizado esté nuestro código, mejor será !
# =======================================================================

from estudiante import Estudiante

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