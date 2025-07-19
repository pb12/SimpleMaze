
# -----------------------------------------------------------------------------
# File: projectroom3.py
# ACS School Project - Simple Maze Example
# Organization: THUAS (The Hague University of Applied Sciences)
# Location: Delft
# Date: July 2025
# -----------------------------------------------------------------------------

from .utils import chooseNextRoom

def enterProjectRoom3(state):
    if not state["visited"]["projectRoom3"]:
        if "key" not in state["inventory"]:
            print("\n🚪 The door to Project Room 3 is locked.")
            print("🔐 You need a key to enter. Maybe it's hidden in another room?")
            return "corridor"
        else:
            print("\n🗝️ You unlock the door using the key you found earlier.")

    print("\n🗣️ You are in Project Room 3.")
    print("🎓 A group of students are having a discussion about their lunch after the project work.")
    print("🎒 Inventory:", state["inventory"])

    if state["visited"]["projectRoom3"]:
        print("📌 You've already completed this room.")
        state["previous_room"] = "projectRoom3"
    else:
        answer = input("Guess a fruit they all like most: ").strip().lower()

        if answer == "apple":
            print("✅ Correct!")
            state["visited"]["projectRoom3"] = True
            state["previous_room"] = "projectRoom3"

            print("\n🎉 CONGRATULATIONS!")
            print("✅ You have successfully explored all the essential rooms of the school.")
            print("\n🏆🏆🏆🏆🏆🏆🏆 You completed the game! 🏆🏆🏆🏆🏆🏆🏆\n")
            exit(0)
        else:
            print("❌ Wrong. Returning to corridor.")
            return "corridor"

    choices = ["corridor"]
    nextRoom = chooseNextRoom(choices)
    return nextRoom if nextRoom else "projectRoom3"
