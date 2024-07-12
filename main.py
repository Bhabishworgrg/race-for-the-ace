from random import choice

def card_shuffler(number, symbol):
    """Shuffles the deck of cards.
    Method: takes the numbers & symbols possible in a card and randomly matches them"""

    shuffledCards = []

    while True:
        randomCard = choice(number) + choice(symbol)
        
        for x in shuffledCards:
            if x == randomCard:
                break
        else:
            shuffledCards.append(randomCard)        
        
        if len(shuffledCards) == 52:
            break    

    return shuffledCards

def AS_finder(cards):
    """Searches for ace of spades."""
    
    if "AS" in cards[:26]:
        return "North" if "AS" in cards[:13] else "South"
    else:
        return "West" if "AS" in cards[39:] else "East"

if __name__ == "__main__":    
    print("Creating pack of cards ...")

    num = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    sym = ["S", "H", "D", "C"]

    allCards = card_shuffler(num, sym)

    print("Shuffling and Dealing ...")

    cardsHanded = [" ".join(allCards[13 * i:13 * (i + 1)]) for i in range(4)]

    print(f"""
Four Hands ...
North --> {cardsHanded[0]}
South --> {cardsHanded[1]}
East --> {cardsHanded[2]}
West --> {cardsHanded[3]}

Looking for the Ace of Spades ...
{AS_finder(allCards)} player has it!
    """)
