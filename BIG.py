import tkinter as tk
import random
from datetime import datetime


# Function to generate random text and numbers
def generate_result():
    global history_text
    
    # Get the user input for a 5-digit period number
    user_input = period_entry.get()
    if len(user_input) != 5 or not user_input.isdigit():
        result_label.config(text="Error: Enter a valid 5-digit number!", fg="red")
        return

    # Determine BIG or SMALL
    category = random.choice(["BIG", "SMALL"])

    # Generate number based on category
    if category == "BIG":
        number = random.choice([5, 6, 7, 8, 9])
    else:
        number = random.choice([0, 1, 2, 3, 4])

    # Determine the color of the number
    if number in [1, 3, 7, 9]:
        color = "green"
    elif number in [2, 4, 6, 8]:
        color = "red"
    else:  # Mixed colors
        if number == 0:
            color = "red violet"
        else:
            color = "green violet"

    # Display the result
    result_label.config(
        text=f"{category} {number}",
        font=("Helvetica", 24, "bold"),
        fg=color,
    )

    # Save result history with a timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    history_text += f"{timestamp} - {category} {number}\n"
    history_label.config(text=history_text)


# Initialize the GUI application
app = tk.Tk()
app.title("Random Text and Number Generator")
app.geometry("500x500")
app.config(bg="white")

# Display the "Created by Satyam" message
welcome_label = tk.Label(
    app,
    text="CREATED BY SATYAM",
    font=("Helvetica", 20, "bold"),
    fg="blue",
    bg="white",
)
welcome_label.pack(pady=20)

# Add a prompt for entering the 5-digit period number
period_label = tk.Label(app, text="Enter a 5-digit period number:", bg="white")
period_label.pack()

period_entry = tk.Entry(app, justify="center", font=("Helvetica", 14))
period_entry.pack(pady=10)

# Add a button to generate random text and numbers
generate_button = tk.Button(
    app,
    text="Generate Result",
    command=generate_result,
    font=("Helvetica", 16),
    bg="orange",
    fg="white",
)
generate_button.pack(pady=20)

# Add a label to display the result
result_label = tk.Label(app, text="", font=("Helvetica", 24, "bold"), bg="white")
result_label.pack(pady=20)

# Add a label to display the result history
history_text = ""
history_label = tk.Label(app, text="", anchor="w", justify="left", bg="white")
history_label.pack(pady=20)

# Run the application
app.mainloop()
