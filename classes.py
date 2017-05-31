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

    def start_task(self, task):
        if self.current_task != None and self.current_task.status == "in progress":
            self.current_task.status == "todo"
        self.current_task = task
        self.current_task.status == "in progress"

    def work(self):
        if (self.current_task == None or self.current_task.status == "done") and len(self.tasks) > 0:
            tasks = [task for task in self.tasks if not task.is_blocked and not task.status == "done"]
            tasks.sort(key=lambda x: x.priority)
            self.start_task(tasks[0])
        if self.current_task != None and self.current_task.status == "in progress":
            print("should work")
            self.progress_task()

    def progress_task(self):
        print(current_task)
        print("---")
        multiplier = 1
        if random.randrange(0, 10) > self.luck:
            multiplier *= -1
        self.current_task.change_progress(self.productivity * multiplier)
        print(current_task)

class Requirement(object):
    def __init__(self, tasks):
        self.tasks = tasks
        self.fulfilled = False

    def add(self, tasks):
        for task in tasks:
            if task not in self.tasks:
                self.tasks.append(task)

    def check(self):
        for task in self.tasks:
            if task.status != "done":
                return False
        self.fulfilled = True
        return self.fulfilled

class Task(object):
    def __init__(self, name, priority, max_progress, requirement=None):
        self.name = name
        self.status = "todo"
        self.progress = 0
        self.priority = priority
        self.max_progress = max_progress
        self.requirement = requirement

    @property
    def is_blocked(self):
        return not self.requirement.check()

    def change_progress(self, amount):
        self.progress = max(min(self.progress + amount, self.max_progress), 0)
        if self.progress >= self.max_progress:
            self.status = "done"

    def __str__(self):
        mystr = self.name + ": " + self.status + " " + str(self.progress) + "/" + str(self.max_progress)
        mystr += ", blocked: " + str(self.is_blocked)
        if self.requirement != None and len(self.requirement.tasks) > 0:
            mystr += ", blocked by: ["
            for task in self.requirement.tasks:
                mystr += " " + task.name
            mystr += "]"
        return mystr

class Feature(Task):
    def __init__(self, name, priority, max_progress, task_max_progress, max_length):
        Task.__init__(self, name, priority, max_progress)
        self.tasks = []
        self.generate_tasks(task_max_progress, max_length)

    def generate_tasks(self, task_max_progress, max_length):
        task_max_progresses = []
        progress_left = self.max_progress
        task_max_progresses.append(task_max_progress)
        progress_left -= task_max_progress
        while progress_left > 0:
            task_progress = min(random.randint(1, progress_left), task_max_progress)
            task_max_progresses.append(task_progress)
            progress_left -= task_progress

        lines = []
        starting_positions = []
        tasks_count = len(task_max_progresses)
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
                starting_position = random.randrange(0, max_length - length)
            except ValueError:
                starting_position = 0
            starting_positions.append(starting_position)
        count = 1
        for line in lines:
            for i in range(len(line)):
                task_progress = random.choice(task_max_progresses)
                task_max_progresses.remove(task_progress)
                requirement = Requirement([])
                if i > 0:
                    requirement.add([line[i-1]])
                line[i] = Task("Task " + str(count), 1, task_progress, requirement)
                count += 1
        real_positions = []
        for i in range(len(lines)):
            real_positions.append([])
            start_pos = starting_positions[i]
            for j in range(len(lines[i])):
                real_positions[i].append(start_pos + j)

        for i in range(len(lines)):
            for j in range(len(lines[i])):
                if real_positions[i][j] > 0:
                    additional_tasks_by_chances = {0.10: 2, 0.35: 1, 1.0: 0}
                    if j == 0:
                        additional_tasks_by_chances = {1.0: 1}
                    dice_roll = random.random()
                    for chance in sorted(additional_tasks_by_chances.keys()):
                        if dice_roll <= chance:
                            additional_tasks = additional_tasks_by_chances[chance]
                            break
                    for d in range(additional_tasks):
                        line_indices = []
                        for k in range(len(starting_positions)):
                            if starting_positions[k] < real_positions[i][j]:
                                line_indices.append(k)
                        random_index = random.choice(line_indices)
                        random_line = lines[random_index]
                        valid_tasks = []
                        for k in range(len(real_positions[random_index])):
                            if real_positions[random_index][k] < real_positions[i][j]:
                                valid_tasks.append(random_line[k])
                        blocker = random.choice(valid_tasks)
                        lines[i][j].requirement.add([blocker])

        for line in lines:
            for task in line:
                self.tasks.append(task)

ft = Feature("f1", 1, 63, 10, 4)
dave = Developer("dave", (0, 6), 10, 7)
for task in ft.tasks:
    dave.take_task(task)

for i in range(10):
    dave.work()
