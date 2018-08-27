import json

class Csanad:
    def myFunc(self, stringJSON):
        print("CSANAD")
        try:
            parsed = json.loads(stringJSON)
            hand = parsed["players"][parsed["in_action"]]
            # HAND[0] = first card
            # HAND[1] = second card
            print("FIRST CARD="+hand[0]["rank"]+","+hand[0]["suit"])
            print("SECOND CARD="+hand[1]["rank"]+","+hand[1]["suit"])
        except Exception as ex:
            print("bad csanad " + ex)