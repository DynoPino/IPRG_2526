# Activatat 6.1 Exlicación
a = [5, 10, 15]
b = 20

if 5 in a:
    b -= 5
if 10 in a:
    b -= 10
if 15 in a:
    b -= 15

print(b)

# a = [5, 10, 15] → Crea una llista amb tres elements
# b = 20 → Inicialitza b amb valor 20
#if 5 in a: → True (5 està a la llista)
# b -= 5 → b passa a ser 15
# if 10 in a: → True (10 està a la llista)
# b -= 10 → b passa a ser 5
# if 15 in a: → True (15 està a la llista)
# b -= 15 → b passa a ser -10
# print(b) → Imprimeix -10








#Exercici 6.2

a = [5, 10, 15]
b = 20

if 5 in a:
    b -= 5
elif 10 in a:
    b -= 10
elif 15 in a:
    b -= 15

print(b)

#Atenció: Aquest codi té un ERROR de sintaxi!
#La línia else 15 in a: és incorrecta. Hauria de ser elif 15 in a:. El else no pot portar una condició.
#Si el corregim a elif, el comportament seria:
#Execució pas a pas:
#a = [5, 10, 15]
#b = 20
#if 5 in a: → True (5 està a la llista)
#b -= 5 → b passa a ser 15
#Com és True, les següents condicions elif i else NO s'executen
#print(b) → Imprimeix 15
#Diferència clau: Amb if/elif/else, només s'executa una branca. Amb if/if/if (exercici 6.1), s'executen totes les condicions que siguin certes.
#Resultat (si es corregeix): 15










#Exercici 6.3

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(6))



#Què fa el codi:
#Aquesta és una funció recursiva que calcula el factorial d'un nombre. El factorial de n (escrit n!) és el producte de tots els nombres enters positius fins a n.
#Execució amb n = 6:

#factorial(6)
#  → 6 * factorial(5)
#       → 5 * factorial(4)
#            → 4 * factorial(3)
#                 → 3 * factorial(2)
#                      → 2 * factorial(1)
#                           → 1 * factorial(0)
#                                → return 1



#Càlcul cap enrere:
#factorial(0) = 1
#factorial(1) = 1 × 1 = 1
#factorial(2) = 2 × 1 = 2
#factorial(3) = 3 × 2 = 6
#factorial(4) = 4 × 6 = 24
#factorial(5) = 5 × 24 = 120
#factorial(6) = 6 × 120 = 720
#Resultat: 720