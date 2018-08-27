import json

class Csanad:
    def myFunc(self, game_state):
        print("CSANAD")
        try:
            print(game_state["players"][game_state["in_action"]])
            return
        except Exception as ex:
            print("bad csanad")
            print(ex)