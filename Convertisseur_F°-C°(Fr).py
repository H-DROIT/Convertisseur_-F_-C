#Convertisseur degrés Farenheit en degrés Celsuis

run = True

while run == True: 
    temp_F = float(input("Entrez une température en degrés Farenheit (pas besoin d'écrire l'unité)"))
    temp_C = ( ((temp_F) - 32)/1.8 )
    print(f"La température en Celsuis de {temp_F}°F est de {temp_C}°C.")
    print("")