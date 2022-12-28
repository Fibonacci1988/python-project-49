import prompt


name = ''


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    with open("user_name.txt", "w") as f:
        f.write(name)
