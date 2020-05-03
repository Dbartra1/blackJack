import random

class Card:
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val

    def getRank(self, cardValue):
        # Return rank if this is a face card, otherwise return the passed value 
        switcher = {
            1: "Ace",
            11: "Jack",
            12: "Queen",
            13: "King",
        }

        return switcher.get(cardValue, cardValue)

    def show(self):
        print ("{} of {}".format(self.getRank(self.value), self.suit))

class Deck:
    def __init__(self):
        self.cards = []
        self.build()
    
    # Create the card deck
    def build(self):
        for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for v in range(1,13):
                self.cards.append(Card(s, v))

    # Shuffle the deck
    def shuffle(self):
        for i in range(len(self.cards) -1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    # Pulls a card from the deck
    def drawCard(self):
        return self.cards.pop()
        self.shuffle()

    # Shows the card
    def show(self):
        for c in self.cards:
            c.show()

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.acePresent = False

    def draw(self, deck):
        # Get next card
        card = deck.drawCard()
        # Inspect card to see if it's an Ace
        if card.value == 1:
            self.acePresent = True
            print("Ace present")
        self.hand.append(card)
    
    def showHand(self):
        for card in self.hand:
            card.show()

    def showHandScore(self):
        score = 0
        for card in self.hand:
            # If the card value is >= 11, it is a face card, which is scored as 10
            if card.value >= 11:
                score += 10
            # Other cards, scored as actual value (Ace scores as 1)
            else:
                score += card.value
        
        # Evaluate score and account for Ace, as needed to maximize score without busting
        if score <= 10 and self.acePresent == True:
            # Bump the score by 10 to switch Ace value from 1 to 11
            score += 10
        
        return score
# Stunt code

# Initalize two players
dealer = Player("Dealer")
player = Player("Bettor")

deck = Deck()
deck.shuffle()
bob = Player("Bob")

for i in range(0, 2):
    bob.draw(deck)
    i = i + 1
bob.showHand()
bob.showHandScore()
