# =======================================================================================
# Reasignar Valor de Variable en Python

# - Python nos permite esto
# - Otro lenguaje que lo permite es Javascript
# - Quería recalcar esto porque en otros lenguajes esto no es posible
# - en otros lenguajes cuando se DECLARA una variable como int por ejemplo
# - luego no es posible reasignarle un valor string por ejemplo
# - Python / JavaScript no trabajan de manera IMPRESCINDIBLE con el tipado
# - Esto es bueno y malo a la vez
# - El tipado de datos nos da mayor seguridad a nuestro código
# - Por eso existen extensiones / bibliotecas externas que permiten incorporar tipado
# - EJ: TypeScript / PyScript
# =======================================================================================

#? Fases de una variable

# 1) Creación = Declaración + Asignación
variable = 'hola mundo'

# variable        => declaración / nombramos / ponemos nombre a la variable
# = 'hola mundo'  => asignación de valor a la variable declarada

print(variable, type(variable))

# 2) Reasignación de valor a variable con el mismo tipo
variable = 'otro string'
print(variable, type(variable))

# 3) Reasignación de valor con otro tipo de dato
variable = 123
print(variable, type(variable))

variable = False
print(variable, type(variable))

variable = None
print(variable, type(variable))

variable = 'hola mundo'
print(variable, type(variable))

