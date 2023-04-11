import random

ph = 10
dh = 10
mh = 10
dd = 0

player_art = """
        O
      / | \\
     /  |  \\
        |
       / \\
"""

dragon_art = """
      /\\_/\\
   VS   ( o.o )
        > ^ <
"""

combined_art = ""

player_lines = player_art.split("\n")
dragon_lines = dragon_art.split("\n")

# calculate the offset for the dragon's lines
offset = len(player_lines) - len(dragon_lines)
if offset < 0:
    offset = 0

# horizontally concatenate the player art and dragon art
for i in range(max(len(player_lines), len(dragon_lines))):
    if i < len(player_lines):
        combined_art += player_lines[i]
    else:
        combined_art += " " * len(player_lines[0])
    combined_art += " " * 3  # add some padding between the two ASCII art
    if i >= offset and i < offset + len(dragon_lines):
        combined_art += dragon_lines[i - offset]
    else:
        combined_art += " " * len(dragon_lines[0])
    combined_art += "\n"

while True:
    ph_bar = "Health: " + "x" * ph + " " * (mh - ph)
    dh_bar = "Health: " + "x" * dh + " " * (mh - dh)
    pa = "         /|\\       \n         ( )       \n         / \\       \n        /   \\      \n       /     \\     \n      /       \\    \n     /         \\   \n    /           \\  \n   /             \\ \n  /               \\"
    da = "      _,=''=,_   \n     /         \\  \n    |  /\\_/\\  |  \n    |  |  |  |  \n  __\\|  |  |/__\n /`    \\  \\    `\\\n/       \\_/     \\\n|                  |\n|                  |\n \\                /\n  \\  /\\    /\\  /\n   \\/  \\  /  \\/\n        \\/"
    print(combined_art)
    print(f"Player HP: {ph_bar}   Dragon HP: {dh_bar}")
    print(f"Player Defense: {0}     Dragon Defense: {dd}")
    pm = input("Enter 'a' to attack or 'h' to heal: ")
    if pm == "a":
        dh -= 1
        print("\nYou hit the dragon!")
    elif pm == "h":
        ha = random.randint(0, 5)
        ph = min(ph + ha, mh)
        print(f"\nYou healed {ha} HP. Your HP is now {ph}.")
    else:
        print("\nInvalid input. Try again.")
        continue
    if dh <= 0:
        print("\nCongratulations! You defeated the dragon!")
        break
    dm = random.choice(["a", "d", "d", "d"])
    if dm == "a":
        ph -= 1
        print("\nThe dragon hit you!")
    else:
        dd += 1
        print("\nThe dragon raised its defense.")
    if ph <= 0:
        print("\nYou were defeated by the dragon!")
        break
