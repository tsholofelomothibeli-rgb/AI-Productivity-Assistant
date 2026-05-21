# AI Workplace Assistant - Basic Version

def greet():
    print("AI Assistant: Hello! I can help you with emails, tasks, and questions.")

def generate_email(name, purpose):
    return f"""
Subject: {purpose}

Dear {name},

I hope you are well.

I am writing regarding {purpose}. Please let me know if you need any additional information.

Kind regards,
AI Assistant
"""

def task_planner(tasks):
    print("\nYour Task Plan:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

def chatbot():
    greet()

    while True:
        print("\nWhat do you need help with?")
        print("1. Email generation")
        print("2. Task planning")
        print("3. Ask a question")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            name = input("Who is the email for? ")
            purpose = input("What is the email about? ")
            print("\n" + generate_email(name, purpose))

        elif choice == "2":
            tasks = input("Enter tasks separated by commas: ").split(",")
            task_planner([t.strip() for t in tasks])

        elif choice == "3":
            question = input("Ask me anything: ")
            print("AI Assistant:", "I am still learning, but here is a simple answer:")
            print("->", question)

        elif choice == "4":
            print("Goodbye! 👋")
            break

        else:
            print("Invalid option. Try again.")

chatbot()
