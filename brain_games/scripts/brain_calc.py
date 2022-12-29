import random
import prompt
import brain_games.scripts.brain_games as welcome


# define a function to generate a random number from 1 to 99
def get_random_number():
    return random.randint(1, 20)


def get_random_operator():
    operator_number = random.randint(1, 3)
    if operator_number == 1:
        return '-'
    elif operator_number == 2:
        return '+'
    else:
        return '*'


# define a function to check if a number is even or odd
def evaluate(equation):
    return eval(equation)


def game():
    first_number = str(get_random_number())
    second_number = str(get_random_number())
    equation = first_number + get_random_operator() + second_number
    print(equation)
    answer = prompt.string('Your answer: ')
    if str(answer) == str(evaluate(equation)):
        return "Correct"
    else:
        answer = "'" + answer + "' is wrong answer ;(. Correct answer was '"
        print(answer + str(evaluate(equation)) + "'")
        return ""


def main():
    welcome.main()
    user_name = welcome.user_name
    print("What is the result of the expression?")
    if game() == 'Correct':
        print("Correct")
        if game() == 'Correct':
            print("Correct")
            if game() == 'Correct':
                print("Correct")
                print('Congratulations, ', user_name)
            else:
                print("Let's try again, ", user_name, "!")
        else:
            print("Let's try again, ", user_name, "!")
    else:
        print("Let's try again, ", user_name, "!")


if __name__ == '__main__':
    main()
