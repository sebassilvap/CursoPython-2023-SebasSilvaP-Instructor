# ===============================================================
# Usando los argumentos mandados desde el CMD

# - al poder capturar estos argumentos
# - entonces los podríamos usar
# - esta sería entonces otra manera
# - como el usuario podría interactuar con un script de Python

# ! RECORDAR:
# - elemento 0 de lista => path
# - de 1 en adelante => argumentos sys.argvs

# ! NOTA
# - estos argumentos vienen como STRING
# - cuando se utiliza """ """ el archivo no corre en el command window con sys
# - ver la imagen de referencia => ejemplo
# ===============================================================


#? Script para cálculo de promedio de valores numéricos
print('\nScript para cálculo de promedio de valores')

import sys

argumentos_cmd = sys.argv[1:] # el 0 => es el path

# ----------------------------------------------
# TEST: Comprobación tipo de dato de argumentos
# ----------------------------------------------


#for argumento in argumentos_cmd:
#    print( argumento , type(argumento) )
## end for

# => TEST en CMD:
#*   C:\Users\Admin\Desktop\CLUB CODING GAMING 2023-2024\03-Instructor\70-Command-Line-Args>python 02-usando_sys_args.py 10 hola 3 4
#    Script para cálculo de promedio de valores
#    10 <class 'str'>
#    hola <class 'str'>
#    3 <class 'str'>
#    4 <class 'str'>


# ----------------------------------
# Función para cálculo de promedio
# ----------------------------------

def calculo_promedio(lista_valores):
    suma = 0
    for valor in lista_valores:
        suma += float(valor)
    # end for
    
    promedio = suma / len(lista_valores)
    
    return promedio
# end def


# -----------------------------------------
# Función para presentación de resultados
# -----------------------------------------

def presentar_resultados(lista_valores, promedio):
    print('Los valores numéricos ingresados son: ')
    for i, valor in enumerate(lista_valores):
        print( 'Valor # {} = {}'.format( i+1 , float(valor) ) )
    # end for
    print('El cálculo del promedio es:')
    print( 'PROMEDIO = {:.4f}'.format(promedio) )
# end def


# ----------------------
# Cálculo del promedio
# ----------------------
promedio = calculo_promedio(argumentos_cmd)


# -----------------------------------
# Presentación de Resultados en CMD
# -----------------------------------

presentar_resultados(
    argumentos_cmd,
    promedio
)