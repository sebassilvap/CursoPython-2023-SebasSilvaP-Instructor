# ===================================
# importación dentro del mismo path
# ===================================
import modulo_hola
import folder2.despedidas
import folder1.folder1_1.saludos
import folder1.folder1_1.mensajes as msg




# ============================
# importación desde otro path
# ============================
import sys
# - para insertar la ubicación del path
# - en la ubicación de nuestro sistema
# - dentro de este script

sys.path.append('c:\\Users\\Admin\\Desktop\\CLUB CODING GAMING 2023-2024\\03-Instructor\\71-modulos\\01-intro-tipos-import')
sys.path.append('C:\\Users\\Admin\\Desktop\\CLUB CODING GAMING 2023-2024\\03-Instructor\\71-modulos\\02-import-diferentes-path\\folder1\\folder 1 2')

print(sys.path) # para ver los path del sistema, al último veremos el añadido!

import aritmetica
import capitales




# =======
# test
# =======

print('--------------------------------------------------')

modulo_hola.hola_mundo()
folder2.despedidas.despedida_aleman()
folder1.folder1_1.saludos.saludo_ingles()
msg.primer_mensaje() # mucho mejor usar un alias!

print('--------------------------------------------------')

capitales.capital_ecuador()
aritmetica.suma(5,2)



# ========================================================================================
# ! POCO RECOMENDABLE HACER ESTO
# - como buena práctica es mejor tener en el path principal nuestro archivo principal
# - y a partir de aquí, carpetas y subcarpetas donde tengamos el resto de nuestros módulos

# * RECOMENDACIÓN
# - al trabajar con python y módulos
# - para evitar estos problemas
# - tratar SIEMPRE que las carpetas y los archivos de python
# - mantegan una estructura en sus nombres, sin espacios
# - y de ser posible con "_" => guión bajo
# ========================================================================================
