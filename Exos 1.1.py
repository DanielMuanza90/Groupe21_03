# Demande d'information à l'utilisateur
prenom = input("Entrez votre prénom:")
age = int(input("Entrez votre âge:"))
ville = input("Entrez votre ville :")
metier = input("Entrez votre metier")



# Approximation des jours vécus
jours_vecus = age * 365

# affichage formaté
print("\n=== PROFIL UTILISATEUR ===")
print(f"Prénom : {prenom}")
print(f"Âge: {age} ans ({jours_vecus } jours vécus environ")
print(f"ville : {ville}")
print(f"Métier : {metier}")
