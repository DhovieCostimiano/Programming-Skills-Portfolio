import tkinter as tk  # Import the tkinter library for creating GUI applications
from tkinter import messagebox, simpledialog  # Import specific components for dialogs

# Student class to store information about each student
class Student:
    def __init__(self, number, name, coursework1, coursework2, coursework3, exam):
        # Initialize student attributes
        self.number = number  # Student number
        self.name = name  # Student name
        self.coursework = [coursework1, coursework2, coursework3]  # List of coursework scores
        self.exam = exam  # Exam score
        self.total_coursework = sum(self.coursework)  # Total coursework score
        self.total_score = self.total_coursework + self.exam  # Total score (coursework + exam)
        self.percentage = (self.total_score / 160) * 100  # Calculate percentage based on total score
        self.grade = self.calculate_grade()  # Calculate the letter grade

    def calculate_grade(self):
        # Determine the letter grade based on percentage
        if self.percentage >= 70:
            return 'A'  # Grade A for 70% and above
        elif self.percentage >= 60:
            return 'B'  # Grade B for 60% to 69%
        elif self.percentage >= 50:
            return 'C'  # Grade C for 50% to 59%
        elif self.percentage >= 40:
            return 'D'  # Grade D for 40% to 49%
        else:
            return 'F'  # Grade F for below 40%

# Function to load student data from a file
def load_data():
    students = []  # Create an empty list to hold student objects
    try:
        # Open the specified file for reading
        with open(r"C:\Users\April Joy Romina\Desktop\studentMarks.txt", 'r') as file:
            num_students = int(file.readline().strip())  # Read the number of students
            # Read each line and create Student objects
            for line in file:
                parts = line.strip().split(',')  # Split line into parts
                number = int(parts[0])  # Student number
                name = parts[1]  # Student name
                coursework1 = int(parts[2])  # Coursework score 1
                coursework2 = int(parts[3])  # Coursework score 2
                coursework3 = int(parts[4])  # Coursework score 3
                exam = int(parts[5])  # Exam score
                # Create a Student object and add it to the list
                students.append(Student(number, name, coursework1, coursework2, coursework3, exam))
    except Exception as e:
        # Show an error message if there was a problem loading data
        messagebox.showerror("Error", f"Could not load student data: {e}")
    return students  # Return the list of students

# Main application class for the student management system
class StudentApp:
    def __init__(self, root):
        self.root = root  # Store the main window
        self.root.title("Student Management")  # Set the window title
        self.students = load_data()  # Load the student data

        # Create a label to display instructions
        self.label = tk.Label(root, text="Choose an option:", font=("Arial", 12))
        self.label.pack(pady=10)  # Add some space around the label

        # Create buttons for different functionalities
        tk.Button(root, text="1. View All Students", command=self.view_all_students).pack(pady=5)
        tk.Button(root, text="2. View Student Record", command=self.view_student_record).pack(pady=5)
        tk.Button(root, text="3. Show Highest Score", command=self.highest_student).pack(pady=5)
        tk.Button(root, text="4. Show Lowest Score", command=self.lowest_student).pack(pady=5)
        tk.Button(root, text="Exit", command=root.quit).pack(pady=10)  # Exit button

    # Function to view all student records
    def view_all_students(self):
        all_students = ""  # Initialize a string to hold student information
        total_percentage = 0  # Variable to calculate the total percentage of all students

        # Loop through each student to compile their information
        for student in self.students:
            total_percentage += student.percentage  # Add each student's percentage to total
            all_students += f"Name: {student.name}\nNumber: {student.number}\n" \
                           f"Total Coursework: {student.total_coursework}\n" \
                           f"Exam: {student.exam}\n" \
                           f"Percentage: {student.percentage:.2f}%\n" \
                           f"Grade: {student.grade}\n" + "-"*20 + "\n"
        
        # Calculate the average percentage of all students
        avg_percentage = total_percentage / len(self.students) if self.students else 0
        all_students += f"Total Students: {len(self.students)}\nAverage: {avg_percentage:.2f}%"
        # Show all student information in a message box
        messagebox.showinfo("All Students", all_students)

    # Function to view an individual student's record
    def view_student_record(self):
        names = [f"{i+1}. {s.name}" for i, s in enumerate(self.students)]  # List of student names
        names_str = "\n".join(names)  # Join names into a single string for display
        choice = simpledialog.askinteger("Select Student", f"Choose a student:\n{names_str}")  # Ask for user input

        # Check if the choice is valid
        if choice and 1 <= choice <= len(self.students):
            student = self.students[choice - 1]  # Get the selected student
            # Create a string with the student's information
            info = f"Name: {student.name}\nNumber: {student.number}\n" \
                   f"Total Coursework: {student.total_coursework}\n" \
                   f"Exam: {student.exam}\n" \
                   f"Percentage: {student.percentage:.2f}%\n" \
                   f"Grade: {student.grade}"
            # Show the student's information in a message box
            messagebox.showinfo("Student Record", info)
        else:
            # Show an error if the selection is invalid
            messagebox.showerror("Error", "Invalid selection!")

    # Function to find and show the student with the highest score
    def highest_student(self):
        if self.students:  # Check if there are any students
            best_student = max(self.students, key=lambda s: s.total_score)  # Find the student with the highest score
            # Create a string with the best student's information
            info = f"Name: {best_student.name}\nNumber: {best_student.number}\n" \
                   f"Total Coursework: {best_student.total_coursework}\n" \
                   f"Exam: {best_student.exam}\n" \
                   f"Percentage: {best_student.percentage:.2f}%\n" \
                   f"Grade: {best_student.grade}"
            # Show the information in a message box
            messagebox.showinfo("Highest Score", info)
        else:
            # Show an error if no students are found
            messagebox.showerror("Error", "No students found!")

    # Function to find and show the student with the lowest score
    def lowest_student(self):
        if self.students:  # Check if there are any students
            worst_student = min(self.students, key=lambda s: s.total_score)  # Find the student with the lowest score
            # Create a string with the worst student's information
            info = f"Name: {worst_student.name}\nNumber: {worst_student.number}\n" \
                   f"Total Coursework: {worst_student.total_coursework}\n" \
                   f"Exam: {worst_student.exam}\n" \
                   f"Percentage: {worst_student.percentage:.2f}%\n" \
                   f"Grade: {worst_student.grade}"
            # Show the information in a message box
            messagebox.showinfo("Lowest Score", info)
        else:
            # Show an error if no students are found
            messagebox.showerror("Error", "No students found!")

# Start the Tkinter application
if __name__ == "__main__":
    root = tk.Tk()  # Create the main window
    app = StudentApp(root)  # Create an instance of the StudentApp class
    root.mainloop()  # Start the Tkinter event loop to run the application
