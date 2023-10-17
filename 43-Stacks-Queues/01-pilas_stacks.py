# ===============================================
# Pilas / Stacks / LIFO

# - Concepto de Colección de datos
# - Viene del inglés => Stack
# - También se lo conoce como estructura LIFO
# - LIFO = Last In / First Out
# - Permiten 2 acciones:
#       => Añadir un elemento / Push / Apilar
#       => Sacar un elemento / Pop / Desapilar

# - En Python poodemos simular esto con listas
# ===============================================

pila = [100, 500, 800]

print( pila, type(pila), len(pila) )

# Añadir elemento a la pila => .append()
pila.append(900)

print( pila, type(pila), len(pila) )

# Sacar elemento de pila => .pop()
# - el último
pila.pop()

print( pila, type(pila), len(pila) )

# ----------------------------------------------------
# Básicamente
# - cuando un elemento entra => entra al último
# - cuando un elemento sale  => sale desde el último
# ----------------------------------------------------