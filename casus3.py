'''
Casus 3:Fietsverhuur.
· De gebruiker geeft in hoeveel fietsen hij wenst te huren(hoofdprogramma). Per fiets wordt er een kostprijs berekend. De berekening doen we met een functie, de afdruk wordt vanuit het hoofdprogramma gedaan, dus de functie geeft de kostprijs terug.
· Aantal dagen kan verschillend zijn, zo kan iemand bvb 1 kinderfiets voor 5 dagen geven en een elektrisch fiets voor 3.
· Functie verhuurfiets(Type,Dagen,Verzekering)

Type · Dagprijs
Kinderfiets € 30
Volwassenfiets € 40
Tandem € 50
Elektrische fiets € 50
Pedelec(45 km), Rijbewijs verplicht € 70

· Indien de gebruiker geen rijbewijs heeft, krijgt hij een elektrische fiets in de plaats pedelec, aan € 50 per dag.
· Indien de gebruiker een Verzekering wenst kan dit. Dit is de dagprijs.

Type Dagprijs
Kinderfiets € 8
Volwassenfiets € 10
Tandem € 10
Elektrische fiets € 15
Pedelec(45 km), Rijbewijs verplicht € 25
· Ook zal er een waarborg aangerekend worden, Dit is een vast bedrag dus niet afhankelijk van het aantal dagen
Type
Kinderfiets € 100
Volwassenfiets € 150
Tandem € 150
Elektrische fiets € 200
Pedelec(45 km), Rijbewijs verplicht € 350

Print in hef hoofd programma de prijzen van verhuur. Als ook de totaal prijs
'''

bikes = {"A": {"type": "kinderfiets", "day_price": 30, "deposit": 100, "insurance": 8},
         "B": {"type": "volwassenenfiets", "day_price": 40, "deposit": 200, "insurance": 10},
         "C": {"type": "tandem", "day_price": 50, "deposit": 150, "insurance": 10},
         "D": {"type": "elektrische fiets", "day_price": 50, "deposit": 200, "insurance": 15},
         "E": {"type": "Pedelec(45km)", "day_price": 70, "deposit": 350, "insurance": 25},
         }


def select_bike():
    while True:
        try:
            for key, value in bikes.items():
                print(f"{key} : {value['type']}")
            user_input = input("> ").strip().upper()
            if user_input in [x.upper() for x in bikes.keys()]:
                return user_input
            else:
                raise ValueError()
        except ValueError:
            print(f"only {[x for x in bikes.keys()]} are accepted")


def ask_insurance():
    while True:
        try:
            user_input = input("Wil je graag een verzekering afsluiten (J/N) ").strip().lower()
            if user_input == "ja" or user_input == "j":
                return True
            elif user_input == "nee" or user_input == "n":
                return False
            else:
                raise ValueError
        except ValueError:
            print("Invalid input. enkel ja of nee")


def ask_license():
    while True:
        try:
            user_input = input("Heb je een rijbewijs (J/N) ").strip().lower()
            if user_input == "ja" or user_input == "j":
                return True
            elif user_input == "nee" or user_input == "n":
                return False
            else:
                raise ValueError
        except ValueError:
            print("Invalid input. enkel ja of nee")


def cost_rent(bike, days):
    return bikes[bike]['day_price'] * days


def total_cost_bike(bike, days, insurance):
    price_rent = cost_rent(bike, days)
    cost_insurance = bikes[bike]['insurance'] * days if insurance else 0
    cost_deposit = bikes[bike]['deposit']
    return cost_deposit + price_rent + cost_insurance


nr_of_bikes = int(input("Hoeveel fietsen wilt u huren? "))
rented_bikes = []
for i in range(nr_of_bikes):
    selected_bike = select_bike()
    if selected_bike == 'E':
        if ask_license():
            has_insurance = True
        else:
            print("We gaan je dan een Elektrische fiets moeten geven")
            selected_bike = 'D'
            has_insurance = ask_insurance()
    else:
        has_insurance = ask_insurance()
    days_rented = int(input("Hoeveel dagen wil je de fiets? "))
    rented_bikes.append(
        f"Keuze ({i+1}): een {bikes[selected_bike]['type']} voor {days_rented} dag(en) kost\n"
        f"huur {cost_rent(selected_bike, days_rented)} \n"
        f"waarborg {bikes[selected_bike]['deposit']} \n"
        f"Totale kost is {total_cost_bike(selected_bike, days_rented, has_insurance)}\n")

for bike in rented_bikes:
    print(bike)
