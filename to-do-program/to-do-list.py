import json
import os
import sys

def save_tasks(to_do, filename="todo_list.json"):
    """Save your task list to a file"""
    try:

        with open(filename, 'w') as f:
            json.dump(to_do, f, indent=2)

        print("💾 Tasks saved successfully!")
        sys.exit()

    except Exception as e:
        print(f"⚠️ Error saving tasks: {e}")
        sys.exit()

def load_tasks(filename="todo_list.json"):
 
    if os.path.exists(filename):
        try:
            with open(filename, 'r') as f:
                return json.load(f)
            
        except (json.JSONDecodeError, FileNotFoundError) as e:

            print(f"Error loading tasks: {e}")
            return {}
        
    return {}

def main():

    to_do_list = load_tasks()
    if to_do_list:
        print(f"📂 Loaded {len(to_do_list)} tasks from previous session!")
    priority_list = {
        'non-urgent': 0,
        'important': 1,
        'urgent': 2
    }

    while True:
        try:
            print("Welcome to your To-do List! What would you like to do?")
            print("1. View List")
            print("2. Add")
            print("3. Delete")
            print("4. Complete Task")
            print("5. Save and Exit!")

            while True:

                choice = input()

                if choice == '1':
                    display_list(to_do_list, priority_list)
                    break

                elif choice == '2':
                    add_to_list(to_do_list, priority_list)
                    break

                elif choice == '3':
                    remove_from_list(to_do_list, priority_list, 'deleted')
                    break

                elif choice == '4':
                    remove_from_list(to_do_list, priority_list, 'completed')
                    break

                elif choice == '5':
                    save_tasks(to_do_list)
                    print("👋 Goodbye!")
                    break

                else:
                    print("Please enter a choice!")
                    continue

        except (EOFError, KeyboardInterrupt):
            print("Bye!")
            break

def display_list(to_do, order):

    print("\n--- Current List ---")

    sorted_tasks = sorted(to_do.items(), key = lambda item: order[item[1]])
    for task, priority in sorted_tasks:
        print(f"{task}: {priority}")

def add_to_list(to_do, order):

    while True:

        addition = input("New task: ").strip()
        if addition:
            addition = addition.title()
            break
        print("You can't leave this empty!")


    while True:

        priority = input("Choose priority (non-urgent, important, urgent): ").lower().strip()

        match priority:

            case 'non-urgent' | 'important' | 'urgent':

                to_do[addition] = priority
                break
            
            case _:

                print("Choose one of the options!")

           
    display_list(to_do, order)


def remove_from_list(to_do, order, action_type):

    while True:

        if action_type == 'deleted':
            deletion = input('Delete: ').strip().title()
        else:
            deletion = input('Complete: ').strip().title()

        if not deletion:
            print("Please enter a task name!")
            continue

        if deletion in to_do:
            to_do.pop(deletion)
            print(f"{deletion} has been {action_type}!")
            break

        else:
            print("That's not in your list!")

        display_list(to_do, order)


if __name__ == "__main__":
    main()
