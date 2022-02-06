from Habit import Habit
import json

class User:
    def __init__(self, name):
        self.name = name
        self.daily_habits = [ Habit("Gaming", 3, 'daily'), Habit("Sweeming", 1, 'daily')]
        self.weekly_habits = [Habit("Go to church", 1, 'weekly'), Habit("Shoping", 1, 'weekly')]

    def addHabit(self, habit):
        if(habit.type == 'daily'):
            self.daily_habits.append(habit)
            return "daily habit created!"
        else:
            self.weekly_habits.append(habit)
            return 'weekly habit created!'

    def create_Habit(self, habitname, periodicity, habtype):
        h = Habit(habitname, periodicity, habtype)
        h.add_Tasks()
        self.addHabit(h)

    def show_daily_habits(self):
        print("Your daily habits are :\n")
        for h in self.daily_habits:
            print(f"Habit Name :{h.name} \nperiodicity: {h.periodicity} \ntime created: {h.time}\nCompleted time: {h.time_completed}\n")

    def show_weekly_habits(self):
        print("Your weekly habits are :\n")
        for h in self.weekly_habits:
            print(f"Habit Name :{h.name} \nperiodicity: {h.periodicity} \ntime created: {h.time}\nCompleted time: {h.time_completed}\n")

    def remove_daily_habit(self, name):
        for habit in self.daily_habits[:]:
            if habit.name == name:
                self.daily_habits.remove(habit)
                print(f"you removed {name}!")
                print()

    def remove_weekly_habit(self, name):
        for habit in self.weekly_habits[:]:
            if habit.name == name:
                self.weekly_habits.remove(habit)
                print(f"you removed {name}!")
                print()

    def save_daily_habits(self):
        with open('DailyHabits.json', 'w') as f:
            for h in self.daily_habits:
                f.write("Name :" + h.name +  "  Created Time: " + h.time  + " Periodicity: " + str(h.periodicity) + " Time completed " + h.time_completed + "\n")
        print('data save successfully!')

    def save_weekly_habits(self):
        with open('WeeklyHabits.json', 'w') as f:
            for h in self.weekly_habits:
                f.write("Name :" + h.name +  "  Created Time: " + h.time  + " Periodicity: " + str(h.periodicity) + " Time completed " + h.time_completed + "\n")
        print('data save successfully!')

    def read_daily_habits(self):
        with open('DailyHabits.json', 'r') as f:
            f_conten = f.read()
            print(f_conten)

    def read_weekly_habits(self):
        with open('WeeklyHabits.json', 'r') as f:
            f_conten = f.read()
            print(f_conten)

    def perform_daily_habit_tasks(self, habit_name):
        for h in self.daily_habits:
            if(h.name == habit_name):
                h.showTasks()

    def perform_weekly_habit_tasks(self, habit_name):
        for h in self.weekly_habits:
            if(h.name == habit_name):
                h.showTasks()


    def add_twonumbers(self, firstnumber, secondnumber):
        return firstnumber + secondnumber
