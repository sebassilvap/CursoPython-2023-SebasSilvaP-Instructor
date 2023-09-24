# ========================================
# Condicional - Anidado

# - es básicamente un if dentro de un if
# ========================================

#? Ejemplo
# - Análisis de un número

#numero = 8

# => interactuando con el usuario
numero = int( input('Ingrese un número: ') )

if numero >= 0 and numero <= 10:
    print('Número entre 0 y 10')
    
    if numero >= 0 and numero <= 5:
        print('Número entre 0 y 5 !!')
    elif numero > 5 and numero <= 10:
        print('Número mayor que 5 y menor o igual que 10')
else:
    print('Número mayor a 10')