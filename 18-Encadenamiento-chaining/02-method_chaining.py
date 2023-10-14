# =========================================================
# Encadenamiento de Métodos
# (Method - Chaining)

# - chaining / encadenamiento de métodos
# - es un estilo de programación
# - se invocan métodos de manera secuencial / uno tras otro
# - en orden de izquierda a derecha
# - aplicados sobre una variable
# =========================================================


#? 1) Sin usar method-chaining
print('\n1) Sin usar method-chaining\n')

nombre = input('Su nombre & apellido: ')
nombre = nombre.strip(' ') # 1
nombre = nombre.title() # 2
nombre = ' '.join(nombre) # 3
print('Nombre con Formato: ' , nombre) # 4

# => 4 líneas de código en total



#? 2) CON method chaining
print('\n2) CON method chaining\n')

# => el orden es importante !! 
# ejecución SECUENCIAL de izquierda a derecha

# => 1 línea de código
print( ' '.join( input('Nombre & Apellido: ').strip(' ').title() ) ) 
