import json
from pprint import pprint

class Player:
    VERSION = "Default Python folding player"

    def betRequest(self, game_state):
        print("PARSED JSON")
        parsedJson = json.load(game_state)
        pprint(parsedJson)
        return 1

    def showdown(self, game_state):
        pass

