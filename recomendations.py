def main():
    difficulty = input("Difficult or casual?\n")
    if not (difficulty == "Difficult" or difficulty =="casual"):
        print("Enter a valid difficulty")
        return 
    players = input("Multiplayer or Single-Player?\n")
    if not (players == "Multiplayer" or players =="Single-Player"):
        print("Enter a valid number of players")
        return
    if difficulty == "Difficult" and players == "Multiplayer":
            recommend ("Poker")
    elif difficulty == "Difficult" and players == "Single-Player":
        recommend("Sollitaire")
    elif difficulty == "casual" and players == "Multiplayer":
         recommend("Hearts")
    else:
         recommend("Clock")


def recommend(game):
    print(f"You might like {game}")

main()  