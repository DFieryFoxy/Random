import random

cards = ["Ace", "King", "Queen", "Jack", "Ten"]
def main():
    #random.seed(0)
    print (random.choices(cards, weights=[25,10,35,15,15], k=5))



main()