class Balint:
    def myFunc(self, game, hand, cards):
        print("Balint")
        try:
            hand = game["players"]["in_action"]
            print("FIRST HAND:")
            print(hand[0])
        except:
            print("We have an exception in class Balint.")

    def calcBet(self, game):
        return game["minimum_raise"] + 20