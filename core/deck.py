import random

def build_standard_deck() -> list[dict]:
    deck = []
    card = {}
    while len(deck) < 52:
        suite = ["H", "C", "D", "S"]
        rank = ["A", "2", "3", "4", "5", "6", "7", "8", "9","10", "J", "Q", "K"]
        for i in range(len(suite)):
            for j in range(len(rank)):
                card["suite"] = suite[i]
                card["rank"] = rank[j]
                deck.append(card)
                card = {}
    return deck


def shuffle_by_suit(deck: list[dict], swaps: int = 5000) -> list[dict]:
    count = 0
    i = 0
    j = 0
    while count < 5000:
        i = random.randint(0, 51)
        while i == j:
            j = random.randint(0, 51)
            if deck[i]["suite"] == "H" and j % 5 != 0:
                continue
            elif deck[i]["suite"] == "C" and j % 3 != 0:
                continue
            elif deck[i]["suite"] == "D" and j % 2 != 0:
                continue
            elif deck[i]["suite"] == "S" and j % 7 != 0:
                continue
        deck[i], deck[j] = deck[j], deck[i]
        count += 1
    return deck



