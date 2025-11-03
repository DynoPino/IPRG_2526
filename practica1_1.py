print("CALCULADORA SIMPLE OPTATIVA")

num1 = int(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

print("RESULTAT DE LES OPERACIONS")
print(f"Suma: {num1} + {num2} = {num1 + num2}")
print(f"Resta: {num1} - {num2} = {num1 - num2}")
print(f"Multiplicación: {num1} * {num2} = {num1 * num2}")

if num2 != 0:
    print(f"División: {num1} / {num2} = {num1 / num2}")
    print(f"División entera: {num1} // {num2} = {num1 // num2}")
    print(f"Resto: {num1} % {num2} = {num1 % num2}")
else:
    print("No se puede realizar la división por cero.")
    print("No se puede realizar la división entera por cero.")
    print("No se puede calcular el resto de la división por cero.")

print("CONCATENACIÓN DE CADENAS")
missatge = "El resultado de sumar de = " + str(num1) + " + " + str(num2) + " és [" + str(num1 + num2) + "]"
print(missatge)

missatge = "El resultado de restar de = " + str(num1) + " - " + str(num2) + " és [" + str(num1 - num2) + "]"
print(missatge)

missatge = "El resultado de multiplicar de = " + str(num1) + " * " + str(num2) + " és [" + str(num1 * num2) + "]"
print(missatge)

missatge = "El resultado de la división de = " + str(num1) + " / " + str(num2) + " és [" + str(num1 + num2) + "]"
print(missatge)

missatge = "El resultat de la división entera de = " + str(num1) + " // " + str(num2) + " és [" + str(num1 // num2) + "]"
print(missatge)

missatge = "El resultat de los residuos de " + str(num1) + " % " + str(num2) + " és [" + str(num1 % num2) + "]"
print(missatge)

missatge_alt = f"Has intoducido el numero [{num1} como primer numero] y [{num2} como segundo numero]"
print(missatge_alt)