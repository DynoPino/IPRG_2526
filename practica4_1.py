x = 10
y = 5

print("== VARIABLES INICIALS ==")
print(f"x = {x}")
print(f"y = {y}")

print("== OPERACIONS ENTRE X & Y")
print(f"Suma: {x} + {y} = {x + y}")
print(f"Resta: {x} - {y} = {x - y} ")
print(f"Multiplicación: {x} * {y} = {x * y}")
print(f"Modul: {x} % {y} = {x % y}")

print("== IGUALTATS ==")
print(f"Quin es mes gran (x) o (y): {x > y} (x) es mes gran que (y)")
print(f"Les dos variables seran iguals entre si? {x == y} perque (x) es mes major que (y)")

print("== OPERADORS LOGICS ==")

condicio1 = x > y
condicio2 = x % 2 == 0

resultat_dues = condicio1 and condicio2
print(f"x es mes gran que y? {condicio1}")
print(f"El modul x entre 2 es 0 (x es parell?)? {condicio2}")
print(f"Les dos condicions són verdades? {resultat_dues}")