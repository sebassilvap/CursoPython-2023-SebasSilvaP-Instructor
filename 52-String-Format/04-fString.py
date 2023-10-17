# =========================================================
# fString

# * Se lo puede usar a partir de Python 3.6
# - es una simplificación más grande del string.format()
# - realiza lo mismo que el string.format()
# - y algunas cosas adicionales
# =========================================================


#? 1) Uso Básico de fString
print('\n1) Uso Básico de fString')

lenguaje = 'python'

# ----------------------------
# => str.format()
print('\n=> str.format()\n')
# ----------------------------

print( 'Me encanta programar en {}'.format(lenguaje) )


# -----------------------
# => fString
print('\n=> fString\n')
# -----------------------
# - crea un string con variables dinámicas
# - se lo puede crear con '', "", o también ''', """

print( f"Me encanta {lenguaje} !!" )
print( f'El mejor lenguaje de todos es {lenguaje}' )

txt_1 = f'''
{lenguaje} es divertido de aprender!
Me encanta {lenguaje}.
'''

txt_2 = f"""
Los fString son increíbles!
{lenguaje} no deja de sorprenderme
"""

print(txt_1, type(txt_1))
print(txt_2, type(txt_2))



#? 2) Podemos usar cualquier tipo de variable
print('\n2) Podemos usar cualquier tipo de variable')

auto = {
    'marca' : 'Chevrolet',
    'tipo' : 'Vitara',
    'km' : 10000,
    'en_venta' : False
}

# ----------------------------
# => str.format()
print('\n=> str.format()\n')
# ----------------------------

print( 'El auto {} de marca: {} tiene {} km. ¿Está en venta? => {}'.format(
    auto['tipo'], auto['marca'], auto['km'], auto['en_venta']
) )

# -----------------------
# => fString
print('\n=> fString\n')
# -----------------------

print( f"El auto {auto['tipo']} de marca {auto['marca']} tiene {auto['km']} km. ¿Está en venta? => {auto['en_venta']}" )



#? 3) Podemos pasar valores, variables o hasta expresiones
print('\n3) Podemos pasar valores, variables o hasta expresiones')

num = 10

def sumar100(n):
    return n + 100
# end def


# ----------------------------
# => str.format()
print('\n=> str.format()\n')
# ----------------------------

result_1 = 'El número {} - {} = {}. sumar100 = {} y es {}'.format(
    num, 5, num - 5, sumar100(num), 'PAR' if num % 2 == 0 else 'IMPAR'
)

print(result_1)


# -----------------------
# => fString
print('\n=> fString\n')
# -----------------------

result_2 = f'El número {num} - 5 = {num - 5}. sumar100 = {sumar100(num)} y es {"PAR" if num % 2 == 0 else "IMPAR"}'

print(result_2)



#? 4) Alineación & Truncamiento con fString
print('\n4) Alineación & Truncamiento con fString')
# Alineación / Padding de Caracteres
#*   {:<x}         =>  alineación o padding a la izquierda con x caracteres
#*   {:>x}         =>  alineación o padding a la derecha con x caracteres
#*   {:^x}         =>  alineación o padding al centro con x caracteres

#*   {:x}          =>  alineación o padding a la IZQUIERDA con x caracteres (texto)
#*   {:x}          =>  alineación o padding a la DERECHA con x caracteres (numeros)

# Truncamiento / Recorte de caracteres
#*   {:.x}         =>  Recorte de string a x caracteres

# Alineación + Truncamiento
#*   {:x.y}        =>  Padding a la izquierda en x + truncamiento en y
#*   {:<x.y}       =>  Padding a la izquierda en x + truncamiento en y
#*   {:>x.y}       =>  Padding a la derecha en x + truncamiento en y
#*   {:^x.y}       =>  Padding al centro en x + truncamiento en y


# ----------------------------
# => str.format()
print('\n=> str.format()\n')
# ----------------------------

p = 'capitalización'

print( 'La palabra {} es muy grande'.format(p) )
print( 'La palabra {:>15.7} es muy grande'.format(p) )
print( 'La palabra {:<15.7} es muy grande'.format(p) )
print( 'La palabra {:^15.7} es muy grande'.format(p) )


# -----------------------
# => fString
print('\n=> fString\n')
# -----------------------
# - la única diferencia
# - es que antes de los 2 puntos :
# - debemos poner la variable

print( f'La palabra {p} es muy grande!' )
print( f'La palabra {p:>15.7} es muy grande!' )
print( f'La palabra {p:<15.7} es muy grande!' )
print( f'La palabra {p:^15.7} es muy grande!' )



#? 5) Formato de Texto utilizando variables
print('\n5) Formato de Texto utilizando variables')
# - esta es una ventaja del fString
# - que no podemos utilizar con el str.format()
# - podemos definir los valores de formato como variables
# - para esto se debe usar doble llave {{ }}


# -------------------------------------------
# => Intentando con str.format()
print('\n=> Intentando con str.format()\n')
# -------------------------------------------

nombre = 'Mariana'
recorte = 4
espacios = 10

print( 'La estudiante {:>10.4} ha aprobado todas las materias!'.format(nombre) )

#print( 'La estudiante {:>{espacios}.{recorte}} ha aprobado todas las materias!'.format(nombre) )
#! KeyError: 'espacios'

#print( 'La estudiante {:>espacios.recorte} ha aprobado todas las materias!'.format(nombre) )
#! ValueError: Invalid format specifier '>espacios.recorte' for object of type 'str'


# -----------------------
# => fString
print('\n=> fString\n')
# -----------------------

print( f'La estudiante {nombre:>10.4} es muy aplicada!' )

#print( f'La estudiante {nombre:>espacios.recorte} es muy aplicada!' )
#! ValueError: Invalid format specifier '>espacios.recorte' for object of type 'str'


# * SOLUCIÓN CORRECTA
# - se debe usar doble llave {{ }}

print( f'La estudiante {nombre:>{espacios}.{recorte}} es muy aplicada!' )