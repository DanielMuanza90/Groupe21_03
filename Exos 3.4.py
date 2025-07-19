from traceback import print_tb

temp = float(input("Temperature (°c): "))

if temp  >=  35:
    print("Très chaud, restez hydraté.")
elif temp >= 25:
    print("Chaud, faites attention au soleil.")
elif temp  >=  15:
    print("Temps agréable.")
else:
    print("Il fait frais, couvrez-vous.")
