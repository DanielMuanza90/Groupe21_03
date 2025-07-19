import random
# Génération d'un nombre aléatoire
nombre_secret = random.randint(1, 100)
essai = None


while essai != nombre_secret:
    essai = int(input("devine le nombre (1-100) : "))
    if essai < nombre_secret:
        print("trop petit.")
    elif essai > nombre_secret:
        print("trop grand.")
    else:
        print("Bravo, tu as trouvé !")
