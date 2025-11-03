estudiants = ['Carles', 'Jaume', 'Leonardo', 'Ubay', 'Mateo', 'Anegel', 'Pau', 'Joel']

print("== ESTUDIANTS DE 2A-SMX ==")
print(f"Nombres dels estudiant a classe: {estudiants}")
print(f"Total dels estudiants a classe: {len(estudiants)}\n")

nou_estudiant = "Iker"
estudiants.append(nou_estudiant)
nou_estudiant2 = "Moncho"
estudiants.append(nou_estudiant2)

print("== ESTUDIANTS DE 2A-SMX (nou estudiant afegit) ==")
print(f"Nou alumne afegit: {nou_estudiant}, {nou_estudiant2}")
print(f"Nombres dels estudiant a classe: {estudiants}")
print(f"Total dels estudiants a classe: {len(estudiants)}\n")

estudiant_eliminat = estudiants.pop(1)

print("== ESTUDIANTS DE 2A-SMX (eliminació d'un estudiant) ==")
print(f"Estudiant a eliminar: {estudiant_eliminat}")
print(f"Nombres dels estudiant a classe: {estudiants}")
print(f"Total dels estudiants a classe: {len(estudiants)}")
