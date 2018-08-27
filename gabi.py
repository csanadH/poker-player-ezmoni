class Gabi:
    def myFunc(self, game):
        print("GABI")
        try:
            print(game["minimum_raise"])
        except:
            print("bad gabi")

    def calcBet(self, game):
        return game["minimum_raise"] + 10