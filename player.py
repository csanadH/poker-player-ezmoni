import json
from pprint import pprint

class Player:
    VERSION = "Default Python folding player"

    def betRequest(self, game_state):
        print("RAISE")
        players = game_state["in_action"]
        print(players)
        print(game_state["community_cards"])
        return 100

    def showdown(self, game_state):
        pass

