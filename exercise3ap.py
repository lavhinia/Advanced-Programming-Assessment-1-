#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 16 17:52:00 2025

@author: lavignejoicee
"""

# This is a student records with the help of GUI with the help of different dictionaries and libraries 
# This program loads student data from studentMarks.txt and provides GUI options
# to view all records, view one record (by name or ID), show highest and lowest.

import tkinter as tk                     # main tkinter module for GUI
from tkinter import messagebox, simpledialog  # dialogs for input and messages
import os                                  # to check file existence

# ---------- Helper functions for data handling ----------

def load_students(filename="/Users/lavignejoicee/Desktop/advanced programming/studentMarks.txt"):
    """Load student data from file into a list of dicts."""
   
    students = []
    if not os.path.exists(filename):
        messagebox.showerror("File error", f"Cannot find {filename}")
        return students
    with open(filename, "r", encoding="utf-8") as f:
        lines = [ln.strip() for ln in f if ln.strip()]
    if not lines:
        return students
    # First line is count (we trust but do not require it)
    try:
        _ = int(lines[0])  # read but ignore
        data_lines = lines[1:]
    except ValueError:
        # If first line is not an integer, assume all lines are data
        data_lines = lines
    for ln in data_lines:
        parts = [p.strip() for p in ln.split(",")]
        if len(parts) < 6:
            continue  # skip malformed lines
        sid = parts[0]
        name = parts[1]
        try:
            cw1, cw2, cw3 = int(parts[2]), int(parts[3]), int(parts[4])
            exam = int(parts[5])
        except ValueError:
            continue  # skip if marks not integers
        students.append({
            "id": sid,
            "name": name,
            "cw": [cw1, cw2, cw3],
            "exam": exam
        })
    return students

def overall_percentage(student):
    """Calculate overall percentage out of 160 marks."""
    cw_total = sum(student["cw"])            # coursework total out of 60
    exam = student["exam"]                   # exam out of 100
    overall = (cw_total + exam) / 160 * 100  # percentage
    return overall

def grade_from_percent(pct):
    """Convert percentage to letter grade."""
    if pct >= 70:
        return "A"
    if pct >= 60:
        return "B"
    if pct >= 50:
        return "C"
    if pct >= 40:
        return "D"
    return "F"

def format_student_block(student):
    """Return a nicely formatted block string for one student."""
    cw_total = sum(student["cw"])
    exam = student["exam"]
    pct = overall_percentage(student)
    grd = grade_from_percent(pct)
    block = (
        "------------------------------\n"
        f"Name: {student['name']}\n"
        f"ID: {student['id']}\n"
        f"Coursework Total: {cw_total} / 60\n"
        f"Exam Mark: {exam} / 100\n"
        f"Overall Percentage: {pct:.2f}%\n"
        f"Grade: {grd}\n"
        "------------------------------\n"
    )
    return block

# ---------- GUI action functions ----------

def view_all():
    """Show all student records and summary (count and average)."""
    if not students:
        text_display.delete("1.0", tk.END)
        text_display.insert(tk.END, "No student data loaded.\n")
        return
    text_display.delete("1.0", tk.END)
    for s in students:
        text_display.insert(tk.END, format_student_block(s))
    # summary
    count = len(students)
    avg = sum(overall_percentage(s) for s in students) / count if count else 0
    summary = f"\nNumber of students: {count}\nClass average: {avg:.2f}%\n"
    text_display.insert(tk.END, summary)

def view_individual():
    """Prompt user to enter name or ID and show that student's record."""
    if not students:
        messagebox.showinfo("Info", "No data loaded.")
        return
    query = simpledialog.askstring("Find student", "Enter student name or student number:")
    if not query:
        return
    q = query.strip().lower()
    # Try to match by id first, then by name (case-insensitive)
    found = None
    for s in students:
        if s["id"].lower() == q or s["name"].lower() == q:
            found = s
            break
    if not found:
        # allow partial name matches
        for s in students:
            if q in s["name"].lower():
                found = s
                break
    text_display.delete("1.0", tk.END)
    if found:
        text_display.insert(tk.END, format_student_block(found))
    else:
        text_display.insert(tk.END, f"No student found for '{query}'.\n")

def show_highest():
    """Find and display student with highest overall percentage."""
    if not students:
        messagebox.showinfo("Info", "No data loaded.")
        return
    best = max(students, key=overall_percentage)
    text_display.delete("1.0", tk.END)
    text_display.insert(tk.END, "Student with highest overall mark:\n")
    text_display.insert(tk.END, format_student_block(best))

def show_lowest():
    """Find and display student with lowest overall percentage."""
    if not students:
        messagebox.showinfo("Info", "No data loaded.")
        return
    worst = min(students, key=overall_percentage)
    text_display.delete("1.0", tk.END)
    text_display.insert(tk.END, "Student with lowest overall mark:\n")
    text_display.insert(tk.END, format_student_block(worst))

def reload_data():
    """Reload student data from file (in case file changed)."""
    global students
    students = load_students()
    messagebox.showinfo("Reload", f"Loaded {len(students)} student records.")

def quit_app():
    """Close the GUI window and exit."""
    window.destroy()

# ---------- Build the GUI ----------

# main window
window = tk.Tk()
window.title("Student Marks Manager")
window.geometry("600x500")

# load students at start
students = load_students()

# top frame for buttons
top_frame = tk.Frame(window)
top_frame.pack(pady=10)

# Buttons for each menu action (block-style outputs requested)
btn_all = tk.Button(top_frame, text="1. View All Records", width=18, command=view_all)
btn_ind = tk.Button(top_frame, text="2. View Individual", width=18, command=view_individual)
btn_high = tk.Button(top_frame, text="3. Highest Score", width=18, command=show_highest)
btn_low = tk.Button(top_frame, text="4. Lowest Score", width=18, command=show_lowest)
btn_reload = tk.Button(top_frame, text="Reload Data", width=12, command=reload_data)
btn_quit = tk.Button(top_frame, text="Exit", width=8, command=quit_app)

# place buttons in grid for tidy layout
btn_all.grid(row=0, column=0, padx=5, pady=2)
btn_ind.grid(row=0, column=1, padx=5, pady=2)
btn_high.grid(row=0, column=2, padx=5, pady=2)
btn_low.grid(row=0, column=3, padx=5, pady=2)
btn_reload.grid(row=1, column=0, padx=5, pady=5)
btn_quit.grid(row=1, column=3, padx=5, pady=5)

# Text widget to display results in block format
text_display = tk.Text(window, wrap="word", font=("Courier", 10))
text_display.pack(expand=True, fill="both", padx=10, pady=10)

# show a starter message
text_display.insert(tk.END, "Welcome! Choose an option above to manage student records.\n")

# start the GUI event loop
window.mainloop()
