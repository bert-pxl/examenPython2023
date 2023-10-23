'''
Casus 2: Aanspreking met gebruik van een functie, afdruk gebruik vanuit de functie
De gebruiker geeft 3 keer de waarde van de functie in
· Aanspreking(geslacht,Familie_naam,beroep)
· Indien het geslacht M: Heer, Geslacht V: Mevrouw
· Titel, deze titels zijn gekend door het programma.
o Dokter: Dr.
o Professor: Prof.
o Ingenieur: Ir.
o Andere: Geen aanspreking
§ Titels worden niet gecombineerd in deze opdracht.
· Voorbeeld output(Man,Peeters,Dokter): Geachte Heer Dr Peeters.
'''


def get_gender_string():
    while True:
        try:
            user_input = str(input("Wat is je geslacht (M/V) ").strip().lower())
            if user_input == "m":
                return "Meneer"
            elif user_input == "v":
                return "Mevrouw"
            else:
                raise ValueError
        except ValueError:
            print("Invalid input. enkel M of V wordt geaccepteerd.")


def get_title_string():
    print("A) Dokter")
    print("B) Professor")
    print("C) Ingenieur")
    print("X) Geen titel")
    user_input = input("Heeft u een titel (A/B/C/X) ").strip().lower()
    if user_input == "a":
        return "Dr."
    elif user_input == "b":
        return "Prof."
    elif user_input == "c":
        return "Ir."
    else:
        return ""


for i in range(1, 4):
    print("persoon", i)
    print("Geachte", get_gender_string(), get_title_string(), input("Wat is familienaam "))
