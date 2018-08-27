import json
from pprint import pprint

class Player:
    VERSION = "Default Python folding player"

    def betRequest(self, game_state):
        print(game_state["pot"])        
        return 1

    def showdown(self, game_state):
        pass

