note1 = float(int("première note : "))
note2 = float(int("Deuxième note : " ))
note3 = float(input("Troisième note : "))

moyenne = (note1 + note2 + note3) / 3

print(f"Moyenne : {moyenne:.2f}")

if moyenne >= 10 :
    print("l'étudiant est reçu.")
else:
    print("L'étudiant n'est pas reçu.")
    