#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  7 19:13:27 2025

@author: lavignejoicee
"""

# Import tkinter for GUI and random for picking random jokes
import tkinter as tk
import random

# In this Function, it will try to load jokes from the text file
def load_jokes():
    try:
        # Open the text file and read each line
        with open("/Users/lavignejoicee/Downloads/randomJokes.txt", "r") as file:
            jokes = [line.strip() for line in file.readlines() if "?" in line]
        return jokes  """ It tries ro open the file and it will allow to 
        read each line and keeps only a joke that has a "?" so it will know where to split setup and puncline"""
    except FileNotFoundError:
        #If the file does not exists, the it will allow the code it return on a default joke instead of crashing
        return ["Why can't I tell a joke?Because the joke file is missing."]

# Function to show the setup part of the joke
def tell_joke(): #This function will allow to pick and shows only the first part of the joke 
    global current_joke  # Make it accessible to other functions
    # Pick a random joke from the list
    current_joke = random.choice(jokes) #This will make a current joke as a variable to other functions can use it 
    # Split setup and punchline using '?'
    parts = current_joke.split("?") #This will split the joke into two parts which are the setup and puncline that was based on ?
    setup_label.config(text=parts[0] + "?")  # Show setup only
    punchline_label.config(text="")  # Clear previous punchline
    show_btn.config(state="normal")  # Enable punchline button
    ask_btn.config(state="disabled")  # Disable ask button for now

# Function to show the punchline of the current joke
def show_punchline(): #This function reveals the punchline 
    # Split again to get punchline part
    parts = current_joke.split("?") #it will show the second part of the punchline
    # Display the punchline
    punchline_label.config(text=parts[1]) 
    show_btn.config(state="disabled")  # Disable punchline button
    ask_btn.config(state="normal")  # Enable ask button again
    #This will enable to ask the joke but wont be able to click the puncline again 

# Function to process user input from the entry box
def process_command(): #This will check on what the user has typed in the box 
    # Get what the user typed and remove extra spaces
    user_input = entry.get().strip().lower() #If you type the phrase correctly then alexa will give a joke
    if user_input == "alexa tell me a joke":
        tell_joke()  # If correct phrase, show a joke
    else:
        # If wrong phrase, show hint message
        setup_label.config(text="Type: Alexa tell me a joke")
        punchline_label.config(text="")

# Function to close the program
def quit_app(): #This will allow to close the window when you click on quit 
    window.destroy()

# Create the main GUI window
window = tk.Tk() #it creates the main window and gives a title size anf the background
window.title("Alexa Joke Teller")  # Set title of the window
window.geometry("400x300")  # Set window size
window.config(bg="lightblue")  # Set background color

# Load jokes when program starts
jokes = load_jokes() 
current_joke = "" #This will allow to load jokes once at start and prepares a variable to the store the currernt one

# Label for program title
title_label = tk.Label(window, text="Alexa Joke Teller", font=("Arial", 16, "bold"), bg="lightblue")
title_label.pack(pady=10)

# Entry box for user to type the command
entry = tk.Entry(window, width=30)
entry.pack(pady=5)

# Button to process command
command_btn = tk.Button(window, text="Submit", command=process_command, bg="white")
command_btn.pack(pady=5)

# Label to show the setup of the joke
setup_label = tk.Label(window, text="", font=("Arial", 12), bg="lightblue")
setup_label.pack(pady=10)

# Label to show the punchline later
punchline_label = tk.Label(window, text="", font=("Arial", 12, "italic"), bg="lightblue")
punchline_label.pack(pady=10)

# Button to show punchline, starts disabled
show_btn = tk.Button(window, text="Show Punchline", command=show_punchline, state="disabled", bg="lightyellow")
show_btn.pack(pady=5)

# Button to ask for a new joke
ask_btn = tk.Button(window, text="New Joke", command=tell_joke, state="disabled", bg="lightgreen")
ask_btn.pack(pady=5)

# Quit button to close program
quit_btn = tk.Button(window, text="Quit", command=quit_app, bg="red", fg="white")
quit_btn.pack(pady=5)

# Run the GUI loop
window.mainloop()
