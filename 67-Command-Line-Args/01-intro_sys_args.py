# ==============================================================
# sys.argv

# - nos permite mandar argumentos desde el Command Window
# - CMD => Command Prompt
# - se necesita el módulo interno "sys"
# ==============================================================


# => importación del módulo sys

import sys

print('-----------------------')
print( sys.argv )
print( type(sys.argv) )
print('-----------------------')

# Respuesta:
# ['c:\\Users\\Admin\\Desktop\\CLUB CODING GAMING 2023-2024\\03-Instructor\\70-Command-Line-Args\\01-intro_sys_args.py']



# ===================================================================
# - nos devuelve una lista
# - donde el primer elemento es el path del archivo
# - de este archivo que lo ejecutamos
# - los siguientes elementos son argumentos que pasemos con el CMD
# ===================================================================



# =====================================================================================================
# EJEMPLO
# - ir al CMD
# - ir al directorio donde se encuentra este Script
# - en mi caso es el siguiente:

#*   cd "C:\Users\Admin\Desktop\CLUB CODING GAMING 2023-2024\03-Instructor\70-Command-Line-Args"

# - una vez dentro del path en el CMD
# - ejecutar el archivo de python y adicionalmente
# - enviar 3 datos numéricos, por ejemplo: 10, 20, 30

#*   C:\Users\Admin\Desktop\CLUB CODING GAMING 2023-2024\03-Instructor\70-Command-Line-Args>python 01-intro_sys_args.py 10 20 30
#!   python 01-intro_sys_args.py 10 20 30

# - El resultado va a ser el siguiente:

"""
-----------------------
['01-intro_sys_args.py', '10', '20', '30']
<class 'list'>
-----------------------
"""

# - 10, 20, 30 => son los argumentos pasados con el CMD
# - a partir del elemento 1 de la lista veremos estos argumentos
# - el elemento de posición 0 => el path del archivo

#* NOTA AUXILIAR:
# - ver la imagen de referencia con el mismo nombre del script
# - para ver como se utiliza el CMD
# =====================================================================================================
