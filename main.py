from imaplib import Flags

dealAgain = "y"

def main():
    global dealAgain

    import random
    from art import logo
    print(logo)
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    compCards = []
    playerCards = []

    def dealerDelt():
        for i in range(2):
            card =  random.choice(cards)
            if card == 11 and card + sum(compCards) >21:
                    card = 1
            compCards.append(card)
        while sum(compCards) < 17:
            card = random.choice(cards)
            compCards.append(card)

    dealerDelt()

    def playerDelt():
        for i in range(2):

            card = random.choice(cards)
            if card == 11 and card + sum(playerCards) > 21:# condidtion for when you are delt an ace
                card = 1

            playerCards.append(card)


    playerDelt()
    stopgame = False
    def playerHit():
        card = random.choice(cards)
        playerCards.append(card)
        if sum(playerCards) >21:
            print(f"Your Final hand: {playerCards}, final score: {sum(playerCards)}")
            print(f"Computers final hand: {compCards[0]}")
            print("you went over you lose :(")
        else:
            print(f"Your Cards: {playerCards}, current score: {sum(playerCards)}")
            print(f"Computers first Card: {compCards[0]}")

    def evalaute():

        if sum(playerCards) > sum(compCards):
            print(f"Your Final hand: {playerCards}, final score: {sum(playerCards)}")
            print(f"Computers final hand: {compCards}  final score {sum(compCards)}")
            print("you have more you win")


        elif sum(compCards) > 21:
            print(f"Your Final hand: {playerCards}, final score: {sum(playerCards)}")
            print(f"Computers final hand: {compCards}  final score {sum(compCards)}")
            print("opponent went over you win")
        elif sum( compCards) > sum(playerCards):
            print(f"Your Final hand: {playerCards}, final score: {sum(playerCards)}")
            print(f"Computers final hand: {compCards}  final score {sum(compCards)}")
            print("you lose")
        elif sum(compCards) == sum(playerCards):
            print(f"Your Final hand: {playerCards}, final score: {sum(playerCards)}")
            print(f"Computers final hand: {compCards}  final score {sum(compCards)}")
            print("its a draw")





    print(f"Your Cards: {playerCards}, current score: {sum(playerCards)}")
    print(f"Computers first Card: {compCards[0]}")
    while dealAgain == 'y' and sum(playerCards) <= 21 :
        dealAgain = input("type y to get another card, type n to pass:")

        if dealAgain == "y":
            playerHit()

        elif dealAgain == "n":
            evalaute()


# main()

def playGame():
    play = True
    while play:
        play = input("play a game? of black jack: ")
        if play == 'yes':
            play =True
            main()
        else:
            play = False
            print("GoodBye from Casino de Talha, Have a nice day")

playGame()