from django.shortcuts import render
from threading import Thread
import time
import pyautogui

# Function to save user-set interval to a file
def save_interval(minutes):
    with open('interval.txt', 'w') as f:
        f.write(str(minutes))

# Function to read user-set interval from file
def get_interval():
    try:
        with open('interval.txt', 'r') as f:
            return int(f.read().strip())
    except FileNotFoundError:
        return 10  # Default to 10 minutes if file not found

def display_popup():
    """Trigger a PyAutoGUI popup after the user-defined interval."""
    while True:
        interval = get_interval()
        print(f"Sleeping for {interval} minutes")
        time.sleep(interval * 60)  # Convert minutes to seconds
        print("Time's up! Displaying popup...")
        pyautogui.alert(text='STAND UP & STRETCH', title='Health Reminder', button='OK')


def reminder_view(request):
    """Display the flashing 'Stand Up' message."""
    message = ""
    if request.method == 'POST':
        interval = int(request.POST.get('interval'))
        save_interval(interval)
        message = f"Reminder set for every {interval} minutes."
    
    return render(request, 'reminder.html', {'message': message})

# Start the popup thread when the server runs
Thread(target=display_popup, daemon=True).start()
