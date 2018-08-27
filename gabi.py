class Gabi:
    def myFunc(self, game):
        print("GABI")
        try:
            print(game["minimum_raise"])
            for player in game["players"]:
                print(palyer)

            print(game["community_cards"])
        except:
            print("bad gabi")

    def calcBet(self, game):
        return game["minimum_raise"] + 10