import random
import prompt
import brain_games.scripts.brain_games as welcome


def game():
    start = random.randint(1, 100)
    diff = random.randint(1, 10)
    hidden_position = random.randint(0, 9)
    progression = []
    for i in range(10):
        progression.append(start + i * diff)
    correct_answer = progression[hidden_position]
    progression[hidden_position] = '..'
    print('Question:', " ".join(map(str, progression)))
    answer = prompt.string('Your answer: ')
    if str(answer) == str(correct_answer):
        return "Correct"
    else:
        answer = "'" + str(answer)
        answer = answer + "' is wrong answer ;(. Correct answer was '"
        print(answer + str(correct_answer) + "'.")
        return ""


def main():
    welcome.main()
    user_name = welcome.user_name
    print("What number is missing in the progression?")
    if game() == 'Correct':
        print("Correct!")
        if game() == 'Correct':
            print("Correct!")
            if game() == 'Correct':
                print("Correct!")
                print('Congratulations, ' + user_name + '!')
            else:
                print("Let's try again, " + user_name + "!")
        else:
            print("Let's try again, " + user_name + "!")
    else:
        print("Let's try again, " + user_name + "!")


if __name__ == '__main__':
    main()
