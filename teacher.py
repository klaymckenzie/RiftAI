from lessons import lessons
from brain import load_progress, save_progress

def teach(lesson_id):
    lesson = lessons.get(lesson_id)
    if not lesson:
        print("Lesson not found.")
        return

    print(f"\n {lesson['title']}")
    print(f"{lesson['content']}")
    input("\nPress Enter to continue to quiz...")

    print(f"\n Quiz: {lesson['quiz']}")
    user_answer = input("Your answer: ")

    if user_answer.strip().lower() in lesson["answer"].lower():
        print("Correct! Great job.")
    else:
        print(f"Almost! The correct answer is:\n{lesson['answer']}")

    data = load_progress()
    if lesson_id not in data["completed"]:
        data["completed"].append(lesson_id)
        save_progress(data)
        print("Progress saved.")
