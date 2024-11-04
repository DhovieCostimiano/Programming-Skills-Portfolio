import tkinter as tk  # Import the tkinter library for creating GUI applications
import random  # Import the random library to select jokes randomly

# Create the main window for the application
root = tk.Tk()  # Only one instance of Tk is created
root.title("Alexa's Joke")  # Set the title of the window
root.geometry("300x250")  # Set the size of the window

# Function to load jokes from a file
def load_jokes(filename):
    jokes = []  # Initialize an empty list to store jokes
    try:
        # Open the specified file in read mode
        with open(filename, 'r') as file:
            # Read each line from the file
            for line in file:
                # Split each line into setup and punchline using '?' as the separator
                parts = line.strip().split('?')
                # Check if the line contains both a setup and a punchline
                if len(parts) == 2:
                    jokes.append(parts)  # Add the joke to the list
        # If no jokes were loaded, print a warning
        if not jokes:
            print("Warning: No jokes found in the file.")
    except FileNotFoundError:
        # Print an error message if the file is not found
        print(f"Error: The file {filename} was not found.")
    return jokes  # Return the list of jokes

# Function to tell a random joke
def tell_joke():
    # Check if there are any jokes available
    if not jokes:
        joke_label.config(text="No jokes available!")  # Update label if no jokes are found
        punchline_button.config(state=tk.DISABLED)  # Disable punchline button
        return  # Exit the function

    # Choose a random joke from the list
    setup, punchline = random.choice(jokes)  
    joke_label.config(text=setup)  # Display the setup of the joke
    # Enable the punchline button and set its command to show the punchline
    punchline_button.config(state=tk.NORMAL, command=lambda: show_punchline(punchline))
    tell_joke_button.config(state=tk.DISABLED)  # Disable the "Tell me a joke" button

# Function to show the punchline of the joke
def show_punchline(punchline):
    joke_label.config(text=punchline)  # Update the label to show the punchline
    punchline_button.config(state=tk.DISABLED)  # Disable punchline button after showing it
    tell_joke_button.config(state=tk.NORMAL)  # Re-enable the "Tell me a joke" button

# Function to create the GUI elements
def create_gui(root):
    global joke_label, punchline_button, tell_joke_button  # Declare global variables for the buttons and label

    # Create a label to display the joke setup or punchline
    joke_label = tk.Label(root, text="Alexa, Tell me a Joke!", font=("Arial", 14), wraplength=300)
    joke_label.pack(pady=20)  # Add some space around the label

    # Create a button to tell a joke and set its command to tell_joke function
    tell_joke_button = tk.Button(root, text="Tell me a joke", command=tell_joke, font=("Arial", 12))
    tell_joke_button.pack(pady=10)  # Add some space around the button

    # Create a button to show the punchline, initially disabled
    punchline_button = tk.Button(root, text="Show punchline", state=tk.DISABLED)
    punchline_button.pack(pady=10)  # Add some space around the button

    # Create a button to quit the application
    quit_button = tk.Button(root, text="Quit", command=root.quit, font=("Arial", 12))
    quit_button.pack(pady=20)  # Add some space around the button

# Load jokes from the specified file
jokes = load_jokes(r"C:\Users\April Joy Romina\Desktop\randomJokes.txt")  # Adjust the path as needed
create_gui(root)  # Call the function to create the GUI elements
root.mainloop()  # Start the Tkinter event loop to run the application
