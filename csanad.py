import json

class Csanad:
    def myFunc(self, stringJSON):
        print("CSANAD")
        try:
            parsed = json.loads(stringJSON)
            print(parsed["in_action"])
            print("IN_ACTION")
            print(parsed["players"]["in_action"])
        except:
            print("bad csanad")