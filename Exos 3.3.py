panier = float(input("montant du panier ($) : "))

if panier  >=  100:
    frais = 0
elif panier  >=  50:
    frais = 5
else:
    frais = 10
total = panier + frais
print(f"Frais de livraison : {frais} ($)")
print(f"Total à payer : {total:.2f} $")
