import json
from pprint import pprint

class Player:
    VERSION = "Default Python folding player"

    def betRequest(self, game_state):
        print("RAISE")
        players = game_state["in_action"]
        print(players)
        bet = players["bet"]
        print(bet)
        print(game_state["community-cards"])
        print(game_state["current_buy_in"] - bet)
        return 100

    def showdown(self, game_state):
        pass

