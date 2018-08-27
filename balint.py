class Balint:
    def myFunc(self, game):
        print("Balint")
        try:
            hand = game["players"][game["in_action"]]
            print("First hand: " + hand[0])
        except:
            print("We have an exception in class Balint.")

    def calcBet(self, game):
        return game["minimum_raise"] + 20