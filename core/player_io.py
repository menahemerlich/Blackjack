
def ask_player_action() -> str:
    choice = input("Enter your choice: ")
    options = ["S", "H"]
    while choice not in options:
        choice = input("Enter your choice: ")
    return choice

