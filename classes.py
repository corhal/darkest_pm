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
        if (self.current_task == None or self.current_task.status == "done") and len(self.tasks > 0):
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

class Feature(Task):
    def __init__(self, name, priority, max_progress):
        Task.__init__(self, name, priority, max_progress)
        self.tasks = []
        self.generate_tasks()

    def generate_tasks(self):
        task_max_progresses = []
        progress_left = self.max_progress
        task_max_progress = random.randint(progress_left // 8, progress_left // 5)
        task_max_progresses.append(task_max_progress)
        progress_left -= task_max_progress
        while progress_left > 0:
            task_progress = min(random.randint(1, progress_left), task_max_progress)
            task_max_progresses.append(task_progress)
            progress_left -= task_progress

        lines = []
        starting_positions = []
        tasks_count = len(task_max_progresses)
        max_length = random.randint(tasks_count // 3, tasks_count // 2)
        tasks_count -= max_length
        line = [0] * max_length
        lines.append(line)
        starting_position = 0
        starting_positions.append(starting_position)
        while tasks_count > 0:
            length = min(random.randint(1, tasks_count), max_length)
            line = [0] * length
            lines.append(line)
            tasks_count -= length
            try:
                print(max_length - length)
                starting_position = random.randrange(0, max_length - length)
            except ValueError:
                starting_position = 0
            starting_positions.append(starting_position)

        for line in lines:
            for i in range(len(line)):
                task_progress = random.choice(task_max_progresses)
                task_max_progresses.remove(task_progress)
                line[i] = task_progress

        print("Max progress:" + str(self.max_progress))
        print(lines)
        print(starting_positions)


ft = Feature("f1", 1, 63)
