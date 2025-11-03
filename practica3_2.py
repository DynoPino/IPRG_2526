import math

def calculadora_area_cercle(radi):
    area = math.pi * (radi ** 2)
    return area

usuari_radi = float(input("Introdueix el radi del cercle: "))

area_calculada = calculadora_area_cercle(usuari_radi)

print(f"El area del cercle amb radi {usuari_radi} és {area_calculada:.2f}")