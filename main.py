# -----------------------------------------------------------------------------
# File: main.py
# ACS School Project - Simple Maze Example
# Organization: THUAS (The Hague University of Applied Sciences)
# Location: Delft
# Date: July 2025
# -----------------------------------------------------------------------------

from rooms import enterCorridor, enterLobby, enterClassroom2015, enterProjectRoom3

print("🎓 Welcome to the School Maze!")
print("🏫 Your goal is to explore all important rooms in the school.")
print("🔑 You may need to solve challenges to collect items and unlock rooms.")
print("🎯 Once you've visited all rooms, you win!")

state = {
    "current_room": "corridor",
    "previous_room": "corridor",
    "visited": {
        "classroom2015": False,
        "projectRoom3": False
    },
    "inventory": []
}

while True:
    current = state["current_room"]

    if current == "corridor":
        state["current_room"] = enterCorridor(state)

    elif current == "lobby":
        state["current_room"] = enterLobby(state)

    elif current == "classroom2015":
        state["current_room"] = enterClassroom2015(state)

    elif current == "projectRoom3":
        state["current_room"] = enterProjectRoom3(state)

    else:
        print("Unknown room. Exiting game.")
        break
