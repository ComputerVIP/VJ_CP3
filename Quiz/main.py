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
        reader = csv.reader(file)
        for row in reader:
            questions.append([row[0], [row[1], row[2], row[3], row[4]]])  # Question, options, correct answer index

    # Initialize score
    score = 0
    rounds = 0

    def end_quiz():
        messagebox.showinfo("Quiz Ended", "You ended the quiz")
        nonlocal repeat 
        repeat = 1
        root.destroy()

        with open('Quiz\questions1.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            for question in questions:
                try:
                    writer.writerow([question[0]] + question[1])
                except Exception as e:
                    print(f"Error writing question {question[0]}: {e}")
        
        questions.clear()  # Clear the questions list after saving to CSV

        

    def to_menu():
        nonlocal rounds
        nonlocal score
        rounds = 0
        score = 0

        for child in mainframe.winfo_children():
            child.destroy()

        ttk.Label(mainframe, text="Quiz Game", font=("Helvetica", 16)).grid(column=0, row=0, columnspan=2, pady=10)

        # Start the quiz
        ttk.Button(mainframe, text="Start Quiz", command=lambda: ask_question(mainframe, questions)).grid(column=0, row=1, pady=10, columnspan=2)

        ttk.Button(mainframe, text="Add questions", command=lambda: add_question()).grid(column=0, row=2, pady=10, columnspan=2)

        ttk.Button(mainframe, text="Exit", command=lambda: end_quiz()).grid(column=0, row=10, pady=10, columnspan=2)
    
    def show_score():
        messagebox.showinfo("Score", f"Your score is: {score}/{rounds}")
        to_menu()  # Return to the main menu after showing the score

    def add_question():
        nonlocal questions
        question_text = simpledialog.askstring("Add Question", "Enter the question:")
        if not question_text:
            return
        options = []   
        for i in range(1, 5):
            option = simpledialog.askstring(f"Option {i}", f"Enter option {i}:")
            if not option:
                return
            options.append(option)
        correct_option = simpledialog.askstring("Correct Option", "Enter the correct option (1, 2, 3, or 4):")
        if not correct_option or correct_option not in ['1', '2', '3', '4']:
            messagebox.showerror("Error", "Invalid correct option")
            return
        correct_index = int(correct_option) - 1

        options = [f"T_{options[correct_index]}"] + [f"F_{opt}" for idx, opt in enumerate(options) if idx != correct_index]
        random.shuffle(options)

        questions.append([question_text, options])

    # Function to ask questions
    def ask_question(mainframe, questions):

        nonlocal rounds
        nonlocal score

        # Clear all widgets in the mainframe
        for child in mainframe.winfo_children():
            child.destroy()

        # Select a random question
        line = random.randint(0, len(questions) - 1)
        question = questions[line]
        options = question[1]  # The list of options

        # Display the question
        ttk.Label(mainframe, text=question[0], font=("Helvetica", 16), wraplength=350).grid(column=0, row=0, columnspan=2, pady=10)

        # Display the options
        for idx, option in enumerate(options):
            if "T_" in option:
                option_text = option.replace("T_", "")

                ttk.Button(
                    mainframe,
                    text=option_text,
                    command=lambda: [
                        messagebox.showinfo("Correct!", "You were correct!"),
                        ask_question(mainframe, questions),
                        increment_score()
                    ]
                ).grid(column=0, row=idx + 1, pady=10, columnspan=2)
            else:
                option_text = option.replace("F_", "")

                ttk.Button(
                    mainframe,
                    text=option_text,
                    command=lambda: [
                        messagebox.showinfo("Incorrect!", "You were incorrect"),
                        ask_question(mainframe, questions),
                        increment_rounds()
                    ]
                ).grid(column=0, row=idx + 1, pady=10, columnspan=2)

        ttk.Button(mainframe, text="End Quiz", command=lambda: show_score()).grid(column=1, row=len(options) + 1, pady=10, columnspan=2)

    def increment_score():
        nonlocal score
        nonlocal rounds
        score += 1
        rounds += 1
    def increment_rounds():
        nonlocal rounds
        rounds += 1
        

    to_menu()

    # Run the application
    root.mainloop()
    return repeat


if __name__ == "__main__":
    while repeat == 0:
        repeat = main(repeat)  # Call the main function to run the application