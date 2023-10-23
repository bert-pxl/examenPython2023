'''Casus 1: Willekeurige lijst.
· Vul een lijst met 47 willekeurige getallen tussen 20 en 200.
· De gebruiker geef hierna zelf nog 3 getallen in. Geen invoercontrole nodig
· Druk de 3 grootste getallen uit de lijst af
· Toon het gemiddelde van de lijst.
· Druk de lijst van groot naar klein af.
'''
from random import randint

lst = [randint(20,200) for x in range(47)]

for i in range(3):
    lst.append(int(input(f"geef getal {i+1} in: ")))

lst.sort()
print("de drie grootste getallen", lst[-3:])
print("het gemiddelde:", sum(lst)/len(lst))
lst.reverse()
print("de omgekeerde lijst")
for i in lst:
    print(i)
