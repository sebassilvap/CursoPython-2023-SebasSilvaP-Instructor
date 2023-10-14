# =============================================================
# Introducción a Funciones

# - ¿Por qué Funciones?
# - Veamos un ejemplo de cómo sería la programación sin ellas
# =============================================================

nombre = 'Sebas'
edad = 36
nota_final = 15.5

print( '\nSu nombre es:', nombre )
print( 'Usted tiene', edad, 'años' )
print( 'Su nota final es =', nota_final )


nombre = 'Andy'
edad = 25
nota_final = 16.8

print( '\nSu nombre es:', nombre )
print( 'Usted tiene', edad, 'años' )
print( 'Su nota final es =', nota_final )

nombre = 'Carla'
edad = 30
nota_final = 19.9

print( '\nSu nombre es:', nombre )
print( 'Usted tiene', edad, 'años' )
print( 'Su nota final es =', nota_final )


# ------------------------------------------------------------
# - ¿Es esto óptimo?
# - ¿Repetir líneas de programación que hacen lo mismo?
# - en este caso son 3
# - pero si se tratase de una funcionalidad de 1000 líneas
# - ¿sería conveniente hacerlo así?
# * => NO
# ------------------------------------------------------------

# => en el siguiente script veamos como sería esto de manera óptima utilizando funciones

