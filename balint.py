import json

class Balint:
    def myFunc(self, game, hand, cards):
        print("Balint")
        try:
            print(hand)
            print(cards)
        except:
            print("We have an exception in class Balint.")

    def calcBet(self, game):
        return game["minimum_raise"] + 20

    if __name__ == '__main__':
        json_data=open("sample.json").read()
        data = json.loads(json_data)
        hole_cards = data["players"][data["in_action"]]["hole_cards"]
        print(hole_cards)
    