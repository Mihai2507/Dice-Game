from Roll import roll_dice
from Bet import bet


def play():
    name1 = input("Player 1's name:\n")
    name2 = input("Player 2's name:\n")
    print(f"Welcome to ~~DICE-GAME~~, {name1} and {name2}!\n")

    money1 = 100
    money2 = 100

    while True:
        choice = input(f"Would you like to start first, {name1}? (y/n) ").lower()
        if choice in ('y', 'n'):
            break
        else:
            print("Please enter 'y' or 'n'.")

    while True:
        print(f"{name1} has ${money1}. {name2} has ${money2}.")

        bet1 = bet(name1, money1)
        bet2 = bet(name2, money2)

        if choice == 'y':
            player1_roll1 = roll_dice()
            player1_roll2 = roll_dice()
            player2_roll1 = roll_dice()
            player2_roll2 = roll_dice()
        else:
            player2_roll1 = roll_dice()
            player2_roll2 = roll_dice()
            player1_roll1 = roll_dice()
            player1_roll2 = roll_dice()

        print(f"{name1} rolled: {player1_roll1} - {player1_roll2}")
        print(f"{name2} rolled: {player2_roll1} - {player2_roll2}")

        is_player1_double = player1_roll1 == player1_roll2
        is_player2_double = player2_roll1 == player2_roll2

        if is_player1_double and not is_player2_double:
            print(f"{name1} wins with a double!")
            money1 += bet1
            money2 -= bet2
        elif not is_player1_double and is_player2_double:
            print(f"{name2} wins with a double!")
            money1 -= bet1
            money2 += bet2
        else:
            if is_player1_double:
                total1 = (player1_roll1 + player1_roll2) ** 2
            else:
                total1 = player1_roll1 + player1_roll2

            if is_player2_double:
                total2 = (player2_roll1 + player2_roll2) ** 2
            else:
                total2 = player2_roll1 + player2_roll2

            if total1 > total2:
                print(f"{name1} wins!")
                money1 += bet1
                money2 -= bet2
            elif total1 < total2:
                print(f"{name2} wins!")
                money1 -= bet1
                money2 += bet2
            else:
                print("It's a tie!")

        print(f"{name1} now has ${money1}.\n{name2} now has ${money2}.")

        if money1 <= 0:
            print(f"{name1} is out of money.\n{name2} wins the game!")
            break
        if money2 <= 0:
            print(f"{name2} is out of money.\n{name1} wins the game!")
            break

        play_again = input("Do you want to play again? (y/n) ").lower()
        if play_again != 'y':
            break
