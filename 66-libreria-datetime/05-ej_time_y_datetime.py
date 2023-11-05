# ================================================
# EJERCICIO

# - mostrar la fecha / hora actual con datetime
# - en la consola con un bucle while
# - actualizar cada segundo esta fecha / hora
# - utilizando time.sleep()
# ================================================


#? 1) importación de los módulos / librerías

import time
import datetime



#? 2) definición de la función para mostrar fecha/hora actual

def mostrar_fecha_hora():
    fecha_actual = datetime.datetime.now()
    formato_personalizado = '%B %dth, %Y - %Hh:%Mm:%Ss'
    fecha_personalizada = fecha_actual.strftime(formato_personalizado)
    print( fecha_personalizada )
# end def



#? 3) generación del bucle con sleep de 1 segundo

while True:
    mostrar_fecha_hora()
    time.sleep(1)
# end while