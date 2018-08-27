import json
class Gabi:
    def myFunc(self, game, hand, cards):
        print("GABI")
        try:
            print(game["minimum_raise"])
            print(data["current_buy_in"] - data["players"][data["in_action"]]["bet"])
        except Exception as ex:
            print("bad gabi")
            print(ex)

        finally:
            print("GABI END")

    def calcBet(self, game):
        return 1000


    if __name__ == '__main__':
        json_data=open("sample.json").read()
        data = json.loads(json_data)
        asd = data["current_buy_in"] - data["players"][data["in_action"]]["bet"]
        print(asd)
    