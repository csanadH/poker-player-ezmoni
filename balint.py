class Balint:
    def myFunc(self, game):
        print("Balint")
        try:
            print(game["players"])
        except:
            print("We have an exception in class Balint.")

    def calcBet(self, game):
        return game["minimum_raise"] + 20