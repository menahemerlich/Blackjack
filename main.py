from core.deck import build_standard_deck, shuffle_by_suit

deck = build_standard_deck()
game_desk = shuffle_by_suit(deck)
print(game_desk)
print(len(deck))