# ============================================================
# time.time() & time.time_ns()

# *     time.time() => milisegundos desde el tiempo 0 / float
# *     time.time_ns() => nanosegundos desde el tiempo 0 / int

# - puede ser muy útil para crear un indentificador único
# - cuando realizamos un programa sencillo
# - identificador único, ej: la cédula
# ============================================================

import time


#? 1) Uso básico de time & time_ns
print('\n1) Uso básico de time & time_ns')

print( time.time() ) # 1699114323.1108518
print( time.time_ns() ) # 1699114323110851800



#? 2) Ejemplo - Entrada de un usuario
print('\n2) Ejemplo - Entrada de un usuario')
# - realizar un programa
# - donde por medio de un bucle, tengamos 3 opciones
# - ingresar un usuario
# - mostrar usuarios
# - salir
# - los usuarios se guardan con id y nombre por medio de un diccionario


# --------------------------------------
# crear diccionario inicial de usuarios
# --------------------------------------

usuarios = {
    'id' : 'nombre_usuario'
}

# ---------------------------
# funciones para el programa
# ---------------------------

def presentar_opciones():
    print('\nPROGRAMA PARA CREAR USUARIO')
    print('1 - ingresar usuario')
    print('2 - mostrar usuarios')
    print('3 - salir (s)')
    print()
# end def


def crear_id():
    return time.time_ns()
# end def


def agregar_usuario():
    # => pedir el nombre de nuevo usuario
    nombre_usuario = input('Ingrese el nombre: ')
    nombre_usuario = nombre_usuario.strip(' ').title()
    
    # => crear id
    id_usuario = crear_id()
    
    # => agregar al diccionario
    usuarios[id_usuario] = nombre_usuario
# end def


def mostrar_usuarios(diccionario_usuarios):
    counter = 0
    
    for id, usuario in diccionario_usuarios.items():
        if counter == 0:
            print('ID   |   NOMBRE')
            counter += 1
        else:
            print( 'id: {} | nombre: {}'.format(id, usuario) )
            counter += 1
    # end for
# end def


# --------------------
# bucle del programa  
# --------------------

while True:
    presentar_opciones()
    
    opcion_user = input('Ingrese su opción: ')
    opcion_user = opcion_user.strip(' ').lower()
    
    if opcion_user == '1':
        agregar_usuario()
    elif opcion_user == '2':
        mostrar_usuarios(usuarios)
    elif opcion_user == '3' or opcion_user == 's':
        break # salir del loop
    else:
        print('ERROR - opción incorrecta')
# end while