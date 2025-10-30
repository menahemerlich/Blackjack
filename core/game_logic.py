from .player_io import ask_player_action

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
    print(f"sum_player: {calculate_hand_value(player["hand"])}")
    print(f"sum_dealer: {calculate_hand_value(dealer["hand"])}")


def dealer_play(deck: list[dict], dealer: dict) -> bool:
    sum_dealer = calculate_hand_value(dealer["hand"])
    while sum_dealer <= 17:
        card = deck.pop(0)
        dealer["hand"].append(card)
        sum_dealer = calculate_hand_value(dealer["hand"])
        print(f"sum_dealer: {sum_dealer}")
    if sum_dealer > 21:
        print("disqualification!")
        return False
    return True

def run_full_game(deck: list[dict], player: dict, dealer: dict) -> None:
    deal_two_each(deck, player, dealer)
    while True:
        choice = ask_player_action()
        if choice == "H":
            card = deck.pop(0)
            player["hand"].append(card)
            sum_player =  calculate_hand_value(player["hand"])
            print(f"sum_player: {sum_player}")
            if sum_player > 21:
                print("disqualification!")
                break
        else:
            if dealer_play(deck, dealer):
                continue
            else:
                break

    sum_player = calculate_hand_value(player["hand"])
    sum_dealer = calculate_hand_value(dealer["hand"])
    if sum_player > sum_dealer:
        print(f"player is the winer!! sum_player: {sum_player}")
    elif sum_dealer > sum_player:
        print(f"dealer is the winer!! sum_dealer: {sum_dealer}")
    else:
        print("WAR")


