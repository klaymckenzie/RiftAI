import json

def save_user_profile(username, goals):
    data = {"username": username, "goals": goals}
    with open("user_profile.json", "w") as file:
        json.dump(data, file)

def load_user_profile():
    try:
        with open("user_profile.json", "r") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return None