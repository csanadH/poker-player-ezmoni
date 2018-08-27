import json
from pprint import pprint
from gabi import *


class Player:
    VERSION = "Default Python folding player"

    def betRequest(self, game_state):
        try:
            Gabi().myFunc(game_state)
            
            stringJSON = json.dumps(game_state)

            parsedJSON = json.loads(stringJSON)
            print("MINIMUM RAISE")
            print(parsedJSON["in_action"]["bet"])

            return 100
        except Exception as ex:
            print(ex)
            return 0

    def showdown(self, game_state):
        pass