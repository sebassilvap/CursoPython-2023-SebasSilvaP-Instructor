# ==========================================================================
# Formato de texto con string.format()

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

# ==========================================================================


#? 1) Alineación / Padding a la izquierda => {:x} ó {:<x}
print('\n1) Alineación / Padding a la izquierda => {:<x}')

pais = 'Ecuador'

print('\nUsando {:<x}\n')
print('Mi país se llama {}. Es un país muy hermoso!'.format(pais))
print('Mi país se llama {:<5}. Es un país muy hermoso!'.format(pais))
print('Mi país se llama {:<10}. Es un país muy hermoso!'.format(pais))
print('Mi país se llama {:<20}. Es un país muy hermoso!'.format(pais))
print('Mi país se llama {:<30}. Es un país muy hermoso!'.format(pais))


# => CONSOLA:
# Mi país se llama Ecuador. Es un país muy hermoso!
# Mi país se llama Ecuador. Es un país muy hermoso!
# Mi país se llama Ecuador   . Es un país muy hermoso!
# Mi país se llama Ecuador             . Es un país muy hermoso!
# Mi país se llama Ecuador                       . Es un país muy hermoso!



#? 2) Alineación / Padding a la derecha => {:>x}
print('\n2) Alineación / Padding a la derecha => {:>x}')

pais = 'Ecuador'

print('Mi país se llama {}. Es un país muy hermoso!'.format(pais))
print('Mi país se llama {:>5}. Es un país muy hermoso!'.format(pais))
print('Mi país se llama {:>10}. Es un país muy hermoso!'.format(pais))
print('Mi país se llama {:>20}. Es un país muy hermoso!'.format(pais))
print('Mi país se llama {:>30}. Es un país muy hermoso!'.format(pais))

# => CONSOLA:
# Mi país se llama Ecuador. Es un país muy hermoso!
# Mi país se llama Ecuador. Es un país muy hermoso!
# Mi país se llama    Ecuador. Es un país muy hermoso!
# Mi país se llama              Ecuador. Es un país muy hermoso!
# Mi país se llama                        Ecuador. Es un país muy hermoso!



#? 3) Alineación / Padding al centro => {:^x}
print('\n3) Alineación / Padding al centro => {:^x}')

pais = 'Ecuador'

print('Mi país se llama {}. Es un país muy hermoso!'.format(pais))
print('Mi país se llama {:^5}. Es un país muy hermoso!'.format(pais))
print('Mi país se llama {:^10}. Es un país muy hermoso!'.format(pais))
print('Mi país se llama {:^20}. Es un país muy hermoso!'.format(pais))
print('Mi país se llama {:^30}. Es un país muy hermoso!'.format(pais))

# => CONSOLA:
# Mi país se llama Ecuador. Es un país muy hermoso!
# Mi país se llama Ecuador. Es un país muy hermoso!
# Mi país se llama  Ecuador  . Es un país muy hermoso!
# Mi país se llama       Ecuador       . Es un país muy hermoso!
# Mi país se llama            Ecuador            . Es un país muy hermoso!



#? 4) {:x} => IZQUIERDA para texto / DERECHA para números
print('\n4) {:x} => IZQUIERDA para texto / DERECHA para números')
# ! OJO:
# - el tema completo de alineación para números
# - lo vamos a ver en la siguiente lección
# - por el momento se presenta este tema
# - para evitar la confusión del uso de este format
# - entre números y cadenas de texto

# ------------------------------------
# => IZQUIERDA para texto
print('\n=> IZQUIERDA para texto\n')
# ------------------------------------

p = 'sol'

print('El {:5} es nuestra estrella!'.format(p))
print('El {:<5} es nuestra estrella!'.format(p))


# --------------------------------------
# => DERECHA para números int
print('\n# => DERECHA para números int\n')
# --------------------------------------

n1 = 1
n2 = 12
n3 = 123

print('El valor del número = {}'.format(n1))
print('El valor del número = {}'.format(n2))
print('El valor del número = {}'.format(n3))

print()

print('El valor del número = {:3}'.format(n1))
print('El valor del número = {:3}'.format(n2))
print('El valor del número = {:3}'.format(n3))

print()

print('El valor del número = {:>3}'.format(n1))
print('El valor del número = {:>3}'.format(n2))
print('El valor del número = {:>3}'.format(n3))


# ---------------------------------------
# => DERECHA también con float
print('\n=> DERECHA también con float\n')
# ---------------------------------------

d1 = 1.2
d2 = 1.23
d3 = 1.234
d4 = 1.2345


print('El valor del número decimal = {}'.format(d1))
print('El valor del número decimal = {}'.format(d2))
print('El valor del número decimal = {}'.format(d3))
print('El valor del número decimal = {}'.format(d4))

print()

print('El valor del número decimal = {:6}'.format(d1))
print('El valor del número decimal = {:6}'.format(d2))
print('El valor del número decimal = {:6}'.format(d3))
print('El valor del número decimal = {:6}'.format(d4))

print()

print('El valor del número decimal = {:>6}'.format(d1))
print('El valor del número decimal = {:>6}'.format(d2))
print('El valor del número decimal = {:>6}'.format(d3))
print('El valor del número decimal = {:>6}'.format(d4))



#? 5) Truncamiento => {:.x}
print('\n5) Truncamiento => {:.x}')

p = 'contextualización'

print( 'La palabra {} es muy grande'.format(p) )
print( 'La palabra {:.8} es muy grande'.format(p) )
print( 'La palabra {:.6} es muy grande'.format(p) )
print( 'La palabra {:.4} es muy grande'.format(p) )
print( 'La palabra {:.1} es muy grande'.format(p) )

# => CONSOLA:
# La palabra contextualización es muy grande
# La palabra contextu es muy grande
# La palabra contex es muy grande
# La palabra cont es muy grande
# La palabra c es muy grande



#? 6) Alineación + Truncamiento => {:<x.y} | {:>x.y} | {:^x.y}
print('\n6) Alineación + Truncamiento => {:<x.y} | {:>x.y} | {:^x.y}')

p = 'contextualización'

print( 'La palabra {} es muy grande'.format(p) )
print( 'La palabra {:<15.5} es muy grande'.format(p) )
print( 'La palabra {:>15.5} es muy grande'.format(p) )
print( 'La palabra {:^15.5} es muy grande'.format(p) )

# => CONSOLA:
# La palabra contextualización es muy grande
# La palabra conte           es muy grande
# La palabra           conte es muy grande
# La palabra      conte      es muy grande



#? 7) Alineación + Truncamiento con Argumentos Posicionales
print('\n7) Alineación + Truncamiento con Argumentos Posicionales')

n1 = 'Andy'
n2 = 'Xime'

print('{1} viene de Quito y {0} de Cuenca'.format(n1, n2))
print('{0} viene de Quito y {1} de Cuenca'.format(n1, n2))
print('{1} viene de Quito y {1} de Cuenca'.format(n1, n2))

# => aplicando Alineación + Truncamiento
print('{1:>10} viene de Quito y {0:^20} de Cuenca'.format(n1, n2))
print('{1:>10.3} viene de Quito y {0:^20.3} de Cuenca'.format(n1, n2))

# => CONSOLA:
# Xime viene de Quito y Andy de Cuenca
# Andy viene de Quito y Xime de Cuenca
# Xime viene de Quito y Xime de Cuenca
#       Xime viene de Quito y         Andy         de Cuenca
#        Xim viene de Quito y         And          de Cuenca



#? 8) Alineación + Truncamiento con Argumentos de Keyword
print('\n8) Alineación + Truncamiento con Argumentos de Keyword')

print( 'Me gusta el {b} con {a}'.format(a='pan', b='jugo') )
print( 'Me gusta el {a} con {b}'.format(a='pan', b='jugo') )
print( 'Me gusta el {a} con {a}'.format(a='pan', b='jugo') )
print( 'Me gusta el {a} con {a}'.format(a='pan', b='jugo') )

# => aplicando Alineación + Truncamiento
print( 'Me gusta el {b:<10} con {a:>15}'.format(a='pan', b='jugo') )
print( 'Me gusta el {b:<10.2} con {a:>15.2}'.format(a='pan', b='jugo') )

# => CONSOLA:
# Me gusta el jugo con pan
# Me gusta el pan con jugo
# Me gusta el pan con pan
# Me gusta el pan con pan
# Me gusta el jugo       con             pan
# Me gusta el ju         con              pa