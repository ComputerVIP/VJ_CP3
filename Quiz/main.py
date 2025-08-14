#Vincent Johnson - Quiz game

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import simpledialog
import csv
import random

repeat = 0

def main(repeat):
    # Create the main window
    root = tk.Tk()
    root.title("Quiz Game")
    root.geometry("400x300")

    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))

    # Configure resizing behavior
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    # Load questions from CSV file
    questions = []
    with open('Quiz\questions1.csv', 'r') as file:
        input("H")
        reader = csv.reader(file)
        for row in reader:
            print(row)  # Debugging line to see the content of each row
            questions.append([row[0], [row[1], row[2], row[3], row[4]]])  # Question, options, correct answer index

    # Initialize score
    score = 0

    def end_quiz():
        messagebox.showinfo("Quiz Ended")
        nonlocal repeat 
        repeat = 1
        root.destroy()
        

    def to_menu():
        ttk.Label(mainframe, text="Quiz Game", font=("Helvetica", 16)).grid(column=0, row=0, columnspan=2, pady=10)

        # Start the quiz
        ttk.Button(mainframe, text="Start Quiz", command=lambda: ask_question(mainframe, questions)).grid(column=0, row=1, pady=10)

        ttk.Button(mainframe, text="Exit", command=lambda: end_quiz()).grid(column=1, row=1, pady=10)

    # Function to ask questions
    def ask_question(mainframe, questions):
        for child in mainframe.winfo_children():
            child.destroy()

        line = random.randint(0, len(questions) - 1)
        done = [0]
        ttk.Label(mainframe, text=questions[line][0], font=("Helvetica", 16)).grid(column=0, row=0, columnspan=2)
        

    to_menu()

    # Run the application
    root.mainloop()
    return repeat


if __name__ == "__main__":
    while repeat == 0:
        repeat = main(repeat)  # Call the main function to run the application