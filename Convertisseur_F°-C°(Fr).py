#Convertisseur degrés Farenheit en degrés Celsius

run = True

while run == True: 
    temp_F = float(input("Entrez une température en degrés Farenheit (pas besoin d'écrire le symbole)"))
    temp_C = ( ((temp_F) - 32)/1.8 )
    print(f"La température en Celsius de {temp_F}°F est de {temp_C}°C.")
    print("")
