#azul = 1 , rojo = 2 , verde = 3, amarillo = 4, violeta = 5, gris = 6, marron= 7, negro = 8


# gris = 6, marron= 7,

print("La tabla de colores se clasifica de la siguiente manera:\n1 - Azul\n2 - Rojo\n3 - Verde\n4 - Amarillo\n5 - Violeta\n6 - Gris\n7 - Marron\n8 - Negro\n")
print("ORDERNAR LOS COLORES SEGÚN LA PREFERENCIAS\n")

color1  =   int(input("Ingresa el primer color de tu agrado: "))
color2  =   int(input("Ingresa el segundo color de tu agrado: "))
color3  =   int(input("Ingresa el tercer color de tu agrado: "))
color4  =   int(input("Ingresa el cuarto color de tu agrado: "))
color5  =   int(input("Ingresa el quinto color de tu agrado: "))
color6  =   int(input("Ingresa el sexto color de tu agrado: "))
color7  =   int(input("Ingresa el septimo color de tu agrado: "))
color8  =   int(input("Ingresa el octavo color de tu agrado: "))

listaColores    =  {
    1   :  "El azul simboliza la armonia y la satisfacción",
    2   :  "El rojo simboliza la actividad, el dinamismo y la pasión",
    3   :  "El verde simboliza la capacidad de imponerse y la perseverancia",
    4   :  "El amarillo simboliza el optimizmo y el afán de progreso",
    5   :  "El violeta simboliza la vanidad y el egocentrismo",
    6   :  "El gris simboliza la neutralidad.",
    7   :  "El marron simboliza las necesidades físicas, La sensualidad y la comodidad.",
    8   :  "El negro simboliza la negación y la agresión.",
}

listaAspiraciones   =   {
    1   :  "simbolizan las aspiraciones del sujeto",
    2   :  "simbolizan las aspiraciones del sujeto",
    3   :  "Simbolizan la situación actual del sujeto",
    4   :  "Simbolizan la situación actual del sujeto",
    5   :  "Simbolizan las inclinaciones latenetes, momentáneamente reprimidas.",
    6   :  "Simbolizan las inclinaciones latenetes, momentáneamente reprimidas.",
    7   :  "Simbolizan los sentimientos que el sujeto rechaza completamente",
    8   :  "Simbolizan los sentimientos que el sujeto rechaza completamente"
}

azul    =   {
    1   : "Deseo de armonia.",
    2   : "Deseo de armonia.",
    3   : "Simboliza un estádo de armonia ya alcanzado.",
    4   : "Simboliza un estádo de armonia ya alcanzado.",
    5   : "Significa que el sujeto no ve que su deseo de armonía pueda realizarse actualmente.",
    6   : "Significa que el sujeto no ve que su deseo de armonía pueda realizarse actualmente.",
    7   : "Significa que el deseo de armonia es reprimido",
    8   : "Significa que el deseo de armonia es reprimido",
}

rojo    =   {
    1   :  "Significa el deseo de actividad",
    2   :  "Significa el deseo de actividad",
    3   :  "Actividad efectiva",
    4   :  "Actividad efectiva",
    5   :  "Actividad frenada",
    6   :  "Actividad frenada",
    7   :  "Rechazo de toda actividad",
    8   :  "Rechazo de toda actividad",
}

verde   =   {
    1   :  "El deseo de autoafirmación",
    2   :  "El deseo de autoafirmación",
    3   :  "Autoafirmación lograda",
    4   :  "Autoafirmación lograda",
    5   :  "La necesidad de adaptarse",
    6   :  "La necesidad de adaptarse",
    7   :  "Significa la dependencia",
    8   :  "Significa la dependencia",
}

amarillo    =   {
    1   :  "Optimista",
    2   :  "Optimista",
    3   :  "Optimista",
    4   :  "Optimista",
    5   :  "Miedo a las decepciones",
    6   :  "Miedo a las decepciones",
    7   :  "Miedo a las decepciones",
    8   :  "Miedo a las decepciones",
}

violeta     =   {
    1   :   "Vanidad",
    2   :   "Vanidad",
    3   :   "Sensibilidad",
    4   :   "Sensibilidad",
    5   :   "Empática",
    6   :   "Empática",
    7   :   "Escaza capacidad empática",
    8   :   "Escaza capacidad empática",
}


gris = {
    1   :   "El deseo de poner barreras",
    2   :   "El deseo de poner barreras",
    3   :   "El deseo de poner barreras",
    4   :   "El deseo de poner barreras",
    5   :   "Disposición al contacto",
    6   :   "Disposición al contacto",
    7   :   "Disposición al contacto",
    8   :   "Disposición al contacto",
}

marron = {
    1   :   "El deseo de la satisfacción de los deseos corporales",
    2   :   "El deseo de la satisfacción de los deseos corporales",
    3   :   "El deseo de la satisfacción de los deseos corporales",
    4   :   "El deseo de la satisfacción de los deseos corporales",
    5   :   "El rechazo de las necesidades corporales",
    6   :   "El rechazo de las necesidades corporales",
    7   :   "El rechazo de las necesidades corporales",
    8   :   "El rechazo de las necesidades corporales",
}

negro = {
    1   :   "Busca la agresión",
    2   :   "Busca la agresión",
    3   :   "Ha ejercido agresión",
    4   :   "Ha ejercido agresión",
    5   :   "La agresión está reprimida",
    6   :   "La agresión está reprimida",
    7   :   "El sujeto rechaza la agresividad",
    8   :   "El sujeto rechaza la agresividad",
}


#azul = 1 , rojo = 2 , verde = 3, amarillo = 4, violeta = 5, gris = 6, marron= 7, negro = 8

#PARA EL COLOR1
if      color1  ==  1   :
    print(f"\n\nColor 1\n{listaColores[1]}\n{listaAspiraciones[1]}\n{azul[1]}\n")
elif    color1  ==  2 :
    print(f"\nColor 1\n{listaColores[2]}\n{listaAspiraciones[1]}\n{rojo[1]}\n")
elif    color1  ==  3   :
    print(f"\nColor 1\n{listaColores[3]}\n{listaAspiraciones[1]}\n{verde[1]}\n")
elif    color1  ==  4   :
    print(f"\nColor 1\n{listaColores[4]}\n{listaAspiraciones[1]}\n{amarillo[1]}\n")
elif    color1  ==  5   :
    print(f"\nColor 1\n{listaColores[5]}\n{listaAspiraciones[1]}\n{violeta[1]}\n")
elif    color1  ==  6   :
    print(f"\nColor 1\n{listaColores[6]}\n{listaAspiraciones[1]}\n{gris[1]}\n")
elif    color1  ==  7   :
    print(f"\nColor 1\n{listaColores[7]}\n{listaAspiraciones[1]}\n{marron[1]}\n")
elif    color1  ==  8   :
    print(f"\nColor 1\n{listaColores[8]}\n{listaAspiraciones[1]}\n{marron[1]}\n")
else:
    print("Número inválido")


#PARA EL COLOR2
if      color2  ==  1   :
    print(f"Color 2\n{listaColores[1]}\n{listaAspiraciones[2]}\n{azul[2]}\n")
elif    color2  ==  2 :
    print(f"Color 2\n{listaColores[2]}\n{listaAspiraciones[2]}\n{rojo[2]}\n")
elif    color2  ==  3   :
    print(f"Color 2\n{listaColores[3]}\n{listaAspiraciones[2]}\n{verde[2]}\n")
elif    color2  ==  4   :
    print(f"Color 2\n{listaColores[4]}\n{listaAspiraciones[2]}\n{amarillo[2]}\n")
elif    color2  ==  5   :
    print(f"Color 2\n{listaColores[5]}\n{listaAspiraciones[2]}\n{violeta[2]}\n")
elif    color2  ==  6   :
    print(f"Color 2\n{listaColores[6]}\n{listaAspiraciones[2]}\n{gris[2]}\n")
elif    color2  ==  7   :
    print(f"Color 2\n{listaColores[7]}\n{listaAspiraciones[2]}\n{marron[2]}\n")
elif    color2  ==  8   :
    print(f"Color 2\n{listaColores[8]}\n{listaAspiraciones[2]}\n{marron[2]}\n")
else:
    print("Número inválido")

#PARA EL COLOR3
if      color3  ==  1   :
    print(f"Color 3\n{listaColores[1]}\n{listaAspiraciones[3]}\n{azul[3]}\n")
elif    color3  ==  2 :
    print(f"Color 3\n{listaColores[2]}\n{listaAspiraciones[3]}\n{rojo[3]}\n")
elif    color3  ==  3   :
    print(f"Color 3\n{listaColores[3]}\n{listaAspiraciones[3]}\n{verde[3]}\n")
elif    color3  ==  4   :
    print(f"Color 3\n{listaColores[4]}\n{listaAspiraciones[3]}\n{amarillo[3]}\n")
elif    color3  ==  5   :
    print(f"Color 3\n{listaColores[5]}\n{listaAspiraciones[3]}\n{violeta[3]}\n")
elif    color3  ==  6   :
    print(f"Color 3\n{listaColores[6]}\n{listaAspiraciones[3]}\n{gris[3]}\n")
elif    color3  ==  7   :
    print(f"Color 3\n{listaColores[7]}\n{listaAspiraciones[3]}\n{marron[3]}\n")
elif    color3  ==  8   :
    print(f"Color 3\n{listaColores[8]}\n{listaAspiraciones[3]}\n{marron[3]}\n")
else:
    print("Número inválido")


#PARA EL COLOR4
if      color4  ==  1   :
    print(f"Color 4\n{listaColores[1]}\n{listaAspiraciones[4]}\n{azul[4]}\n")
elif    color4  ==  2 :
    print(f"Color 4\n{listaColores[2]}\n{listaAspiraciones[4]}\n{rojo[4]}\n")
elif    color4  ==  3   :
    print(f"Color 4\n{listaColores[3]}\n{listaAspiraciones[4]}\n{verde[4]}\n")
elif    color4  ==  4   :
    print(f"Color 4\n{listaColores[4]}\n{listaAspiraciones[4]}\n{amarillo[4]}\n")
elif    color4  ==  5   :
    print(f"Color 4\n{listaColores[5]}\n{listaAspiraciones[4]}\n{violeta[4]}\n")
elif    color4  ==  6   :
    print(f"Color 4\n{listaColores[6]}\n{listaAspiraciones[4]}\n{gris[4]}\n")
elif    color4  ==  7   :
    print(f"Color 4\n{listaColores[7]}\n{listaAspiraciones[4]}\n{marron[4]}\n")
elif    color4  ==  8   :
    print(f"Color 4\n{listaColores[8]}\n{listaAspiraciones[4]}\n{marron[4]}\n")
else:
    print("Número inválido")


#PARA EL COLOR5
if      color5  ==  1   :
    print(f"Color 5\n{listaColores[1]}\n{listaAspiraciones[5]}\n{azul[5]}\n")
elif    color5  ==  2 :
    print(f"Color 5\n{listaColores[2]}\n{listaAspiraciones[5]}\n{rojo[5]}\n")
elif    color5  ==  3   :
    print(f"Color 5\n{listaColores[3]}\n{listaAspiraciones[5]}\n{verde[5]}\n")
elif    color5  ==  4   :
    print(f"Color 5\n{listaColores[4]}\n{listaAspiraciones[5]}\n{amarillo[5]}\n")
elif    color5  ==  5   :
    print(f"Color 5\n{listaColores[5]}\n{listaAspiraciones[5]}\n{violeta[5]}\n")
elif    color5  ==  6   :
    print(f"Color 5\n{listaColores[6]}\n{listaAspiraciones[5]}\n{gris[5]}\n")
elif    color5  ==  7   :
    print(f"Color 5\n{listaColores[7]}\n{listaAspiraciones[5]}\n{marron[5]}\n")
elif    color5  ==  8   :
    print(f"Color 5\n{listaColores[8]}\n{listaAspiraciones[5]}\n{marron[5]}\n")
else:
    print("Número inválido")

# PARA EL COLOR6
if color6 == 1:
    print(f"Color 6\n{listaColores[1]}\n{listaAspiraciones[6]}\n{azul[6]}\n")
elif color6 == 2:
    print(f"Color 6\n{listaColores[2]}\n{listaAspiraciones[6]}\n{rojo[6]}\n")
elif color6 == 3:
    print(f"Color 6\n{listaColores[3]}\n{listaAspiraciones[6]}\n{verde[6]}\n")
elif color6 == 4:
    print(f"Color 6\n{listaColores[4]}\n{listaAspiraciones[6]}\n{amarillo[6]}\n")
elif color6 == 5:
    print(f"Color 6\n{listaColores[5]}\n{listaAspiraciones[6]}\n{violeta[6]}\n")
elif color6 == 6:
    print(f"Color 6\n{listaColores[6]}\n{listaAspiraciones[6]}\n{gris[6]}\n")
elif color6 == 7:
    print(f"Color 6\n{listaColores[7]}\n{listaAspiraciones[6]}\n{marron[6]}\n")
elif color6 == 8:
    print(f"Color 6\n{listaColores[8]}\n{listaAspiraciones[6]}\n{marron[6]}\n")
else:
    print("Número inválido")


# PARA EL COLOR7
if color7 == 1:
    print(f"Color 7\n{listaColores[1]}\n{listaAspiraciones[7]}\n{azul[7]}\n")
elif color7 == 2:
    print(f"Color 7\n{listaColores[2]}\n{listaAspiraciones[7]}\n{rojo[7]}\n")
elif color7 == 3:
    print(f"Color 7\n{listaColores[3]}\n{listaAspiraciones[7]}\n{verde[7]}\n")
elif color7 == 4:
    print(f"Color 7\n{listaColores[4]}\n{listaAspiraciones[7]}\n{amarillo[7]}\n")
elif color7 == 5:
    print(f"Color 7\n{listaColores[5]}\n{listaAspiraciones[7]}\n{violeta[7]}\n")
elif color7 == 6:
    print(f"Color 7\n{listaColores[6]}\n{listaAspiraciones[7]}\n{gris[7]}\n")
elif color7 == 7:
    print(f"Color 7\n{listaColores[7]}\n{listaAspiraciones[7]}\n{marron[7]}\n")
elif color7 == 8:
    print(f"Color 7\n{listaColores[8]}\n{listaAspiraciones[7]}\n{marron[7]}\n")
else:
    print("Número inválido")



# PARA EL COLOR8
if color8 == 1:
    print(f"Color 8\n{listaColores[1]}\n{listaAspiraciones[8]}\n{azul[8]}\n")
elif color8 == 2:
    print(f"Color 8\n{listaColores[2]}\n{listaAspiraciones[8]}\n{rojo[8]}\n")
elif color8 == 3:
    print(f"Color 8\n{listaColores[3]}\n{listaAspiraciones[8]}\n{verde[8]}\n")
elif color8 == 4:
    print(f"Color 8\n{listaColores[4]}\n{listaAspiraciones[8]}\n{amarillo[8]}\n")
elif color8 == 5:
    print(f"Color 8\n{listaColores[5]}\n{listaAspiraciones[8]}\n{violeta[8]}\n")
elif color8 == 6:
    print(f"Color 8\n{listaColores[6]}\n{listaAspiraciones[8]}\n{gris[8]}\n")
elif color8 == 7:
    print(f"Color 8\n{listaColores[7]}\n{listaAspiraciones[8]}\n{marron[8]}\n")
elif color8 == 8:
    print(f"Color 8\n{listaColores[8]}\n{listaAspiraciones[8]}\n{marron[8]}\n")
else:
    print("Número inválido")







#Primero: azul - el azul simboliza x cosa - simboliza las aspiraciones del sujeto
#Segundo: verde - el verde simboliza x cosa - simboliza las aspiraciones del sujeto
#Tercero: morado - el morado simboliza x cosa - simboliza la situación actual del sujeto
#Cuarto: amarillo - el amarillo simboliza x cosa - simboliza la situación actual del sujeto
#Quinto: negro - el negro simboliza x cosa - Simbolizan las inclinaciones latenetes, momentáneamente reprimidas
#Sexto: gris - el gris simboliza x cosa - Simbolizan las inclinaciones latenetes, momentáneamente reprimidas.
#Septimo: rojo - el rojo simboliza x cosa - Simbolizan los sentimientos que el sujeto rechaza completamente
#Octavo: marron - el marron simboliza x cosa - Simbolizan los sentimientos que el sujeto rechaza completamente