import tkinter as tk
from tkinter import messagebox
import time

# Function to display the reminder popup
def show_reminder():
    for i in range(5):  # Flash the message 5 times
        root.attributes('-topmost', 1)  # Bring window to the top
        root.deiconify()  # Show the window
        root.update()
        time.sleep(0.5)
        root.withdraw()  # Hide the window
        time.sleep(0.5)
    root.attributes('-topmost', 0)
    messagebox.showinfo("Reminder", "STAND UP & STRETCH!")

# Function to set the interval and start the reminder timer
def start_reminder():
    try:
        minutes = int(entry.get())
        if minutes <= 0:
            raise ValueError
        messagebox.showinfo("Reminder Set", f"Reminder set for every {minutes} minutes!")
        reminder_timer(minutes)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number of minutes.")

# Function that runs the reminder after the set interval
def reminder_timer(interval):
    # Wait for the set interval, then show the reminder
    root.after(interval * 60000, show_reminder)

# Create the Tkinter GUI
root = tk.Tk()
root.withdraw()  # Hide the root window initially

# Create a window for setting the interval
settings_window = tk.Tk()
settings_window.title("Health Reminder")
settings_window.geometry("300x150")

label = tk.Label(settings_window, text="Set reminder interval (minutes):")
label.pack(pady=10)

entry = tk.Entry(settings_window)
entry.pack(pady=10)

button = tk.Button(settings_window, text="Start Reminder", command=start_reminder)
button.pack(pady=10)

settings_window.mainloop()
