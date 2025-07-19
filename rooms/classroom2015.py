# -----------------------------------------------------------------------------
# File: classroom2015.py
# ACS School Project - Simple Maze Example
# Organization: THUAS (The Hague University of Applied Sciences)
# Location: Delft
# Date: July 2025
# -----------------------------------------------------------------------------

from .utils import chooseNextRoom

def enterClassroom2015(state):
    print("\n🏫 You are in Classroom 2.015.")
    print("🧮 This is where math is taught. You see formulas written on the board.")
    print("🎒 Inventory:", state["inventory"])

    if state["visited"]["classroom2015"]:
        print("📌 You've already completed this room.")
        state["previous_room"] = "classroom2015"
    else:
        answer = input("What is 7 * 6? ")

        if answer.strip() == "42":
            print("✅ Correct!")
            state["visited"]["classroom2015"] = True

            if "key" not in state["inventory"]:
                print("🔑 You found a key under a calculator and added it to your inventory.")
                state["inventory"].append("key")

            state["previous_room"] = "classroom2015"
        else:
            print("❌ Wrong. Returning to corridor.")
            return "corridor"

    choices = ["corridor"]
    nextRoom = chooseNextRoom(choices)

    return nextRoom if nextRoom else "classroom2015"
