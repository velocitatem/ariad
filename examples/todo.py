
# we define a simple ariad decorator
# it lets the function pass but also stores it in the database under a specified name in the decorator
# ex @part("AddTodo")

def part(name: str):
    def decorator(func):
        import os
        import pickle
        import inspect
        # make .ariad folder if it doesn't exist
        if not os.path.exists(".ariad"):
            os.makedirs(".ariad")
        # pickle the function's name and code
        with open(f".ariad/{name}.pickle", "wb") as f:
            pickle.dump({'name': func.__name__, 'code': inspect.getsource(func)}, f)
        return func
    return decorator


# Global todo list
todoList = []

@part("AddTodo")
def add_todo(todoItem):
    """Adds a todo item to the list."""
    todoList.append(todoItem)
    return todoList

@part("RemoveTodo")
def remove_todo(todoItem):
    """Removes a todo item from the list."""
    if todoItem in todoList:
        todoList.remove(todoItem)
    return todoList

@part("DisplayTodos")
def display_todos(todoList):
    """Displays the todo list."""
    if not todoList:
        return "You have no todos left!"
    return "Your Todos: " + ", ".join(todoList)

def cli_loop():
    global todoList
    while True:
        userInput = input("Enter command: ")
        if userInput.startswith("add "):
            todoItem = userInput[4:]
            updatedList = add_todo(todoItem)
            print(f"Todo added: {todoItem}")
        elif userInput.startswith("remove "):
            todoItem = userInput[7:]
            updatedList = remove_todo(todoItem)
            print(f"Todo removed: {todoItem}")
        elif userInput == "display":8
            displayMessage = display_todos(todoList)
            print(displayMessage)
        elif userInput == "exit":
            break
        else:
            print("Unknown command. Please use 'add', 'remove', 'display', or 'exit'.")

# Entry point for the application
cli_loop()
