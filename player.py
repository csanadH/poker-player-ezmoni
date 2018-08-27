import json
from pprint import pprint
from gabi import *
from csanad import *
from balint import *
from mate import *


class Player:
    VERSION = "Default Python folding player"

    def betRequest(self, game_state):
        try:
            cards = game_state["community_cards"]
            if not cards:
                Csanad().myFunc(game_state)
            Gabi().myFunc(game_state)
            Balint().myFunc(game_state)
            print("Mate")
            Mate().isPair(game_state)
            return Gabi().calcBet(game_state)
        except Exception as ex:
            print(ex)
            return 0

    def showdown(self, game_state):
        pass