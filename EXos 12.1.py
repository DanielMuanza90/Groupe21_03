utilisateurs = []

while True:
    nom = input("Entrez un nom d'utilisateur (ou 'stop' pour finir) :")
    if nom.lower() == "stop":
        break
    utilisateurs.append(nom)

with open("utilisateur.txt", "w", encoding="utf-8") as f:
    for u in utilisateurs:
        f.write(u + "\n")

print("utilisateur enregistrés dans 'utilisateurs.txt'.")