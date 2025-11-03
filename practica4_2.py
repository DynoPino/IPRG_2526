fruites = ["Taronja", "Pera", "Poma", "Plátano", "Uva"]

print("== FRUITES DISPONIBLES ==")
print(f"Fruites: {fruites}")
print(f"total de fruites: {len(fruites)}\n")

fruites_buscar = input("Escriu el nom de la fruita que vols buscar: ")

if fruites_buscar in fruites:
    print(f"Si! '{fruites_buscar}' es una de les fruites disponibles.")
    posicio = fruites.index(fruites_buscar)
    print(f"Es troba a la posició {posicio} de la llista.")

if fruites_buscar not in fruites:
    print(f"Ho sentim! '{fruites_buscar}' no es una de les fruites disponibles.")
    print(f"Les fruites disponibles són: {fruites}")
    