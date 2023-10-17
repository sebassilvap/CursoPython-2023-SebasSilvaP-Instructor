# =========================================================
# fString

# * Se lo puede usar a partir de Python 3.6
# - es una simplificación más grande del string.format()
# - realiza lo mismo que el string.format()
# - y algunas cosas adicionales

# =========================================================


#? 1) Variables o Valores de manera directa
print('\n1) Variables o Valores de manera directa')

num = 25

# ----------------------------
# => str.format()
print('\n=> str.format()\n')
# ----------------------------

print( 'El número es = {}'.format(25) )
print( 'El número es = {}'.format(num) )


# -----------------------
# => fString
print('\n=> fString\n')
# -----------------------

print( f'El número es igual a {25}' )
print( f'El número es igual a {num}' )



#? 2) Recortando Número de Digitos y Número de Decimales
print('\n2) Recortando Número de Digitos y Número de Decimales')

#     RECORDAR:
#     str.format() => para formato de números
#*    {:.x}   =>  Recorte de Número de digitos totales a x incluyendo decimales
#*    {:.xf}  =>  Recorte de Número de decimales a x
 

PI = 3.14159265358979323846

# ----------------------------
# => str.format()
print('\n=> str.format()\n')
# ----------------------------

print( 'La constante PI = {}'.format(PI) )

# => recorte de dígitos
print()
print( 'La constante PI = {:.5}'.format(PI) )
print( 'La constante PI = {:.3}'.format(PI) )

# => recorte de decimales
print()
print( 'La constante PI = {:.5f}'.format(PI) )
print( 'La constante PI = {:.3f}'.format(PI) )


# -----------------------
# => fString
print('\n=> fString\n')
# -----------------------
# - igualmente que con el texto
# - las variables van a la izquierda de los 2 puntos

print( f'La constante PI = {PI}' )

# => recorte de dígitos
print()
print( f'La constante PI = {PI:.5}' )
print( f'La constante PI = {PI:.3}' )

# => recorte de decimales
print()
print( f'La constante PI = {PI:.5f}' )
print( f'La constante PI = {PI:.3f}' )



#? 3) Alineación de Números (int / float)
print('\n3) Alineación de Números (int / float)')

#     RECORDAR:
#     str.format() => para formato de números
#*    {:x}    =>  Alineación a la DERECHA (para números int o float, no CON texto) 
#*    {:>x}   =>  Alineación a la DERECHA
#*    {:<x}   =>  Alineación a la IZQUIERDA
#*    {:^x}   =>  Alineación al CENTRO


# => multiasignación
n1 , d1 = 1 , 1.1
n2 , d2 = 12 , 1.12
n3 , d3 = 123 , 1.123
n4 , d4 = 1234 , 1.1234
n5 , d5 = 12345 , 1.12345


# => número máximo de caracteres: dado por n5 & d5 --> 5 y 7
# - una manera de averiguar esto sería así:
#*  print( len(str(n5)), len(str(d5)) ) # 5 7


# ----------------------------
# => str.format()
print('\n=> str.format()\n')
# ----------------------------

# => Sin Alineación
print('\n=> Sin Alineación\n')
print( '{} - {}'.format(n1, d1) )
print( '{} - {}'.format(n2, d2) )
print( '{} - {}'.format(n3, d3) )
print( '{} - {}'.format(n4, d4) )
print( '{} - {}'.format(n5, d5) )

# => Alineación DERECHA por defecto {:x}
print('\n=> Alineación DERECHA por defecto {:x}\n')
print( '{:5} - {:7}'.format(n1, d1) )
print( '{:5} - {:7}'.format(n2, d2) )
print( '{:5} - {:7}'.format(n3, d3) )
print( '{:5} - {:7}'.format(n4, d4) )
print( '{:5} - {:7}'.format(n5, d5) )

# => Alineación DERECHA {:>x}
print('\n=> Alineación DERECHA {:>x}\n')
print( '{:>5} - {:>7}'.format(n1, d1) )
print( '{:>5} - {:>7}'.format(n2, d2) )
print( '{:>5} - {:>7}'.format(n3, d3) )
print( '{:>5} - {:>7}'.format(n4, d4) )
print( '{:>5} - {:>7}'.format(n5, d5) )

# => Alineación IZQUIERDA {:<x}
print('\n=> Alineación IZQUIERDA {:<x}\n')
print( '{:<5} - {:<7}'.format(n1, d1) )
print( '{:<5} - {:<7}'.format(n2, d2) )
print( '{:<5} - {:<7}'.format(n3, d3) )
print( '{:<5} - {:<7}'.format(n4, d4) )
print( '{:<5} - {:<7}'.format(n5, d5) )

# => Alineación CENTRO {:^x}
print('\n=> Alineación CENTRO {:^x}\n')
print( '{:^5} - {:^7}'.format(n1, d1) )
print( '{:^5} - {:^7}'.format(n2, d2) )
print( '{:^5} - {:^7}'.format(n3, d3) )
print( '{:^5} - {:^7}'.format(n4, d4) )
print( '{:^5} - {:^7}'.format(n5, d5) )


# -----------------------
# => fString
print('\n=> fString\n')
# -----------------------
# - aquí podemos hacerlo más práctico
# - y usando algunas facilidades del fString
# - como por ejemplo definir una variable para el espaciado
# - y utilizar la técnica de la doble llave {{ }}

# => en lugar de multiasignación puedo hacer lo siguiente
"""
n1 , d1 = 1 , 1.1
n2 , d2 = 12 , 1.12
n3 , d3 = 123 , 1.123
n4 , d4 = 1234 , 1.1234
n5 , d5 = 12345 , 1.12345
"""

list_int = [n1, n2, n3, n4, n5] = [1, 12, 123, 1234, 12345]
list_float = [d1, d2, d3, d4, d5] = [1.1, 1.12, 1.123, 1.1234, 1.12345]

#print( list_int )
#print( list_float )

len_int = len( str(max(list_int)) )
len_float = len( str(max(list_float)) )

#print( len_int )
#print( len_float )


# => Sin Alineación
print('\n=> Sin Alineación\n')
print( f'{n1} - {d1}' )
print( f'{n2} - {d2}' )
print( f'{n3} - {d3}' )
print( f'{n4} - {d4}' )
print( f'{n5} - {d5}' )

# => Alineación DERECHA por defecto {valor:x}
print('\n=> Alineación DERECHA por defecto {valor:x}\n')
print( f'{n1:{len_int}} - {d1:{len_float}}' )
print( f'{n2:{len_int}} - {d2:{len_float}}' )
print( f'{n3:{len_int}} - {d3:{len_float}}' )
print( f'{n4:{len_int}} - {d4:{len_float}}' )
print( f'{n5:{len_int}} - {d5:{len_float}}' )

# => Alineación DERECHA {valor:>x}
print('\n=> Alineación DERECHA {valor:>x}\n')
print( f'{n1:>{len_int}} - {d1:>{len_float}}' )
print( f'{n2:>{len_int}} - {d2:>{len_float}}' )
print( f'{n3:>{len_int}} - {d3:>{len_float}}' )
print( f'{n4:>{len_int}} - {d4:>{len_float}}' )
print( f'{n5:>{len_int}} - {d5:>{len_float}}' )

# => Alineación IZQUIERDA {valor:<x}
print('\n=> Alineación IZQUIERDA {valor:<x}\n')
print( f'{n1:<{len_int}} - {d1:<{len_float}}' )
print( f'{n2:<{len_int}} - {d2:<{len_float}}' )
print( f'{n3:<{len_int}} - {d3:<{len_float}}' )
print( f'{n4:<{len_int}} - {d4:<{len_float}}' )
print( f'{n5:<{len_int}} - {d5:<{len_float}}' )

# => Alineación CENTRO {valor:^x}
print('\n=> Alineación CENTRO {valor:^x}\n')
print( f'{n1:^{len_int}} - {d1:^{len_float}}' )
print( f'{n2:^{len_int}} - {d2:^{len_float}}' )
print( f'{n3:^{len_int}} - {d3:^{len_float}}' )
print( f'{n4:^{len_int}} - {d4:^{len_float}}' )
print( f'{n5:^{len_int}} - {d5:^{len_float}}' )



#? 4) Relleno de Ceros en Números INT => {valor:0xd} ó {valor:0x}
print('\n4) Relleno de Ceros en Números INT => {valor:0xd}')
# - el formato {:0xd} con la "d" sólo funciona con el fString
# - también podemos usar de manera general sin la d {:0x}
# ! {:0xd} => no funciona con str.format()


list_int = [n1, n2, n3, n4, n5] = [1, 12, 123, 1234, 12345]
len_int = len( str(max(list_int)) ) # 5


# ----------------------------
# => str.format()
print('\n=> str.format()\n')
# ----------------------------

print( 'Número = {:05}'.format(n1) )
print( 'Número = {:05}'.format(n2) )
print( 'Número = {:05}'.format(n3) )
print( 'Número = {:05}'.format(n4) )
print( 'Número = {:05}'.format(n5) )


# -----------------------
# => fString
print('\n=> fString\n')
# -----------------------

print( f'{n1:05d} | {n1:05}' )
print( f'{n2:05d} | {n2:05}' )
print( f'{n3:05d} | {n3:05}' )
print( f'{n4:05d} | {n4:05}' )
print( f'{n5:05d} | {n5:05}' )

print()

print( f'{n1:0{len_int}d} | {n1:0{len_int}}' )
print( f'{n2:0{len_int}d} | {n2:0{len_int}}' )
print( f'{n3:0{len_int}d} | {n3:0{len_int}}' )
print( f'{n4:0{len_int}d} | {n4:0{len_int}}' )
print( f'{n5:0{len_int}d} | {n5:0{len_int}}' )



#? 5) Alineación Derecha + Recorte de Decimales => {:x.yf}
print('\n5) Alineación Derecha + Recorte de Decimales => {:x.yf}')

num_1 = 1234567.123456
num_2 = 123.12345
num_3 = 12345.1
num_4 = 1234
num_5 = 12

# formato deseado: 1234567.12
#print(len('1234567.12')) # 10

# ----------------------------
# => str.format()
print('\n=> str.format()\n')
# ----------------------------
print( '{:10.2f}'.format(num_1) )
print( '{:10.2f}'.format(num_2) )
print( '{:10.2f}'.format(num_3) )
print( '{:10.2f}'.format(num_4) )
print( '{:10.2f}'.format(num_5) )


# -----------------------
# => fString
print('\n=> fString\n')
# -----------------------
num_decimales = 2
num_caracteres = len('1234567.12') # 10

print( f'{num_1:{num_caracteres}.{num_decimales}f}' )
print( f'{num_2:{num_caracteres}.{num_decimales}f}' )
print( f'{num_3:{num_caracteres}.{num_decimales}f}' )
print( f'{num_4:{num_caracteres}.{num_decimales}f}' )
print( f'{num_5:{num_caracteres}.{num_decimales}f}' )



#? 6) Relleno de CEROS + Recorte de Decimales => {:0x.yf}
print('\n6) Relleno de CEROS + Recorte de Decimales => {:0x.yf}')

num_1 = 1234567.123456
num_2 = 123.12345
num_3 = 12345.1
num_4 = 1234
num_5 = 12

# formato deseado: 
# - 15 espaciados
# - 3 decimales

# ----------------------------
# => str.format()
print('\n=> str.format()\n')
# ----------------------------
print( '{:015.3f}'.format(num_1) )
print( '{:015.3f}'.format(num_2) )
print( '{:015.3f}'.format(num_3) )
print( '{:015.3f}'.format(num_4) )
print( '{:015.3f}'.format(num_5) )


# -----------------------
# => fString
print('\n=> fString\n')
# -----------------------
num_decimales = 3
num_caracteres = 15

print( f'{num_1:0{num_caracteres}.{num_decimales}f}' )
print( f'{num_2:0{num_caracteres}.{num_decimales}f}' )
print( f'{num_3:0{num_caracteres}.{num_decimales}f}' )
print( f'{num_4:0{num_caracteres}.{num_decimales}f}' )
print( f'{num_5:0{num_caracteres}.{num_decimales}f}' )