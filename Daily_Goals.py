"""
DAILY GOALS
-----------
The purpose of this program is to focus on just one mini-goal or activity at at a time.
The user inputs a list of activities and the programs shows them only one at random. The user can cycle through the list if they want to focus on a different one.
"""
from dataclasses import dataclass


@dataclass
class Goal:
    def __init__(self, title, dealine=None, area=None, difficulty=None):
        self.title = title
        self.dealine = dealine
        self.area = area
        self.difficulty = difficulty

    def is_completed(self, completed=False):
        return "Goal completed" if completed == True else "Goal NOT completed YET"


list_of_goals = []


while True:
    user = input("type 'new' for new goal, 'see' for seeing the list: ")
    if user == "new":
        title = input("inser title: ")
        new_goal = Goal(title=title)
        list_of_goals.append(new_goal)
    elif user == "see":
        for goal in list_of_goals:
            print("-" * 60)
            print(f"-> {goal.title}", end=" -- ")
            print(f"-> {goal.is_completed()}")
        print("-" * 60)
    elif user == "quit":
        print("-- PROGRAM FINISHED --")
        break
