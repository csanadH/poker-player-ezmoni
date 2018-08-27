import json
from pprint import pprint
from gabi import *


class Player:
    VERSION = "Default Python folding player"

    def betRequest(self, game_state):
        try:
            Gabi().myFunc(game_state)
            
            parsedJSON = json.dumps(game_state)

            print("MINIMUM RAISE")
            print(parsedJSON.minimum_raise)

            return 100
        except Exception as ex:
            print(ex)
            return 0

    def showdown(self, game_state):
        pass