""" Detta är ett Python program för spelet Chomp. Spelet går ut på att två spelare ska försöka att undvika
    att äta den förkiftade chokladrutan."""


def createBord():
    """
    Funktion för att skapa spelplanen för spelet!
    Funktionen tar inga indata men retunerar en 2D lista
    som representerar spelplanen
    """
    nummerKontroll = True
    while (nummerKontroll == True):
        #Är en While loop som körs tills att användaren har skrivit in en korrekt bas och höjd på spelplanen.
        höjd = input("Hur hög ska chokladen vara?\n")
        bredd = input("Hur bredd ska chokladen vara?\n")
        if (höjd.isnumeric() and bredd.isnumeric()):
            #Kontrollerar att höjden och bredden som användaren skrev in är numeriska .
            #Om det är numeriska så sparas de som ints, om de inte är numeriska så får användaren skriva värderna igen. 
            print("Storklek: " + höjd + " * " + bredd)
            nummerKontroll = False
            höjd = int(höjd)
            bredd = int(bredd)
        else:
            print("Du har skrivit fel. Gör om!\n")

    #Spelplanen är skapad i en 2D lista
    spelplan = [0]*höjd
    for i in range(höjd):
        rad = [0]*bredd
        for j in range(bredd):
            if (i == 0 and j == 0):
                rad[j] = "P"
            else:
                rad[j] = str(i+1) + str(j+1)
        spelplan[i] = rad
    return spelplan

def printBord(spelplan):
    """
    Funktion för att skriva ut och den givna spelplanen
    """
    for rad in spelplan:
        raden = ""
        for element in rad:
            if (element == "P"):
                raden += element + "  "
            else:
                raden += element + " "
        print(raden)


def chomp(spelplan):
    """
    Funktion för att ta input och uppdatera chockladen
    """
    korrektKoordinater = False
    #Kontrolera att det man skriver in är en korrekt chockladbit
    while (not korrektKoordinater):
        koordinater = input("Vilken Chockladruta vill du ta?")
        rad = int(koordinater[0])
        kolumn = int(koordinater[1])
        if(1 <= rad <= len(spelplan) and 1 <= kolumn <= len(spelplan[rad - 1])):
            korrektKoordinater = True
        else:
            print("Nu skrev du fel. Försök igen!")
    #Uppdaterar chockladen utifrån vilken bit man valde
    for i in range(rad - 1, len(spelplan)):
        spelplan[i] = spelplan[i][:kolumn - 1]
    return spelplan



def main():
    """
    Huvudfunktionen av programmet. Det är denna funktion som kör spelet
    """
    gameOver = False
    player1Tur = True
    spelplan = createBord()
    while(not gameOver): #Går lika bra att skrivas som 'while(gameOver == False):'
        printBord(spelplan) 
        if (player1Tur): #Går lika bra att skriva 'if(player1Tur == True)'
            print("Spelare 1:s tur")
            player1Tur = False
        else:
            print("Spelare 2:s tur")
            player1Tur = True
        chomp(spelplan)
        
        #Kontrollera om spelet är över genom att kolla på storkleken av chockladen
        if len(spelplan[0]) == 1 and len(spelplan[1]) == 0:
            if(not player1Tur):
                print("\nSpelare 1 vann\n")
            else:
                print("\nSpelare 2 vann\n")
            break
main()