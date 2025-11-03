print("=" * 50)
print("     CALCULADORA D'ÍNDEX DE MASSA CORPORAL (IMC)")
print("=" * 50)

pes = float(input("Introduce el peso en kilogramos: "))
altura = float(input("Introduce la altura en metros: "))

imc = pes / (altura ** 2)

print("\n" + "=" * 50)
print("                  RESULTAT")
print(f"Pes: {pes} kg")
print(f"Altura: {altura} m")
print(f"IMC calculat: {imc:.2f}")
print("-" * 50)

if imc < 18.5:
    categoria = "Pes inferior al saludable"
    emoji = "⚠️"
    consell = "Consulta amb un metje"

elif imc >= 18.5 and imc < 24.9:
    categoria = "Pes saludable"
    emoji = "✅"
    consell = "Mantén els teus hàbits saludables!"

else:
    categoria = "Sobreeiximent de pes"
    emoji = "⚠️"
    consell = "Considera fer exercici i portar una dieta equilibrada."

print(f"\n{emoji} Categoria: {categoria}")
print(f"Consell: {consell}")
print("=" * 50)

print("\n📊 TAULA DE REFERÈNCIA D'IMC:")
print("-" * 50)
print("IMC < 18.5        → Inferior al pes saludable")
print("18.5 ≤ IMC ≤ 24.9 → Pes saludable")
print("25.0 ≤ IMC ≤ 29.9 → Sobrepes")
print("IMC ≥ 30.0        → Obesitat")
print("-" * 50)
print("\n⚕️  Nota: L'IMC és una eina orientativa.")
print("   Consulta sempre amb un professional de la salut.")
print("=" * 50)
