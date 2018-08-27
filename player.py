import json
from pprint import pprint
from gabi import *


class Player:
    VERSION = "Default Python folding player"

    def betRequest(self, game_state):
        try:
            Gabi().myFunc(game_state)
            print("RAISE")
            players = game_state["in_action"]
            print(players)
            print(game_state["community_cards"])
            print(players["hole_cards"])
            return 100
        except Exception as ex:
            print(ex)
            return 0

    def showdown(self, game_state):
        pass