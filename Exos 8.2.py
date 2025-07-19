entree = input("Entrez des éléments : ")
liste = entree.split()

for i, elem in enumerate(liste):
    print(f"indice {i} : {elem}")
