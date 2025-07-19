from itertools import count

phrase = input("Entrez une phrase : ")
mots = phrase.split()

count = 0
for mot in mots:
    if len(mot) > 5:
        count += 1

print(f"Nombre de motes > 5 lettres : {count}")