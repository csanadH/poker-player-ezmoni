import json

class Csanad:
    def myFunc(self, game_state):
        print("CSANAD")
        try:

            print(game_state["players"].__class__)
            return
            hand = game_state["players"][game_state["in_action"]]
            print(game_state["players"][game_state["in_action"]])
            print("FIRST CARD=",hand[0]["rank"],",",hand[0]["suit"])
            print("SECOND CARD=",hand[1]["rank"],",",hand[1]["suit"])
        except Exception as ex:
            print("bad csanad")
            print(ex)