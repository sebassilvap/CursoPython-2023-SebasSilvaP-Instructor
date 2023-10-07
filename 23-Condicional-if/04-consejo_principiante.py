# ============================================================================
# Consejo para principiantes

# - al iniciar en la programación ya sea de python o cualquier otro lenguaje
# - no cohibirse de usar comentarios
# - los comentarios son un recurso INCREÍBLE de aprendizaje
# - en el caso de python podemos usar comentarios para señalar
# - de manera simbólica
# - el final de un bloque de código
# - por ejemplo para el caso del if
# ============================================================================

nivel_gasolina = 60

if nivel_gasolina > 80 and nivel_gasolina <= 100:
    print('Nivel Óptimo - Máxima Condición')
elif nivel_gasolina > 30 and nivel_gasolina <= 80:
    print('Nivel Intermedio - Atención!')
elif nivel_gasolina > 0 and nivel_gasolina <= 30:
    print('Nivel Bajo - Peligro!')
else: 
    print('SIN GASOLINA')
# end if

print('El nivel de gasolina es:', nivel_gasolina, '%')