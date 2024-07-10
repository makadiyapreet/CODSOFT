import tkinter as tk
import random

class RockPaperScissors:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Rock-Paper-Scissors Game")
        self.window.geometry("500x400")
        self.window.configure(bg="#f0f0f0")  # Light grey background

        self.user_score = 0
        self.computer_score = 0

        self.title_label = tk.Label(self.window, text="Rock-Paper-Scissors Game", font=("Arial", 18, "bold"), bg="#f0f0f0", fg="#333")
        self.title_label.pack(pady=10)

        self.user_choice_label = tk.Label(self.window, text="Your Choice:", font=("Arial", 14), bg="#f0f0f0", fg="#555")
        self.user_choice_label.pack(pady=5)

        self.computer_choice_label = tk.Label(self.window, text="Computer's Choice:", font=("Arial", 14), bg="#f0f0f0", fg="#555")
        self.computer_choice_label.pack(pady=5)

        self.result_label = tk.Label(self.window, text="", font=("Arial", 14, "bold"), bg="#f0f0f0", fg="#000")
        self.result_label.pack(pady=10)

        self.score_label = tk.Label(self.window, text=f"Score: You - {self.user_score}, Computer - {self.computer_score}", font=("Arial", 14), bg="#f0f0f0", fg="#333")
        self.score_label.pack(pady=10)

        self.button_frame = tk.Frame(self.window, bg="#f0f0f0")
        self.button_frame.pack(pady=10)

        self.rock_button = tk.Button(self.button_frame, text="Rock", font=("Arial", 12, "bold"), bg="#FF5733", fg="white", width=10, command=lambda: self.play("rock"))
        self.rock_button.grid(row=0, column=0, padx=5)

        self.paper_button = tk.Button(self.button_frame, text="Paper", font=("Arial", 12, "bold"), bg="#33A1FF", fg="white", width=10, command=lambda: self.play("paper"))
        self.paper_button.grid(row=0, column=1, padx=5)

        self.scissors_button = tk.Button(self.button_frame, text="Scissors", font=("Arial", 12, "bold"), bg="#9B59B6", fg="white", width=10, command=lambda: self.play("scissors"))
        self.scissors_button.grid(row=0, column=2, padx=5)

        self.play_again_button = tk.Button(self.window, text="Play Again", font=("Arial", 14, "bold"), bg="green", fg="white", width=15, command=self.play_again)
        self.play_again_button.pack(pady=10)

    def play(self, user_choice):
        computer_choice = random.choice(["rock", "paper", "scissors"])

        self.user_choice_label.config(text=f"Your Choice: {user_choice.capitalize()}")
        self.computer_choice_label.config(text=f"Computer's Choice: {computer_choice.capitalize()}")

        if user_choice == computer_choice:
            result = "It's a tie!"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            result = "You win!"
            self.user_score += 1
        else:
            result = "Computer wins!"
            self.computer_score += 1

        self.result_label.config(text=result)
        self.score_label.config(text=f"Score: You - {self.user_score}, Computer - {self.computer_score}")

    def play_again(self):
        self.user_choice_label.config(text="Your Choice:")
        self.computer_choice_label.config(text="Computer's Choice:")
        self.result_label.config(text="")
        self.score_label.config(text=f"Score: You - {self.user_score}, Computer - {self.computer_score}")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = RockPaperScissors()
    game.run()