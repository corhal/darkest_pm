import random

class Developer(object):
    def __init__(self, name, productivity, stress, luck):
        self.name = name
        self.productivity = productivity
        self.stress = stress
        self.luck = luck
        self.current_task = None
        self.tasks = []

    def change_parameter(self, parameter_name, value):
        self.__setattr__(parameter_name, value)

    def take_task(self, task):
        self.tasks.append(task)

    def start_task(task):
        if self.current_task != None and self.current_task.status == "in progress":
            self.current_task.status == "todo"
            self.current_task = task
            self.current_task.status == "in progress"

    def work(self):
        if (self.current_task == None or self.current_task.status = "done") and len(self.tasks > 0):
            self.tasks.sort(key=lambda x: x.priority)
            self.start_task(self.tasks[0])
        if self.current_task != None and self.current_task.status == "in progress":
            self.progress_task()

    def progress_task(self):
        multiplier = 1
        if random.randrange(0, 10) > self.luck:
            multiplier *= -1
        self.current_task.change_progress += self.productivity * multiplier

class Task(object):
    def __init__(self, name, priority, max_progress):
        self.name = name
        self.status = "todo"
        self.progress = 0
        self.priority = priority
        self.max_progress = max_progress

    def change_progress(self, amount):
        self.progress += amount
        if self.progress >= self.max_progress:
            self.status = "done"

dev = Developer("Bucky", 3, 0, 8)
dev.change_parameter("stress", 1)
