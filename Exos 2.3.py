montant_ht = float(input("Montant HT ($) : "))
taux_tva = float(input("Taux de TVA (%) :"))

# conversion en coéfficient multiplicateur
taux_coef = taux_tva / 100

# Calcul TTC
montant_ttc = montant_ht * (1 + taux_coef)

print(f"montant TTC : {montant_ttc:.2f} $")
