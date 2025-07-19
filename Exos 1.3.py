# Entrée utilisateur
heures = int(input("Nombre d'heures : "))
minutes = int(input("nombre de minutes : "))
secondes = int(input("Nombre de secondes : "))

# Conversion
total_secondes = heures * 3600 + minutes * 60 + secondes


# Résultat
print(f"Durée totale : {total_secondes} secondes.")
