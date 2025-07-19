# Demander deuxx nombres
a = float(input("Entrez le premier nombre :"))
b = float(input("Entrez le deuxième nombre : "))

# Calculs
somme = a + b
difference = a - b
produit = a * b
quotient = a / b if b !=0 else  "Division pa zéro "
division_entiere = a // b if b != 0 else "Division par zéro"
reste = a % b if b != a else "Division par zéro"

# Affichage des résultats
print(f"somme : {somme}")
print(f"différence : {difference}")
print(f"Produit : {quotient}")
print(f"Quotient : {quotient}")
print(f"Division entière : {division_entiere}")
print(f"Reste : {reste}")