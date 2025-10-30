from core.deck import build_standard_deck, shuffle_by_suit
from core.game_logi import calculate_hand_value, deal_two_each

deck = build_standard_deck()
game_desk = shuffle_by_suit(deck)
player = {"hand":[]}
dealer = {"hand":[]}
print(game_desk)
print(len(deck))
deal_two_each(deck, player, dealer)