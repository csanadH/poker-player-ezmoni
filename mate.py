
class Mate:
    def isPair(self, game_state, hand, cards):
        try:
            print(hand[0]["suit"])
            first_card_rank = hand[0]["rank"]
            second_card_rank = hand[1]["rank"]
            if(first_card_rank == second_card_rank):
                return 700
            for card in cards:
                if first_card_rank == second_card_rank == card["rank"]:
                    return 1000
            else: 
                return game_state["current_buy_in"] - game_state["players"][game_state["in_action"]]["bet"]
        except Exception as ex:
            print("bad mate")
            print(ex)
