# BlackJack or 21 game

import random

dealer_hand = []
player_hand = []
suits = ['clubs','spades','hearts','diamonds']

def titlePrint():
    print("\nBlackJack!")

def main():
    titlePrint()
    print ("\n")
    choice1 = 'y'
    while choice1.lower() == 'y':
        while True:
            while len(dealer_hand) != 2:
                dealer_hand.append(random.randint(1, 11))
                random.shuffle(suits)
                if len(dealer_hand) == 2:
                    print("Dealer has X &", dealer_hand[1], suits[0], "\n")


            while len(player_hand) != 2:
                player_hand.append(random.randint(1, 11))
                random.shuffle(suits)
                if len(player_hand) == 2:
                    print("You have ", player_hand[0], suits[0], "and a", player_hand[1], "of", suits[1])
            

                if sum(dealer_hand) <= 21:
                    dealer_hand.append(random.randint(1, 11))
                if sum(dealer_hand) == 21:
                    print("Dealer has 21 and wins!")
                elif sum(dealer_hand) > 21:
                    print("Dealer has busted!")


            while sum(player_hand) < 21:
                action_taken = str(input("Do you want to stay or hit?  "))
                if action_taken == "hit":
                    player_hand.append(random.randint(1, 11))
                    print("You now have a total of " + str(sum(player_hand)) + " from these cards ", player_hand)
                else:
                    print("The dealer has a total of " + str(sum(dealer_hand)) + " with ", dealer_hand)
                    print("You have a total of " + str(sum(player_hand)) + " with ", player_hand)

                    if sum(dealer_hand) > sum(player_hand):
                        print("Dealer wins!")
                        break
                    else:
                        print("You win!")
                        break

            if sum(player_hand) > 21:
                print("You BUSTED! Dealer wins.")
                break
            elif sum(player_hand) == 21:
                print("You have BLACKJACK! You Win!! 21")
                break            

        choice1 = str(input("Would you like to continue? (y/n): "))
        if choice1.lower() != 'y':
            print("\nBYE!!!!")
            break


if __name__ == "__main__":

    main()


    
