import json

class Csanad:
    def myFunc(self, stringJSON):
        print("CSANAD")
        try:
            parsed = json.loads(stringJSON)
            print(parsed["in_action"])
        except:
            print("bad csanad")