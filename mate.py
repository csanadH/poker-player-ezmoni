
class Mate:
    def isPair(self, game_state):
        hand = game_state["players"][game_state["in_action"]]
        first_card_suit = hand[0]["suit"]
        first_card_rank = hand[0]["rank"]
        second_card_suit = hand[1]["suit"]
        second_card_rank = hand[1]["rank"]
        print("pair")
        print(first_card_rank)
        print(second_card_rank)
        if(first_card_rank == second_card_rank):
            return game_state["minimum_raise"] + 100
        else: 
            return 0
