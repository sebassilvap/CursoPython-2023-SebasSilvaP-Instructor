# =============================================
# Condicional - Anidado

# - Ejemplo práctico
# - Aplicado al diseño del comando de un juego
# =============================================

#? Ejemplo práctico

# El player tiene 2 opciones
# (1) Ataque
# (2) Defensa

# Existen 2 ataques:
# (A) Golpe Directo
# (B) Hechizo

# => todo esto es controlado por un comando
# - el comando es dado por el usuario con un input
# -------------------------------------------------
# Diseño de input
# - si por ejemplo elijo la opción: (A) Ataque
# - el comando es válido si el usuario ingresa
#   * 1
#   * A o a
#   * 'ataque', 'Ataque', 'AtaQuE'
# -------------------------------------------------

print('''
Opciones de Jugador:
(1) Ataque
(2) Defensa
**********************
''')

comando = input('Ingrese su opción: ')
comando = comando.strip(' ') # para eliminar cualquier tipo de espacio

# opción ataque
if comando == '1' or comando.lower() == 'ataque' or comando.lower() == 'a':
    print('''
          Opciones de Ataque:
          (A) Golpe Directo
          (B) Hechizo
          **********************
          ''')
    opcion_ataque = input('Ingrese su opción: ')
    opcion_ataque = opcion_ataque.strip(' ')
    
    if opcion_ataque.lower() == 'a' or opcion_ataque.lower() == 'golpe directo' or opcion_ataque.lower() == 'g':
        print('Ataque con Golpe Directo - 40 pts')
    elif opcion_ataque.lower() == 'b' or opcion_ataque.lower() == 'hechizo' or opcion_ataque.lower() == 'h':
        print('Ataque con Hechizo - 90 pts')
    else:
        print('Ups! Comando Desconocido!')

# opción defensa
elif comando == '2' or comando.lower() == 'defensa' or comando.lower() == 'd':
    print('Jugador en modo defensa - 50 pts')

# opción incorrecta
else:
    print('Lo siento! Opción Incorrecta!')