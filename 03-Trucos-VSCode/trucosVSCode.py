'''
=========================================
Shortcuts y Comandos Rápidos en VS Code
=========================================

En esta sección vamos a aprender algunos trucos de VSCode

# SHORTCUTS Y COMANDOS RÁPIDOS
	- IMPORTANTE !!! => no es necesario memorizar esto
	- Los vamos a ir practicando a lo largo del CURSO
	- Entender como funcionan
	- No vamos a ver todos (los que a mi criterio son importantes saber)
	- No frustrarse si al inicio no los usamos con fluidez - todo es cuestión de práctica
	- Usar esto como referencia
'''

# =========================================================================================

#? (1) Memorizar solo este !! - Abrir Ventana de Shortcuts (Atajos)
# - CTRL + K + S ==> sin soltar ninguna tecla
# - Click en Engranaje + Keyboard Shortcuts

#! No confundir con:

# - CTRL + K (suelto teclas) + S ==> guardar todos los archivos activos

# =========================================================================================

#? (2) Copiar / Cortar / Pegar / Deshacer

# - CTRL + C  =>  copiar contenido 
# - CTRL + X  =>  cortar contenido
# - CTRL + V  =>  copiar contenido 
# - CTRL + Z  =>  copiar contenido 

#! WINDOWS
# - WINDOWS + V => pegar del portapapeles

## EJERCICIO de Edición

print('Copiar y Pegar esta línea abajo')

print('Copia y Pega con Windows + V')

print('Corta y Pega en 1era línea')

# ==> Solución:

print('Corta y Pega en 1era línea')
print('Copiar y Pegar esta línea abajo')
print('Copiar y Pegar esta línea abajo')
print('Copiar y Pegar esta línea abajo')
print('Copia y Pega con Windows + V')
print('Copia y Pega con Windows + V')
print('Copia y Pega con Windows + V')


# =========================================================================================

#? (3) Comentario de una línea
# - CTRL + K + / ==> sin soltar CTRL ó K
# - Edit + Toggle Line Comment

# si no funciona por defecto => modificar con CTRL + K + S

## EJERCICIO: Transformar todo esto a comentario con el comando

Este es un comentario 1
Este es un comentario 2
Este es un comentario 3
Este es un comentario 4

# ==> Solución:

# Este es un comentario 1
# Este es un comentario 2
# Este es un comentario 3
# Este es un comentario 4

# =========================================================================================

#? (4) Bloque de Comentarios / Comentario Multilínea
# - SHIFT + ALT + A
# - Edit + Toggle Block Comment


## EJERCICIO: Transformar todo esto a comentario multilínea

Este es un comentario 1
Este es un comentario 2
Este es un comentario 3
Este es un comentario 4

# ==> Solución:

""" Este es un comentario 1
Este es un comentario 2
Este es un comentario 3
Este es un comentario 4 """

# =========================================================================================

#? (5) Desplazamiento Rápido con SHIFT

# - SHIFT + Flechas => Selección de texto
# - HOME            => Puntero a inicio de línea
# - SHIFT + HOME    => Selección hasta inicio de línea
# - END             => Puntero a fin de línea
# - SHIFT + END     => Selección hasta fin de línea

## EJERCICIO: Practicar desplazamiento rápido con SHIFT

print('Este es un texto 1 dentro de la función interna print')
print('Este es un texto 2 dentro de la función interna print')
print('Este es un texto 3 dentro de la función interna print')
print('Este es un texto 4 dentro de la función interna print')

# =========================================================================================

#? (6) Mover una línea de código VERTICALMENTE (arriba / abajo)
# - ALT (presionado) + flecha arriba => mover arriba
# - ALT (presionado) + flecha abajo  => mover abajo

## EJERCICIO: Mover la línea indicada de arriba a abajo

print('texto 1 para imprimir en la consola')
print('texto 2 para imprimir en la consola')
print('texto 3 para imprimir en la consola')
print('***** MOVER ESTA LÍNEA *****')
print('texto 4 para imprimir en la consola')
print('texto 5 para imprimir en la consola')

# =========================================================================================

#? (7) Repetir una línea de código arriba / abajo
# - SHIFT + ALT (sin soltar) + flecha arriba  =>  repetir hacia arriba
# - SHIFT + ALT (sin soltar) + flecha abajo   =>  repetir hacia abajo

## EJERCICIO: Realizar la repetición como se indica

print('Esta línea NO se repite')
print('Esta línea NO se repite')
print('Repetir 2 veces ABAJO')
print('Esta línea NO se repite')
print('Esta línea NO se repite')
print('Repetir 2 veces ARRIBA')
print('Esta línea NO se repite')
print('Esta línea NO se repite')

# ==> Solución:

print('Esta línea NO se repite')
print('Esta línea NO se repite')
print('Repetir 2 veces ABAJO')
print('Repetir 2 veces ABAJO')
print('Repetir 2 veces ABAJO')
print('Esta línea NO se repite')
print('Esta línea NO se repite')
print('Repetir 2 veces ARRIBA')
print('Repetir 2 veces ARRIBA')
print('Repetir 2 veces ARRIBA')
print('Esta línea NO se repite')
print('Esta línea NO se repite')

# =========================================================================================

#? (8) Borrar una línea entera con 2 teclas
# - SHIFT + DEL (tecla delete) => borra una línea entera

## EJERCICIO: Borrar las líneas indicadas con shift + del

print('Línea importante número 1')
print('Línea importante número 2')
print('*** línea a borrar ***')
print('Línea importante número 3')
print('Línea importante número 4')
print('*** línea a borrar ***')
print('Línea importante número 5')
print('Línea importante número 6')
print('*** línea a borrar ***')
print('*** línea a borrar ***')

# ==> Solución

print('Línea importante número 1')
print('Línea importante número 2')
print('Línea importante número 3')
print('Línea importante número 4')
print('Línea importante número 5')
print('Línea importante número 6')

# =========================================================================================

#? (9) Seleccionar contenido RÁPIDAMENTE
# - SHIFT + CTRL + tecla izquierda / derecha
#   => selecciona toda una palabra
#   => o una serie de palabras unidas con guión bajo
#   => cualquier otro caracter (*, -, /) corta la selección

# - SHIFT + ALT + tecla izquierda
#   => selecciona en rango de jerarquía menor a mayor
#   => la primera vez selecciona una palabra
#   => la segunda vez selecciona todo el contenido de la línea (toda una variable por ej.)
#   => una tercera vez puede seleccionar la totalidad del contenido


## EJERCICIO: Practicar la selección rápida (observar los cortes)

'''
Esta es una cadena de texto
nombre_de_variable = valor
nombre-de-variable = valor
nombre*de*variable = valor
nombre/de/variable = valor
nombreDeVariable, nombre_de_variable
'''

print('Este es un texto a seleccionar texto_seleccionar')

# =========================================================================================

#? (10) Multicursor
#! IMPORTANTE

# - CTRL + ALT + flecha arriba / flecha abajo => crea varios cursores para edición
# - ALT (sin soltar) + click izquierdo => crea varios cursores con el mouse

## EJERCICIO:
# - Añadir lo siguiente al final de cada línea
# - Utilizando multicursores (solo con el teclado, NO mouse)
# - Contenido a añadir: 
#   INICIO_LÍNEA => al inicio de cada línea
#   FIN_LÍNEA    => al final de cada línea

print('***línea de texto # 1***')
print('***línea de texto # 2***')
print('***línea de texto # 3***')
print('***línea de texto # 4***')
print('***línea de texto # 5***')

# ==> Solución

print('INICIO_LÍNEA***línea de texto # 1***FIN_LÍNEA')
print('INICIO_LÍNEA***línea de texto # 2***FIN_LÍNEA')
print('INICIO_LÍNEA***línea de texto # 3***FIN_LÍNEA')
print('INICIO_LÍNEA***línea de texto # 4***FIN_LÍNEA')
print('INICIO_LÍNEA***línea de texto # 5***FIN_LÍNEA')

## EJERCICIO:
# - Agregar el siguiente texto en cada una de esas líneas
# - Al final de cada línea
# - Contenido a añadir:
# ---CONTENIDO ADICIONAL---

print('Esta es una primera línea')
print('Aquí va a otra')
print('Una tercera')
print('FIN')

# ==> Solución

print('Esta es una primera línea---CONTENIDO ADICIONAL---')
print('Aquí va a otra---CONTENIDO ADICIONAL---')
print('Una tercera---CONTENIDO ADICIONAL---')
print('FIN---CONTENIDO ADICIONAL---')

# =========================================================================================

#? (11) Abrir la paleta de comandos

# ! IMPORTANTE
# - CTRL + SHIFT + P
# - F1
# - VIEW + Command Palette

# =========================================================================================

#? (12) Ordenar Alfabéticamente con Paleta de Comandos

# - F1 ó (CTRL + SHIFT + P) + Sort Lines Ascending  (A-Z)
# - F1 ó (CTRL + SHIFT + P) + Sort Lines Descending (Z-A)

## Ejercicio
# - Ordenar alfabéticamente las siguientes líneas de código
# - Ordenar de la A-Z y de la Z-A
# - Utilizar la paleta de comandos

print('Perro')
print('Tigre')
print('León')
print('Gato')
print('Ratón')
print('Águila')

# ==> Solución

# (A-Z)
print('Águila')
print('Gato')
print('León')
print('Perro')
print('Ratón')
print('Tigre')

# (Z-A)
print('Tigre')
print('Ratón')
print('Perro')
print('León')
print('Gato')
print('Águila')

# =========================================================================================

#? (13) Transformar a Mayúsculas / Minúsculas / Título con la Paleta de Comandos

# - F1 ó (CTRL + SHIFT + P) + Transform to Uppercase    => MAYÚSCULAS
# - F1 ó (CTRL + SHIFT + P) + Transform to Lowercase    => minúsculas
# - F1 ó (CTRL + SHIFT + P) + Transform to Title Case   => Título

## Ejercicio
# - Transformar el contenido de los siguientes print a
# - MAYÚSCULAS, minúsculas y formato de título
# - Utilizando la paleta de comandos

print('Un PRint Sin orDEN en Sus palABRAS')
print('paRA podER PRACTIcar el CASe tranSFORmatioN')
print('apliCANdo la MAGia de VISual StudIO CODe')

# ==> Solución

# Mayúsculas
print('UN PRINT SIN ORDEN EN SUS PALABRAS')
print('PARA PODER PRACTICAR EL CASE TRANSFORMATION')
print('APLICANDO LA MAGIA DE VISUAL STUDIO CODE')

# Minúsculas
print('un print sin orden en sus palabras')
print('para poder practicar el case transformation')
print('aplicando la magia de visual studio code')

# Formato de Título
print('Un Print Sin Orden En Sus Palabras')
print('Para Poder Practicar El Case Transformation')
print('Aplicando La Magia De Visual Studio Code')

# =========================================================================================

#? (14) Seleccionar todas las ocurrencias
# - CTRL + F2

## EJERCICIO
# - Seleccionar TODAS las ocurrencias en el documento
# - que contengan:
#   estaEsUnaPalabraQueSoloExisteAqui
# - y cambiarla por PALABRA

print('estaEsUnaPalabraQueSoloExisteAqui Texto1 Print1')
print('estaEsUnaPalabraQueSoloExisteAqui Texto2 Print2')
print('estaEsUnaPalabraQueSoloExisteAqui Texto3 Print3')
print('estaEsUnaPalabraQueSoloExisteAqui Texto4 Print4')
print('estaEsUnaPalabraQueSoloExisteAqui Texto5 Print5')

# =========================================================================================

#? (15) Seleccionar ocurrencia SIGUIENTE
# - CTRL + D

## EJERCICIO
# - Seleccionar PalabraEspecial a partir del 2do print
# - y cambiarlo por PythonEspecial

print('No se me ocurre una PalabraEspecial')
print('Necesito una PalabraEspecial para este ejercicio')
print('¿Me podrías sugerir una PalabraEspecial para este ejercicio?')
print('¿Qué PalabraEspecial se te viene en mente ahora?')
print('PalabraEspecial es una palabra extraña')

# ==> Solución

print('No se me ocurre una PalabraEspecial')
print('Necesito una PythonEspecial para este ejercicio')
print('¿Me podrías sugerir una PythonEspecial para este ejercicio?')
print('¿Qué PythonEspecial se te viene en mente ahora?')
print('PythonEspecial es una palabra extraña')