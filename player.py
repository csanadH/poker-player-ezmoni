import json
from pprint import pprint

class Player:
    VERSION = "Default Python folding player"

    def betRequest(self, game_state):
        print("RAISE")
        print(game_state["current_buy_in"] - game_state["players[in_action][bet]"] + game_state["minimum_raise"]  )
        return game_state["current_buy_in"] - game_state["players[in_action][bet]"] + game_state["minimum_raise"]     

    def showdown(self, game_state):
        pass

