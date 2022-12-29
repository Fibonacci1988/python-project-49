import random
import prompt
import math
import brain_games.scripts.brain_games as welcome


# define a function to generate a random number from 1 to 99
def get_random_number():
    return random.randint(1, 100)


# define a function to check if a number is even or odd
def gcd(number1, number2):
    return math.gcd(number1, number2)


def game():
    first_number = get_random_number()
    second_number = get_random_number()
    print('Question:', first_number, second_number)
    answer = prompt.string('Your answer: ')
    if str(answer) == str(gcd(first_number, second_number)):
        return "Correct"
    else:
        answer = "'" + str(answer)
        answer = answer + "' is wrong answer ;(. Correct answer was '"
        print(answer + str(gcd(first_number, second_number)) + "'.")
        return ""


def main():
    welcome.main()
    user_name = welcome.user_name
    print("Find the greatest common divisor of given numbers.")
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
