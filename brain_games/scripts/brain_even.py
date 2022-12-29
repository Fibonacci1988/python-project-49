import random
import prompt
import brain_games.scripts.brain_games as welcome


# define a function to check if a number is even or odd
def is_even(number):
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'


def game():
    number = random.randint(1, 99)
    print("Question:", number)
    answer = prompt.string('Your answer: ')
    if answer == is_even(number):
        return "Correct"
    else:
        answer = "'" + answer + "' is wrong answer ;(. Correct answer was '"
        print(answer + is_even(number) + "'.")
        return ""


def main():
    welcome.main()
    user_name = welcome.user_name
    print('Answer "yes" if the number is even, otherwise answer "no".')
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
