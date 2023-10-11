# =============================================================
# Colas / Queues / FIFO

# - Concepto de Colección de datos
# - Viene del inglés => Queue
# - También se lo conoce como estructura FIFO
# - FIFO = First In / First Out

# - En Python poodemos simular esto con la librería collections
# - importando "deque"

# - EJ: en el banco
# - el primero que llega
# - es el primero que se le atiende
# =============================================================

# importación
from collections import deque


# crear una cola vacía
cola = deque()
print( cola, type(cola), len(cola) )


# crear cola con datos
cola = deque([ 'Bob Esponja', 'Calamardo', 'Patricio' ])
print( cola, type(cola), len(cola) )


# .append() => entran datos al final
cola.append('Arenita')
print( cola, type(cola), len(cola) )


# .popleft() => sacar datos desde el inicio
cola.popleft()
print( cola, type(cola), len(cola) )