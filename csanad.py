import json

class Csanad:
    def myFunc(self, game_state):
        print("CSANAD")
        try:
            hand = game_state["players"][game_state["in_action"]]["hole_cards"]
            print(hand)
            return
        except Exception as ex:
            print("bad csanad")
            print(ex)