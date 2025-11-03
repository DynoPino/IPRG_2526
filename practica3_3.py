def sumar(num1, num2=10):
    rusultat = num1 + num2
    return rusultat

print("== 1. AMB UN SOL VALOR ==")
suma1 = sumar(5)
print(f"sumar(5) = {suma1}")
print(f"Explicació: hem posar que el suma1 siga igual a suma(5) que tindra per defecte eixe numero el 5 y el el num2 té per defecte el valor 10, per aixo donara 15")
print(f"Entonces el sumar(5) posa que el num1=(5) + num2=(10) y si el num1 y el num2 no numero per defecte y coloques els dos numeros en el [sumar] aixi [sumar(5, 10)] el 5 es posaria per defecte al num1 y el 10 al num2, que dona = {suma1}")

print("== 2. AMB DOS VALORS ==")
suma2 = sumar(10, 15)
print(f"sumar(10, 15) = {suma2}")
print(f"Explicació: hem posat que el suma2 siga igual a suma(10, 15) que tindra el num1=10 i el num2=15, per aixo donara 25")