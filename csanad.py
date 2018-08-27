import json

class Csanad:
    def myFunc(self, game_state, hand, cards):
        print("CSANAD START")
        try:
            pot = game_state["pot"]
            min_call = game_state["current_buy_in"] - game_state["players"][game_state["in_action"]]["bet"]
            first_card_rank = hand[0]["rank"]
            second_card_rank = hand[1]["rank"]
            if (len(cards) == 0):
                if (first_card_rank == second_card_rank):
                    print("returning 800")
                    return 800
                elif (first_card_rank in "89TJQKA" or second_card_rank in "89TJQKA"):
                    if (min_call / pot < 0.1):
                        print("returning",min_call)
                        return min_call
                else:
                    print("returning 0")
                    return 0
            else:
                for card in cards:
                    if (first_card_rank == card["rank"] or second_card_rank == card["rank"]):
                        print("returning 800")
                        return 800
                    else:
                        if (min_call / pot < 0.3):
                            print("returning",min_call)
                            return min_call
                        else:
                            return 0
            return 0
        except Exception as ex:
            print("bad csanad")
            print(ex)

if __name__ == '__main__':
    json_data=open("sample.json").read()
    data = json.loads(json_data)
    asd = data["current_buy_in"] - data["players"][data["in_action"]]["bet"]
    print(Csanad().myFunc(data, [{'rank': '3', 'suit': 'hearts'},{'rank': 'K','suit': 'spades'}], []))