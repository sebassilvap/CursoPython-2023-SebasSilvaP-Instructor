# ======================================
# Ejercicio

# - Aplicación de decoradores
# - Resumen de Notas de un Estudiante
# ======================================

#? 1) Definimos 2 estudiantes con diccionarios
print('\n1) Definimos 2 estudiantes con diccionarios')

juan = {
    'Nombre' : 'Juan',
    'Álgebra' : 16,
    'Inglés' : 19,
    'Literatura' : 14,
    'Física' : 17
}

xiomara = {
    'Nombre' : 'Xiomara',
    'Álgebra' : 18,
    'Inglés' : 14,
    'Literatura' : 17,
    'Física' : 19
}



#? 2) Definimos una función normal sin decoradores
print('\n2) Definimos una función normal sin decoradores')
# - para ver como sería este ejercicio
# - sin el uso de decoradores

def presentar_notas(estudiante):
    counter = 1
    promedio = 0
    
    print('\nResumen de Calificaciones para el estudiante {}'.format(estudiante['Nombre']))
    
    for k, v in estudiante.items():
        if k == 'Nombre':
            continue
        else:
            print( '{}) {} : {}'.format(counter, k, v) )
            counter += 1
            promedio += v
        # end if
    # end for
    
    promedio /= len(estudiante) - 1
    
    print('El promedio del estudiante {} es = {:.2f}\n'.format(estudiante['Nombre'], promedio))
# end def

# TEST
presentar_notas(juan)
presentar_notas(xiomara)



#? 3) Utilizando decoradores
print('\n3) Utilizando decoradores')
# - con el decorador pretendemos
# - dar una introducción y un final
# - al momento de llamar la función
# - y evitarnos colocar estos elementos en la función principal


# => definición de función decoradora
def decorador_estudiantes(funcion):
    def funcion_wrapper(*args, **kwargs):
        
        info_estudiante = args[0]
        nombre_estudiante = info_estudiante['Nombre']
        
                
        print('\n\nBienvenido al programa de Evaluación del Estudiante')
        print('Nombre del estudiante: {}'.format(nombre_estudiante))
        
        funcion(*args, *kwargs)
        
        print('--------------------------------------------------')
        print('Fin de la Evaluación del Estudiante: {}\n\n'.format(nombre_estudiante))
    # end def
    
    return funcion_wrapper
# end def


# => función decorada # 1 => evaluar_estudiantes
@decorador_estudiantes
def evaluar_estudiante(estudiante):
    counter = 1
    promedio = 0
    
    for k,v in estudiante.items():
        if k != 'Nombre':
            print( '{}) {}: {}'.format(counter, k, v) )
            counter += 1
            promedio += v
        # end if
    # end for
    
    promedio /= len(estudiante) - 1
    print('El promedio del semestre para el estudiante {} es = {:.3f}'.format(
        estudiante['Nombre'],
        promedio)
        )
# end def


# => función decorada # 2 => presentar_nota_max_min
@decorador_estudiantes
def presentar_nota_max_min(estudiante):
    notas = []
    
    for k, v in estudiante.items():
        if k != 'Nombre':
            notas.append(v)
        # end if
    # end for
    
    nota_max = max(notas)
    nota_min = min(notas)
    
    print('La nota máxima es: {}'.format(nota_max))
    print('La nota mínima es: {}'.format(nota_min))
# end def



#? 4) Test Final
print('\n4) Test Final')

# => estudiante juan
evaluar_estudiante(juan)
presentar_nota_max_min(juan)

# => estudiante xiomara
evaluar_estudiante(xiomara)
presentar_nota_max_min(xiomara)