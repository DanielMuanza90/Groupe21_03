
plat = input("choisissez un plat (viande/poisson/végétarien) : ").lower()

if plat == "viande":
    cuisson = input("cuisson (saignant/à point/bien cuit) :").lower()
    print(f"Vous avez choisi une viande {cuisson}.")
elif plat == "poisson":
    sauce = input("sauce (citron/beurre) : ").lower()
    print(f"Vous avez choisi un poisson sauce {sauce}.")
elif plat == "végétarien":
    choix = input("Souhaitez-vous une salade ou des pâtes ?").lower()
    print(f"vous avez choisi : {choix}.")
else:
    print("choix invalide.")