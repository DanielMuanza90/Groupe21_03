activate = input("Décrivez votre activité du jour : ")

with open("journal.txt", "a", encoding="utf-8") as f:
    f.write(activate + "\n")
