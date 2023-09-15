# ==================================================
# Función slice()

# - podemos crear un objeto de tipo slice
# - luego podemos hacer uso de este objeto

#* RECORDEMOS el string slice
#  variable_string[START : END : STEP]

# - con la misma lógica se puede utilizar slice()
#* slice(START , END , STEP)

# RECORDAR:
# - START => es inclusivo
# - END   => es exclusivo

# => en este caso separamos con una coma ','
# ==================================================

#? 1) Uso básico sin step
#(+)         0123456789012
#(-)                             4321
website_1 = 'https://www.facebook.com'
website_2 = 'https://www.google.com'
website_3 = 'https://www.twitter.com'

patron_corte = slice(12,-4) #! objeto que se puede usar
#! objeto => ya veremos más adelante qué es

web_1 = website_1[patron_corte]
web_2 = website_2[patron_corte]
web_3 = website_3[patron_corte]

print('website :')
print(website_1)
print(website_2)
print(website_3)

print('web :')
print(web_1)
print(web_2)
print(web_3)

#? 2) Utilizando también step
patron_corte_step_2 = slice(12,-4,2)

web_1_reducida = website_1[patron_corte_step_2]
web_2_reducida = website_2[patron_corte_step_2]
web_3_reducida = website_3[patron_corte_step_2]

print('Nombre de página con step 2 :')
print( web_1 , '||' , web_1_reducida )
print( web_2 , '||' , web_2_reducida )
print( web_3 , '||' , web_3_reducida )

