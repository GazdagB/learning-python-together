class rock_paper_scisors():
    def __init__(self):
        pass

    def start(self):
        self.ask_for_choice()
        pass

    def ask_for_choice(self):
        print("Please enter your choice")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissor")
        return input("")

game = rock_paper_scisors()
game.start()