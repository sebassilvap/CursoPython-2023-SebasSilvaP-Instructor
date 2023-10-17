# ==================================================================
# ¿Cuándo usar str.format() y cuándo fString
# Ejemplo para nunca olvidar

# - 2 criterios válidos según las buenas recomendaciones de Python

# *   a) aquel que ocupe menos espacio de escritura
# *   b) aquel que haga mi línea de código más fácil de leer
# *   c) cuando necesito una automatización en el formato
# ==================================================================


#? 1) Ejemplo 1
print('\n1) Ejemplo 1')
# - En este caso
# - por facilidad de lectura de código
# - se preferiría .format() al fString

auto = {
    'marca' : 'Chevrolet',
    'tipo' : 'Vitara',
    'km' : 10000,
    'en_venta' : False
}

# ----------------
# * RECOMENDADO
# ----------------

print( 'El auto {} de marca: {} tiene {} km. ¿Está en venta? => {}'.format(
    auto['tipo'], auto['marca'], auto['km'], auto['en_venta']
) )

# => podría darle una mejor organizacióna los argumentos, 1 en cada línea
print( 'El auto {} de marca: {} tiene {} km. ¿Está en venta? => {}'.format(
    auto['tipo'],
    auto['marca'],
    auto['km'],
    auto['en_venta']
) )


# -------------------
# ! NO RECOMENDADO
# -------------------

print( f"El auto {auto['tipo']} de marca {auto['marca']} tiene {auto['km']} km. ¿Está en venta? => {auto['en_venta']}" )



#? 2) Ejemplo 2
print('\n2) Ejemplo 2')
# - cuando necesito una automatización en mi formato
# - por ejemplo en el caso de números
# - como sabemos con el fString podemos poner variables dentro del formato


# función promedio de números
# - con str.format() => 3 decimales por defecto
# - con fString => número de decimales controlado en función

# --------------------------------
# => usando str.format()
print('\nusando str.format()\n')
# --------------------------------

def calcular_promedio(*args):
    resultado = 0
    for num in args:
        resultado += num
    # end for
    
    #resultado = resultado / len(args)
    resultado /= len(args)
    
    print('Promedio = {:.3f}'.format(resultado))
    return resultado
# end def

# TEST:
print( calcular_promedio(17,13,15,20,14,13) )

# ------------------------------
# => usando fString
print('\n=> usando fString\n')
# ------------------------------

def calcular_promedio(*args, decimales=3):
    resultado = 0
    for num in args:
        resultado += num
    # end for
    
    #resultado = resultado / len(args)
    resultado /= len(args)
    
    print( f'Promedio = {resultado:.{decimales}f}' )
    return resultado
# end def

# TEST:
print( calcular_promedio(17,13,15,20,14,13) )
print( calcular_promedio(17,13,15,20,14,13, decimales=2) )
print( calcular_promedio(17,13,15,20,14,13, decimales=4) )
print( calcular_promedio(17,13,15,20,14,13, decimales=5) )



#? 3) Elementos IMPORTANTES a recordar
print('\n3) Elementos IMPORTANTES a recordar')
# - hemos visto en esta sección muchos fundamentos sobre .format y fString
# - lo más importante es recordar primero, tratar de usarlos de ahora en adelante
# - prácticamente todo lo qe hemos venido haciendo con print
# - ahora lo podemos hacer usando .format o fString
# - vamos a ver un sencillo ejemplo de elementos aprendidos
# - pero en esta ocasión vamos a usar el formato de Strings

# * EJ:

notas_ingles = {
    'arturo' : 15,
    'maria' : 17,
    'carlos' : 18,
    'sebas' : 14
}

def resumen_notas(notas):
    promedio = 0
    counter = 1
    
    for clave, valor in notas.items():
        print( '{} | Estudiante: {} | Nota: {:.2f}'.format(
            counter,
            clave.title(),
            valor
        ) )
        
        promedio += valor
        counter += 1
    # end for
    
    promedio /= len(notas)
    
    print( f'==> El promedio del curso es: {promedio:.2f}' )
# end def

# TEST:
print()
resumen_notas(notas_ingles)