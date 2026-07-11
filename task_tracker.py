"""
task_tracker.py
A simple command-line task tracker for beginners.

What it does:
1. Asks the user to type a task.
2. Saves that task as a new line in 'tasks.txt'.
3. Keeps asking until the user types 'quit' to stop.
"""


def main():
    print("=== Simple Task Tracker ===")
    print("Type a task and press Enter to save it.")
    print("Type 'quit' at any time to exit.\n")

    while True:
        # Ask the user for a task
        task = input("Enter a task: ")

        # Check if the user wants to quit
        if task.lower() == "quit":
            print("Goodbye! Your tasks are saved in tasks.txt")
            break

        # Don't save empty input
        if task.strip() == "":
            print("You didn't type anything. Try again.\n")
            continue

        # Open tasks.txt in 'append' mode so we add to it
        # instead of overwriting it each time. It will be
        # created automatically if it doesn't exist yet.
        with open("tasks.txt", "a") as file:
            file.write(task + "\n")

        print(f"Saved: '{task}'\n")


# This makes sure main() only runs when you run this file directly
if __name__ == "__main__":
    main()
