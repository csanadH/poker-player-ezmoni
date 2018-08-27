class Balint:
    def myFunc(self, game, hand, cards):
        print("Balint")
        try:
            print(hand)
            print(cards)
            return 1000
        except:
            print("We have an exception in class Balint.")
            return 0
