import json

class Csanad:
    def myFunc(self, game_state, hand, cards):
        print("CSANAD START")
        try:
            if (hand[0]["rank"] == hand[1]["rank"]):
                print("pair")
            else:
                print("nopair")
            print("CSANAD END")
            return
        except Exception as ex:
            print("bad csanad")
            print(ex)