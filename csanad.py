import json

class Csanad:
    def myFunc(self, game_state, hand, cards):
        print("CSANAD START")
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
            print("CSANAD END")
            return
        except Exception as ex:
            print("bad csanad")
            print(ex)