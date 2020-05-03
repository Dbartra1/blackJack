from BlackjackClasses import *
import sys

def printTitle():
    print("\n")
    print ("Blackjack!\n")


def score(playerTotal, dealerTotal):

    if playerTotal == 21:
        print ("Congratulations! You got a Blackjack!\n")
    elif dealerTotal == 21:
        print ("Sorry, you lose. The dealer got a blackjack.\n")
    elif playerTotal > 21:
        print ("Sorry. You busted. You lose.\n")
    elif dealerTotal > 21:
        print ("Dealer busts. You win!\n")
    elif playerTotal < dealer.showHandScore():
        print ("Sorry. Your score isn't higher than the dealer. You lose.\n")
    elif playerTotal > dealer.showHandScore():
        print ("Congratulations. Your score is higher than the dealer. You win\n")

def main():
    choice1 = 'y'
    while choice1.lower() == 'y':
        #init Deck and shuffle
        deck = Deck()   
        deck.shuffle()
        
        #init two players
        dealer = Player("Dealer")
        player = Player("Bettor")
        
        #first dealer show card, only showing 1
        print ("DEALER'S SHOW CARD:")
        dealer.draw(deck)
        dealer.showHand()
        dealer.draw(deck)
        print("\n")
        
        #print both cards for the player
        print ("YOUR CARDS:")
        for i in range(0, 2):
            deck.shuffle()
            player.draw(deck)
            i = i + 1
        player.showHand()
        if player.showHandScore() == 21:
            print ("Black Jack!")
            
        else: 
            pass
        print("\n")

        #starting the Hit or Stand loop
        action = ""
        while action.lower() != 'stand':
            action = input(str("\nHit or Stand?: "))
            while action.lower() == "hit":
                deck.shuffle()
                player.draw(deck)
                player.showHand()
                player.showHandScore()
                break
            else: 
                pass 
        
        #dealer draw
        while True:
            if dealer.showHandScore() <= 17:
                dealer.draw(deck)
                break
            else:
                break

    #call function to score game
        

        #print dealers hand
        print ("\n")
        print ("DEALER'S CARDS: ")
        dealer.showHand()
        print ("\n")

        dealerTotal = dealer.showHandScore()
        playerTotal = player.showHandScore()

        print ("DEALER'S Points: {} ".format (dealer.showHandScore()))
        print("PLAYER'S Points: {} ".format (player.showHandScore()))

        score(playerTotal, dealerTotal)
                
        choice1 = input("\ncontinue? (y/n): ")
        if choice1.lower() != 'y':
            print ("\nTHANKS FOR PLAYING BLACKJACK!")
            break



printTitle()
main()
