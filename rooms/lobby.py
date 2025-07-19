# -----------------------------------------------------------------------------
# File: lobby.py
# ACS School Project 1 - Simple Maze Example
# Organization: THUAS (The Hague University of Applied Sciences)
# Location: Delft
# Date: July 2025
# -----------------------------------------------------------------------------

from .utils import chooseNextRoom

def enterLobby(state):
    print("\n🛋️ You are in the lobby of the school.")
    print("📚 Students sometimes gather here to relax.")
    print("🎒 Inventory:", state["inventory"])

    state["previous_room"] = "lobby"

    choices = ["corridor"]
    nextRoom = chooseNextRoom(choices)

    return nextRoom if nextRoom else "lobby"
