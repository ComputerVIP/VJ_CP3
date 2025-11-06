#Vincent Johnson - Quiz game

# Imports
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import simpledialog
import csv
import random
import time

# For repeating the program
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
            options = row[1:]  # Get all options except the question text
            random.shuffle(options)  # Randomly shuffle the options
            questions.append([row[0], options])  # Question, options, correct answer index

    # Initialize score
    score = 0
    rounds = 0
    question_start_time = 0
    time_score = 0

    #Type of game
    type = ""

    def end_quiz():
        messagebox.showinfo("Quiz Ended", "You ended the quiz")
        nonlocal repeat 
        repeat = 1
        root.destroy()

        # Save questions to CSV file
        with open('Quiz\questions1.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            for question in questions:
                try:
                    writer.writerow([question[0]] + question[1])
                except Exception as e:
                    print(f"Error writing question {question[0]}: {e}")
        
        questions.clear()  # Clear the questions variable after saving to CSV

    def regular():
        # Sets the type of game to regular
        nonlocal type
        type = "regular"
        messagebox.showinfo("Regular Mode", "You selected Regular mode")
        ask_question(mainframe, questions)
        return type

    def arcade():
        # Sets the type of game to arcade
        nonlocal type
        type = "arcade"
        messagebox.showinfo("Arcade Mode", "You selected Arcade mode")
        ask_question(mainframe, questions)
        return type

    def show_leaderboard():
        # Clears the window
        for child in mainframe.winfo_children():
            child.destroy()
        # Reads the scores
        try:
            with open('Quiz\scores.csv', 'r') as file:
                reader = csv.reader(file)
                header = next(reader, None)
                if header:
                    rows = list(reader)
                    rows.sort(key=lambda x: float(x[0]), reverse=True)
        except FileNotFoundError:
            leaderboard_text = "No scores available."

        # Scores display
        columns = ["Score", "Name", "Rounds"]
        tree = ttk.Treeview(mainframe, columns=columns, show='headings')
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, anchor="center",width=100)

        for row in rows:
            tree.insert("", "end", values=row)
        
        scrollbar = ttk.Scrollbar(mainframe, orient="vertical", command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        tree.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
        scrollbar.grid(column=1, row=0, sticky=(tk.N, tk.S))

        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)

        #Back to menu button
        ttk.Button(mainframe, text="Back to Menu", command=lambda: to_menu()).grid(column=0, row=1, pady=10, columnspan=2)
        

    def to_menu():
        nonlocal rounds
        nonlocal score
        rounds = 0
        score = 0

        #Clearing the window
        for child in mainframe.winfo_children():
            child.destroy()

        ttk.Label(mainframe, text="Quiz Game", font=("Helvetica", 16)).grid(column=0, row=0, columnspan=2, pady=10)

        # Function buttons
        ttk.Button(mainframe, text="Regular mode", command= regular).grid(column=0, row=1, pady=10, columnspan=2)

        ttk.Button(mainframe, text="Arcade mode", command=arcade).grid(column=0, row=2, pady=10, columnspan=2)

        ttk.Button(mainframe, text="Add questions", command=lambda: add_question()).grid(column=0, row=3, pady=10, columnspan=2)

        ttk.Button(mainframe, text="Leaderboard", command=lambda: show_leaderboard()).grid(column=0, row=4, pady=10, columnspan=2)

        ttk.Button(mainframe, text="Exit", command=lambda: end_quiz()).grid(column=0, row=10, pady=10, columnspan=2)
    
    def show_score():
        # Checks if it was arcade mode or not
        nonlocal type
        if type == "arcade":
            messagebox.showinfo("Score", f"Your arcade score is {time_score}")
            rows = []
            with open('Quiz\scores.csv', 'r') as file:
                reader = csv.reader(file)
                header = next(reader, None)
                for row in reader:
                    rows.append(row)

            # Adds info to scores
            name = simpledialog.askstring("Name", "Enter your name:")
            if name:
                rows.append([str(time_score), name, str(rounds)])

            # Sorts with highest score on the top
            rows.sort(key=lambda x: float(x[0]), reverse=True)

            # Writes to leaderboard
            with open('Quiz\scores.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                if header:
                    writer.writerow(header)
                writer.writerows(rows)
        else:
            # Shows score
            messagebox.showinfo("Score", f"Your score is: {score}/{rounds}")
        to_menu()  # Return to the main menu after showing the score

    def add_question():
        # Asks for a new question
        nonlocal questions
        question_text = simpledialog.askstring("Add Question", "Enter the question:")
        if not question_text:
            return
        # Asks for options and correct answer
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


        # Randomly shuffle the options
        options = [f"T_{options[correct_index]}"] + [f"F_{opt}" for idx, opt in enumerate(options) if idx != correct_index]
        random.shuffle(options)

        questions.append([question_text, options])

    # Function to ask questions
    def ask_question(mainframe, questions):

        nonlocal rounds
        nonlocal score
        nonlocal type

        # Clear all widgets in the mainframe
        for child in mainframe.winfo_children():
            child.destroy()

        # Select a random question
        line = random.randint(0, len(questions) - 1)
        question = questions[line]
        options = question[1]  # The list of options

        # Display the question
        ttk.Label(mainframe, text=question[0], font=("Helvetica", 16), wraplength=350).grid(column=0, row=0, columnspan=2, pady=10)

        def on_correct():
            elapsed = time.time() - question_start_time
            increment_score()
            ask_question(mainframe, questions)

        # Display the options
        for idx, option in enumerate(options):
            if "T_" in option:
                option_text = option.replace("T_", "")

                ttk.Button(
                    mainframe,
                    text=option_text,
                    command=on_correct
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
        nonlocal question_start_time
        question_start_time = time.time()

    def increment_score():
        nonlocal rounds
        # Checks if it was arcade mode or not
        if type == "arcade":
            nonlocal time_score
            nonlocal question_start_time
            # Scores based on timing
            elapsed = time.time() - question_start_time
            if elapsed < 1:
                time_score += 10
                add = 10
            elif elapsed <2:
                time_score +=5
                add = 5
            elif elapsed < 5:
                time_score += 3
                add = 3
            elif elapsed < 10:
                time_score += 1
                add = 1
            rounds += 1
            messagebox.showinfo("Correct!", f"You were correct!\nTime taken: {elapsed:.2f} seconds\nAnd scored {add} points\nTotal Arcade Score: {time_score}")
        else:
            nonlocal score
            score += 1
            rounds += 1
            messagebox.showinfo("Correct!", f"You were correct!\nScore: {score}/{rounds}")
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