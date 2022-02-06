import unittest
from User import User
from Habit import Habit

class TestUser(unittest.TestCase):
    def test_add_twonumbers(self):
        expected = 10
        result = User.add_twonumbers(self, 2, 8)
        self.assertEqual(result, expected)

    def test_add_daily_Habit(self):
        habit = Habit("dinging", 2, "daily")
        user = User("chioma")
        expected = "daily habit created!"
        result = user.addHabit(habit)
        self.assertEqual(result, expected)

    def test_add_weekly_Habit(self):
        habit = Habit("dinging", 2, "weekly")
        user = User("chioma")
        expected = 'weekly habit created!'
        result = user.addHabit(habit)
        self.assertEqual(result, expected)

    def test_create_user(self):
        user = User("chioma")
        expected = "chioma"
        self.assertEqual(user.name, expected)

    def test_create_Habit_sets_correct_habitName(self):
        habit = Habit("drinking", 2, "daily")
        self.assertEqual(habit.name, 'drinking')

    def test_create_Habit_sets_correct_habittype(self):
        habit = Habit("drinking", 2, "daily")
        self.assertEqual(habit.type, 'daily')

    def test_create_Habit_sets_correct_habit_periodicity(self):
        habit = Habit("drinking", 2, "daily")
        self.assertEqual(habit.periodicity, 2)



if __name__ == '__main__':
    unittest.main()
