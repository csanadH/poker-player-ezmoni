import json
class Gabi:
    def myFunc(self, game, hand, cards):
        print("GABI")
        try:
            if (hand[0]["rank"] == hand[1]["rank"]):
                print("pair, returning 800")
                return 800
            elif (hand[0]["rank"] in "89TJQKA" and hand[1]["rank"] in "89TJQKA"):
                print("high card, returning 600")
                return 600
            else:
                return game_state["current_buy_in"] - game_state["players"][game_state["in_action"]]["bet"]
                print("nopair")

        except Exception as ex:
            print("bad gabi")
            print(ex)

        finally:
            print("GABI END")

    def calcBet(self, game):
        return 500

    def straight(self, hand, cards):
        allcards = hand + cards
        result = []
        for card in allcards:
            if (card["rank"] == "J"):
                card["rank"] = 11
            elif (card["rank"] == "Q"):
                card["rank"] = 12
            elif (card["rank"] == "K"):
                card["rank"] = 13
            elif (card["rank"] == "A"):
                card["rank"] = 14
            else:
                card["rank"] = int(card["rank"])
            result.append(card["rank"])
        result.sort()
        j = 0
        for i in range(0, len(result) - 1):
            if (result[i] + 1 == result[i + 1]):
                j+=1
        if (j > 3):
            return True
        else:
            return False


if __name__ == '__main__':
    json_data=open("sample.json").read()
    data = json.loads(json_data)
    asd = data["current_buy_in"] - data["players"][data["in_action"]]["bet"]
    print(Gabi().myFunc(data, "" ,""))
    