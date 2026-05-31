import json
import os
from pathlib import Path
from colored import Fore, Back, Style


class TodoApp:
    def __init__(self):
        self.file_path = Path("todos.json")

        # Create file with default JSON if missing or empty
        if not self.file_path.exists() or self.file_path.stat().st_size == 0:
            with open(self.file_path, "w") as file:
                json.dump({"todos": []}, file, indent=4)

    def clear_console(self):
        # Works better in many terminals/IDEs
        print("\033[2J\033[H", end="")

    def header(self, title):
        print(f"{Fore.blue}{'=' * 35}{Style.reset}")
        print(f"{Fore.yellow}{Style.bold} {title}{Style.reset}")
        print(f"{Fore.blue}{'=' * 35}{Style.reset}")

    def greet(self):
        self.clear_console()

        self.header("TODO APP")

        print(f"{Fore.cyan}1.{Style.reset} List Todos")
        print(f"{Fore.cyan}2.{Style.reset} Add Todo")
        print(f"{Fore.cyan}3.{Style.reset} Remove Todo")
        print(f"{Fore.cyan}4.{Style.reset} Exit")
        print()

    def start(self):
        while True:
            self.greet()

            choice = input(
                f"{Style.bold}{Back.blue}{Fore.black} Choose an option: {Style.reset}"
            )

            if choice == "1":
                self.list_todos()
                input("\nPress ENTER to continue...")

            elif choice == "2":
                self.add_todo()
                input("\nPress ENTER to continue...")

            elif choice == "3":
                self.remove_todo()
                input("\nPress ENTER to continue...")

            elif choice == "4":
                self.clear_console()
                self.header("GOODBYE!")
                break

            else:
                print(f"\n{Fore.red}❌ Invalid choice!{Style.reset}")
                input("\nPress ENTER to continue...")

    def load_data(self):
        with open(self.file_path, "r") as file:
            return json.load(file)

    def save_data(self, data):
        with open(self.file_path, "w") as file:
            json.dump(data, file, indent=4)

    def add_todo(self):
        self.clear_console()
        self.header("ADD TODO")

        title = input(f"{Fore.green}Todo title: {Style.reset}")

        data = self.load_data()

        data["todos"].append({
            "title": title
        })

        self.save_data(data)

        print(f"\n{Fore.green}✅ '{title}' added successfully!{Style.reset}")

    def list_todos(self):
        self.clear_console()
        self.header("YOUR TODOS")

        data = self.load_data()

        todos = data["todos"]

        if not todos:
            print(f"{Fore.yellow}No todos yet.{Style.reset}")
            return

        for index, todo in enumerate(todos, start=1):
            print(f"{Fore.cyan}[{index}]{Style.reset} {todo['title']}")

    def remove_todo(self):
        self.clear_console()
        self.header("REMOVE TODO")

        data = self.load_data()

        todos = data["todos"]

        if not todos:
            print(f"{Fore.yellow}No todos to remove.{Style.reset}")
            return

        for index, todo in enumerate(todos, start=1):
            print(f"{Fore.cyan}[{index}]{Style.reset} {todo['title']}")

        print()

        try:
            todo_number = int(
                input(f"{Fore.red}Enter todo number: {Style.reset}")
            )

            if 1 <= todo_number <= len(todos):
                removed = todos.pop(todo_number - 1)

                self.save_data(data)

                print(
                    f"\n{Fore.red}🗑️ Removed:{Style.reset} {removed['title']}"
                )

            else:
                print(f"\n{Fore.red}❌ Invalid todo number!{Style.reset}")

        except ValueError:
            print(f"\n{Fore.red}❌ Please enter a valid number!{Style.reset}")


todo_app = TodoApp()
todo_app.start()