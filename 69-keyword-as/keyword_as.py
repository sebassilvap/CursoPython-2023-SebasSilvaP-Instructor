# ========================================
# Palabra Clave - as

# - as => para crear un alias
# - al momento que hacemos importaciones
# ========================================


#? 1) SIN utilizar alias - as
print('\n1) SIN utilizar alias - as')

"""
import math
import datetime

CONST_PI = math.pi
fecha_actual = datetime.datetime.now()

print( CONST_PI ) # 3.141592653589793
print( fecha_actual ) # 2023-11-10 23:50:55.178115
"""


#? 2) Utilizando alias - as

import math as m
import datetime as dt

CONST_PI = m.pi
fecha_actual = dt.datetime.now()

print( CONST_PI ) # 3.141592653589793
print( fecha_actual ) # 2023-11-10 23:52:59.998398