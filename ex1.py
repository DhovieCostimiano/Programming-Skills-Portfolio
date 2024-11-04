import tkinter as tk
import random
from tkinter import messagebox

# Initialize the main window for the quiz application
root = tk.Tk()
root.title("Simple Math Quiz")  # Set the title of the window
root.geometry("300x200")  # Set the size of the window

# Global variables to keep track of the score, question number, and difficulty
score = 0
question_number = 1
difficulty = 1

# Function to start the quiz
def start_quiz():
    global difficulty, score, question_number
    # Get the difficulty level selected by the user
    difficulty = int(diff_var.get())
    # Check if the selected difficulty is valid (1, 2, or 3)
    if difficulty not in [1, 2, 3]:
        messagebox.showerror("Error", "Please select a difficulty level.")
        return  # Exit the function if the selection is invalid

    # Reset the score and question number for the new quiz
    score = 0
    question_number = 1
    # Hide the menu frame and show the quiz frame
    menu_frame.pack_forget()
    quiz_frame.pack()
    ask_question()  # Start asking questions

# Function to generate a question based on the selected difficulty
def ask_question():
    global num1, num2, operation, answer
    # Generate random numbers based on difficulty level
    if difficulty == 1:  # Easy level (1-digit numbers)
        num1, num2 = random.randint(0, 9), random.randint(0, 9)
    elif difficulty == 2:  # Moderate level (2-digit numbers)
        num1, num2 = random.randint(10, 99), random.randint(10, 99)
    elif difficulty == 3:  # Advanced level (4-digit numbers)
        num1, num2 = random.randint(1000, 9999), random.randint(1000, 9999)

    # Randomly choose an operation (addition or subtraction)
    operation = random.choice(['+', '-'])
    # Calculate the correct answer using the eval function
    answer = eval(f"{num1} {operation} {num2}")
    # Display the question to the user
    question_label.config(text=f"Q{question_number}: {num1} {operation} {num2} = ?")
    answer_entry.delete(0, tk.END)  # Clear the answer entry field

# Function to check the user's answer and move to the next question
def check_answer():
    global score, question_number
    try:
        # Get the user's answer from the entry field and convert it to an integer
        user_answer = int(answer_entry.get())
        # Check if the answer is correct
        if user_answer == answer:
            score += 10  # Increase the score for a correct answer
            messagebox.showinfo("Correct!", "Well done!")  # Show success message
        else:
            messagebox.showinfo("Incorrect", f"Oops! The correct answer was {answer}.")  # Show correct answer
    except ValueError:
        messagebox.showerror("Error", "Please enter a number.")  # Handle invalid input
        return  # Exit the function if input is not a number

    question_number += 1  # Move to the next question
    if question_number <= 10:  # Check if there are more questions to ask
        ask_question()  # Ask the next question
    else:
        display_results()  # Show the results when the quiz is finished

# Function to display the final score
def display_results():
    quiz_frame.pack_forget()  # Hide the quiz frame
    results_label.config(text=f"Your Score: {score} / 100")  # Display the score
    results_frame.pack()  # Show the results frame

# Create frames for different screens in the quiz
menu_frame = tk.Frame(root)  # Frame for the menu
quiz_frame = tk.Frame(root)  # Frame for the quiz
results_frame = tk.Frame(root)  # Frame for the results

# Menu Frame: Contains difficulty selection and start button
tk.Label(menu_frame, text="Select Difficulty Level", font=("Arial", 12)).pack(pady=10)  # Label for difficulty selection
diff_var = tk.IntVar()  # Variable to store the selected difficulty level
tk.Radiobutton(menu_frame, text="Easy (1-digit)", variable=diff_var, value=1).pack(anchor='w')  # Easy option
tk.Radiobutton(menu_frame, text="Moderate (2-digit)", variable=diff_var, value=2).pack(anchor='w')  # Moderate option
tk.Radiobutton(menu_frame, text="Advanced (4-digit)", variable=diff_var, value=3).pack(anchor='w')  # Advanced option
tk.Button(menu_frame, text="Start Quiz", command=start_quiz).pack(pady=10)  # Start quiz button

# Quiz Frame: Contains the question and answer entry
question_label = tk.Label(quiz_frame, text="", font=("Arial", 12))  # Label for displaying the question
question_label.pack(pady=10)  # Add some space around the label
answer_entry = tk.Entry(quiz_frame)  # Entry field for user answers
answer_entry.pack(pady=5)  # Add some space around the entry
tk.Button(quiz_frame, text="Submit Answer", command=check_answer).pack(pady=5)  # Button to submit the answer

# Results Frame: Displays the user's final score and options to play again or quit
results_label = tk.Label(results_frame, text="", font=("Arial", 12))  # Label for displaying the score
results_label.pack(pady=10)  # Add some space around the label
tk.Button(results_frame, text="Play Again", command=lambda: [results_frame.pack_forget(), menu_frame.pack()]).pack(pady=5)  # Button to restart the quiz
tk.Button(results_frame, text="Quit", command=root.quit).pack(pady=5)  # Button to quit the application

# Start with the menu frame
menu_frame.pack()

# Run the application
root.mainloop()
