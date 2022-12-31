import random
import prompt
import math
import brain_games.scripts.brain_games as welcome


# a function to check if a number is even or odd (for brain-even game)
def is_even(number):
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'


# a function to generate random operator -,+ or * (for brain-calc game)
def get_random_operator():
    operator_number = random.randint(1, 3)
    if operator_number == 1:
        return '-'
    elif operator_number == 2:
        return '+'
    else:
        return '*'


# a function to check if a number is even or odd (for brain-prime game)
def prime(number):
    is_prime = True
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        return 'yes'
    else:
        return 'no'


def incorrect_reply(answer, correct_answer):
    answer = "'" + str(answer) + "' is wrong answer ;(. Correct answer was '"
    answer = answer + str(correct_answer) + "'."
    return answer


# logic of brain-even game
def even_logic():
    number = random.randint(1, 99)
    print("Question:", number)
    answer = prompt.string('Your answer: ')
    if answer == is_even(number):
        return "Correct!"
    else:
        return incorrect_reply(answer, is_even(number))


# logic of brain-calc game
def calc_logic():
    first_number = str(random.randint(1, 20))
    second_number = str(random.randint(1, 20))
    operator = get_random_operator()
    equation = first_number + operator + second_number
    print('Question:', first_number, operator, second_number)
    answer = prompt.string('Your answer: ')
    if str(answer) == str(eval(equation)):
        return "Correct!"
    else:
        return incorrect_reply(answer, eval(equation))


# logic of brain-gcd game
def gcd_logic():
    first_number = random.randint(1, 100)
    second_number = random.randint(1, 100)
    print('Question:', first_number, second_number)
    answer = prompt.string('Your answer: ')
    if str(answer) == str(math.gcd(first_number, second_number)):
        return "Correct!"
    else:
        return incorrect_reply(answer, math.gcd(first_number, second_number))


# logic of brain-prime game
def prime_logic():
    number = random.randint(1, 100)
    print('Question:', number)
    answer = prompt.string('Your answer: ')
    correct_answer = prime(number)
    if str(answer) == str(correct_answer):
        return "Correct!"
    else:
        return incorrect_reply(answer, correct_answer)


# logic of brain-progression game
def progression_logic():
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
        return "Correct!"
    else:
        return incorrect_reply(answer, correct_answer)


def game(game_name):
    answer = ''
    if game_name == 'even':
        answer = even_logic()
    elif game_name == 'calc':
        answer = calc_logic()
    elif game_name == 'gcd':
        answer = gcd_logic()
    elif game_name == 'prime':
        answer = prime_logic()
    elif game_name == 'progression':
        answer = progression_logic()
    return answer


def first_message(game_name):
    if game_name == 'even':
        print('Answer "yes" if the number is even, otherwise answer "no".')
    elif game_name == 'calc':
        print("What is the result of the expression?")
    elif game_name == 'gcd':
        print("Find the greatest common divisor of given numbers.")
    elif game_name == 'prime':
        print('Answer "yes" if given number is prime. Otherwise answer "no".')
    elif game_name == 'progression':
        print("What number is missing in the progression?")


def game_coordination(user_name, game_name):
    rounds = 3
    while rounds > 0:
        result = game(game_name)
        print(result)
        if result == 'Correct!':
            rounds -= 1
        else:
            rounds = -1
    if rounds == 0:
        print('Congratulations, ' + user_name + '!')
    else:
        print("Let's try again, " + user_name + "!")


def main(game_name):
    welcome.main()
    user_name = welcome.user_name
    first_message(game_name)
    game_coordination(user_name, game_name)
