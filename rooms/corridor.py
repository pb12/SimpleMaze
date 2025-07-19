# -----------------------------------------------------------------------------
# File: corridor.py
# ACS School Project 1 - Simple Maze Example
# Organization: THUAS (The Hague University of Applied Sciences)
# Location: Delft
# Date: July 2025
# -----------------------------------------------------------------------------

from .utils import chooseNextRoom

def enterCorridor(state):
    print("\n🚶 You are in the main corridor of the school.")
    print("🏫 Doors lead to various rooms.")
    print("🎒 Inventory:", state["inventory"])

    choices = ["classroom2015", "projectRoom1", "lobby"]
    nextRoom = chooseNextRoom(choices)

    if nextRoom:
        state["previous_room"] = "corridor"
        return nextRoom
    else:
        print("You stay in the corridor.")
        return "corridor"
