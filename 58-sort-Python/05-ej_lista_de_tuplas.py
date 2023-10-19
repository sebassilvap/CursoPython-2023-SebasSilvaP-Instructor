# ===========================================================
# Ejercicio
# En casos reales y prácticos tenemos lo siguiente:

#       * Listas de Listas (Listas 2D)
#       * Listas de Tuplas
#       * Listas de Diccionarios

# PERO:
# - Básicamente, lo que aprendimos en la lección anterior
# - sobre la clasificación de diccionarios
# - utilizando key y la función lambda
# - se aplica en estos casos para permitirnos el orden
# - en el caso de diccionarios, es un poco especial
# - porque no podemos acceder con indexing normal
# - por lo cual como ya aprendimos podemos trasnformar
# - a lista de tuplas y luego a diccionario con dict()
# ===========================================================


#? EJERCICIO - Lista de Tuplas
print('\nEJERCICIO - Lista de Tuplas\n')

# ---------------------------------------------------------------------------
# - tenemos una estructura de notas para la clase de programación
# - la primera columna es el nombre del estudiante
# - la segunda es la nota de deberes / 20
# - la tercera es la nota del proyecto final / 20
# - la cuarta es la nota del examen / 20
# - por seguridad esta estructura está dada como una lista de tuplas
# - de tal manera que esta estructura no se pueda modificar
# - se pide "modificar" esta estructura en una nueva variable
# - que me muestre la nota final en una quinta columna
# - la nota final obedece a la siguiente ecuación:

# *    nota_final = nota_deberes*0.2 + nota_proyecto*0.3 + nota_examen*0.5

# - en base a la nota final se pide crear una sexta columna

# *    si la nota_final < 15 => el estudiante reprueba

# - mostrar 3 ordenamientos:
#?     1) quienes aprueban primero, quienes no segundo
#?     2) ordenar por nota_final de la más alta a la más baja
#?     3) ordenar por nota_examen de la más baja a la más alta
# ---------------------------------------------------------------------------

#     nombre, deberes, proyecto, examen
notas_programacion = [
    ('Xime', 12, 14, 18),
    ('Sebas', 18, 14, 10),
    ('Andrea', 10, 15, 17),
    ('Roberto', 20, 10, 13),
    ('Marcelo', 17, 15, 14)
]


# -----------------------------------------------
#? 1) Función de Ayuda: print_datos()
print('\n1) Función de Ayuda: print_datos()\n')
# -----------------------------------------------

def print_datos(lista):
    for sublista in lista:
        print(sublista)
    # end for
# end def



# ------------------------------------
#? 2) ¿Por qué con tuplas?
print('\n2) ¿Por qué con tuplas?\n')
# ------------------------------------

# => si trato de cambiar una nota:

#! notas_programacion[0][3] = 14 
#! TypeError: 'tuple' object does not support item assignment

# => si fuese lista de listas

test = [
    ['Xime', 12, 14, 18],
    ['Sebas', 18, 14, 10],
    ['Andrea', 10, 15, 17],
    ['Roberto', 20, 10, 13],
    ['Marcelo', 17, 15, 14]
]

test[0][3] = 14 

print_datos(test)

#! Pero queremos restingir el acceso para evitar hacer esto
# - por eso lo ponemos como tuplas



# ------------------------------------------------------------------------
#? 3) Función para cambiar de lista de tuplas a lista de listas
print('\n3) Función para cambiar de lista de tuplas a lista de listas\n')
# ------------------------------------------------------------------------
# - para poder manipular los datos
# - vamos a cambiar en primer lugar la estructura
# - en una nueva variable

def cambiar_a_lista_de_listas(lista_tuplas):
    lista_de_lista = []
    
    for elemento in lista_tuplas:
        lista_de_lista.append( list(elemento) )
    # end for
    
    return lista_de_lista
# end def

notas_programacion_mod = cambiar_a_lista_de_listas(notas_programacion)

#print_datos(notas_programacion_mod) # TEST



# -------------------------------------------------------
#? 4) Función para cálculos y añadir columnas
print('\n4) Función para cálculos y añadir columnas\n')
# -------------------------------------------------------
# - 5ta columna: nota_final
#   * nota_final = nota_deberes*0.2 + nota_proyecto*0.3 + nota_examen*0.5
# - 6ta columna: PASA ó NO PASA
#   * PASA si > nota_final > 14

def calculos_modificacion(lista_mod):
    nueva_lista_mod = []
    
    for fila in lista_mod:

        fila_temp = []
        nota_final = 0
        
        for i, v in enumerate(fila):
            match i:
                case 0:
                    fila_temp.append(v)
                case 1:
                    fila_temp.append(v)
                    nota_final += 0.2*v
                case 2:
                    fila_temp.append(v)
                    nota_final += 0.3*v
                case 3:
                    fila_temp.append(v)
                    nota_final += 0.5*v
            # end match-case
        # end for
        
        # => append de 5ta columna : nota_final
        nota_final = float('{:.2f}'.format(nota_final)) # truco para reducir a máximo 2 decimales
        fila_temp.append(nota_final)
        
        # => append de 6ta columna : pasa o no pasa
        fila_temp.append( 'PASA' if nota_final > 14 else 'NO PASA' )
        
        # => append de fila_temp en nueva_lista_mod
        nueva_lista_mod.append(fila_temp)
    # end for
    
    return nueva_lista_mod
# end def

notas_programacion_mod = calculos_modificacion(notas_programacion_mod)

#print_datos(notas_programacion_mod) # TEST



# ------------------------------------------------------------------------
#? 5) Función para cambiar de lista de listas a lista de tuplas
print('\n5) Función para cambiar de lista de listas a lista de tuplas\n')
# ------------------------------------------------------------------------

def cambiar_a_lista_de_tuplas(lista_listas):
    lista_de_tupla = []
    
    for elemento in lista_listas:
        lista_de_tupla.append( tuple(elemento) )
    # end for
    
    return lista_de_tupla
# end def

notas_programacion_mod = cambiar_a_lista_de_tuplas(notas_programacion_mod)

#print_datos(notas_programacion_mod) # TEST



# ---------------------------
#? 6) Ordenamientos
print('\n6) Ordenamientos')
# ---------------------------

orden_pasa_no = lambda columna : columna[5]
orden_nota_final = lambda columna : columna[4]
orden_examen = lambda columna : columna[3]

notas_orden_pasa_no = sorted(
    notas_programacion_mod,
    key = orden_pasa_no,
    reverse = True
)

notas_orden_nota_final = sorted(
    notas_programacion_mod,
    key = orden_nota_final,
    reverse = True
)

notas_orden_examen = sorted(
    notas_programacion_mod,
    key = orden_examen
)

# TEST FINAL
print('\n\nOrdenamiento: PASA / NO PASA')
print_datos(notas_orden_pasa_no)

print('\n\nOrdenamiento: Nota Final')
print_datos(notas_orden_nota_final)

print('\n\nOrdenamiento: Nota Examen')
print_datos(notas_orden_examen)