# ============================================================
# Recorrido de Diccionarios con Bucle

# - existen varias maneras de hacerlo
# - cada programa o código es distinto
# - el programador debe elegir la manera que más convenga
# - Recordar, que en programación
# - NO existe una sola manera de hacer las cosas
# ============================================================

personaje = {
    'tipo' : 'guerrero',
    'nivel_EXP' : 45,
    'ataque' : 150,
    'defensa' : 200,
    'activo' : True,    
}

print(personaje)


#? 1) for normal => recorre las claves
print('\n1) for normal => recorre las claves')

for elemento in personaje:
    print(elemento)
# end for

print()

for value in personaje:
    print(value)
# end for
    
print()

for key in personaje:
    print(key)
# end for


#? 2) for normal => para acceder al valor con la clave
print('\n2) for normal => para acceder al valor con la clave')

for i in personaje:
    print( i, '--', personaje[i] )
# end for


#? 3) for + .keys() => otra manera de acceder a las claves
print('\n3) for + .keys() => otra manera de acceder a las claves')

for clave in personaje.keys():
    print(clave)
# end for


#? 4) for + .values() => para acceder a los valores de la clave:
print('\n4) for + .values() => para acceder a los valores de la clave:')

for valor in personaje.values():
    print(valor)
# end for


#? 5) for + .items() => manera más usada : clave + valor
print('\n5) for + .items() => manera más usada : clave + valor')

for clave, valor in personaje.items():
    print( clave, '--', valor )
# end for