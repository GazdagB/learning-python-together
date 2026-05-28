class Calculator:
    GREEN = "\033[32m"
    RED = "\033[31m"
    YELLOW = "\033[33m"
    CYAN = "\033[36m"
    BOLD = "\033[1m"
    RESET = "\033[0m"

    def __init__(self):
        self.isSolved = False
        self.firstDigit = 0
        self.secondDigit = 0
        self.operation_str = ""
        self.resolution = 0

    def start(self):
        while not self.isSolved:
            print(f"\n{self.CYAN}{self.BOLD}=== PYTHON CALCULATOR ==={self.RESET}")
            print(f"{self.YELLOW}To close, type exit anytime.{self.RESET}")

            self.firstDigit = self.ask_digit("Enter the first number")

            self.operation_str = self.show_menu().lower()

            if self.validate_input(self.operation_str):
                if self.operation_str in ["exit", "esc", "back", "quit", "5"]:
                    self.exit_program()
                    continue

                self.secondDigit = self.ask_digit("Enter the second number")
                self.solve()
                self.show_result()
            else:
                print(f"{self.RED}Invalid operation. Try again.{self.RESET}")

    def solve(self):
        if self.operation_str in ["add", "plus", "+", "and", "1"]:
            self.resolution = self.add(self.firstDigit, self.secondDigit)

        elif self.operation_str in ["subtract", "sub", "minus", "min", "2"]:
            self.resolution = self.sub(self.firstDigit, self.secondDigit)

        elif self.operation_str in ["multiply", "mul", "3", "times", "*"]:
            self.resolution = self.mul(self.firstDigit, self.secondDigit)

        elif self.operation_str in ["divide", "divided", "/", "4"]:
            if self.secondDigit == 0:
                print(f"{self.RED}Cannot divide by zero.{self.RESET}")
                return

            self.resolution = self.div(self.firstDigit, self.secondDigit)

    def validate_input(self, input_str):
        valid_operations = [
            "add", "plus", "+", "and", "1",
            "subtract", "sub", "minus", "min", "2",
            "multiply", "mul", "3", "times", "*",
            "divide", "divided", "/", "4",
            "exit", "esc", "back", "quit", "5"
        ]

        return input_str in valid_operations

    def ask_digit(self, label):
        while True:
            digit = input(f"{self.CYAN}{label}: {self.RESET}")

            if digit.lower() in ["exit", "esc", "back", "quit"]:
                self.exit_program()

            try:
                return float(digit)
            except ValueError:
                print(f"{self.RED}Please enter a valid number.{self.RESET}")

    def show_menu(self):
        self.line()
        print(f"{self.YELLOW}Choose operation:{self.RESET}")
        print("1. ➕ Add")
        print("2. ➖ Subtract")
        print("3. ✖️  Multiply")
        print("4. ➗ Divide")
        print("5. 🚪 Exit")
        self.line()

        return input(f"{self.CYAN}Your choice: {self.RESET}")

    def show_result(self):
        print(f"{self.GREEN}{self.BOLD}Result: {self.resolution}{self.RESET}")

    def line(self):
        print(f"{self.CYAN}{'─' * 35}{self.RESET}")

    def exit_program(self):
        print(f"{self.YELLOW}Goodbye! 👋{self.RESET}")
        self.isSolved = True
        exit()

    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b


calculator = Calculator()
calculator.start()