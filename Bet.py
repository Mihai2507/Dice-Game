def bet(player_name, player_money):
    while True:
        try:
            money = int(input(f"{player_name}, how much money do you want to bet?\n"))
            if money <= 0:
                print("Sorry, you can't bet negative or zero money!")
            elif money > player_money:
                print(f"Sorry, you don't have enough money. You currently have ${player_money}.")
            else:
                return money
        except ValueError:
            print("Please enter a valid amount.")