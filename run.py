import os

# Run the Django development server
try:
    # Run the Django development server
    os.system('python manage.py runserver')
except Exception as e:
    # Print any errors to the console
    print(f"An error occurred: {e}")
    input("Press Enter to exit...")