from teacher import teach
from brain import load_progress
from lessons import lessons

print("Welcome to RiftAI – Your Python Mentor")

while True:
    data = load_progress()
    print("\nChoose a lesson:")
    for lid, ldata in lessons.items():
        status = "Completed" if lid in data["completed"] else "Available"
        print(f"{lid}. {ldata['title']} [{status}]")

    choice = input("\nEnter lesson number or 'q' to quit: ")
    if choice.lower() == 'q':
        print("Session ended. Keep coding strong.")
    break

teach(choice)
