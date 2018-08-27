import json
from pprint import pprint

class Player:
    VERSION = "Default Python folding player"

    def betRequest(self, game_state):
        print("RAISE")
        players = game_state["in_action"]
        bet = players["bet"]
        print(game_state["current_buy_in"] - bet)
        return game_state["current_buy_in"] - bet  

    def showdown(self, game_state):
        pass

