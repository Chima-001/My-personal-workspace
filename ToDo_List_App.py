from rich import print
from rich import print as rprint
from rich.prompt import Prompt

print()
print("[#808080]-[/]" * 60)
print("\n[yellow][bold]Welcome to My ToDo List App[/bold][/yellow]")

tasks = []
user_input = ""

while user_input.lower() != "quit".lower():
    print("\nChoose one of the following options to continue:\n[cyan]1.[/cyan] [green]New Task[/green]\n[cyan]2.[/cyan] [green]Edit[/green]\n[cyan]3.[/cyan] [green]Quit[/green]")

    user_input = Prompt.ask("[#808080][italic]Enter action [/italic][/]")
    
    print()

    if user_input.lower() == "new task".lower():
        def add_tasks():
            add_task = ""
            while add_task.lower() != "done".lower():

                add_task = Prompt.ask("[#808080][italic]Add a new task or Done to complete [/italic][/]")
                if add_task != "done".lower():
                    tasks.append(add_task)
                else:
                    break
                print("[green]Task added.[/green]\n")
        add_tasks()
        #print(tasks)
    
    elif user_input.lower() == "edit".lower():
        if not tasks:
            print("[red]No task available. You are caught up for today.[/]")
        else:
            edit_tasks = ""
            while edit_tasks.lower() != "back".lower():
                for i in range(len(tasks)):
                    print(f"{i + 1} - {tasks[i].capitalize()}")
                
                print("\nEnter 'Mark'  to mark as completed.\nEnter 'Unmark' to unmark.\nEnter 'Delete' to delete tasks.\nEnter 'Add' to add task\nEnter 'Back' to go back to previous menu")
                edit_tasks = Prompt.ask("\n[#808080][italic]Select option: [/italic][/]")

                if edit_tasks.lower() == "mark".lower():
                    task_number = int(Prompt.ask("[#808080][italic]Enter task number to mark: [/italic][/]")) - 1
                    tasks[task_number] = f"[strike]{tasks[task_number]}[/strike]"
                    rprint("[green]Task marked.[/green]\n")

                elif edit_tasks.lower() == "unmark".lower():
                    task_number = int(Prompt.ask("[#808080][italic]Enter task number to unmark: [/italic][/]")) - 1
                    tasks[task_number] = tasks[task_number].replace("[strike]", "").replace("[/strike]", "")
                    rprint("[red]Task unmarked[red]\n")

                elif edit_tasks.lower() == "delete".lower():
                    task_number = int(Prompt.ask("[#808080][italic]Enter task number to delete: [/italic][/]")) - 1
                    del tasks[task_number]
                elif edit_tasks.lower() == "add".lower():
                    print()
                    add_tasks()
                else:
                    rprint("[red]Invalid input.[/red]")
    
    elif user_input.lower() == "quit".lower():
        break

    else:
        print("[red]Invalid input.[/red]")

print("[yellow]See you soon, Your Majesty.[/yellow]\n")
print("[#808080]-[/]" * 60)