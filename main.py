import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
        if 11 in cards and 10 in cards and len(cards) == 2:
            return 0 
        if 11 in cards and sum(cards) > 21:
            cards.remove(11)
            cards.append(1)

        return sum(cards)

def compare(user_score, comp_score):
    if user_score == comp_score:
        return "Draw"
    elif comp_score == 0:
        return "loose, opponent has Blackjack"
    elif user_score == 0:
        return " win with a blackjack"
    elif user_score > 21:
        return "You went over, you loose"
    elif comp_score > 21:
        return "Opponent went over, You Won"
    elif user_score > comp_score:
        return "you win"
    else:
        return " You loose"
    
def play_game():

    user_cards = []
    computer_cards = []
    is_gave_over = False

    for _ in range(2):
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())

    while not is_gave_over:

        user_score = calculate_score(user_cards)
        comp_score = calculate_score(computer_cards)
        print(f" Yours Cards = {user_cards}, Current score = {user_score}")
        print(f" Computer first card : {computer_cards[0] }")

        if user_score == 0 or comp_score == 0 or user_score > 21:
            is_gave_over = True
        else: 
            user_problem = input("y to get another card or n to end it? ")
            if user_problem == "y":
                user_cards.append(deal_cards())
            else: 
                is_gave_over = True

    while comp_score != 0 and comp_score < 17:
        computer_cards.append(deal_cards())
        comp_score = calculate_score(computer_cards)

    print(f" Yours final hand {user_cards} and your score {user_score}")
    print(f" Computer final hands {computer_cards} and score is {comp_score}")
    print(compare(user_score, comp_score))

while input("Do you wanna play another Black jack game y or n") == "y":
    play_game()
