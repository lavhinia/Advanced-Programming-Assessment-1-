# Arithmetic Quiz Game using Tkinter
# This program lets the user pick a difficulty and answer 10 random math questions.
# It gives points for correct answers and shows a grade at the end.

import tkinter as tk 
import random

# this function makes random numbers based on what level the player picks
def randomInt(level):
    if level == 1: #If level is 1 or easy, it will generate a 1 digit number which runs from 0 to 9
        return random.randint(0, 9)     # easy = 1 digit
    elif level == 2: #If level is 2 then it will generate a 2 digit number 
        return random.randint(10, 99)   # moderate = 2 digits
    else: #Else then it will generate a 4 digit number 
        return random.randint(1000, 9999)  # advanced = 4 digits

# this randomly picks if it’s addition or subtraction based on the operations 
def decideOperation(): 
    return random.choice(['+', '-'])
# this starts the quiz when a level is picked
def start_quiz(level):
    global current_level, score, question_count 
    current_level = level #This will allow to set the level, score, and question number to zero at start
    score = 0 
    question_count = 0 #This will show the first question 
    show_question()  # move to first question

# In this code, it will shows a new question each time
def show_question():
    global a, b, op, correct_answer, attempt, question_count

    #  then if the user already asked 10 questions then it will stop and show the score 
    if question_count == 10:
        show_results()
        return

    # This will create or make a random math problem
    a = randomInt(current_level)
    b = randomInt(current_level)
    op = decideOperation()
    correct_answer = a + b if op == '+' else a - b
    attempt = 1  # this will try to attempt first try 

    # update what’s shown on the screen
    question_label.config(text=f"Question {question_count + 1}: {a} {op} {b} = ?") #This will allow to show the math problem on the screeen.
    answer_entry.delete(0, tk.END) #This will allow to clear the answer box
    feedback_label.config(text="") #It will allow to remove the previous message 
    submit_btn.config(state="normal") #It will submit the button on so user can answer

# this will allow to checks if the answer is correct or not
def check_answer():
    global attempt, score, question_count

    try:
        user_answer = int(answer_entry.get()) #this will try to convert user input into a number 
    except ValueError:
        feedback_label.config(text="Please type a number.", fg="red")
        return # If by any chance that the user write something wrong like letter , it will ask them to type a number

    if user_answer == correct_answer:
        #  if the first try gives 10 points, second try gives 5
        if attempt == 1: 
            score += 10
        else:
            score += 5
        feedback_label.config(text="Correct!", fg="green") #It will tell the user that the answer is correct
        question_count += 1 #This will allow to move on the next question 
        window.after(1000, show_question)  # wait a second then show next question
    else:
        if attempt == 1: #if its a wrong answer 
            feedback_label.config(text=" Wrong. Try again!", fg="orange") 
            attempt += 1
            answer_entry.delete(0, tk.END) #If its a first try they got it wrong then it will ask them to try again
        else:
            feedback_label.config(text=f"Wrong again. The right answer was {correct_answer}.", fg="red")
            question_count += 1
            window.after(1500, show_question) #The second wrong try will allow them to show the correct answer and move on

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
#This is a grading system that was based on the score 
    question_label.config(text=f"Quiz done!\nScore: {score}/100\nGrade: {grade}") #this will allow to display the final result 
    feedback_label.config(text="")
    answer_entry.delete(0, tk.END)
    submit_btn.config(state="disabled") #this willl be clean screen and disable the answer

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
