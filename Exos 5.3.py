texte = input("Entrez une chaîne :")
inverse = ""

for char in texte:
    inverse = char + inverse # on ajoute chaque caractère devant

print(f"chaîne inversée : {inverse}")
