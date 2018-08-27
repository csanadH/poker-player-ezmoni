import json

class Player:
    VERSION = "Default Python folding player"

    def betRequest(self, game_state):
        print("PARSED JSON")
        parsed = json.loads(game_state)
        print(parsed)
        return 1

    def showdown(self, game_state):
        pass

