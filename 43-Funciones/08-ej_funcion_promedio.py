# ===================================
# Ejercicio

# Función para calcular el promedio
# ===================================

#? 1) Solución Básica
print('\n1) Solución Básica')

def promedio_2_numeros(a, b):
    return (a+b)/2
# end def

def promedio_3_numeros(a, b, c):
    return (a+b+c)/3
# end def

# TEST
print( promedio_2_numeros(5,9) )
print( promedio_3_numeros(17,15,20) )


#? 2) Solución con Listas
print('\n2) Solución con Listas')

notas_1 = [17, 14, 16, 19, 13]
notas_2 = [15, 12, 20]

def promedio(lista):
    temp = 0
    
    for nota in lista:
        temp += nota
    # end for
    
    return temp / len(lista)
# end def

# TEST
print( promedio(notas_1) )    
print( promedio(notas_2) )    