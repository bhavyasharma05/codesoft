
import tkinter as tk
from tkinter import messagebox
import random

# Initialize scores
user_score = 0
computer_score = 0

# Options
choices = ["Rock", "Paper", "Scissors"]

# Game logic
def play(user_choice):
    global user_score, computer_score

    computer_choice = random.choice(choices)
    result = ""

    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        user_score += 1
        result = "You Win!"
    else:
        computer_score += 1
        result = "You Lose!"

    # Update UI
    user_choice_label.config(text=f"You chose: {user_choice}")
    comp_choice_label.config(text=f"Computer chose: {computer_choice}")
    result_label.config(text=result)
    score_label.config(text=f"Score → You: {user_score} | Computer: {computer_score}")

# Reset game
def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    user_choice_label.config(text="You chose:")
    comp_choice_label.config(text="Computer chose:")
    result_label.config(text="Result")
    score_label.config(text="Score → You: 0 | Computer: 0")

# Setup window
app = tk.Tk()
app.title("Rock-Paper-Scissors Game")
app.geometry("400x400")
app.configure(bg="#f0f4f7")

# Title
tk.Label(app, text="Rock-Paper-Scissors", font=("Segoe UI", 16, "bold"), bg="#f0f4f7").pack(pady=10)

# Choice Buttons
btn_frame = tk.Frame(app, bg="#f0f4f7")
btn_frame.pack(pady=10)

rock_btn = tk.Button(btn_frame, text="Rock", width=10, bg="#81C784", fg="white", font=("Segoe UI", 12), command=lambda: play("Rock"))
rock_btn.grid(row=0, column=0, padx=5)

paper_btn = tk.Button(btn_frame, text="Paper", width=10, bg="#64B5F6", fg="white", font=("Segoe UI", 12), command=lambda: play("Paper"))
paper_btn.grid(row=0, column=1, padx=5)

scissors_btn = tk.Button(btn_frame, text="Scissors", width=10, bg="#E57373", fg="white", font=("Segoe UI", 12), command=lambda: play("Scissors"))
scissors_btn.grid(row=0, column=2, padx=5)

# Result Display
user_choice_label = tk.Label(app, text="You chose:", font=("Segoe UI", 11), bg="#f0f4f7")
user_choice_label.pack(pady=5)

comp_choice_label = tk.Label(app, text="Computer chose:", font=("Segoe UI", 11), bg="#f0f4f7")
comp_choice_label.pack(pady=5)

result_label = tk.Label(app, text="Result", font=("Segoe UI", 12, "bold"), fg="#333", bg="#f0f4f7")
result_label.pack(pady=10)

# Score
score_label = tk.Label(app, text="Score → You: 0 | Computer: 0", font=("Segoe UI", 11), bg="#f0f4f7")
score_label.pack(pady=5)

# Play again button
reset_btn = tk.Button(app, text="Play Again", bg="#FFA726", fg="white", font=("Segoe UI", 10, "bold"), command=reset_game)
reset_btn.pack(pady=10)

# Run the app
app.mainloop()
