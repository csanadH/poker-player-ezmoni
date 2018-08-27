class Gabi:
    def myFunc(self, game):
        print("GABI")
        try:
            print(game["minimum_raise"])
            for player in game["players"]:
                print(palyer)

            print(game["community_cards"])
        except Exception as ex:
            print("bad gabi " + ex)

    def calcBet(self, game):
        return game["minimum_raise"] + 10