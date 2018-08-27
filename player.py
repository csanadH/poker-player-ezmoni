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
            hand = game_state["players"][game_state["in_action"]]["hole_cards"]
            print("player.py")
            if not cards:
                print("csanad")
                return Csanad().myFunc(game_state, hand, cards)
            elif (len(cards) == 3):
                print("mate")
                return Mate().isPair(game_state, hand, cards)
            elif (len(cards) == 4):
                Balint().myFunc(game_state, hand, cards)
            else:
                Gabi().myFunc(game_state, hand, cards)
            return Gabi().calcBet(game_state)
        except Exception as ex:
            print(ex)
            return 0

    def showdown(self, game_state):
        pass