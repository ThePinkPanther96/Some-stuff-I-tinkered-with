from datetime import datetime
from dateutil import parser as date_parser


class Task:
    name: str
    description: str
    due_date: str
    status: str
    id: int
    creation_date: datetime

    id_index = 0 
    
    def __init__(self, name, description, due_date):
        self.name = name
        self.due_date = due_date
        self.status = "Backlog"
        
        if len(description) > 50:
            raise ValueError("Description must be 50 characters or fewer.")
        self.description = description
        
        self.creation_date = datetime.now()
        self.formatted_date = self.creation_date.strftime("%d-%m-%Y")
        
        Task.id_index += 1
        self.id = Task.id_index

    def __str__(self):
        return f"""Task ID: {self.id}
        Created on: {self.formatted_date}
        Task name: {self.name}
        Description: {self.description}
        Completion status: {self.status} 
        Due date: {self.due_date}"""

    def check_status(self):
        due_date_dt = date_parser.parse(self.due_date)
        current_date = datetime.now()
        
        if self.status == "Backlog" and current_date < due_date_dt:
            self.status = "In Progress"
        elif current_date >= due_date_dt:
            self.status = "Done or overdue"
        else:
            self.status = "Done"
        
        return self.status
    

class TodoList:
    owner: str
    department: str

    def __init__(self, owner, department):
        self.owner = owner
        self.department = department
        self.todo = []

    def __str__(self):
        return f"To-Do list owner: {self.owner} Department: {self.department}"
    
    def get_tasks_by_status(self, status):
        return [task for task in self.todo if task.status == status]
    
    def get_smallest_duration_task(self):
        if not self.todo:
            return None
        return min(self.todo, key=lambda task: date_parser.parse(task.due_date) - datetime.now())

    def get_biggest_duration_task(self):
        if not self.todo:
            return None
        return max(self.todo, key=lambda task: date_parser.parse(task.due_date) - datetime.now())

    def add_task(self, task):
        if not isinstance(task, Task):
            raise ValueError("Must add an instance of Task")
        self.todo.append(task)

    def check_progress(self):
        for task in self.todo:
            task.check_status()

    def task_count(self):
        return len(self.todo)

    def compare_task_counts(*todo_lists):
        if not todo_lists:
            return "No todo lists provided."
        
        max_tasks_list = max(todo_lists, key=lambda t: t.task_count())
        min_tasks_list = min(todo_lists, key=lambda t: t.task_count())
        
        max_tasks_count = max_tasks_list.task_count()
        min_tasks_count = min_tasks_list.task_count()
        
        return (f"{max_tasks_list.owner} has the most tasks with {max_tasks_count} tasks.",
                f"{min_tasks_list.owner} has the least tasks with {min_tasks_count} tasks.")

    def print_tasks(self):
        self.check_progress()
        for task in self.todo:
            print(task)

    def print_tasks_by_status(self):
            statuses = ["Backlog", "In Progress", "Done or overdue"]
            for status in statuses:
                print(f"\n{status} Tasks:")
                tasks = self.get_tasks_by_status(status)
                for task in tasks:
                    print(task)
    
    def print_smallest_duaration_task(self):
        smallest_duration_task = self.get_smallest_duration_task()
        print("\nTask with the shortest time left:")
        print(smallest_duration_task)

    def print_biggest_duaration_task(self):
        longest_duration_task = self.get_biggest_duration_task()
        print("\nTask with the longest time left:")
        print(longest_duration_task)






# Add tasks
# Second person with 3 tasks
dolist1 = TodoList("Yossi", "Fullstack")
dolist1.add_task(Task("Bugs", "Alot of bugs, Jesus Christ", "24.9.2024"))
dolist1.add_task(Task("Cleaning", "Clean the floor", "21-7-2024"))
dolist1.add_task(Task("Weekend", "Buy beers for the game", "29/7/2024"))

# Second person with 5 tasks
dolist2 = TodoList("Anna", "Marketing")
dolist2.add_task(Task("Report", "Complete quarterly report", "15-8-2024"))
dolist2.add_task(Task("Meeting", "Schedule team meeting", "10-7-2024"))
dolist2.add_task(Task("Campaign", "Launch new campaign", "25.8.2024"))
dolist2.add_task(Task("Budget", "Prepare budget proposal", "1/9/2024"))
dolist2.add_task(Task("Presentation", "Create presentation for clients", "5-7-2024"))

# Third person with 6 tasks
dolist3 = TodoList("David", "Development")
dolist3.add_task(Task("Code Review", "Review the new code", "30-6-2024"))
dolist3.add_task(Task("Testing", "Test the new features", "25/7/2024"))
dolist3.add_task(Task("Documentation", "Update project documentation", "1-8-2024"))
dolist3.add_task(Task("Deployment", "Deploy the latest build", "15.7.2024"))
dolist3.add_task(Task("Bug Fix", "Fix critical bugs", "5-8-2024"))
dolist3.add_task(Task("Team Meeting", "Team meeting to discuss progress", "22-7-2024"))



do = [dolist1, dolist2]
for status in do:
    backlog_tasks = status.get_tasks_by_status("Backlog")
    in_progress_tasks = status.get_tasks_by_status("In Progress")
    done_tasks = status.get_tasks_by_status("Done or overdue")

for i in do:
    print(i)
    i.print_tasks()
    i.print_tasks_by_status()
    i.print_smallest_duaration_task()
    i.print_biggest_duaration_task()

# Compare task counts
most_tasks, least_tasks = TodoList.compare_task_counts(dolist1, dolist2)
print(most_tasks)
print(least_tasks)


