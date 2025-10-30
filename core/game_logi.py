
def calculate_hand_value(hand: list[dict]) -> int:
    sum_hand = 0
    for i in hand:
        if i["rank"] == "A":
            sum_hand += 1
        elif i["rank"] == "J" or i["rank"] == "Q" or i["rank"] == "K":
            sum_hand += 10
        else:
            sum_hand += int(i["rank"])
    return sum_hand



def deal_two_each(deck: list[dict], player: dict, dealer: dict) -> None:
    for i in range(2):
        card = deck.pop(0)
        player["hand"].append(card)

    for i in range(2):
        card = deck.pop(0)
        dealer["hand"].append(card)
    print(calculate_hand_value(player["hand"]))
    print(calculate_hand_value(dealer["hand"]))


def dealer_play(deck: list[dict], dealer: dict) -> bool:
    while dealer["hand"] <= 17:
        card = deck.pop(0)
        dealer["hand"].append(card)
        if dealer["hand"] > 21:
            print("disqualification!")
            return False
    return True

