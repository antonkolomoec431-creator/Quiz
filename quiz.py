import random
import os

vragen=[
    {
        "vak":"programmeren",
        "vraag":"Wat is Python?",
        "antwoorden":["Programmeertaal", "Soort slang", "Scripts taal", "Framework"],
        "goed":"Programmeertaal"
    },
    {
        "vak":"programmeren",
        "vraag":"Wat is het moeilijkste programmeertaal ter wereld?",
        "antwoorden":["Lua", "Python", "C+", "Malbolge"],
        "goed":"Malbolge"
    },
    {
        "vak":"programmeren",
        "vraag":"Waarom wordt 'Hello World' gebruikt aan de begin van een code?",
        "antwoorden":["Om 'Hallo' tegen de computer te zeggen", "Om de computer jou te laten groeten","Om simpelweg te testen en controleren of het programma juist werkt", "Zodat je een computer laat weten dat je gaat coderen"],
        "goed":"Om simpelweg te testen en controleren of het programma juist werkt"
   
    },
    {
        "vak":"programmeren",
        "vraag":"Wat gebeurt er in Python wanneer je de operatoren // en % gebruikt om twee getallen te delen?",
        "antwoorden":["// geeft de rest van de deling en % geeft het resultaat als een kommagetal", " // rondt de uitkomst altijd af naar het dichtstbijzijnde gehele getal en % vermenigvuldigt de twee getallen", "// geeft het quotiënt afgerond naar beneden en % geeft de rest van de deling", "// deelt de getallen zonder de rest te verwijderen en % geeft het quotiënt afgerond naar beneden"],
        "goed":"// geeft het quotiënt afgerond naar beneden, terwijl % de rest van de deling teruggeeft"
    },
    {
        "vak":"programmeren",
        "vraag":"Hoe maak je een lijst in Python?",
        "antwoorden":["kleuren = [rood, groen, blauw]", "kleuren = (rood, groen, blauw)", "kleuren = {rood, groen, blauw}", "kleuren = [rood, groen, blauw]"],
        "goed":"kleuren = [rood, groen, blauw]"
    },
    {
        "vak":"programmeren",
        "vraag":"Welke teken gebruik je voor een commentaarregel in Python",
        "antwoorden":["//", "#", "**", "/*"],
        "goed":"#"
    },
    {
        "vak":"programmeren",
        "vraag":"Hoe maak je een functie met de naam groet?",
        "antwoorden":["def groet():", "function groet():", "groet():", "print('groet')"],
        "goed":"def groet():"
    },
    {
        "vak":"programmeren",
        "vraag":"Welke datatype gebrruikt Python voor True en False?",
        "antwoorden":["str", "bool", "int", "list"],
        "goed":"bool"
    },
    {
        "vak":"programmeren",
        "vraag":"Wat geeft len('Python') terug?",
        "antwoorden":["5", "6", "7", "Python"],
        "goed":"6"
    },
    {
        "vak":"programmeren",
        "vraag":"Welke tekenpaar controleert of twee waarden gelijk zijn?",
        "antwoorden":["==", "=", "!=", "<>"],
        "goed":"=="
    },
    {
        "vak":"programmeren",
        "vraag":"Wat is de uitkomst van 10 % 3?",
        "antwoorden":["1", "10", "3", "0"],
        "goed":"1"
    },
    {
        "vak":"programmeren",
        "vraag":"Welke woordt gebruik je om een voorwaarde te beginnen?",
        "antwoorden":["if", "for", "while", "def"],
        "goed":"if"
    },
    {
        "vak":"programmeren", 
         "vraag":"Hoe controleer je of getal groter is dan 67?",
        "antwoorden":["getal => 10", "getal > 10", "getal < 10", "getal = 10"],
        "goed":"getal > 10"
    },
    {
        "vak":"programmeren",
        "vraag":"Welke functie zet tekst om naar kleine letters?",
        "antwoorden":["lower()", "upper()", "small()", "str()"],
        "goed":"lower()"
    },
    {
        "vak":"programmeren",
        "vraag":"Hoe begin je een for-lus die 5 keer herhaalt?",
        "antwoorden":["foreach i in 5", "for i in range(5):", "for i in 5:", " for (i = 0; i < 5; i++)"],
        "goed":"for i in range(5):"
    },
    {
        "vak":"programmeren",
        "vraag": "Wat is de uitkomst van Python[::-1]?",
        "antwoorden":["nohtyP", "Python", "Een foutmelding", "n"],
        "goed":"nohtyP"
    }
]


# Highscore laden 
def highscore_laden():
    if os.path.exists("highscore.txt"):
        with open("highscore.txt","r") as bestand:
            inhoud=bestand.read().strip()
            if inhoud!="":
                return int(inhoud)            
    return 0        


# Highscore opslaan
def highscore_opslaan(score):
    with open("highscore.txt","w") as bestand:
        bestand.write(str(score))


def quiz():
    score=0

    # Vragen door elkaar
    random.shuffle(vragen)

    print()
    print("========================================")
    print("       MODULE 01 - OPLEIDINGSQUIZ")
    print("========================================")
    print()
    print("Test hoeveel jij weet over de opleiding!")
    print()
    for vraag in vragen:
        print(f"Vak: {vraag['vak']}")
        print(f"Vraag: {vraag['vraag']}")
        for i in range(4):
            print(f"{i+1}. {vraag['antwoorden'][i]}")
        user_input = input("Kies het juiste antwoord (1-4): ")
        if user_input not in ["1", "2", "3", "4"]:
            print("Ongeldige invoer. Kies een nummer tussen 1 en 4.")
            continue
        elif vraag['antwoorden'][int(user_input)-1] == vraag['goed']:
            print("Correct!")
            score += 1
        else:
            print(f"Fout! Het juiste antwoord is: {vraag['goed']}")
        print(f"Je score is: {score}")

    totaal = len(vragen)
    percentage = (score / totaal) * 100
    print("========================================")
    print("              QUIZ KLAAR!")
    print("========================================")
    print()
    print(f"Je hebt {score} van de {totaal} vragen goed.")
    print(f"Percentage: {(score / totaal) * 100:.0f}%")
    print()

    # Beoordeling
    if percentage == 100:
        print("Perfect! Jij weet echt heel veel over de opleiding!")
    elif percentage >= 80:
        print("Heel goed! Je kent de opleiding goed.")
    elif percentage >= 60:
        print("Goed gedaan! Er is nog wat ruimte om te oefenen.")
    elif percentage >= 50:
        print("Voldoende. Je kunt nog wat meer leren over Module 01.")
    else:
        print("Je kunt de onderwerpen van Module 01 nog wat beter oefenen.")

    oude_highscore=highscore_laden()
    if score> oude_highscore:
        print()
        print("Nieuwe Highscroe!")
        print(f"Je oude score is: {oude_highscore}")
        print(f"Je nieuwe score is: {score}")

        highscore_opslaan(score)
    else:
        print(f"De huidige highscore is: {oude_highscore}")


while True:
    quiz()
    opnieuw = input("Wil je nog een keer spelen? (ja/nee): ")
    if opnieuw.lower() != "ja":
        print()
        print("Bedankt voor het spelen!")
        print("Tot de volgende keer!")
        break
        