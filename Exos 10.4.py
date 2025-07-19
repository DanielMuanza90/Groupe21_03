numero = input("Entrez un numéro : ")

if len(numero) > 3:
    masque ="*" * (len(numero) - 3) + numero[-3:]
else:
    print("Numéro trop court pour masquer.")