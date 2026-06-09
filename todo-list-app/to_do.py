import csv


class Task():
    def __init__(self, task_name, description, priority):
        self.task_name = task_name
        self.description = description
        self.priority = priority
    
    
    def show_task(self):
        print(f"task:\n\t{self.task_name.upper()}\ndescription:\n\t{self.description.upper()}\nwith priority level:\n\t{self.priority.upper()}")
    
    
class ToDoList():
    def __init__(self):
        self.tasks = []
        
        
    def add_task(self, task):
        self.tasks.append(task)
    
    
    def remove_task(self, index):
        self.tasks.remove(index)
    
    
    def show_tasks(self):
        for task in self.tasks:
            print(task)
    
    
    def load_from_csv(self, filename):
        try:
            with open(filename, 'r') as file :
                reader = csv.reader(file)
        
        except FileExistsError:
            print("No existing file. Will create when saving first task.")
            self.tasks = []
    
    def save_to_csv(self, filename):
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['name', 'description', 'priority'])
            
            for task in self.tasks:
                writer.writerow([task.task_name, task.description, task.priority])
                 
    
    
    
english_task = Task('english language', 'i want to read and practice every day about 4 houre', 'high')
math_task = Task("Solving problems", "Chapter 3", "Medium")



my_list = ToDoList()
my_list.add_task(english_task)
my_list.add_task(math_task)

my_list.save_to_csv('my_tasks')
my_list.load_from_csv('my_tasks')

