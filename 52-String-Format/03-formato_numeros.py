# ===============================================================================
# str.format() => para formato de números

#*   {:.x}    =>  Recorte de Número de digitos totales a x incluyendo decimales
#*   {:.xf}   =>  Recorte de Número de decimales a x
 
#*   {:x}     =>  Alineación a la DERECHA (para números int o float, NO con texto) 
#*   {:>x}    =>  Alineación a la DERECHA
#*   {:<x}    =>  Alineación a la IZQUIERDA
#*   {:^x}    =>  Alineación al CENTRO
 
#*   {:0x}    =>  Relleno de x Ceros para int / float
 
#*   {:x.yf}  =>  Alineación DERECHA en x y Recorte de decimales en y

#*   {:0x.yf} =>  Relleno de x Ceros y Recorte de decimales en y

#*   {:,}     =>  Añadir separador de miles
 
#*   {:b}     =>  De decimal a binario
#*   {:x}     =>  De decimal a hexadecimal
 
#*   {:e}     =>  Notación Científica con 'e'
#*   {:.xe}   =>  Notación Científica con 'e' + Recorte de Decimales a x
#*   {:E}     =>  Notación Científica con 'e'
#*   {:.xE}   =>  Notación Científica con 'e' + Recorte de Decimales a x

# ===============================================================================

PI = 3.14159265358979323846


#? 1) Cambiando número de dígitos incluyendo decimales => {:.x}
print('\n1) Cambiando número de dígitos incluyendo decimales => {:.x}')

print( 'Constante PI = {}'.format(PI) )    # Constante PI = 3.141592653589793
print( 'Constante PI = {:.1}'.format(PI) ) # Constante PI = 3e+00
print( 'Constante PI = {:.2}'.format(PI) ) # Constante PI = 3.1
print( 'Constante PI = {:.3}'.format(PI) ) # Constante PI = 3.14
print( 'Constante PI = {:.4}'.format(PI) ) # Constante PI = 3.142
print( 'Constante PI = {:.5}'.format(PI) ) # Constante PI = 3.1416



#? 2) Cambiando número de puntos decimales => {:.xf}
print('\n2) Cambiando número de puntos decimales => {:.xf}')

print( 'Constante PI = {}'.format(PI) )     # Constante PI = 3.141592653589793
print( 'Constante PI = {:.1f}'.format(PI) ) # Constante PI = 3.1
print( 'Constante PI = {:.2f}'.format(PI) ) # Constante PI = 3.14
print( 'Constante PI = {:.3f}'.format(PI) ) # Constante PI = 3.142
print( 'Constante PI = {:.4f}'.format(PI) ) # Constante PI = 3.1416
print( 'Constante PI = {:.5f}'.format(PI) ) # Constante PI = 3.14159



#? 3) Alineación de Números
print('\n3) Alineación de Números')

n1, n2, n3, n4, n5 = 1, 12, 123, 1234, 12345 # 5
d1, d2, d3, d4, d5 = 1.1, 1.12, 1.123, 1.1234, 1.12345 # 7

# => Sin Alineación
print('\n=> Sin Alineación\n')
print( 'Entero = {} | Float = {}'.format(n1 , d1) )
print( 'Entero = {} | Float = {}'.format(n2 , d2) )
print( 'Entero = {} | Float = {}'.format(n3 , d3) )
print( 'Entero = {} | Float = {}'.format(n4 , d4) )
print( 'Entero = {} | Float = {}'.format(n5 , d5) )

# => Alineación DERECHA por defecto {:x}
print('\n=> Alineación DERECHA por defecto {:x}\n')
print( 'Entero = {:5} | Float = {:7}'.format(n1 , d1) )
print( 'Entero = {:5} | Float = {:7}'.format(n2 , d2) )
print( 'Entero = {:5} | Float = {:7}'.format(n3 , d3) )
print( 'Entero = {:5} | Float = {:7}'.format(n4 , d4) )
print( 'Entero = {:5} | Float = {:7}'.format(n5 , d5) )

# => Alineación DERECHA {:>x}
print('\n=> Alineación DERECHA {:>x}\n')
print( 'Entero = {:>5} | Float = {:>7}'.format(n1 , d1) )
print( 'Entero = {:>5} | Float = {:>7}'.format(n2 , d2) )
print( 'Entero = {:>5} | Float = {:>7}'.format(n3 , d3) )
print( 'Entero = {:>5} | Float = {:>7}'.format(n4 , d4) )
print( 'Entero = {:>5} | Float = {:>7}'.format(n5 , d5) )

# => Alineación IZQUIERDA {:<x}
print('\n=> Alineación IZQUIERDA {:<x}\n')
print( 'Entero = {:<5} | Float = {:<7}'.format(n1 , d1) )
print( 'Entero = {:<5} | Float = {:<7}'.format(n2 , d2) )
print( 'Entero = {:<5} | Float = {:<7}'.format(n3 , d3) )
print( 'Entero = {:<5} | Float = {:<7}'.format(n4 , d4) )
print( 'Entero = {:<5} | Float = {:<7}'.format(n5 , d5) )

# => Alineación CENTRO {:^x}
print('\n=> Alineación CENTRO {:^x}\n')
print( 'Entero = {:^5} | Float = {:^7}'.format(n1 , d1) )
print( 'Entero = {:^5} | Float = {:^7}'.format(n2 , d2) )
print( 'Entero = {:^5} | Float = {:^7}'.format(n3 , d3) )
print( 'Entero = {:^5} | Float = {:^7}'.format(n4 , d4) )
print( 'Entero = {:^5} | Float = {:^7}'.format(n5 , d5) )



#? 4) Relleno de CEROS (int/float)
print('\n4) Relleno de CEROS (int/float)')

n1, n2 = 123, 12345
d1, d2 = 123.123, 12.1234

# => sin relleno
print('\n=> sin relleno\n')
print( '{} | {}'.format(n1, d1) )
print( '{} | {}'.format(n2, d2) )

# => relleno de 8 ceros
print('\nrelleno de 8 ceros\n')
print( '{:08} | {:08}'.format(n1, d1) )
print( '{:08} | {:08}'.format(n2, d2) )

# => relleno de 10 ceros
print('\n=> relleno de 10 ceros\n')
print( '{:010} | {:010}'.format(n1, d1) )
print( '{:010} | {:010}'.format(n2, d2) )



#? 5) Alineación Derecha + Recorte de Decimales => {:x.yf}
print('\n5) Alineación Derecha + Recorte de Decimales => {:x.yf}')

num_1 = 1234567.123456
num_2 = 1234.12345

print( '{}'.format(num_1) )
print( '{}'.format(num_2) )

print()

print( '{:10.2f}'.format(num_1) )
print( '{:10.2f}'.format(num_2) )



#? 6) Relleno de x Ceros + Recorte de Decimales en y => {:0x.yf}
print('\n6) Relleno de x Ceros + Recorte de Decimales en y => {:0x.yf}')

num_1 = 1234567.123456
num_2 = 1234.12345

print( '{}'.format(num_1) )
print( '{}'.format(num_2) )

print()

print( '{:015.2f}'.format(num_1) )
print( '{:015.2f}'.format(num_2) )



#? 7) Añadir separador de miles => {:,}
print('\n7) Añadir separador de miles => {:,}')

mil = 1000
diez_mil = mil * 10
cien_mil = mil * 100
millon = mil * 1000

print( '{} | {} | {} | {}'.format(mil, diez_mil, cien_mil, millon) )
print( '{:,} | {:,} | {:,} | {:,}'.format(mil, diez_mil, cien_mil, millon) )



#? 8) Expresar un número decimal en binario => {:b}
print('\n8) Expresar un número decimal en binario => {:b}')

"""
Decimal Binario
   0     0000
   1     0001
   2     0010
   3     0011
   4     0100
   5     0101
   6     0110
   7     0111
   8     1000
   9     1001
"""

"""

EJ: binario del 9

9   |___2
-8      4
1

4  |____2
-4      2
0

2  |____ 2
-2       1
0

# => yendo de abajo hacia arriba
# - empezando con el resultado de la división y tomando los residuos
1001

"""

print('El número {} en binario es igual a = {:b}'.format(1,1))
print('El número {} en binario es igual a = {:b}'.format(2,2))
print('El número {} en binario es igual a = {:b}'.format(3,3))
print('El número {} en binario es igual a = {:b}'.format(4,4))
print('El número {} en binario es igual a = {:b}'.format(5,5))
print('El número {} en binario es igual a = {:b}'.format(6,6))
print('El número {} en binario es igual a = {:b}'.format(7,7))
print('El número {} en binario es igual a = {:b}'.format(8,8))
print('El número {} en binario es igual a = {:b}'.format(9,9))



#? 9) Expresar un número decimal en hexadecimal => {:x}
print('\n9) Expresar un número decimal en hexadecimal => {:x}')


# -----------------------------------------------------
# 9.1) Recordando la función interna hex()
print('\n9.1) Recordando la función interna hex()\n')
# -----------------------------------------------------

#   EJEMPLO DE LA LECCIÓN id / hex
# - en google color picker podemos ver 
#   https://g.co/kgs/7ZLMrw

# *    RGB(20,50,80) = HEX(#143250)

# => vamos a transformar cada valor RGB a hexadecimal
# - para eso usamos la función interna hex()

print( 'El color RGB({}) en hexadecimal es HEX({})'.format(20, hex(20)) )
print( 'El color RGB({}) en hexadecimal es HEX({})'.format(50, hex(50)) ) 
print( 'El color RGB({}) en hexadecimal es HEX({})'.format(80, hex(80)) ) 


# ----------------------------------------------------
# 9.2) Utilizando string.format() con {:x}
print('\n9.2) Utilizando string.format() con {:x}\n')
# ----------------------------------------------------

c1 = 20
c2 = 50
c3 = 80

print( 'El color RGB({}) en hexadecimal es HEX({:x})'.format(c1, c1) )
print( 'El color RGB({}) en hexadecimal es HEX({:x})'.format(c2, c2) ) 
print( 'El color RGB({}) en hexadecimal es HEX({:x})'.format(c3, c3) ) 


#? 10) Mostrar Número en Notación Científica => {:e} / {:E} / {:.xe} / {:.xE}
print('\n10) Mostrar Número en Notación Científica')

num_avogadro = 6.02214076 * 10 ** 23

numero = 1500.123456789

# => por defecto si el número es muy grande, Python utiliza la notación científica
print( 'Número de Avogadro = {}'.format(num_avogadro) )
print( 'Cualquier Número = {}'.format(numero) )

# => forzar notación científica con "e"
print()
print( 'Número de Avogadro = {:e}'.format(num_avogadro) )
print( 'Cualquier Número = {:e}'.format(numero) )

# => forzar notación científica con "E"
print()
print( 'Número de Avogadro = {:E}'.format(num_avogadro) )
print( 'Cualquier Número = {:E}'.format(numero) )

# => notación científica + recorte de decimales
print('\n2 decimales')
print( 'Número de Avogadro = {:.2e}'.format(num_avogadro) )
print( 'Cualquier Número = {:.2e}'.format(numero) )
print( 'Número de Avogadro = {:.2E}'.format(num_avogadro) )
print( 'Cualquier Número = {:.2E}'.format(numero) )


print('\n3 decimales')
print( 'Número de Avogadro = {:.3e}'.format(num_avogadro) )
print( 'Cualquier Número = {:.3e}'.format(numero) )
print( 'Número de Avogadro = {:.3E}'.format(num_avogadro) )
print( 'Cualquier Número = {:.3E}'.format(numero) )

print('\n4 decimales')
print( 'Número de Avogadro = {:.4e}'.format(num_avogadro) )
print( 'Cualquier Número = {:.4e}'.format(numero) )
print( 'Número de Avogadro = {:.4E}'.format(num_avogadro) )
print( 'Cualquier Número = {:.4E}'.format(numero) )