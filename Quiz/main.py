#Vincent Johnson - Quiz game

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import simpledialog
import csv

def main(repeat):
    # Create the main window
    root = tk.Tk()
    root.title("Quiz Game")
    root.geometry("400x300")

    # Load questions from CSV file
    questions = []
    with open('questions.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            questions.append(row)

    # Initialize score
    score = 0

    # Function to ask questions
    def ask_question(index):
        

    # Start the quiz
    ask_question(0)

    # Run the application
    root.mainloop()