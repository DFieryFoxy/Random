def get_guess():
    guess = input("Enter a guess:\n")
    return guess


def main():
    guess = get_guess()
    if guess == "fifity":
        print("Correct!")
    else:
        print("Incorrect!")

main ()