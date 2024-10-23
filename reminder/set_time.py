import tkinter as tk
from tkinter import messagebox

# Create the root window
root = tk.TK()
root.title("Set Reminder Interval")
root.geometry("300x150")

# Set default interval
reminder_time = tk.IntVar(value=2) # Default interval (10 minutes)

# Function to save the interval time to a file
def save_time():
    time = reminder_time.get()
    with open('interval.txt', 'w') as f:
        f.write(str(time))
    messagebox.showinfo("Saved", f"Reminder set for {time} minutes")
    root.quit()


# UI element
label = tk.Label(root, text="Set reminder interval (minute):")
label.pack(pady=2)

entry = tk.Entry(root, textvariable=reminder_time)
entry.pack(pady=2)

button = tk.Button(root, text="Set Time", command=save_time)
button.pack(pady=2)

# Run the app
root.mainloop()