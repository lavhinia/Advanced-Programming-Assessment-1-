#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  7 19:13:27 2025

@author: lavignejoicee
"""

# Import tkinter for GUI and random for picking random jokes
import tkinter as tk
import random

# Function to load jokes from the text file
def load_jokes():
    try:
        # Open the text file and read each line
        with open("/Users/lavignejoicee/Downloads/randomJokes.txt", "r") as file:
            jokes = [line.strip() for line in file.readlines() if "?" in line]
        return jokes  # Return list of jokes
    except FileNotFoundError:
        # Show a default message if file not found
        return ["Why can't I tell a joke?Because the joke file is missing."]

# Function to show the setup part of the joke
def tell_joke():
    global current_joke  # Make it accessible to other functions
    # Pick a random joke from the list
    current_joke = random.choice(jokes)
    # Split setup and punchline using '?'
    parts = current_joke.split("?")
    setup_label.config(text=parts[0] + "?")  # Show setup only
    punchline_label.config(text="")  # Clear previous punchline
    show_btn.config(state="normal")  # Enable punchline button
    ask_btn.config(state="disabled")  # Disable ask button for now

# Function to show the punchline of the current joke
def show_punchline():
    # Split again to get punchline part
    parts = current_joke.split("?")
    # Display the punchline
    punchline_label.config(text=parts[1])
    show_btn.config(state="disabled")  # Disable punchline button
    ask_btn.config(state="normal")  # Enable ask button again

# Function to process user input from the entry box
def process_command():
    # Get what the user typed and remove extra spaces
    user_input = entry.get().strip().lower()
    if user_input == "alexa tell me a joke":
        tell_joke()  # If correct phrase, show a joke
    else:
        # If wrong phrase, show hint message
        setup_label.config(text="Type: Alexa tell me a joke")
        punchline_label.config(text="")

# Function to close the program
def quit_app():
    window.destroy()

# Create the main GUI window
window = tk.Tk()
window.title("Alexa Joke Teller")  # Set title of the window
window.geometry("400x300")  # Set window size
window.config(bg="lightblue")  # Set background color

# Load jokes when program starts
jokes = load_jokes()
current_joke = ""

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
