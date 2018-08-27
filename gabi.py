class Gabi:
    def myFunc(self, game):
        print("GABI")
        try:
            print(game["minimum_raise"])
            print(game["in_action"]["hole_cards"])

            print(game["community_cards"])
        except Exception as ex:
            print("bad gabi")
            print(ex)

        finally:
            print("GABI END")

    def calcBet(self, game):
        return game["minimum_raise"] + 10


    if __name__ == '__main__':
        print("gabi")