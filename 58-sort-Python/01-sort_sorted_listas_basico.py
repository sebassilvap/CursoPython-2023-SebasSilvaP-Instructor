# ==========================================================================
# sort / map / filter / reduce
# => sort en Python

# ! PARTE 1: RECORDATORIO básico de .sort() y sorted() en LISTAS

# - son funciones MUY, MUY importantes
# - al momento de trabajar con colecciones de datos
# - nos permiten masajear los datos 
# - no solo son importantes en Python, sino en algunos lenguajes
# - por ejemplo en la programación WEB, en javascript, son muy conocidas
# - para trabajar y presentar datos de manera personalizada

# * SORT
# => Clasificar datos
# - por ejemplo:
# - ordenar de mayor a menor / menor a mayor
# - ordenar alfabéticamente (A-Z) / (Z-A)
# - ordenar en base a algún criterio especial (ej: tamaño de palabra)

# => Existen 2 maneras de hacer "sort" en Python:

# ?   A) método .sort()   => sólo funciona en listas
# ?   B) función sorted() => para cualquier colección de datos
# ==========================================================================


#? 1) .sort() en listas
print('\n1) .sort() en listas')
# - recordar que al final .sort() y sorted()
# - hacen lo mismo en listas
# - la diferencia es que .sort() afecta la variable original
# - sorted() me devuelve una lista nueva ordenada

palabras = ['sol', 'planeta', 'hola', 'investigación']
numeros = [80, 50, 70, 10, 20, 60]

# -------------------------------------------------
# 1.1) Ordenar (A-Z) elementos de texto
print('\n1.1) Ordenar (A-Z) elementos de texto\n')
# -------------------------------------------------

palabras.sort()
print(palabras)

# => o también usando reverse=False (por defecto es False)
print()
palabras.sort(reverse=False)
print(palabras)


# ------------------------------------------------------------------
# 1.2) Ordenar (Z-A) elementos de texto => reverse=True
print('\n1.2) Ordenar (Z-A) elementos de texto => reverse=True\n')
# ------------------------------------------------------------------

palabras.sort(reverse=True)
print(palabras)


# --------------------------------------------------
# 1.3) Ordenar Números de Menor a Mayor
print('\n1.3) Ordenar Números de Menor a Mayor\n')
# --------------------------------------------------

numeros.sort()
print(numeros)

# => o también usando reverse=False (por defecto es False)
print()
numeros.sort(reverse=False)
print(numeros)


# --------------------------------------------------------
# 1.4) Ordenar Números de Mayor a Menor => reverse=True
print('\n1.4) Ordenar Números de Mayor a Menor => reverse=True\n')
# --------------------------------------------------

numeros.sort(reverse=True)
print(numeros)


# -------------------------------------------------------------------------
# 1.5) Orden especial: EJ => en función al tamaño de la palabra
print('\n1.5) Orden especial: EJ => en función al tamaño de la palabra\n')
# -------------------------------------------------------------------------
# - usamos 2 parámetros de .sort() => key & reverse


#= > por defecto: palabra más pequeña a más grande
# - reverse por defecto False
# - podemos no ponerlo si así queremos
palabras.sort(key=len)
print(palabras)

print()

palabras.sort(key=len, reverse=False)
print(palabras)


# => reverse=True: palabra más grande a más pequeña
print()

palabras.sort(key=len, reverse=True)
print(palabras)



#? 2) función interna sorted()
print('\n2) función interna sorted()')
# * función interna de python (built-in function)
# - hace exactamente lo mismo que .sort() en listas
# - pero sirve para cualquier colección de datos, no solo listas
# - no modifica la variable original
# - retorna una copia con el orden establecido
# - https://www.w3schools.com/python/ref_func_sorted.asp


palabras = ['sol', 'planeta', 'hola', 'investigación']
numeros = [80, 50, 70, 10, 20, 60]

print('original palabras =', palabras)
print('original numeros =', numeros)


# -------------------------------------------------
# 2.1) Ordenar (A-Z) elementos de texto
print('\n2.1) Ordenar (A-Z) elementos de texto\n')
# -------------------------------------------------

#! palabras.sort()
palabras_sorted = sorted(palabras)
print(palabras)
print(palabras_sorted)

# => o también usando reverse=False (por defecto es False)
print()

#! palabras.sort(reverse=False)
palabras_sorted = sorted(palabras, reverse=False)
print(palabras_sorted)


# ------------------------------------------------------------------
# 2.2) Ordenar (Z-A) elementos de texto => reverse=True
print('\n2.2) Ordenar (Z-A) elementos de texto => reverse=True\n')
# ------------------------------------------------------------------

#! palabras.sort(reverse=True)
palabras_sorted = sorted(palabras, reverse=True)
print(palabras_sorted)


# --------------------------------------------------
# 2.3) Ordenar Números de Menor a Mayor
print('\n2.3) Ordenar Números de Menor a Mayor\n')
# --------------------------------------------------

#! numeros.sort()
numeros_sorted = sorted(numeros)
print(numeros_sorted)

# => o también usando reverse=False (por defecto es False)
print()

#! numeros.sort(reverse=False)
numeros_sorted = sorted(numeros, reverse=False)
print(numeros_sorted)


# --------------------------------------------------------
# 2.4) Ordenar Números de Mayor a Menor => reverse=True
print('\n2.4) Ordenar Números de Mayor a Menor => reverse=True\n')
# --------------------------------------------------

#! numeros.sort(reverse=True)
numeros_sorted = sorted(numeros, reverse=True)
print(numeros_sorted)


# -------------------------------------------------------------------------
# 2.5) Orden especial: EJ => en función al tamaño de la palabra
print('\n2.5) Orden especial: EJ => en función al tamaño de la palabra\n')
# -------------------------------------------------------------------------
# - usamos 2 parámetros de .sort() => key & reverse


#= > por defecto: palabra más pequeña a más grande
# - reverse por defecto False
# - podemos no ponerlo si así queremos

#! palabras.sort(key=len)
palabras_sorted = sorted(palabras, key=len)
print(palabras_sorted)

print()

#! palabras.sort(key=len, reverse=False)
palabras_sorted = sorted(palabras, key=len, reverse=False)
print(palabras_sorted)


# => reverse=True: palabra más grande a más pequeña

print()

#! palabras.sort(key=len, reverse=True)
palabras_sorted = sorted(palabras, key=len, reverse=True)
print(palabras_sorted)

# => después de todo lo que hice con sorted()
# - como vemos la variable original sigue intacta
print()
print('original palabras =', palabras)
print('original numeros =', numeros)