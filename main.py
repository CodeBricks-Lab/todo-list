
class Item():
    def __init__(self, name, id):
        self.name = name
        self.completed = False
        self.id = id
    
    def print(self):
        print(f'{self.id}: {self.name}: ')
        if self.completed is True:
            print('Completed')
        else:
            print('not completed')

# item1 = Item('eat', 1)
# item2 = Item('pet', 2)
# item3 = Item('study', 3)

# item1.print()
# item1.completed = True
# item1.print()



class ToDoList():
    def __init__(self, name):
       self.name = name
       self.items = []
    #    self.completed = []

    def add_task(self, task):
        item = Item(task, len(self.items) + 1)
        self.items.append(item)

    def view_tasks(self):
        print('=' * 15)
        print(f'{self.name} List')
        print('-' * 15)
        for item in self.items:
            item.print()
        print('=' * 15)

    def mark_completed(self, task_id):
        for item in self.items:
            if item.id == task_id:
                # print(f'i found the item {i.id}')
                item.completed = True
    

    def remove_task(self, task_id):
        task_to_remove = None
        for i, item in enumerate(self.items):
            if item.id == task_id:
                # print(f'i found the item {i.id}')
                task_to_remove = i
        
        self.items.pop(task_to_remove)



class ToDoApp():
    def __init__(self, name='defalt todo'):
        self.todolists = [] # multiple to-do list
    
    # need a method to add todolist
    # create an object of it
    
        
    def print_commands(self):
        pass

    def run(self):
        while True:
            self.print_commands()
            command = int(input('give your command'))
            if command == 1:
                task = input('what is your task to add? ')
                # work_todo_list.add_task(task)


if __name__ == '__main__':
    app = ToDoApp()
    app.run()

    