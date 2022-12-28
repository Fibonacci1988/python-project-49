import random
import prompt
import math


# define a function to check if a number is even or odd
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


def game():
    number = random.randint(1, 100)
    print('Question: ', number)
    answer = prompt.string('Your answer: ')
    correct_answer = prime(number)
    if str(answer) == str(correct_answer):
        return "Correct"
    else:
        answer = "'" + str(answer)
        answer = answer + "' is wrong answer ;(. Correct answer was '"
        print(answer + str(correct_answer) + "'")
        return ""


def main():
    with open("user_name.txt", "r") as f:
        user_name = f.read()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
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
