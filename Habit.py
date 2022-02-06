from Task import Task
import time

class Habit:
    def __init__(self, habitName, periodicity, h_type):
        self.name = habitName
        self.periodicity = periodicity
        self.type=h_type
        self.Tasks = []
        self.time = time.ctime(time.time())
        self.time_completed = 'Not completed'

    def showTasks(self):
        for t in self.Tasks:
            print()
            print(t)
        for t in self.Tasks:
            print()
            print( "Task  "+ t + " started ...")
            task_state = input(print("Press 1 when finish or 0 if not able to finish"))
        self.time_completed = time.ctime(time.time())
        print()
        print('Congratulations, you finished performing the tasks for  ' + self.name + '!' )
        print()

    def add_Tasks(self):
        number_of_tasks = input(print("Please this habit will have how many tasks?"))
        for x in range(int(number_of_tasks)):
            task_name = input(print("Enter task name"))
            self.Tasks.append(task_name)
            print("tasks " + task_name + 'added !')
