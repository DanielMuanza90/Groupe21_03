note = float(input("Entrez votre note sur 100 : "))

if note >= 90:
    print("Mention : Excellent")
elif note >= 75:
    print("Mention : Très bien ")
elif note  >= 50:
    print("Mention : Passable ")
else:
    print("Mention : Insuffisant")
