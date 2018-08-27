import json
from pprint import pprint
from gabi import *


class Player:
    VERSION = "Default Python folding player"

    def betRequest(self, game_state):
        Gabi.myFunc()
        print("RAISE")
        players = game_state["in_action"]
        print(players)
        print(game_state["community_cards"])
        self.checkHand(game_state)
        return 100

    def showdown(self, game_state):
        pass


    def checkHand(game_state):
        print(players["in_action"]["hole_cards"])

