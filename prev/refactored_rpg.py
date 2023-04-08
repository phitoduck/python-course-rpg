import random

PLAYER_ART = """
        O
      / | \\
     /  |  \\
        |
       / \\
"""

DRAGON_ART = """
      /\\_/\\
   VS   ( o.o )
        > ^ <
"""

PLAYER_MAX_HEALTH = 10
DRAGON_MAX_HEALTH = 10
DRAGON_DEFENSE = 0


def play_game(player_health: int, dragon_health: int, dragon_defense: int) -> None:
    while True:
        print(draw_ascii_art(player_art=PLAYER_ART, dragon_art=DRAGON_ART))
        print(
            draw_health_bars(
                player_health=player_health,
                dragon_health=dragon_health,
            )
        )
        print(draw_defense(player_defense=0, dragon_defense=dragon_defense))
        player_move = get_player_move()
        if player_move == "a":
            dragon_health = handle_player_attack(dragon_health=dragon_health)
        elif player_move == "h":
            player_health = handle_player_heal(player_health=player_health)
        else:
            handle_invalid_input()
            continue
        if dragon_health <= 0:
            handle_dragon_defeat()
            break
        dragon_move = random.choice(["a", "d", "d", "d"])
        if dragon_move == "a":
            player_health = handle_dragon_attack(player_health=player_health)
        else:
            dragon_defense = handle_dragon_defend(dragon_defense=dragon_defense)
        if player_health <= 0:
            handle_player_defeat()
            break


def draw_ascii_art(player_art: str, dragon_art: str) -> str:
    """Combine the player and dragon ASCII art into one string."""
    player_lines = player_art.split("\n")
    dragon_lines = dragon_art.split("\n")
    offset = len(player_lines) - len(dragon_lines)
    if offset < 0:
        offset = 0

    combined_art_lines = [
        horizontally_concat_strings(
            player_lines[i] if i < len(player_lines) else " " * len(player_lines[0]),
            " " * 3,
            dragon_lines[i - offset]
            if i >= offset and i < offset + len(dragon_lines)
            else " " * len(dragon_lines[0]),
        )
        for i in range(max(len(player_lines), len(dragon_lines)))
    ]
    return "\n".join(combined_art_lines)


def horizontally_concat_strings(*strings: str) -> str:
    """Concatenates a sequence of strings horizontally."""
    return "".join(strings)


def draw_health_bars(player_health: int, dragon_health: int) -> str:
    """Draw the player and dragon health bars."""
    player_bar = (
        f"Health: {'x' * player_health} {' ' * (PLAYER_MAX_HEALTH - player_health)}"
    )
    dragon_bar = (
        f"Health: {'x' * dragon_health} {' ' * (DRAGON_MAX_HEALTH - dragon_health)}"
    )
    return f"Player HP: {player_bar}   Dragon HP: {dragon_bar}"


def draw_defense(player_defense: int, dragon_defense: int) -> str:
    """Draw the player and dragon defense info."""
    return f"Player Defense: {player_defense}     Dragon Defense: {dragon_defense}"


def get_player_move() -> str:
    """Prompt the player for their move and return it."""
    return input("Enter 'a' to attack or 'h' to heal: ")


def handle_player_attack(dragon_health: int) -> int:
    """Calculate the dragon's new health after the player attacks."""
    print("\nYou hit the dragon!")
    return dragon_health - 1


def handle_player_heal(player_health: int) -> int:
    """Calculate the player's new health after they heal."""
    ha = random.randint(0, 5)
    new_health = min(player_health + ha, PLAYER_MAX_HEALTH)
    print(
        f"\nYou healed {new_health - PLAYER_MAX_HEALTH} HP. Your HP is now {new_health}."
    )
    return new_health


def handle_dragon_attack(player_health: int) -> int:
    """Calculate the player's new health after the dragon attacks."""
    print("\nThe dragon hit you!")
    return player_health - 1


def handle_dragon_defend(dragon_defense: int) -> int:
    """Calculate the dragon's new defense after they defend."""
    print("\nThe dragon raised its defense.")
    return dragon_defense + 1


def handle_invalid_input() -> None:
    """Handle the user inputting an invalid move."""
    print("\nInvalid input. Try again.")


def handle_dragon_defeat() -> None:
    """Handle the player defeating the dragon."""
    print("\nCongratulations! You defeated the dragon!")


def handle_player_defeat() -> None:
    """Handle the dragon defeating the player."""
    print("\nYou were defeated by the dragon!")


if __name__ == "__main__":
    play_game(PLAYER_MAX_HEALTH, DRAGON_MAX_HEALTH, DRAGON_DEFENSE)
