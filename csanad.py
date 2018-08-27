import json

class Csanad:
    def myFunc(self, stringJSON):
        print("CSANAD")
        try:
            parsed = json.loads(stringJSON)
            print(parsed["in_action"])
            print("IN_ACTION")
            print(parsed["players"])
        except Exception as ex:
            print("bad csanad " + ex)