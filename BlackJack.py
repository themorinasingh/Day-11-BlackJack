import random
from random import choice
from design import design

def black_jack():
    print(design)
    deck = [11, 2, 3 , 4, 5, 6, 7, 8, 9 , 10, 10, 10, 10]

    dealer_hand = [choice(deck), choice(deck)]

    player_hand = [choice(deck), choice(deck)]

    print(f"Computer's Hand: {dealer_hand[0]}")

    print(f"Your Hand: {player_hand} \n")

    hit_or_stand = input("hit or stand: ").lower()

    if hit_or_stand == "hit":
        player_hand.append(random.choice(deck))
        print("You chose hit")
        print(f"Your Hand: {player_hand}")

    computer_total = sum(dealer_hand)

    while computer_total < 17:
        dealer_hand.append(random.choice(deck))
        computer_total = sum(dealer_hand)

    player_sum = sum(player_hand)
    if player_sum > 21 and 11 in player_hand:
        player_hand.remove(11)
        player_hand.append(1)
        player_sum = sum(player_hand)

    print(f"The computer's cards: {dealer_hand}")
    print(f"Your Cards: {player_hand}")


    if computer_total > 21 and player_sum > 21:
        print("You both loose")
    elif player_sum > 21:
        print("You Busted")
        print("Computer Won")
    elif computer_total > 21:
        print("Computer Busted")
        print("You Won")
    elif player_sum > computer_total:
        print("You Won")
    elif  player_sum < computer_total:
        print("You Lost")
    elif computer_total == player_sum:
        print("Game Drawn")


    play_again = input("Do you want to play another game? y/: n").lower()

    if play_again == 'y':
        black_jack()
    else:
        print("Thank You for playing")

black_jack()