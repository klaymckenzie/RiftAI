# lessons.py
lessons = {
    "1": {
        "title": "Variables",
        "content": "Variables store information. Example:\nx = 5\n print(x)",
        "quiz": "What does x = 5 do?",
        "answer": "It assigns the value 5 to the variable x."
    },
    #... more lessons
    "2": {
        "title": "Loops",
        "content": "Loops store information. Example:\nfor x in range(5):\n print(i)",
        "quiz": "What does range(3) do?",
        "answer": "It generates numbers 0, 1, and 2."
    },
    "3": {
        "title": "Functions",
        "content": "Functions group code blocks. Example:\ndef greet(name):\n print('Hello ' + name)",
        "quiz": "What does 'def greet(name)' do?",
        "answer": "It defines a function named greet that takes one parameter."
    }

}

if __name__ == "__main__":
    for key, lesson in lessons.items():
        print(f"{key}: {lesson['title']}")