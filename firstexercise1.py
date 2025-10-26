# Arithmetic Quiz Game using Tkinter
# This program lets the user pick a difficulty and answer 10 random math questions.
# It gives points for correct answers and shows a grade at the end.

import tkinter as tk
import random

# this function makes random numbers based on what level the player picks
def randomInt(level):
    if level == 1:
        return random.randint(0, 9)     # easy = 1 digit
    elif level == 2:
        return random.randint(10, 99)   # moderate = 2 digits
    else:
        return random.randint(1000, 9999)  # advanced = 4 digits

# this randomly picks if it’s addition or subtraction based on the operations 
def decideOperation():
    return random.choice(['+', '-'])

# this starts the quiz when a level is picked
def start_quiz(level):
    global current_level, score, question_count
    current_level = level
    score = 0
    question_count = 0
    show_question()  # move to first question

# this shows a new question each time
def show_question():
    global a, b, op, correct_answer, attempt, question_count

    # stop if 10 questions are done
    if question_count == 10:
        show_results()
        return

    # make a random math problem
    a = randomInt(current_level)
    b = randomInt(current_level)
    op = decideOperation()
    correct_answer = a + b if op == '+' else a - b
    attempt = 1  # first try

    # update what’s shown on the screen
    question_label.config(text=f"Question {question_count + 1}: {a} {op} {b} = ?")
    answer_entry.delete(0, tk.END)
    feedback_label.config(text="")
    submit_btn.config(state="normal")

# this checks if the answer is correct or not
def check_answer():
    global attempt, score, question_count

    try:
        user_answer = int(answer_entry.get())
    except ValueError:
        feedback_label.config(text="Please type a number.", fg="red")
        return

    if user_answer == correct_answer:
        # first try gives 10 points, second try gives 5
        if attempt == 1:
            score += 10
        else:
            score += 5
        feedback_label.config(text="Correct!", fg="green")
        question_count += 1
        window.after(1000, show_question)  # wait a second then show next question
    else:
        if attempt == 1:
            feedback_label.config(text=" Wrong. Try again!", fg="orange")
            attempt += 1
            answer_entry.delete(0, tk.END)
        else:
            feedback_label.config(text=f"Wrong again. The right answer was {correct_answer}.", fg="red")
            question_count += 1
            window.after(1500, show_question)

# shows final score and grade after the quiz
def show_results():
    if score >= 90:
        grade = "A+"
    elif score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 60:
        grade = "C"
    elif score >= 50:
        grade = "D"
    else:
        grade = "F"

    question_label.config(text=f"Quiz done!\nScore: {score}/100\nGrade: {grade}")
    feedback_label.config(text="")
    answer_entry.delete(0, tk.END)
    submit_btn.config(state="disabled")

# resets everything to pick a new level again
def reset_game():
    question_label.config(text="CHOOSE YOUR DIFFICULTY:")
    feedback_label.config(text="")
    submit_btn.config(state="disabled")
    answer_entry.delete(0, tk.END)

# ------------ Tkinter GUI setup ------------ #

window = tk.Tk()
window.title("Lavhinia's Math Quiz Game")
window.geometry("500x500")
window["bg"] = "lightblue"
window.resizable(False, False)

# main question or message
question_label = tk.Label(window, text="CHOOSE YOUR DIFFICULTY:", font=("PT Sans Bold", 16))
question_label.pack(pady=20)

# buttons for difficulty levels
level_frame = tk.Frame(window)
level_frame.pack()
tk.Button(level_frame, text="Easy", width=10, command=lambda: start_quiz(1)).grid(row=0, column=0, padx=5)
tk.Button(level_frame, text="Moderate", width=10, command=lambda: start_quiz(2)).grid(row=0, column=1, padx=5)
tk.Button(level_frame, text="Advanced", width=10, command=lambda: start_quiz(3)).grid(row=0, column=2, padx=5)

# box where user types answer
answer_entry = tk.Entry(window, font=("PT Sans Bold", 16), justify="center")
answer_entry.pack(pady=10)

# button to check the answer
submit_btn = tk.Button(window, text="Submit", width=10, state="disabled", command=check_answer)
submit_btn.pack(pady=5)

# label to show messages or feedback
feedback_label = tk.Label(window, text="", font=("PT Sans Bold", 16))
feedback_label.pack(pady=10)

# button to play again
play_again_btn = tk.Button(window, text="Play Again", command=reset_game)
play_again_btn.pack(pady=10)

# start the GUI loop
window.mainloop()
